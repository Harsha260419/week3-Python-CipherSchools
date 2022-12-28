user={}
name=input("enter your name: ")
age=int(input("enter your age: "))
fav_movies=input("enter your favorite movies seperated by comma: ").split(",")
fav_songs=input("enter your favorite songs seperated by comma: ").split(",")
user['Name']=name
user['age']=age
user['Favorite Movies']=fav_movies
user['Favorite Songs']=fav_songs
for key,value in user.items():
    print(f"{key}:{value}")