### Install dependencies (Run first time project started)
# !pip install -r requirements.txt

import datarobot as dr
import json
import pandas as pd
import requests, sys

### Instantiate PyQIX
from pyqlikengine import instantiate_helper as helper

### Get a list of apps
apps = helper.ega.get_doc_list()

### List Apps available (identify the App GUID to open)
for app in apps:
    print (app['qTitle']+'-'+app['qDocId'])

opened_app = helper.ega.open_doc('de1eb0ac-7c1c-406d-a9b6-4fde5d201183') ##Price Analysis
app_handle = helper.ega.get_handle(opened_app)


from pyqlikengine import engine_helper as pyqlikhelper

dimensions =["id","Rating_Class","Sub_Rating_Class","Renewal_class","Sub_Renewal_Class","Property_size","Residents","Commercial","Norm_monthly_rent","No_claim_Years","Previous_claims","Norm_area_m","Premium_remain","Premium_renew","Renewal_Type","crime_property_type","crime_residents","crime_area","crime_arson","crime_burglary","crime_neighbour_watch","crime_community","crime_risk","Geographical_risk","Weather_risk","ISO_cat","ISO_desc","review_scores","region","last_review"]
measures = []
selections = {"id": ["9120"]}
df = pyqlikhelper.getDataFrame(helper.conn, app_handle, measures, dimensions, selections)
df

row = df.loc[[0]]
row_json = row.to_json(orient='records')
print row_json

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
  
# read prediction file and filter on top row
test_data = pd.read_csv('test/test-data.csv', nrows=1)
row = test_data.loc[[0]]
row_json = row.to_json(orient='records')
print row_json  


#make prediction for expected loss
output = predict_API_call(host=prediction_host, 
                         headers=headers, 
                         username=username, 
                         token=token, 
                         model_id=loss_model_id,
                         project_id=loss_project_id,
                         data=row_json,
                         classif=False)
print 'Expected Loss: %.3f' % output[0]

# Add expected loss into the data
row[u'predicted_loss'] = output[0]

# Add price range from 80% to 120%, step 1%
rows = pd.concat([row]*41, ignore_index=True) # duplicate the row
rows['renewal_price'] = range(80,121)
rows = rows[['id', 'predicted_loss', 'renewal_price', 
             'review_scores', 'region', 'last_review']]
rows_json = rows.to_json(orient='records')


# Generate predictions from conversion model given the range of prices
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
