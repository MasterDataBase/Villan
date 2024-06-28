import csv

class ipVidTx: 
    def __init__(self, idx,  VidTxPriIPaddr, VidTxPriUDPport, VidTxSecIPaddr,  VidTxSecUDPport, 
                 VidTxPriWANSel="WAN 1", VidTxSecWANSel = "WAN 2",
                 VidTxEnable=True, VidTxMode="ST2110-20", VidTxSDExtSize=0, VidTxPackMode="GPM"):
        self.idx = idx
        self.VidTxEnable = VidTxEnable
        self.VidTxSDExtSize = VidTxSDExtSize
        self.VidTxPackMode = VidTxPackMode
        self.VidTxMode = VidTxMode
        self.VidTxPriIPaddr = VidTxPriIPaddr
        self.VidTxPriWANSel = VidTxPriWANSel
        self.VidTxPriUDPport = VidTxPriUDPport
        self.VidTxSecIPaddr = VidTxSecIPaddr
        self.VidTxSecWANSel = VidTxSecWANSel
        self.VidTxSecUDPport = VidTxSecUDPport    

    def to_dict(self):
        return {
            "idx": self.idx,
            "VidTxEnable": self.VidTxEnable,
            "VidTxSDExtSize": self.VidTxSDExtSize,
            "VidTxPackMode": self.VidTxPackMode,
            "VidTxMode": self.VidTxMode,
            "VidTxPriIPaddr": self.VidTxPriIPaddr,
            "VidTxPriWANSel": self.VidTxPriWANSel,
            "VidTxPriUDPport": self.VidTxPriUDPport,
            "VidTxSecIPaddr": self.VidTxSecIPaddr,
            "VidTxSecWANSel": self.VidTxSecWANSel,
            "VidTxSecUDPport": self.VidTxSecUDPport
        }
        
    def __repr__(self):
        return (f"VidTxCtrl(VidTxSecUDPport={self.VidTxSecUDPport}, VidTxPriIPaddr={self.VidTxPriIPaddr}, "
                f"VidTxSDExtSize={self.VidTxSDExtSize}, VidTxMode={self.VidTxMode}, VidTxSecIPaddr={self.VidTxSecIPaddr}, "
                f"VidTxPackMode={self.VidTxPackMode}, VidTxPriWANSel={self.VidTxPriWANSel}, VidTxPriUDPport={self.VidTxPriUDPport}, "
                f"VidTxSecWANSel={self.VidTxSecWANSel}, idx={self.idx}, VidTxEnable={self.VidTxEnable})")
        
    CONFIG_IPVIDTX = {
        "type": "ipVidTx",
        "fme_ip": "",
        "name": "ipVidTx",
        "object_ID": "ipVidTx",
        "parent_object_ID": "snpIpTx",
        "config": {
            "ipVidTxCtrl": {}
        }
    }
    
