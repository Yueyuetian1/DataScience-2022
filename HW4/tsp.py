
from random import choice
import numpy as np

from routes import route


dt = np.dtype([("place_start", str, 100), ("place_end", str, 100), ("distance", np.float32)])
data_set = np.array(route, dtype=dt)


def all_places():
    """Finds unique places
    array([["A", "A"],
    ["A", "B"]])
    """
    places = {}
    place_set = set(data_set["place_end"])
    for place in place_set:
        places[place] = ""
    return places


def greedy_tsp():
    """Select the next path to travel based on the shortest, nearest path"""

    itinerary = []
    places = all_places()
    starting_place = choice(list(places.keys()))
    # print "starting_place: %s" % starting_place
    placees_visited = {}
    # we want to iterate through all cities once
    count = 1
    while True:
        possible_routes = []
        # print "starting place: %s" % starting_place
        for path in data_set:
            if starting_place in path["place_start"]:
                # we can't go to places we have already visited
                if path["place_end"] in placees_visited:
                    continue
                else:
                    # print "path: ", path
                    possible_routes.append(path)

        if not possible_routes:
            break
        # append this to itinerary
        route = sorted(possible_routes, key=lambda dist: dist[2]).pop(0)
        # print "Route(%s): %s " % (count, route)
        count += 1
        itinerary.append(route)
        # add this place to the visited place list
        placees_visited[route[0]] = count
        # print "place_visited: %s " % place_visited
        # reset the starting_place to the next place
        starting_place = route[1]
        # print "itinerary: %s" % itinerary
    return itinerary

def get_total_distance(complete_itinerary):
    distance = sum(z for x, y, z in complete_itinerary)
    return round(distance,3)

def lowest_simulation(num):
    routes = {}
    for _ in range(num):
        itinerary = greedy_tsp()
        distance = get_total_distance(itinerary)
        routes[distance] = itinerary
    shortest_distance = min(routes.keys())
    tsp_route = routes[shortest_distance]
    return shortest_distance, tsp_route

def tsp(iterations):
    """runs everything"""
    print
    if iterations != 0:
        distance, tsp_route = lowest_simulation(iterations)
        print("Running simulation %s times" % iterations)
        print("Shortest Distance: %s" % distance)
        print("Optimal Route: %s" % tsp_route)
        return tsp_route, distance
    else:
        # print "All Routes: %s" % data_set
        itinerary = greedy_tsp()
        distance = get_total_distance(itinerary)
        print("Optimal Route: %s" % itinerary)
        print("Distance: %s" % distance)
        return itinerary, distance

# if __name__ == "__main__":
#     tsp()
