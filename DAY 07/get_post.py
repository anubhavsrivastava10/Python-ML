import requests
import json

host = "https://enekbqpdp360f.x.pipedream.net/"
data = {"firstname":"dev","language":"English"}
headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response1 = requests.post(host,data,headers)
    return response1

print ( post_method().text)


def get_method():
    response = requests.get("https://enekbqpdp360f.x.pipedream.net/get?firstname=Dev&language=English")
    return response

print (get_method().text)


#check on the site that data has been post and get