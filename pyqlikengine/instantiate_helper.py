import structs as structs
from engine_communicator import *
from engine_global_api import *
from engine_app_api import *
from engine_generic_object_api import *
from engine_field_api import *
import engine_field_api
# from engine_communicator import SecureEngineCommunicator

host = "cloudera.qlik.com"
proxyPrefix = "jupyter"
userDirectory = "CLOUDERA"
userId = "user_1"
privateKey = "./private.key"

conn = SecureEngineCommunicator(host, proxyPrefix, userDirectory, userId, privateKey)
efa = engine_field_api.EngineFieldApi(conn)
Structs = structs.Structs()
egoa = EngineGenericObjectApi(conn)
ega = EngineGlobalApi(conn)
eaa = EngineAppApi(conn)
conn.ws.recv()
