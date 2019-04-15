
import secrets
import json

from datetime import timedelta
from datetime import datetime  
from dateutil import parser
import time


data_string = """{
	"battery": 80, 
	"id": "47a038d5eb032640", 
	"magnetic_fieldz": -0.1484375, 
	"magnetic_fieldx": -0.3125, 
	"magnetic_fieldy": 0.515625, 
	"end": "1548194024.99", 
	"temperature": 25.5, 
	"cputemp1": 45.0, 
	"memory": 42.6, 
	"protocol_version": 2, 
	"current_motion": 420, 
	"te": "39.767373085", 
	"systemtime": "01/22/2019 16:53:44", 
	"cputemp": 43.0, 
	"uptime": 4870800, 
	"host": "Laptop", 
	"diskusage": "418124.2", 
	"ipaddress": "192.168.1.241", 
	"uuid": "20190122215344_2a41168e-31da-4ae7-bf62-0b300c69cd5b", 
	"is_moving": false, 
	"accelerationy": 0.015748031496062992, 
	"accelerationx": 0.0, 
	"accelerationz": 1.0236220472440944, 
	"starttime": "01/22/2019 16:53:05", 
	"rssi": -63, 
	"bt_addr": "fa:e2:20:6e:d4:a5"
   }"""



data = json.loads(data_string)



while True:
    id_Hex = secrets.token_hex(8)
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    now_delate = (parser.parse(now) - timedelta(seconds=15)).strftime("%d/%m/%Y %H:%M:%S")
    

    data['id']          = id_Hex
    data['systemtime']  = now
    data['starttime']   = now_delate 

    new_data = json.dumps(data, indent=2)
    print(new_data)
    time.sleep(4)

