import copy
import logging
import os
from pathlib import Path
import sys
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
            handle_http_error(response, "token")
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
        for row in output_configs: 
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
                handle_http_error(response=response, channel="ipVidTx")
    else:
        print("Failed to retrieve token")    
        return False        
    
def config_ipAncTx():
    token = get_auth_token()
    if token: 
        payloadAnc = copy.deepcopy(utils.ipAncTx.CONFIG_IPANCTX)
        payloadAnc['fme_ip'] = machine
        
        ipAncTxCtrl = list()
        for row in output_configs: 
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
                handle_http_error(response=response, channel="ipAncTx")
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
        for row in output_configs: 
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
                handle_http_error(response=response, channel="ipAudTx")
    else:
        print("Failed to retrieve token")    
        return False       
    
def config_ipAudRx_Routing():
    token = get_auth_token()
    if token: 
        payloadAud = copy.deepcopy(utils.ipAudRx.CONFIG_IPAUDRX)
        payloadAud['fme_ip'] = machine
        
        idx = (utils.idx_by_process_ipAudRx(audio_configs[0].processor) + int(audio_configs[0].source_channel))
        audRxRouting = list()
        for row in audio_configs:                 
            routingElm = utils.ipAudRx(idx=idx, AudRxStreamSelect=int(row.source_stream[0]), AudRxChannelInStream=int(row.source_channel))
            audRxRouting.append(routingElm.to_dict())
            idx = idx + 1
        payloadAud['config']['AudRxRouting'] = audRxRouting
          
        with open(str('ipAudRx_Routing') + '.json', 'w') as file_a:
            json.dump(payloadAud, file_a, indent=2)
        
        if debug_mode:
            print ("ipAudRx json printed")
            return
        else: 
            api_url = base_url + "/api/elements/" +  machine + "/config/ipAudRx"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            payloadAud['config'] = json.dumps(payloadAud['config'])
            response = requests.put(api_url, data=json.dumps(payloadAud), headers=headers, verify=False, stream=True)
            if response.status_code == 200: 
                print("Audio input streams 1 and 2 configured")
            else: 
                handle_http_error(response=response, channel="ipAudRx")
    else:
        print("Failed to retrieve token")    
        return False    
    
def config_ipVidRx():
    token = get_auth_token()
    if token: 
        payloadVid = copy.deepcopy(utils.ipVidRx.CONFIG_IPVIDRX)
        payloadVid['fme_ip'] = machine
        
        ipVidRxCtrl = list()
        for row in input_config: 
            if row.flow_format == "2110-20-V":
                idx = utils.idx_by_process_ipVidTx(row.processor) + int(row.pgm_n)
                elm = utils.ipVidRx(idx=idx,
                                    VidRxNextPriIPaddr=row.mcast_red,
                                    VidRxNextPriUDPport=int(row.port),
                                    VidRxPriMcastSrc1=row.ssm_red,
                                    VidRxNextSecIPaddr=row.mcast_blue,
                                    VidRxNextSecUDPport=int(row.port),
                                    VidRxSecMcastSrc1=row.ssm_blue,
                                    VidRxEnable=eval(row.enable))             
                ipVidRxCtrl.append(elm.to_dict())
        payloadVid['config']['ipVidRxCtrl'] = ipVidRxCtrl
        with open(str('ipVidRx') + '.json', 'w') as file_a:
            json.dump(payloadVid, file_a, indent=2)
        
        if debug_mode:
            print ("ipVidRx json printed")
            return
        else: 
            api_url = base_url + "/api/elements/" +  machine + "/config/ipVidRx"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            payloadVid['config'] = json.dumps(payloadVid['config'])
            response = requests.put(api_url, data=json.dumps(payloadVid), headers=headers, verify=False, stream=True)
            if response.status_code == 200: 
                print("Video input 2110 configured")
            else: 
                handle_http_error(response=response, channel="ipVidRx")
    else:
        print("Failed to retrieve token")    
        return False     
    
