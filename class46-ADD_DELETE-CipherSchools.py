user_info= {
          "name":"soumith",
          "age":20,
          "fav-movies":["bahubali","saaho","radheshyam"],
          "fav-songs":["oo antaavaa","ennai vittu"]
}


user_info["fav-tunes"]=["awara"]
print(user_info)
user_pop=user_info.pop("fav-movies")
print(user_info)

popped_items=user_info.pop("fav-songs")
print(type(popped_items))
print(popped_items)




















