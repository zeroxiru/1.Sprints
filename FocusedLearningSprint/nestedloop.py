
# for i in range(1, 6):
#     row = " "
#     for j in range(1, 11):
#         row += str(i * j)  + " "
#     print( str(i) + " " + row)
#
# for i in range(1, 6):
#     for j in range(1, 11):
#         print(i * j, end=" ")
#     print(i)

import json

json_str = '{"food": "Hamburger", "color": "Red"}'
print(type(json_str))

data = json.loads(json_str)
data = json.loads(json_str)
print(type(data))
print(data["food"])
print(data["color"])