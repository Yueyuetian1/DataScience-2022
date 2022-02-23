"""
Step 1: Goolgle Serach key words: "Find all of the locations that Hemingway lived"
Step 2: Select the first url: https://www.nytimes.com/2015/10/04/travel/places-where-hemingway-lived-or-traveled.html
Step 3: Find the places in the content
Step 4: Search longitude, latitude in Google map
"""

locate = {
    'Oak Park, Illinois, America': (41.883340, -87.800000),
    'Quai Saint-Michel, Paris': (48.863190, 2.339754),
    'PAMPLONA, Spain': (42.812790, -1.643320),
    'MADRID, Spain': (40.416670, -3.716667),
    'Havana, Cuba': (23.136670, -82.358890),
    'Key West, Florida, America': (24.559750, -81.783710),
    'KETCHUM, IDAHO, America': (43.681110, -114.371700)
}
# Oak Park, Illinois, America
# from haversine import haversine, Unit
# places = list(locate.keys())
# place_num = len(places)
# routes = list()
# for i in range(place_num):
#     for j in range(place_num):
#         if j == i:
#             continue
#         point1 = places[i]
#         point2 = places[j]
#         distance = haversine(locate[point1], locate[point2], unit=Unit.KILOMETERS)
#         routes.append((point1, point2, round(distance, 3)))
# print(routes)
