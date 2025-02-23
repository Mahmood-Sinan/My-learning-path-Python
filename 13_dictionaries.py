capitals = {"USA": "Washington D. C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(capitals.get("Japan"))
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()
# capitals.clear()
keys = capitals.keys()

# print(keys)
print("Keys - ",end = "")
for key in keys:
   print(key,end = " ")
print("\nValues - ", end = "")
values = capitals.values()
for value in values:
   print(value, end = " ")
print()
print("Printing key value pairs using .keys() method: ")
for key in keys:
   print(f"{key} - {capitals.get(key)}")

items = capitals.items() # returns a 2d tuple with each tuple being key value pair
print("Printing key value pairs using .items() method: ")
for key, value in items:
   print(f"{key}: {value}")
# print(capitals)