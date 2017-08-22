def get_city_landmarks(google_api_key, city, landmark_types,limit=-1):
	google_places = GooglePlaces(google_api_key)
	query_result = google_places.nearby_search(
		location=city, 
		type=landmark_types)
	places_details=[]
	for place in query_result.places:
		places_details.append(place.name)
	return places_details[:limit]


from googleplaces import GooglePlaces, types, lang
import googlemaps

x=str(get_city_landmarks("AIzaSyCcB6x1vFGflBctPmhwPaHWf2zdDghKVXY", "London", "museum"))
print(x) 
