user_info= {
          "name":"soumith",
          "age":20,
          "fav-movies":["bahubali","saaho","radheshyam"],
          "fav-songs":["oo antaavaa","ennai vittu"]
}
if "name" in user_info:
          print("present")
else:
          print("not present")

if "soumith" in user_info.values():
          print("present")
else:
          print("not present")

# for i in user_info


user_info_values=user_info.values()
print(user_info_values)
print(type(user_info_values))



for i in user_info:
          print(i)
user_items=user_info.items()
print(user_items)
print(type(user_items))
for i,j in user_items:
          print(f"keys are {i} and values are {j}")