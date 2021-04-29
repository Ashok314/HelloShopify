import requests

#get meta field info 
url='replace_me'
x = requests.get('replace_me')
print(x.status_code)
print(x.content)
print(x.json())

# if doesnot exist post 0  ,; if status_code is less than 400, otherwise False
if (x.ok == True):
    myobj ={
    "metafield": {
    "namespace": "global",
    "key": "test",
    "value": 0,
    "value_type": "integer"
    }
    }
    x = requests.post(url, data = myobj)
    
    print("\n",x.json())

# #if exists post 1 
else:
    myobj ={
    "metafield": {
    "namespace": "global",
    "key": "test",
    "value": 1,
    "value_type": "integer"
    }
    }
    x = requests.post(url, data = myobj)
    
    print("\n",x.json())

# #check metafield
# y = requests.get('replace_me')
# print("\n after post",y.status_code)
# print(y.content)
# print(y.json())