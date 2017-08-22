from googleplaces import GooglePlaces, types, lang
import wikipedia
import googlemaps
from datetime import datetime,timedelta

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

def get_route_details(google_api_key, point1, point2, type_of_transport, when=None):
	gmaps = googlemaps.Client(key=google_api_key)
	try:
		res = gmaps.distance_matrix(origins=point1,destinations=point2,mode=type_of_transport, departure_time=when)

		t = res['rows'][0]['elements'][0]['duration']['value']
		d = res['rows'][0]['elements'][0]['distance']['value']
		
		return [d/1000.0,t/60.0]
	except:
		return [0,0]   


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
k=0 
visit=[] #list with the landmarks that the user will visit
distance=[] #list with the distance of each landmark

while a!=0:
    p=get_place_details(w[a-1])
    print('\n',p)
    b=str(input('\nDo you want to visit this landmark? (type yes or no):'))
    if b=='yes':
            visit.insert(k,w[a-1])
            k=k+1
            print("\nLandmarks you are going to visit:\n")
            for i in visit:
                    print(i,"\n")
        
    number=1
    for i in w:
        print('\n',number,'.',i,'\n')
        number=number+1
    a=int(input("Write the number of the landmark for which you are interested in (press 0 to exit):\n"))
    

counter1=1
while counter1<len(visit):
    distance.insert(counter1-1, get_route_details("AIzaSyCcB6x1vFGflBctPmhwPaHWf2zdDghKVXY", visit[counter1-1], visit[counter1], "walking",None))
    counter1=counter1+1
    

counter2=0

counter=1
print("Places you are going to visit:")
for l in visit:
          print('\n',counter,'.',l,'\n')
          if counter2<len(distance):
           print('You will have to walk a distance of', distance[counter2][0], 'Km for', distance[counter2][1], 'minutes')
          counter=counter+1
          counter2=counter2+1

          
          