class ipAncTx:
    def __init__(self,  idx, AncTxPriIPaddr, AncTxPriUDPport, AncTxSecIPaddr, AncTxSecUDPport,
                 AncTxPriWANSel="WAN 1", AncTxSecWANSel="WAN 2", AncTxTag="", AncTxEnable=True,
                 ):
        self.idx = idx
        self.AncTxPriIPaddr = AncTxPriIPaddr
        self.AncTxPriUDPport = AncTxPriUDPport
        self.AncTxSecIPaddr = AncTxSecIPaddr
        self.AncTxSecUDPport = AncTxSecUDPport
        self.AncTxPriWANSel = AncTxPriWANSel
        self.AncTxSecWANSel = AncTxSecWANSel
        self.AncTxTag = AncTxTag
        self.AncTxEnable = AncTxEnable

    def to_dict(self):
        return {
            "idx": self.idx,
            "AncTxPriIPaddr": self.AncTxPriIPaddr,
            "AncTxPriUDPport": self.AncTxPriUDPport,
            "AncTxSecIPaddr": self.AncTxSecIPaddr,
            "AncTxSecUDPport": self.AncTxSecUDPport,
            "AncTxPriWANSel": self.AncTxPriWANSel,
            "AncTxSecWANSel": self.AncTxSecWANSel,
            "AncTxTag": self.AncTxTag,
            "AncTxEnable": self.AncTxEnable,
    }
    
    def __repr__(self):
        return (f"ipAncTx(AncTxTag={self.AncTxTag}, AncTxSecUDPport={self.AncTxSecUDPport}, "
                f"AncTxSecIPaddr={self.AncTxSecIPaddr}, AncTxPriUDPport={self.AncTxPriUDPport}, "
                f"AncTxEnable={self.AncTxEnable}, AncTxPriWANSel={self.AncTxPriWANSel}, "
                f"idx={self.idx}, AncTxPriIPaddr={self.AncTxPriIPaddr}, AncTxSecWANSel={self.AncTxSecWANSel})")    
        
    CONFIG_IPANCTX = {
        "type": "ipAncTx",
        "fme_ip": "",
        "name": "ipAncTx",
        "object_ID": "ipAncTx",
        "parent_object_ID": "snpIpTx",
        "config":{
            "ipAncTxCtrl": {}
        }
    }        
    
class ipAudTx:
    def __init__(self, 
                idx, AudTxPriIPaddr, AudTxPriUDPport, AudTxSecIPaddr, AudTxSecUDPport,
                AudTxNumCh = 8, AudTxTag = "", AudTxEnable = True, AudTxMode = "ST2110-30", AudTxPriWANSel = "WAN 1", AudTxSecWANSel = "WAN 2"):
        self.idx = idx
        self.AudTxNumCh = AudTxNumCh
        self.AudTxTag = AudTxTag
        self.AudTxMode = AudTxMode
        self.AudTxPriIPaddr = AudTxPriIPaddr
        self.AudTxPriUDPport = AudTxPriUDPport
        self.AudTxPriWANSel = AudTxPriWANSel 
        self.AudTxSecIPaddr = AudTxSecIPaddr
        self.AudTxSecUDPport = AudTxSecUDPport
        self.AudTxSecWANSel = AudTxSecWANSel
        self.AudTxEnable = AudTxEnable

    def __repr__(self):
        return (f"AudioStreamConfig(AudTxNumCh={self.AudTxNumCh}, AudTxPriIPaddr={self.AudTxPriIPaddr}, AudTxTag={self.AudTxTag},"
                f"AudTxPriUDPport={self.AudTxPriUDPport}, AudTxEnable={self.AudTxEnable}, AudTxSecIPaddr={self.AudTxSecIPaddr},"
                f"AudTxMode={self.AudTxMode}, AudTxPriWANSel={self.AudTxPriWANSel}, idx={self.idx}," 
                f"AudTxSecUDPport={self.AudTxSecUDPport}, AudTxSecWANSel='{self.AudTxSecWANSel}")

    def to_dict(self):
        return {
            "idx": self.idx,
            "AudTxNumCh": self.AudTxNumCh,
            "AudTxTag": self.AudTxTag,
            "AudTxMode": self.AudTxMode,
            "AudTxPriIPaddr": self.AudTxPriIPaddr,
            "AudTxPriUDPport": self.AudTxPriUDPport,
            "AudTxPriWANSel": self.AudTxPriWANSel,
            "AudTxSecIPaddr": self.AudTxSecIPaddr,
            "AudTxSecUDPport": self.AudTxSecUDPport,
            "AudTxSecWANSel": self.AudTxSecWANSel,
            "AudTxEnable": self.AudTxEnable,
        }    

    CONFIG_IPAUDTX = {
        "type": "ipAudTx",
        "fme_ip": "10.130.13.232",
        "name": "ipAudTx",
        "object_ID": "ipAudTx",
        "parent_object_ID": "snpIpTx",
        "config":{
            "ipAudTxCtrl": {},
            "AudTxRouting": {}
        }
    }

