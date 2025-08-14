#!/usr/bin/env python3

"""
OTA
"""

import os
import sys
import math
import time
import asyncio
import argparse
import hashlib
import logging
import pycyphal

import pycyphal.application
from pycyphal.transport.can import CANTransport, CANTransportStatistics
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from pycyphal.transport.can.media.socketcand import SocketcandMedia
from pycyphal.transport.redundant import RedundantTransport
from pycyphal.transport.can.media.pythoncan import PythonCANMedia
import uavcan.node
import dinosaurs.bootstrap.updatee

__doc__ = """
Example:
    $ ./DevTesting/ota/firmware_updater.py -c "can1" -n 24 -m 8 -u "app_updatee" -f /home/weig/work/embedded/dragonball_ws/build_space/data_collection/vulture_dcb_h723ve@7.0.5/data_collection/zephyr/zephyr.signed.bin

    $ ./DevTesting/ota/firmware_updater.py -c "can1" -n 24 -m 8 -u "boot" -f /home/weig/work/embedded/dragonball_ws/build_space/data_collection/vulture_dcb_h723ve@7.0.5/mcuboot/zephyr/zephyr.bin

    $ ./DevTesting/ota/firmware_updater.py -c "can1" -n 25 -m 8 -u "app_updatee" -f /home/zhangge/worknote/dragonBall_ws/build_space/super_lifter/super_lifter_h723/super_lifter/zephyr/zephyr.signed.bin

"""

def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter, allow_abbrev=False)

    parser.add_argument("-c", "--can", required=False, type=str, default='can1',
                        help='can bus')
    parser.add_argument("-n", "--node_id", required=True, type=int, default=11,
                        help='node id')
    parser.add_argument("-m", "--mtu", required=False, type=int, default=8,
                        help='can mtu')
    parser.add_argument("-u", "--updatee", required=False, type=str, default='app_updatee',
                        help='updatee')
    parser.add_argument("-f", "--firmware", required=True, type=str,
                        help='firmware path')

    return parser.parse_args()

