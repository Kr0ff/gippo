import argparse

from .http import *

def arg_parser():
    # Print ASCII cos its cool :)
    # print(printAscii())

    parser = argparse.ArgumentParser(description='gippo - Retrieve information about a given IP address from \"iplocation.net\"')
    
    parser.add_argument("-i", "--ip", help="IP address to check against \"iplocation.net\"", required=False)
    parser.add_argument("-v", "--version", help="Show version", required=False, action="store_true")
    arg = parser.parse_args()
    
    if arg.version:
        print(f"[*] Version: {VERSION}")
    
    if arg.ip:
        send_request(arg.ip)
    
    