from engine_communicator import EngineCommunicator
from engine_global_api import EngineGlobalApi
from engine_app_api import EngineAppApi
import time
import json

url = 'ws://localhost:4848/app'
conn = EngineCommunicator(url)
ega = EngineGlobalApi(conn)
eaa = EngineAppApi(conn)
#conn.connect()
doclist=ega.get_doc_list() 
for doc in doclist:
	print doc['qTitle']
	
#print conn.get_os_name()
#ega.create_app('theApp')
#time.sleep(1)
ega.open_doc('Executive Dashboard')
doc = ega.get_active_doc()
time.sleep(1)
handle = ega.get_doc_handle(doc)
print eaa.get_script(handle)
#ega.delete_app('C:\\Users\\cls\\Documents\\Qlik\\Sense\\Apps\\theApp.qvf')
conn.close_qvengine_connection(conn)