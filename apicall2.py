import requests as rq

Base_url = 'http://swaraj66.pythonanywhere.com/'
ss='0.00'
payload={'input':ss}
response=rq.get(Base_url,params=payload)
json_value=response.json()
rq_input1=json_value['input']
rq_input2=json_value['convert']

print("Value is -----------------------")
# Base_url = 'http://swaraj66.pythonanywhere.com/'
# ss='10'
# payload={'input':ss}
# response=rq.get(Base_url,params=payload)
# json_value=response.json()
# rq_input1=json_value['input']
# rq_input2=json_value['convert']

print(rq_input1)
print(rq_input2)