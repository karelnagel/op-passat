#!/usr/bin/env python3
from argparse import ArgumentParser

from panda import Panda
from tp20 import TP20Transport
from kwp2000 import KWP2000Client, ECU_IDENTIFICATION_TYPE


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--bus", default=1, type=int, help="CAN bus number to use")
    parser.add_argument("--start-address", default=0, type=int, help="start address")
    parser.add_argument(
        "--end-address", default=0x5FFFF, type=int, help="end address (inclusive)"
    )
    args = parser.parse_args()

    p = Panda()
    p.can_clear(0xFFFF)
    p.set_safety_mode(Panda.SAFETY_ALLOUTPUT)

    print("Connecting using KWP2000...")
    tp20 = TP20Transport(p, 0x9, bus=args.bus, timeout=1)
    kwp_client = KWP2000Client(tp20, debug=True)

    print("Reading ecu identification & flash status")
    ident = kwp_client.read_ecu_identifcation(ECU_IDENTIFICATION_TYPE.ECU_IDENT)
    print("ECU identification", ident)

    status = kwp_client.read_ecu_identifcation(ECU_IDENTIFICATION_TYPE.STATUS_FLASH)
    print("Flash status", status)


# If your car is not factory fitted with LKAS, you will (probably) need to enable the HCA-message-receiving-feature in your steering rack by editing its configuration. If your rack (adress 44) supports coding it is at byte 0, bit 4 (set it to 1).
# Some of the racks dont support coding (e.g. 1K0909144M). In this case you need to do it via Adaptations. Select "Lane Assist" (Channel 06) from the dropdown in your software and enable it (set it to 1).
