import datarobot as dr

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