class FirmwareUpdater:
    def __init__(self, args:argparse) -> None:
        self.args = args
        node_info = uavcan.node.GetInfo_1.Response(
            software_version=uavcan.node.Version_1(major=1, minor=0),
            name="dinosaurs.bootstrap.updatee",
        )

        self.updatee_index = -1
        if not os.path.exists(self.args.firmware):
            print(f"Error firmware not exists!")
            sys.exit(1)

        transport = CANTransport(SocketCANMedia(args.can, mtu=args.mtu), local_node_id=88)
        self.node = pycyphal.application.make_node(node_info, transport=transport)
        self.updatee_iterator_ = self.node.make_client(dinosaurs.bootstrap.updatee.UpdateeIterator_1,
                                                       args.node_id, 250)
        self.prepare_ota_ = self.node.make_client(dinosaurs.bootstrap.updatee.PrepareOTA_1,
                                                  args.node_id, 245)
        self.start_ota_ = self.node.make_client(dinosaurs.bootstrap.updatee.StartOTA_1, args.node_id, 249)
        self.write_updatee_ = self.node.make_client(dinosaurs.bootstrap.updatee.WriteUpdatee_1,
                                                    args.node_id, 248)
        self.integarity_check_ = self.node.make_client(dinosaurs.bootstrap.updatee.UpdateeIntegarityCheck_1,
                                                       args.node_id, 247)
        self.stop_ota_ = self.node.make_client(dinosaurs.bootstrap.updatee.StopOTA_1, args.node_id, 246)
        self.node.start()

    async def updatee_iterator(self):
        index = 0
        updatee_list = []
        try:
            while(True):
                request = dinosaurs.bootstrap.updatee.UpdateeIterator_1.Request(
                    index = index
                )

                result = await self.updatee_iterator_.call(request)
                if result is None:
                    raise ValueError("Updatee is not exist")

                response, transfer = result
                updatee = ''.join(chr(x) for x in response.updatee.name)

                if len(updatee) == 0:
                    print(f"Could not found updatee in {updatee_list}")
                    break # no found updatee
                elif self.args.updatee == updatee:
                    self.updatee_index = index
                    break
                else:
                    updatee_list.append(updatee)
                    index = index + 1
        except Exception as e:
            print(f"Error: {str(e)}")

    async def prepare_ota(self):
        print("Prepare OTA")
        request = dinosaurs.bootstrap.updatee.PrepareOTA_1.Request(
            index = self.updatee_index
        )
        try:
            result = await self.prepare_ota_.call(request)
            if result is None:
                raise ValueError("Updatee is not exist")
            else:
                time.sleep(1) # wait jump to bootloader
        except Exception as e:
            print(f"Error: {str(e)}")

    async def start_ota(self):
        print("Start OTA")
        request = dinosaurs.bootstrap.updatee.StartOTA_1.Request(
            index = self.updatee_index,
            file_size = os.path.getsize(self.args.firmware)
        )
        try:
            self.start_ota_.response_timeout = 30.0  # wait flash erased
            result = await self.start_ota_.call(request)
            if result is None:
                raise ValueError("Start OTA failed")
            else:
                response, transfer = result
                if response.error.value != 0:
                    raise ValueError("StartOTA Failed {response.error.value}")
        except Exception as e:
            print(f"Error: {str(e)}")

    async def write_updatee(self):
        offset = 0
        file_size = os.path.getsize(self.args.firmware)
        print("Write updatee")
        try:
            with open(self.args.firmware, "rb") as f:
                while (offset != file_size):
                    f.seek(offset)
                    request = dinosaurs.bootstrap.updatee.WriteUpdatee_1.Request(
                        index = self.updatee_index,
                        offset = offset,
                        data = uavcan.primitive.Unstructured_1(f.read(256))
                    )
                    result = await self.write_updatee_.call(request)
                    if result is None:
                        raise ValueError("Write updatee failed")

                    response, transfer = result
                    if response.error.value != 0:
                        raise ValueError("Write updatee failed {reponse.error.value}")
                    else:
                        offset = offset + len(request.data.value)
                        # update jin du tiao
        except Exception as e:
            print(f"Error: {str(e)}")

    async def integarity_check(self):
        sha256sum = ''
        request = dinosaurs.bootstrap.updatee.UpdateeIntegarityCheck_1.Request(
            index = self.updatee_index
        )
        print("IntegarityCheck")
        with open(self.args.firmware, "rb") as f:
            f.seek(0)
            sha256sum = hashlib.sha256(f.read()).hexdigest()

        try:
            self.integarity_check_.response_timeout = 30.0  # wait sha256sum calc
            result = await self.integarity_check_.call(request)
            if result is None:
                raise ValueError("Updatee Integarity Check Failed")

            response, transfer = result
            if response.algorithm == dinosaurs.bootstrap.updatee.UpdateeIntegarityCheck_1.Response.SHA256_SUM:
                if sha256sum == response.data.tobytes().hex():
                    print("Updata Sucess!")
                else:
                    raise ValueError("Updatee Integarity Check Failed {response.error.value}")
        except Exception as e:
            print(f"Error: {str(e)}")

    async def stop_ota(self):
        print("Stop OTA")
        request = dinosaurs.bootstrap.updatee.StopOTA_1.Request(
            index = self.updatee_index,
            error = dinosaurs.bootstrap.updatee.Error_1(0)
        )
        try:
            result = await self.stop_ota_.call(request)
            if result is None:
                raise ValueError("Stop OTA failed")
            else:
                response, transfer = result
                if response.error.value != 0:
                    raise ValueError("Stop OTA Failed {response.error.value}")
        except Exception as e:
            print(f"Error: {str(e)}")

    async def run(self) -> None:
        await self.updatee_iterator()
        if self.updatee_index >= 0:
            await self.prepare_ota()
            await self.start_ota()
            await self.write_updatee()
            await self.integarity_check()
            await self.stop_ota()

    async def close(self) -> None:
        self.node.close()

async def main() -> None:
    args = parse_args()
    app = FirmwareUpdater(args)
    try:
        await app.run()
    except KeyboardInterrupt:
        pass
    finally:
        await app.close()


if __name__ == "__main__":
    asyncio.run(main())
