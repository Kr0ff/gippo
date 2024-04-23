import json
from prettytable import PrettyTable

from .globals import *
from .exception import *
from .http import *

def CreateTable(
    ip, 
    ip_number, 
    ip_version, 
    country_name, 
    country_code2, 
    isp, 
    response_code, 
    response_message ):
    
    table = PrettyTable(['IP Address', 'IP Number (Int)', 'IP Type', 'Country', 'Country Code', 'ISP', 'HTTP Response Code', 'HTTP Response Msg'])
    table.add_row([ip, ip_number, ip_version, country_name, country_code2, isp, response_code, response_message])
    return table

def parse_output(payload: str) -> bool:
    
    # Payload is already returned as a serialized json object
    # so we just load it and parse 
    decoded_dump = json.loads(payload)
    
    t = CreateTable(
        decoded_dump['ip'],
        decoded_dump['ip_number'],
        decoded_dump['ip_version'],
        decoded_dump['country_name'],
        decoded_dump['country_code2'],
        decoded_dump['isp'],
        decoded_dump['response_code'],
        decoded_dump['response_message']
        )
    
    print(t)