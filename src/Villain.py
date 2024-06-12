import copy
import requests
import json
import urllib3
# Disable https warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import utils

# Define machine and proto to use
machine = ""
proto = ""
port = ""
base_url = ""

# Define account to use
username = ""
password = ""
account = ""

debug_mode = True

headers = {
    'Content-Type': 'application/json'
}

def compose_account():
    account = {
        "username": username,
        "password": password
    }
    return account

# Function to get authentication token
def get_auth_token():
    try:
        auth_url = base_url + "/api/auth"
        payload = json.dumps(account)
        response = requests.post(auth_url, headers=headers, data=payload, verify=False, stream=True)
        if response.status_code == 200:
            token = response.text.split()[1]
            if not token:
                raise ValueError("Token not found in response")
            return token
        else:
            handle_http_error(response)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    
def check_token(token):
    if token:
        print("Token retrieved successfully:", token)
    else:
        print("Failed to retrieve token")    
        return False

# Function to make an authenticated request using the token
def make_authenticated_request(token):
    # Define the URL and headers for the authenticated request
    api_url = base_url + "/api/elements/127.0.0.1/config/processorC"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    try:
        print(headers)
        response = requests.get(api_url, headers=headers, verify=False)
        if response.status_code == 200:
            return response.json()
        else: 
            handle_http_error(response)                         
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def config_ipVidTx():
    token = get_auth_token()
    if token: 
        payloadVid = copy.deepcopy(utils.ipVidTx.CONFIG_IPVIDTX)
        payloadVid['fme_ip'] = machine
        
        ipVidTxCtrl = list()
        for row in input_configs: 
            if row.flow_format == "2110-20-V":
                idx = utils.idx_by_process_ipVidTx(row.processor) + int(row.pgm_n)
                elm = utils.ipVidTx(idx=idx,
                                    VidTxPriIPaddr=row.mcast_red,
                                    VidTxPriUDPport=int(row.port),
                                    VidTxSecIPaddr=row.mcast_blue,
                                    VidTxSecUDPport=int(row.port),
                                    VidTxEnable=eval(row.enable))
                ipVidTxCtrl.append(elm.to_dict())
        payloadVid['config']['ipVidTxCtrl'] = ipVidTxCtrl
        
        with open(str('ipVidTx') + '.json', 'w') as file_a:
            json.dump(payloadVid, file_a, indent=2)
        
        if debug_mode:
            print ("ipVidTx json printed")
            return
        else: 
            api_url = base_url + "/api/elements/" +  machine + "/config/ipVidTx"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            payloadVid['config'] = json.dumps(payloadVid['config'])
            response = requests.put(api_url, data=json.dumps(payloadVid), headers=headers, verify=False, stream=True)
            if response.status_code == 200: 
                print("Video audio 2110 configured")
            else: 
                handle_http_error(response=response)
    else:
        print("Failed to retrieve token")    
        return False        
    
def config_ipAncTx():
    token = get_auth_token()
    if token: 
        payloadAnc = copy.deepcopy(utils.ipAncTx.CONFIG_IPANCTX)
        payloadAnc['fme_ip'] = machine
        
        ipAncTxCtrl = list()
        for row in input_configs: 
            if row.flow_format == "2110-10_M":
                idx = ((utils.idx_by_process_ipVidTx(row.processor) + int(row.pgm_n)) * 4) - 3
                elm = utils.ipAncTx(idx=idx,
                                    AncTxPriIPaddr=row.mcast_red,
                                    AncTxPriUDPport=int(row.port),
                                    AncTxSecIPaddr=row.mcast_blue,
                                    AncTxSecUDPport=int(row.port),
                                    AncTxEnable=eval(row.enable))
                ipAncTxCtrl.append(elm.to_dict())
        payloadAnc['config']['ipAncTxCtrl'] = ipAncTxCtrl
        
        with open(str('ipAncTx') + '.json', 'w') as file_a:
            json.dump(payloadAnc, file_a, indent=2)
        
        if debug_mode:
            print ("ipAncTx json printed")
            return
        else: 
            api_url = base_url + "/api/elements/" +  machine + "/config/ipAncTx"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            payloadAnc['config'] = json.dumps(payloadAnc['config'])
            response = requests.put(api_url, data=json.dumps(payloadAnc), headers=headers, verify=False, stream=True)
            if response.status_code == 200: 
                print("Ancillary Data 2110 configured")
            else: 
                handle_http_error(response=response)
    else:
        print("Failed to retrieve token")    
        return False          
    