class audTxRouting:
    def __init__(self, idx, AudTxCh1Select, AudTxCh2Select, AudTxCh3Select, AudTxCh4Select, AudTxCh5Select, AudTxCh6Select, AudTxCh7Select, AudTxCh8Select):
        self.idx = idx
        self.AudTxCh1Select = AudTxCh1Select
        self.AudTxCh2Select = AudTxCh2Select
        self.AudTxCh3Select = AudTxCh3Select
        self.AudTxCh4Select = AudTxCh4Select
        self.AudTxCh5Select = AudTxCh5Select
        self.AudTxCh6Select = AudTxCh6Select
        self.AudTxCh7Select = AudTxCh7Select
        self.AudTxCh8Select = AudTxCh8Select
        
    def __repr__(self):
        return (f"AudTxRouting(AudTxCh1Select={self.AudTxCh1Select}, AudTxCh2Select={self.AudTxCh2Select}, "
                f"AudTxCh3Select={self.AudTxCh3Select}, AudTxCh4Select={self.AudTxCh4Select}, "
                f"AudTxCh5Select={self.AudTxCh5Select}, AudTxCh6Select={self.AudTxCh6Select}, "
                f"AudTxCh7Select={self.AudTxCh7Select}, AudTxCh8Select={self.AudTxCh8Select}, idx={self.idx})")
        
    def to_dict(self):
        return {
            "idx": self.idx,
            "AudTxCh1Select": self.AudTxCh1Select,
            "AudTxCh2Select": self.AudTxCh2Select,
            "AudTxCh3Select": self.AudTxCh3Select,
            "AudTxCh4Select": self.AudTxCh4Select,
            "AudTxCh5Select": self.AudTxCh5Select,
            "AudTxCh6Select": self.AudTxCh6Select,
            "AudTxCh7Select": self.AudTxCh7Select,
            "AudTxCh8Select": self.AudTxCh8Select,
        }   
        
class ipAudRx:
    def __init__(self,  idx, AudRxStreamSelect, AudRxChannelInStream):
        self.idx = idx
        self.AudRxStreamSelect = AudRxStreamSelect
        self.AudRxChannelInStream = AudRxChannelInStream

    def __repr__(self):
        return (f"AudRxRouting(idx={self.idx}, AudRxStreamSelect={self.AudRxStreamSelect}, AudRxChannelInStream={self.AudRxChannelInStream}")

    def to_dict(self):
        return {
            "idx": self.idx,
            "AudRxStreamSelect": self.AudRxStreamSelect,
            "AudRxChannelInStream": self.AudRxChannelInStream
        }    

    CONFIG_IPAUDRX = {
        "type": "ipAudRx",
        "fme_ip": "",
        "name": "ipAudRx",
        "object_ID": "ipAudRx",
        "parent_object_ID": "snpIpRx",
        "config":{
            "AudRxRouting": {}
        }
    }
    
