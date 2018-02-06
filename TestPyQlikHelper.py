from pyqlikengine.engine_communicator import EngineCommunicator
from pyqlikengine.engine_global_api import EngineGlobalApi
from pyqlikengine.engine_app_api import EngineAppApi
from pyqlikengine.engine_communicator import SecureEngineCommunicator

host = "cloudera.qlik.com"
proxyPrefix = "jupyter"
userDirectory = "CLOUDERA"
userId = "user_1"
privateKey = "./private.key"

conn = SecureEngineCommunicator(host, proxyPrefix, userDirectory, userId, privateKey)
conn.ws.recv()
ega = EngineGlobalApi(conn)

# eaa = EngineAppApi(conn)

import pyqlikengine.engine_communicator
import pyqlikengine.engine_global_api
import pyqlikengine.engine_app_api
from pyqlikengine.engine_generic_object_api import EngineGenericObjectApi
import pyqlikengine.engine_field_api
import pyqlikengine.structs
conn = SecureEngineCommunicator(host, proxyPrefix, userDirectory, userId, privateKey)
efa = pyqlikengine.engine_field_api.EngineFieldApi(conn)
Structs = pyqlikengine.structs.Structs()
egoa = pyqlikengine.engine_generic_object_api.EngineGenericObjectApi(conn)
ega = EngineGlobalApi(conn)
eaa = EngineAppApi(conn)
conn.ws.recv()

apps = ega.get_doc_list()
### List Apps available (identify the App GUID to open)
for app in apps:
    print app['qTitle']
    
opened_app = ega.open_doc('8921dfe7-f46c-437c-bdb3-eb16c768793f') ##Executive Dashboard
app_handle = ega.get_handle(opened_app)


from pyqlikengine import engine_helper as pyqlikhelper

dimensions = ["Customer","Order Number"]
measures = ["=Sum([Sales Amount])", "=Avg([Sales Amount])"]
df = pyqlikhelper.getDataFrame(conn, app_handle, dimensions, measures)

############ VISUALIZE #############

df.plot()
print df
