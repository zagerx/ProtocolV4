import asyncio
import pycyphal
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Version_1_0
from uavcan.primitive import String_1_0
from dinosaurs.peripheral.AddonsGetState_1_0 import AddonsGetState_1_0

async def client_addongetstate_process():
    # ================== Node setup (same as motor example) ==================
    transport = CANTransport(
        media=SocketCANMedia("can1", mtu=8),  # Classic CAN configuration
        local_node_id=100  # Hardcoded node ID (adjust as needed)
    )
    node = make_node(
        transport=transport,
        info=NodeInfo(
            name="test_node",
            software_version=Version_1_0(major=1, minor=0),
            unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF01")
        )
    )
    
    # Create client for AddonsGetState service
    # Server node ID 28, port name should match service definition
    client = node.make_client(AddonsGetState_1_0, server_node_id=25, port_name=201)

    try:
        # Prepare request with addon name and device ID
        request = AddonsGetState_1_0.Request(
            name=String_1_0(value="lift"),  # Example addon name
            device_id=0  # Use 0 for single device
        )
        
        try:
            # Send request and get response tuple
            response_tuple = await asyncio.wait_for(client.call(request), timeout=0.2)
            
            # Extract response object from tuple (first element)
            response_obj = response_tuple[0]
            print(f"[Response] Received state: {response_obj}")
            
            # Access state details correctly
            state = response_obj.state
            print(f"Addon state details: current_state={state.current_state}, timestamp={state.timestamp.microsecond}us")
            
        except asyncio.TimeoutError:
            print("[Timeout] No response received within 200ms")
    finally:
        client.close()
        node.close()
        transport.close()

if __name__ == "__main__":
    asyncio.run(client_addongetstate_process())