class ipVidRx: 
    def __init__(self, idx,  VidRxNextPriIPaddr, VidRxNextPriUDPport, VidRxPriMcastSrc1, VidRxNextSecIPaddr,  VidRxNextSecUDPport, VidRxSecMcastSrc1,
                 VidRxPriWANSel="WAN 1", VidRxSecWANSel = "WAN 1", VidRxEnable=True, VidRxMode="ST2110-20"):
        self.idx = idx
        self.VidRxEnable = VidRxEnable
        self.VidRxMode = VidRxMode
        self.VidRxNextPriIPaddr = VidRxNextPriIPaddr
        self.VidRxPriWANSel = VidRxPriWANSel
        self.VidRxNextPriUDPport = VidRxNextPriUDPport
        self.VidRxPriMcastSrc1 = VidRxPriMcastSrc1
        self.VidRxNextSecIPaddr = VidRxNextSecIPaddr
        self.VidRxSecWANSel = VidRxSecWANSel
        self.VidRxNextSecUDPport = VidRxNextSecUDPport
        self.VidRxSecMcastSrc1 = VidRxSecMcastSrc1

    def to_dict(self):
        return {
            "idx": self.idx,
            "VidRxEnable": self.VidRxEnable,
            "VidRxMode": self.VidRxMode,
            "VidRxNextPriIPaddr": self.VidRxNextPriIPaddr,
            "VidRxPriWANSel": self.VidRxPriWANSel,
            "VidRxNextPriUDPport": self.VidRxNextPriUDPport,
            "VidRxPriMcastSrc1": self.VidRxPriMcastSrc1,
            "VidRxNextSecIPaddr": self.VidRxNextSecIPaddr,
            "VidRxSecWANSel": self.VidRxSecWANSel,
            "VidRxNextSecUDPport": self.VidRxNextSecUDPport,
            "VidRxSecMcastSrc1": self.VidRxSecMcastSrc1
        }
        
    def __repr__(self):
        return (f"ipVidRxCtrl(idx={self.idx}, VidRxEnable={self.VidRxEnable}, VidRxMode={self.VidRxMode}, "
                f"VidRxNextPriIPaddr={self.VidRxNextPriIPaddr}, VidRxPriWANSel={self.VidRxPriWANSel}, "
                f"VidRxNextPriUDPport={self.VidRxNextPriUDPport}, VidRxPriMcastSrc1={self.VidRxPriMcastSrc1}, "
                f"VidRxNextSecIPaddr={self.VidRxNextSecIPaddr}, VidRxSecWANSel={self.VidRxSecWANSel}, "
                f"VidRxNextSecUDPport={self.VidRxNextSecUDPport} , VidRxSecMcastSrc1={self.VidRxSecMcastSrc1})")
        
        
        
    CONFIG_IPVIDRX = {
        "type": "ipVidRx",
        "fme_ip": "",
        "name": "ipVidRx",
        "object_ID": "ipVidRx",
        "parent_object_ID": "snpIpRx",
        "config": {
            "ipVidRxCtrl": {}
        }
    }    
        
class ipAudRx_v2:
    def __init__(self,  idx, AudRxNextPriIPaddr, AudRxPriMcastSrc1, AudRxNextPriUDPport,  
                 AudRxSecMcastSrc1, AudRxNextSecIPaddr, AudRxNextSecUDPport,  
                 AudRxPriWANSel = "WAN 1", AudRxSecWANSel = "WAN 1", AudRxEnable = False, AudRxMode = "ST2110-30", AudRxNumCh = 8):
        self.idx = idx
        self.AudRxNextPriIPaddr = AudRxNextPriIPaddr
        self.AudRxPriMcastSrc1 = AudRxPriMcastSrc1
        self.AudRxNextPriUDPport = AudRxNextPriUDPport
        self.AudRxPriWANSel = AudRxPriWANSel
        self.AudRxSecMcastSrc1 = AudRxSecMcastSrc1
        self.AudRxNextSecIPaddr = AudRxNextSecIPaddr
        self.AudRxNextSecUDPport = AudRxNextSecUDPport
        self.AudRxSecWANSel = AudRxSecWANSel
        self.AudRxEnable = AudRxEnable
        self.AudRxMode = AudRxMode
        self.AudRxNumCh = AudRxNumCh

    def __repr__(self):
        return (f"AudRx(idx={self.idx}, AudRxNextPriIPaddr={self.AudRxNextPriIPaddr}, AudRxPriMcastSrc1={self.AudRxPriMcastSrc1}, "
                f"AudRxNextPriUDPport={self.AudRxNextPriUDPport}, AudRxPriWANSel={self.AudRxPriWANSel}, "
                f"AudRxSecMcastSrc1={self.AudRxSecMcastSrc1}, AudRxNextSecIPaddr={self.AudRxNextSecIPaddr},"
                f"AudRxNextSecUDPport={self.AudRxNextSecUDPport}, AudRxSecWANSel={self.AudRxSecWANSel}, AudRxEnable={self.AudRxEnable}, "
                f"AudRxMode={self.AudRxMode}, AudRxNumCh={self.AudRxNumCh})")

    def to_dict(self):
        return {
            "idx": self.idx,
            "AudRxNextPriIPaddr": self.AudRxNextPriIPaddr,
            "AudRxPriMcastSrc1": self.AudRxPriMcastSrc1,
            "AudRxNextPriUDPport": self.AudRxNextPriUDPport,
            "AudRxPriWANSel": self.AudRxPriWANSel,
            "AudRxSecMcastSrc1": self.AudRxSecMcastSrc1,
            "AudRxNextSecIPaddr": self.AudRxNextSecIPaddr,
            "AudRxNextSecUDPport": self.AudRxNextSecUDPport,
            "AudRxSecWANSel": self.AudRxSecWANSel,
            "AudRxEnable": self.AudRxEnable,
            "AudRxMode": self.AudRxMode,
            "AudRxNumCh": self.AudRxNumCh
        }    

    CONFIG_IPAUDRX = {
        "type": "ipAudRx",
        "fme_ip": "",
        "name": "ipAudRx",
        "object_ID": "ipAudRx",
        "parent_object_ID": "snpIpRx",
        "config":{
            "ipAudRxCtrl": {}
        }
    }     
    
