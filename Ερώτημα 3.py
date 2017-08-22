def attraction(): 
    landmarks=str(input("For which landmarks are you interested in?\n(Choose between aquarium, art_gallery, church, museum, park, zoo):"))
    while landmarks!= "aquarium" and landmarks!= "art_gallery" and landmarks!= "church" and landmarks!= "museum" and landmarks!= "park" and landmarks!= "zoo":
        landmarks=str(input("Wrong choice. For which landmarks are you interested in?\n(Choose between aquarium, art_gallery, church, museum, park, zoo):"))
    return landmarks
x=attraction()
print(x)
