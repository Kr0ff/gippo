import requests

from .globals import *
from .exception import *
from .parse_info import *

# Send request to api.iplocation.net
def send_request(target_ip: str) -> None:
    FINAL_URL = IPLOCATION_URL + API_URI + target_ip
    
    s = requests.Session()
    r = s.get(FINAL_URL, verify=True, timeout=10)
    
    if r.status_code == STATUS_FAILURE:
        raise Exception("[-] Failed to send request to \"iplocation.net\"")
    elif r.status_code == STATUS_BADREQUEST:
        raise Exception("[!] Failed to complete the request")
    elif r.status_code == STATUS_SUCCESS:
        ret = True
        parse_output(r.text)
    else:
        raise Exception("[-!-] Unknown error !")