def config_ipAudTx():
    token = get_auth_token()
    if token: 
        payloadAud = copy.deepcopy(utils.ipAudTx.CONFIG_IPAUDTX)
        payloadAud['fme_ip'] = machine
        
        ipAudTxCtrl = list()
        audTxRouting = list()
        for row in input_configs: 
            if row.flow_format == "2110-30 A Grp1 8ch":
                idx = ((utils.idx_by_process_ipVidTx(row.processor) + int(row.pgm_n)) * 16) - 15
                elm = utils.ipAudTx(idx=idx,
                                    AudTxPriIPaddr=row.mcast_red,
                                    AudTxPriUDPport=int(row.port),
                                    AudTxSecIPaddr=row.mcast_blue,
                                    AudTxSecUDPport=int(row.port),
                                    AudTxEnable=eval(row.enable))
                ipAudTxCtrl.append(elm.to_dict())
                routingElm = utils.audTxRouting(idx=idx,
                                                AudTxCh1Select=1, AudTxCh2Select=2, AudTxCh3Select=3, AudTxCh4Select=4,
                                                AudTxCh5Select=5, AudTxCh6Select=6, AudTxCh7Select=7, AudTxCh8Select=8)
                audTxRouting.append(routingElm.to_dict())
            elif row.flow_format == "2110-30 A Grp2 8ch": 
                idx = ((utils.idx_by_process_ipVidTx(row.processor) + int(row.pgm_n)) * 16) - 14
                elm = utils.ipAudTx(idx=idx,
                                    AudTxPriIPaddr=row.mcast_red,
                                    AudTxPriUDPport=int(row.port),
                                    AudTxSecIPaddr=row.mcast_blue,
                                    AudTxSecUDPport=int(row.port),
                                    AudTxEnable=eval(row.enable))
                ipAudTxCtrl.append(elm.to_dict())
                routingElm = utils.audTxRouting(idx=idx,
                                                AudTxCh1Select=9, AudTxCh2Select=10, AudTxCh3Select=11, AudTxCh4Select=12,
                                                AudTxCh5Select=13, AudTxCh6Select=14, AudTxCh7Select=15, AudTxCh8Select=16)
                audTxRouting.append(routingElm.to_dict())                
        payloadAud['config']['ipAudTxCtrl'] = ipAudTxCtrl
        payloadAud['config']['AudTxRouting'] = audTxRouting
          
        with open(str('ipAudTx') + '.json', 'w') as file_a:
            json.dump(payloadAud, file_a, indent=2)
        
        if debug_mode:
            print ("ipAncTx json printed")
            return
        else: 
            api_url = base_url + "/api/elements/" +  machine + "/config/ipAudTx"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            payloadAud['config'] = json.dumps(payloadAud['config'])
            response = requests.put(api_url, data=json.dumps(payloadAud), headers=headers, verify=False, stream=True)
            if response.status_code == 200: 
                print("Audio streams channel 1 and 2 configured")
            else: 
                handle_http_error(response=response)
    else:
        print("Failed to retrieve token")    
        return False       

def handle_http_error(response):
    print(str(response.raw))
    error = {
                'httpCode': response.status_code,
                'error': response.text,
            }
    print(response.status_code)
    print(response.text)
    with open(str('error') + '.json', 'w') as file_a:
        json.dump(error, file_a, indent=2)

if __name__ == "__main__":
    # Main process
    # Load JSON data from the files
    with open('SNPTarget.json', 'r') as file_a:
        snpInfo = json.load(file_a)    
    
    # Define protocol info
    machine = snpInfo['snp']['machine']
    proto = snpInfo['snp']['proto']
    port = snpInfo['snp']['port']
    base_url = str(proto + "://" + machine + ":" + port)
    
    # Define user
    username = snpInfo['snp']['account']['username']
    password = snpInfo['snp']['account']['password']
    account = compose_account()
    
    # Get input config 
    file_path = 'input.csv'
    input_configs = utils.parse_csv(file_path)    
    
    # Define if use debug mode
    debug_mode = snpInfo['debug']
    
    if snpInfo['ipVidTx'] == True:
        config_ipVidTx()
    
    if snpInfo['ipAncTx'] == True:
        config_ipAncTx()
        
    if snpInfo['ipAudTx'] == True:
        config_ipAudTx()
    # Get the authentication token
    # token = get_auth_token()
    # if token:
    #     print("Token retrieved successfully:", token)
    #     # Make the authenticated request using the token
    #     response = make_authenticated_request(token)
    #     if response:
    #         print("Authenticated request successful:", response['config'])
    #     else:
    #         print("Authenticated request failed")
    # else:
    #     print("Failed to retrieve token")
