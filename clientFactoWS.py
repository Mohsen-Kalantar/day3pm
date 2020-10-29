import requests
 
response = requests.post("http://jpf-PC:5000/")
# 
print(response.status_code)
print(response.text)

