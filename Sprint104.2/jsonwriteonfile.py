import json

data = [{
      "name": "Jonathan",
      "grades": [100, 98, 33, 55]
   },
   {
      "name": "Rona",
      "grades": [99, 22]
   },
   {
      "name": "Valentin",
      "grades": [99, 99, 98, 97, 95]
   }]

json_str = json.dumps(data)
with open("myfile.json", "w") as fileobj:
    fileobj.write(json_str)