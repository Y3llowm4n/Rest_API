import requests

BASE= "http://127.0.0.1:5000/"

# When adjusting the data, only change the values after the :

# With this query you can ADD videos to the database
response = requests.put(BASE + "video/5", {"name": "ldasdas", "views": 932, "likes": 38} )
print(response.json())
input()

# With this query you can UPDATE names, views and likes of stored video
response = requests.patch(BASE + "video/4", {"name": "Dropping Divans Alloy", "views": 932, "likes": 38})
print(response.json())
input()

# with this query you can GET a certain video which is stored in database
response = requests.get(BASE + "video/3")
print(response.json())
input()