### Install dependencies (Run first time project started)
# !pip install -r requirements.txt

### Instantiate PyQIX
from pyqlikengine import instantiate_helper as helper

### Get a list of apps
apps = helper.ega.get_doc_list()

### List Apps available (identify the App GUID to open)
for app in apps:
    print (app['qTitle']+'-'+app['qDocId'])
    
opened_app = helper.ega.open_doc('8921dfe7-f46c-437c-bdb3-eb16c768793f') ##Executive Dashboard
app_handle = helper.ega.get_handle(opened_app)


from pyqlikengine import engine_helper as pyqlikhelper

dimensions = ["Customer","Order Number"]
measures = ["=Sum([Sales Amount])", "=Avg([Sales Amount])"]
selections = {"Customer": ["Sigma"]}
df = pyqlikhelper.getDataFrame(helper.conn, app_handle, measures, dimensions, selections)

############ VISUALIZE #############

df.plot()
df
