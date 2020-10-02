# importing the requests library 
import requests 
  
# api-endpoint 
URL = "http://exampleAPI/getRandomNumbers"

# get
response = requests.get(url = URL, params = None)

# transforming data to json
data = response.json()

# Using the data to do something
result = 0
for item in data:
    result += item

print(data)
print(result)

