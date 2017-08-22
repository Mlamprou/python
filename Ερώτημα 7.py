from googleplaces import GooglePlaces, types, lang
import wikipedia

def get_place_details(place):
	try:
		return wikipedia.summary(place)
	except:
		return "-"

def get_city_landmarks(google_api_key, city, landmark_types,limit=-1):
	google_places = GooglePlaces(google_api_key)
	query_result = google_places.nearby_search(
		location=city, 
		type=landmark_types)
	places_details=[]
	for place in query_result.places:
		places_details.append(place.name)
	return places_details[:limit]


def attraction(): 
    landmarks=str(input("For which landmarks are you interested in?\n(Choose between aquarium, art_gallery, church, museum, park, zoo):"))
    while landmarks!= "aquarium" and landmarks!= "art_gallery" and landmarks!= "church" and landmarks!= "museum" and landmarks!= "park" and landmarks!= "zoo":
        landmarks=str(input("Wrong choice. For which landmarks are you interested in?\n(Choose between aquarium, art_gallery, church, museum, park, zoo):"))
    return landmarks

y=str(input("Which city are you visiting?:")) 
z=attraction()
w=get_city_landmarks("AIzaSyCcB6x1vFGflBctPmhwPaHWf2zdDghKVXY", y, z)


number=1
for i in w:
    print('\n',number,'.',i,'\n')
    number=number+1

a=int(input("Write the number of the landmark for which you are interested in (press 0 to exit):"))
while a!=0:
    p=get_place_details(w[a-1])
    print('\n',p)
    number=1
    for i in w:
        print('\n',number,'.',i,'\n')
        number=number+1
    a=int(input("Write the number of the landmark for which you are interested in (press 0 to exit):"))
    