class ipAncRx:
    def __init__(self,  idx, AncRxNextPriIPaddr, AncRxNextPriUDPport, AncRxPriMcastSrc1,
                 AncRxNextSecIPaddr, AncRxNextSecUDPport, AncRxSecMcastSrc1,
                 AncRxPriWANSel="WAN 1", AncRxSecWANSel="WAN 1", AncRxEnable=True):
        self.idx = idx
        self.AncRxNextPriIPaddr = AncRxNextPriIPaddr
        self.AncRxNextPriUDPport = AncRxNextPriUDPport
        self.AncRxPriMcastSrc1 = AncRxPriMcastSrc1
        self.AncRxNextSecIPaddr = AncRxNextSecIPaddr
        self.AncRxNextSecUDPport = AncRxNextSecUDPport
        self.AncRxSecMcastSrc1 = AncRxSecMcastSrc1
        self.AncRxPriWANSel = AncRxPriWANSel
        self.AncRxSecWANSel = AncRxSecWANSel
        self.AncRxEnable = AncRxEnable

    def to_dict(self):
        return {
            "idx": self.idx,
            "AncRxNextPriIPaddr": self.AncRxNextPriIPaddr,
            "AncRxNextPriUDPport": self.AncRxNextPriUDPport,
            "AncRxPriMcastSrc1": self.AncRxPriMcastSrc1,
            "AncRxNextSecIPaddr": self.AncRxNextSecIPaddr,
            "AncRxNextSecUDPport": self.AncRxNextSecUDPport,
            "AncRxSecMcastSrc1": self.AncRxSecMcastSrc1,
            "AncRxPriWANSel": self.AncRxPriWANSel,
            "AncRxSecWANSel": self.AncRxSecWANSel,
            "AncRxEnable": self.AncRxEnable,
    }
    
    def __repr__(self):
        return (f"ipAncRx(AncRxNextPriIPaddr={self.AncRxNextPriIPaddr}, AncRxNextPriUDPport={self.AncRxNextPriUDPport}, "
                f"AncRxPriMcastSrc1={self.AncRxPriMcastSrc1}, AncRxNextSecIPaddr={self.AncRxNextSecIPaddr}, AncRxNextSecUDPport={self.AncRxNextSecUDPport},"
                f"AncRxSecMcastSrc1={self.AncRxSecMcastSrc1}, "
                f"AncRxPriWANSel={self.AncRxPriWANSel}, AncRxSecWANSel={self.AncRxSecWANSel}, AncRxEnable={self.AncRxEnable}, idx={self.idx})")    
        
    CONFIG_IPANCTX = {
        "type": "ipAncRx",
        "fme_ip": "",
        "name": "ipAncRx",
        "object_ID": "ipAncRx",
        "parent_object_ID": "snpIpRx",
        "config":{
            "ipAncRxCtrl": {}
        }
    }        
             

