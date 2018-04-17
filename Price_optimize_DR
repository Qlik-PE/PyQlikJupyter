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
opened_app = ega.open_doc('de1eb0ac-7c1c-406d-a9b6-4fde5d201183') ##Executive Dashboard
app_handle = ega.get_handle(opened_app)

### Define Dimensions of hypercube
hc_inline_dim = Structs.nx_inline_dimension_def(['id', 'predicted_loss', 'renewal_price', 'review_scores', 'region', 'last_review'])

### Set sorting of Dimension by Measure
hc_mes_sort = Structs.nx_sort_by()

### Define Measure of hypercube
#hc_inline_mes = Structs.nx_inline_measure_def([])

import pandas as pd
import datarobot as dr
import json

# Modelling API parameters
token = 'StcF5iwvv8IAjk9Mytl0e8EKkS35hWeA'
host = 'https://qlik.orm.datarobot.com'
username = 'chris.larsen@qlik.com'

dr.Client(token=token, endpoint='%s/api/v2' % host)

# Prediction API parameters
prediction_host = 'https://qlik.orm.datarobot.com'
headers = {'Content-Type': 'application/json', 'datarobot-key': '94d2823a-cd48-8be3-03de-fd0f58515e66'}

loss_model_id = "5ad4d867c2674e17de32822a"
loss_project_id = "5ad4d836e3cd9b0e5e90b89f"

conversion_model_id = "5ad4d9a6c2674e476194eb47"
conversion_project_id = "5ad4d933e3cd9b11099173dc"

# Prediction API function for 1 JSON
import requests, sys

def predict_API_call(host, headers, username, token, model_id, project_id, data, classif=True):
    response = requests.post('%s/api/v1/%s/%s/predict' % (host, project_id, model_id),
                            auth=(username, token), data=data, headers=headers)
    output = response.json()
    if classif:
        predictions = [record['class_probabilities']['1.0'] 
                       for record in output['predictions']]
    else:
        predictions = [record['prediction'] for record in output['predictions']]
    return predictions

conversions = predict_API_call(host=prediction_host, 
                         headers=headers, 
                         username=username, 
                         token=token, 
                         model_id=conversion_model_id,
                         project_id=conversion_project_id,
                         data=rows_json)

table = pd.DataFrame({'price': rows.renewal_price,
                      'conversion': conversions,
                      'loss': rows['predicted_loss']})

# Compute optimal price
table['profitability'] = table.conversion * (table.price*(table.loss*1.2) - table.loss)/100.
best_i = table.profitability.argmax()
print 'Optimal price: %.3f' % ((table.price.iloc[best_i] * table.loss.iloc[best_i])*1.2/100.)
print 'Expected conversion: %.3f \n' % table.conversion.iloc[best_i]
print table

%matplotlib inline
import matplotlib.pyplot as plt

dr_green = '#03c75f'
dr_white = '#ffffff'
dr_purple = '#65147D'
dr_dense_green = '#018f4f'
dr_dark_blue = '#08233F'
dr_blue = '#1F77B4'
dr_orange = '#FF7F0E'

fig = plt.figure(figsize=(8, 8))
axes = fig.add_subplot(1, 1, 1, facecolor=dr_dark_blue)

plt.scatter(table.price, table.profitability, color=dr_green)
plt.plot(table.price, table.profitability, color=dr_green)
plt.title('Profitability')
plt.xlabel('Price (discounted vs current level)')
plt.ylabel('Profitability')
