import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Year': "",   
                            'Month': "1",   
                            'Day': "1",   
                            'Hour': "1",   
                            'Minute': "1",   
                            'Temperature': "1",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/71b88133511644ef8f1c4cf7bf9767b2/services/fafb58d26d6d42ffbe1e9c7d49f59598/execute?api-version=2.0&format=swagger'
api_key = 'abc123' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Year': "2018",   
                            'Month': "07",   
                            'Day': "1",   
                            'Hour': "0",   
                            'Minute': "0",   
                            'Temperature': "0",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/71b88133511644ef8f1c4cf7bf9767b2/services/fafb58d26d6d42ffbe1e9c7d49f59598/execute?api-version=2.0&format=swagger'
api_key = 'oEBxosfRYRo4K3xKffkKPycYxyZUOffbqy/1iMU5GcyEZi9gDz2cN3x2CHBahQC+IZS8GL2dKMa9/99pMhoXQA==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
