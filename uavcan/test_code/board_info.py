#!/usr/bin/env python3

"""
Board Info
"""

import os
import sys
import math
import asyncio
import argparse
import logging
import pycyphal

import pycyphal.application
from pycyphal.transport.can import CANTransport, CANTransportStatistics
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from pycyphal.transport.can.media.socketcand import SocketcandMedia
from pycyphal.transport.redundant import RedundantTransport
from pycyphal.transport.can.media.pythoncan import PythonCANMedia
import uavcan.node
import dinosaurs.component

def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter, allow_abbrev=False)

    parser.add_argument("-c", "--ccan", required=False, type=str, default='can1',
                        help='control can bus')
    parser.add_argument("-i", "--component_id", required=False, type=int, default=0,
                        help='component id')
    return parser.parse_args()

class BoardInfoTest:
    def __init__(self, args:argparse) -> None:
        self.args = args
        node_info = uavcan.node.GetInfo_1.Response(
            software_version=uavcan.node.Version_1(major=1, minor=0),
            name="syriusrobotics.embedded.sensors.sick_lidar_test",
        )

        transport = CANTransport(SocketCANMedia(args.ccan, mtu=8), local_node_id=88)
        self.cnode = self.cnode = pycyphal.application.make_node(node_info, transport=transport)
        self._component_info_query = self.cnode.make_publisher(dinosaurs.component.InfoQuery_1, 998)
        self._component_info_report = self.cnode.make_subscriber(dinosaurs.component.InfoReport_1, 999)
        self.cnode.start()

    async def run(self) -> None:
        def recv_component_info_report(msg: dinosaurs.component.InfoReport_1,
                                       t: pycyphal.transport.TransferFrom) -> None:
            print(msg)

        await self._component_info_query.publish(dinosaurs.component.InfoQuery_1(self.args.component_id))
        self._component_info_report.receive_in_background(recv_component_info_report)
        while True:
            await asyncio.sleep(1)
            sys.exit(0)

    async def close(self) -> None:
        self.cnode.close()


async def main() -> None:
    args = parse_args()
    app = BoardInfoTest(args)
    try:
        await app.run()
    except KeyboardInterrupt:
        pass
    finally:
        await app.close()


if __name__ == "__main__":
    asyncio.run(main())
