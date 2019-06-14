import requests
import json

host = "http://httpbin.org/post"
data = {"Phone_Number":"1235467689","Name":"Aplha","College_Name":"ABC","Branch":"CSE"}
headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response1 = requests.post(host,data,headers)
    return response1

print ( post_method().text)


def get_method():
    response = requests.get("http://httpbin.org/get?Phone_Number=1235467689&Name=Aplha&College_Name=ABC&Branch=CSE")
    return response

print (get_method().text)

#my_data = json.loads(json_string)