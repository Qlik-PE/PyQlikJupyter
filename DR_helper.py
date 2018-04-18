import datarobot as dr

# Modelling API parameters
token = 'StcF5iwvv8IAjk9Mytl0e8EKkS35hWeA'
host = 'https://qlik.orm.datarobot.com'
username = 'chris.larsen@qlik.com'

dr.Client(token=token, endpoint='%s/api/v2' % host)

# Prediction API parameters
prediction_host = 'https://qlik.orm.datarobot.com'
headers = {'Content-Type': 'application/json', 'datarobot-key': '94d2823a-cd48-8be3-03de-fd0f58515e66'}
