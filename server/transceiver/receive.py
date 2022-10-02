# Original credit: https://github.com/milaq/rpi-rf
# Copyright (c) 2016 Suat Özgür, Micha LaQua

import argparse
import signal
import sys
import time
import logging
import time
from rpi_rf import RFDevice

rfdevice = None


# pylint: disable=unused-argument
def exithandler(signal, frame):
    rfdevice.cleanup()
    sys.exit(0)

logging.basicConfig(level=logging.INFO, format='%(message)s')

parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device')
parser.add_argument('-g', dest='gpio', type=int, default=27,
                    help="GPIO pin (Default: 27)")
parser.add_argument('-s', dest='seconds', type=int, default=10,
                    help="Number of seconds to listen for")
args = parser.parse_args()

signal.signal(signal.SIGINT, exithandler)
rfdevice = RFDevice(args.gpio)
rfdevice.enable_rx()
timestamp = None
logging.info(f"Listening for codes on GPIO {args.gpio} for {args.seconds} seconds")

t_end = time.time() + args.seconds
while time.time() < t_end:
    if rfdevice.rx_code_timestamp != timestamp:
        timestamp = rfdevice.rx_code_timestamp
        logging.info(f"{rfdevice.rx_code} [pulselength {rfdevice.rx_pulselength}, protocol {rfdevice.rx_proto}]")
    time.sleep(0.01)
    
logging.info(f"Done Listening.")
rfdevice.cleanup()