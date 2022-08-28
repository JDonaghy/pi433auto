# Original credit: https://github.com/milaq/rpi-rf
# Copyright (c) 2016 Suat Özgür, Micha LaQua

import argparse
import logging
import json

from rpi_rf import RFDevice

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s',)

parser = argparse.ArgumentParser(description='Sends a decimal code via a 433/315MHz GPIO device')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-s', '--setname', metavar='SETNAME', type=str, default = "",
                    help="Remote set to use")
group.add_argument('-c', '--code', metavar='CODE', type=int, default = 0,
                    help="Decimal code to send")

parser.add_argument('-f', '--codefile', metavar='CODEFILE', type=str, default = "codes.json",
                    help="Code file")

parser.add_argument('-b', '--button', metavar='BUTTONINDEX', type=int, default = 1,
                    help="Button Index to use")
parser.add_argument('-o', '--operation', metavar='OPERATION', type=str, default = "on", choices=['on','off'],
                    help="Button Index to use")
parser.add_argument('-g', '--gpio', dest='gpio', type=int, default=17,
                    help="GPIO pin (Default: 17)")
parser.add_argument('-p', '--pulselength', dest='pulselength', type=int, default=161,
                    help="Pulselength (Default: 161)")
parser.add_argument('-t', '--protocol' ,dest='protocol', type=int, default=1,
                    help="Protocol (Default: 1)")
args = parser.parse_args()


if args.setname:
    f = open(args.codefile,)
    codedefs = json.load(f)
    f.close()
    gpio = codedefs["gpio"]
    codeset = codedefs["sets"][args.setname]
    pulselength = codeset["pulselength"]
    protocol = codeset["protocol"]
    buttondef = codeset["buttons"][args.button - 1]
    code = buttondef["on"] if args.operation == "on" else buttondef["off"] 
else:
    gpio = args.gpio
    if args.protocol:
        protocol = args.protocol
    else:
        protocol = "default"
    if args.pulselength:
        pulselength = args.pulselength
    else:
        pulselength = "default"
    protocol = args.protocol
    code = args.code

rfdevice = RFDevice(gpio)    
rfdevice.enable_tx()
logging.info(f"{code} [protocol: {protocol} pulselength: {pulselength}]")

rfdevice.tx_code(int(code), protocol, int(pulselength))
rfdevice.cleanup()