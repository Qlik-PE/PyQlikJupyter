### Install dependencies (Run first time project started)
# !pip install -r requirements.txt

### Import Libraries
from pyqlikengine.engine_communicator import EngineCommunicator
from pyqlikengine.engine_global_api import EngineGlobalApi
from pyqlikengine.engine_app_api import EngineAppApi
from pyqlikengine.engine_communicator import SecureEngineCommunicator
import pyqlikengine.engine_communicator
import pyqlikengine.engine_global_api
import pyqlikengine.engine_app_api
import pyqlikengine.engine_generic_object_api
import pyqlikengine.engine_field_api
import pyqlikengine.structs

host = "cloudera.qlik.com"
proxyPrefix = "jupyter"
userDirectory = "CLOUDERA"
userId = "user_1"
privateKey = "./private.key"

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
    
### Connect to desired app    
opened_app = ega.open_doc('8921dfe7-f46c-437c-bdb3-eb16c768793f') ##Executive Dashboard
app_handle = ega.get_handle(opened_app)

### Define Dimensions of hypercube
hc_inline_dim = Structs.nx_inline_dimension_def(["Customer","Order Number"])

### Set sorting of Dimension by Measure
hc_mes_sort = Structs.nx_sort_by()

### Define Measure of hypercube
hc_inline_mes = Structs.nx_inline_measure_def(["=Sum([Sales Amount])", "=Sum([Sales Quantity])"])

### Build hypercube from above definition
hc_dim = Structs.nx_hypercube_dimensions(hc_inline_dim)
hc_mes = Structs.nx_hypercube_measure(hc_mes_sort, hc_inline_mes)
nx_page = Structs.nx_page(0, 0, 2500, 4)
hc_def = Structs.hypercube_def("$", hc_dim, hc_mes, [nx_page])
hc_response = eaa.create_object(app_handle, "CH01", "Chart", "qHyperCubeDef", hc_def)
hc_handle = ega.get_handle(hc_response)
print hc_response

### Get contents of the hypercube
egoa.get_layout(hc_handle)

### Identify field to make selection on
lb_field = eaa.get_field(app_handle, "Customer")
fld_handle = ega.get_handle(lb_field)

### Set values to select in chosen field above
values_to_select = [{'qText': 'Fins'}, {'qText': 'Bizmarts'}, {'qText': 'Benedict'}, {'qText': 'Earth'}, {'qText': 'Gate'}]
sel_res = efa.select_values(fld_handle,values_to_select)
#desel_res = eaa.clear_all(app_handle);

### Retrieve newly selected data in hypercube
hc_data = egoa.get_hypercube_data(hc_handle, "/qHyperCubeDef", [nx_page])

elems = hc_data["qDataPages"][0]['qMatrix']

print elems

dim1_list = []
dim2_list = []
mes1_list = []
mes2_list = []

for elem in range(len(elems)):
    dim1_list.append(elems[elem][0]["qText"])
    dim2_list.append(elems[elem][1]["qText"])
    mes1_list.append(elems[elem][2]["qNum"])
    mes2_list.append(int(elems[elem][3]["qNum"]))

### Close connection
#conn.close_qvengine_connection(conn)


### Print dimension lists
print(dim1_list)
print(dim2_list)

### Print measure lists
print(mes1_list)
print(mes2_list)

############ VISUALIZE #############

### Import necessarily libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

### Load data
d = {'customer':dim1_list, 'orders':dim2_list, 'sales':mes1_list, 'qty':mes2_list} 
df = pd.DataFrame(d)

## Inspect data frame
df

d1 = {'sales':mes1_list, 'qty':mes2_list}
df1 = pd.DataFrame(d1)

### Set up a factorplot
sns.factorplot(x='orders', y='sales', hue='customer', data=df, scale = .5)

### Try a StripPlot
sns.stripplot(x='customer', y='sales', data=df, jitter=0.05, linewidth=1);

### Try a Scatterplot
sns.lmplot('sales', 'qty', data=df, fit_reg=False)

sns.set(style="whitegrid")

### Simple Bar Plot
sns.barplot(x=df.customer, y=df.sales, data=df.customer.reset_index())

### KDE Plot
sns.kdeplot(df.sales, df.qty)

### Distribution Plot of Sales/Qty
sns.distplot(df['sales'])
sns.distplot(df['qty'])
    
### KDE Histogram of Sales
for col in 'xy':
    sns.kdeplot(df['sales'], shade=True)
    
### Jointplot of sales/qty
with sns.axes_style('white'):
    sns.jointplot("sales", "qty", df, kind='kde');

### Another Jointplot
sns.jointplot(data=df, x='sales', y='qty', kind='reg', color='g')
    
### Violin Plot
sns.violinplot([df.sales, df.qty])


### Cluster Map of just sales/qty
sns.clustermap(df1)

### Heat Map of just sales/qty
sns.heatmap([df1.sales, df1.qty], annot=True, fmt="f")

### BoxPlot
sns.boxplot([df.sales, df.qty])
