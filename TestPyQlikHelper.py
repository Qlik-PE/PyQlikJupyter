### Install dependencies (Run first time project started)
# !pip install -r requirements.txt

### Instantiate PyQIX
from pyqlikengine import instantiate_helper

### Get a list of apps
apps = ega.get_doc_list()

### List Apps available (identify the App GUID to open)
for app in apps:
    print app['qTitle']+'-'+app['qDocId']
    
opened_app = ega.open_doc('8921dfe7-f46c-437c-bdb3-eb16c768793f') ##Executive Dashboard
app_handle = ega.get_handle(opened_app)


from pyqlikengine import engine_helper as pyqlikhelper

dimensions = ["Customer","Order Number"]
measures = ["=Sum([Sales Amount])", "=Avg([Sales Amount])"]
selections = {"Customer": ["Sigma"]}
df = pyqlikhelper.getDataFrame(conn, app_handle, measures, dimensions, selections)
conn.close_qvengine_connection(conn)

############ VISUALIZE #############

df.plot()
print df