class CsvRow:
    def __init__(self, hostname, processor, pgm_n, flow_format, ssm_red, ssm_blue, mcast_red, mcast_blue, port, enable):
        self.hostname = hostname
        self.processor = processor
        self.pgm_n = pgm_n
        self.flow_format = flow_format
        self.ssm_red = ssm_red
        self.ssm_blue = ssm_blue
        self.mcast_red = mcast_red
        self.mcast_blue = mcast_blue
        self.port = port
        self.enable = enable

    def __repr__(self):
        return (f"CsvRow(hostname={self.hostname}, processore={self.processor}, pgm_n={self.pgm_n}, "
                f"tipo_formato_flusso={self.flow_format}, ssm_no_set1={self.ssm_red}, "
                f"ssm_no_set2={self.ssm_blue}, mcast_red={self.mcast_red}, mcast_blue={self.mcast_blue}, "
                f"port={self.port}, enable={self.enable})")
        
class CsvRowAudRx:
    def __init__(self, hostname, processor, pgm_n, source_stream, source_channel):
        self.hostname = hostname
        self.processor = processor
        self.pgm_n = pgm_n
        self.source_stream = source_stream,
        self.source_channel = source_channel

    def __repr__(self):
        return (f"CsvRow(hostname={self.hostname}, processore={self.processor}, pgm_n={self.pgm_n}, "
                f"source_stream={self.source_stream}, source_channel={self.source_channel}")        

def parse_output_config(file_path):
    rows = []
    with open(file_path, mode='r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')
        for row in csvreader:
            csv_row = CsvRow(
                hostname=row['Hostname'],
                processor=row['Processore'],
                pgm_n=row['PGM N.'],
                flow_format=row['Tipo formato flusso'],
                ssm_red=row['SSM No set'],
                ssm_blue=row['SSM No set'],
                mcast_red=row['Mcast Red'],
                mcast_blue=row['Mcast Blue'],
                port=row['Port'],
                enable=row['Enable']
            )
            rows.append(csv_row)
    return rows

def parse_input_config(file_path):
    rows = []
    with open(file_path, mode='r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')
        for row in csvreader:
            csv_row = CsvRow(
                hostname=row['Hostname'],
                processor=row['Processore'],
                pgm_n=row['PGM_N'],
                flow_format=row['Tipo_formato_flusso'],
                ssm_red=row['SSM_Red'],
                ssm_blue=row['SSM_Blue'],
                mcast_red=row['Mcast_Red'],
                mcast_blue=row['Mcast_Blue'],
                port=row['Port'],
                enable=row['Enable']
            )
            rows.append(csv_row)
    return rows

def parse_audio_config(file_path):
    rows = []
    with open(file_path, mode='r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')
        for row in csvreader:
            csv_row = CsvRowAudRx(
                hostname=row['Hostname'],
                processor=row['Processore'],
                pgm_n=row['PGM N.'],
                source_stream=row['Sorgente'],
                source_channel=row['Channel']
            )
            rows.append(csv_row)
    return rows

def idx_by_process_ipVidTx(processor):
    if processor == "A":
        return 0
    elif processor == "B":
        return 8
    elif processor == "C":
        return 16        
    elif processor == "D":
        return 24
    
def idx_by_process_ipAncTx(processor):
    if processor == "A":
        return 0
    elif processor == "B":
        return 32
    elif processor == "C":
        return 64        
    elif processor == "D":
        return 96    
    
def idx_by_process_ipAudTx(processor):
    if processor == "A":
        return 0
    elif processor == "B":
        return 128
    elif processor == "C":
        return 256        
    elif processor == "D":
        return 384        
    
def idx_by_process_ipAudRx(processor):
    if processor == "A":
        return 0
    elif processor == "B":
        return 128
    elif processor == "C":
        return 256        
    elif processor == "D":
        return 384            