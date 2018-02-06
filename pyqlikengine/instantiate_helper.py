from engine_communicator import EngineCommunicator
from engine_global_api import EngineGlobalApi
from engine_app_api import EngineAppApi
from engine_communicator import SecureEngineCommunicator

host = "cloudera.qlik.com"
proxyPrefix = "jupyter"
userDirectory = "CLOUDERA"
userId = "user_1"
privateKey = "./private.key"

conn = SecureEngineCommunicator(host, proxyPrefix, userDirectory, userId, privateKey)
import engine_communicator
import engine_global_api
import engine_app_api
from engine_generic_object_api import EngineGenericObjectApi
import engine_field_api
import structs
conn = SecureEngineCommunicator(host, proxyPrefix, userDirectory, userId, privateKey)
efa = engine_field_api.EngineFieldApi(conn)
Structs = structs.Structs()
egoa = EngineGenericObjectApi(conn)
ega = EngineGlobalApi(conn)
eaa = EngineAppApi(conn)
conn.ws.recv()
