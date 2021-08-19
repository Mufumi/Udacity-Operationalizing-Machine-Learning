import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://9f17d6de-c0c8-4732-97c0-9a933582c741.southcentralus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = ""

# Two sets of data to score, so we get two results back
data = {
    "data": [
    {
      "age": 26,
      "job": "unkown",
      "marital": "single",
      "education": "high.school",
      "default": "unknown",
      "housing": "yes",
      "loan": "yes",
      "contact": "telephone",
      "month": "jun",
      "day_of_week": "wed",
      "duration": 524,
      "campaign": 15,
      "pdays": 999,
      "previous": 0,
      "poutcome": "nonexistent",
      "emp.var.rate": 1.4,
      "cons.price.idx": 94.465,
      "cons.conf.idx": -41.8,
      "euribor3m": 4.864,
      "nr.employed": 5228.1
    }
  ]
}


# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