def config_ipAudRx():
    token = get_auth_token()
    if token: 
        payloadAud = copy.deepcopy(utils.ipAudRx_v2.CONFIG_IPAUDRX)
        payloadAud['fme_ip'] = machine
        
        ipAudRxCtrl = list()
        for row in input_config: 
            if row.flow_format == "2110-30 A Grp1 8ch":
                idx = ((utils.idx_by_process_ipVidTx(row.processor) + int(row.pgm_n)) * 16) - 15
                elm = utils.ipAudRx_v2(idx=idx,
                                    AudRxNextPriIPaddr=row.mcast_red,
                                    AudRxPriMcastSrc1=row.ssm_red,
                                    AudRxNextPriUDPport=int(row.port),
                                    AudRxNextSecIPaddr=row.mcast_blue,
                                    AudRxSecMcastSrc1 = row.ssm_blue,
                                    AudRxNextSecUDPport=int(row.port),
                                    AudRxEnable=eval(row.enable))
                ipAudRxCtrl.append(elm.to_dict())                     
                
            elif row.flow_format == "2110-30 A Grp2 8ch": 
                idx = ((utils.idx_by_process_ipVidTx(row.processor) + int(row.pgm_n)) * 16) - 14
                elm = utils.ipAudRx_v2(idx=idx,
                                    AudRxNextPriIPaddr=row.mcast_red,
                                    AudRxPriMcastSrc1=row.ssm_red,
                                    AudRxNextPriUDPport=int(row.port),
                                    AudRxNextSecIPaddr=row.mcast_blue,
                                    AudRxSecMcastSrc1 = row.ssm_blue,
                                    AudRxNextSecUDPport=int(row.port),
                                    AudRxEnable=eval(row.enable))
                ipAudRxCtrl.append(elm.to_dict())
        payloadAud['config']['ipAudRxCtrl'] = ipAudRxCtrl
        with open(str('ipAudRx') + '.json', 'w') as file_a:
            json.dump(payloadAud, file_a, indent=2)
        
        if debug_mode:
            print ("ipAudRx_Ctrl json printed")
            return
        else: 
            api_url = base_url + "/api/elements/" +  machine + "/config/ipAudRx"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            payloadAud['config'] = json.dumps(payloadAud['config'])
            response = requests.put(api_url, data=json.dumps(payloadAud), headers=headers, verify=False, stream=True)
            if response.status_code == 200: 
                print("Audio input 2110 configured")
            else: 
                handle_http_error(response=response, channel="ipAudRx")
    else:
        print("Failed to retrieve token")    
        return False       

def handle_http_error(response, channel):
    print(str(response.raw))
    error = {
                'httpCode': response.status_code,
                'error': response.text,
            }
    print(response.status_code)
    print(response.text)
    with open(str('error') + "-" + str(channel) + '.json', 'w') as file_a:
        json.dump(error, file_a, indent=2)

# if __name__ == "__main__":
# Main process
try:     
    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)
            
    print(application_path)
    
    cwd = application_path


    # Load JSON data from the files
    with open(cwd + '\SNPTarget.json', 'r') as file_a:
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

    # Get outputConfig file and value
    file_path = (cwd + '\outputConfig.csv')
    output_configs = utils.parse_output_config(file_path)    

    # Get inputAudio file and value 
    file_path = (cwd + '\inputAudio.csv')
    audio_configs = utils.parse_audio_config(file_path)    
    
    file_path = (cwd + '\inputConfig.csv')
    input_config = utils.parse_input_config(file_path)
    
    # Define if use debug mode
    debug_mode = snpInfo['debug']

    if snpInfo['ipVidTx'] == True:
        config_ipVidTx()

    if snpInfo['ipAncTx'] == True:
        config_ipAncTx()
        
    if snpInfo['ipAudTx'] == True:
        config_ipAudTx()
        
    if snpInfo['ipVidRx'] == True:
        config_ipVidRx()
        
    if snpInfo['ipAudRx_Routing'] == True:
        config_ipAudRx_Routing()
        
    if snpInfo['ipAudRx'] == True:
        config_ipAudRx()                

except:
    logging.exception('')
    with open(str('error') + '.json', 'w') as file_a:
        json.dump("error on execution", file_a, indent=2)