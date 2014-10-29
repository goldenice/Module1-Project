import random
import math
points = []
g_weight = 0
def add_point(lat, lng, rad, weight = 1):
    global points
    global g_weight
    g_weight += weight
    points.append({"lat": lat, "lng": lng, "rad": rad, "weight": g_weight, "type": "point"})

def add_line(lat1, lng1, lat2, lng2, rad, weight = 1):
    global points
    global g_weight
    g_weight += weight
    points.append({"lat1": lat1, "lng1": lng1, "lat2": lat2, "lng2": lng2, "rad": rad, "weight": g_weight, "type": "line"})
def line_get_point(line):
    dx = line["lat1"]-line["lat2"]
    dy = line["lng1"]-line["lng2"]
    shift = random.random()
    lat = line["lat1"] - dx*shift
    lng = line["lng1"] - dy*shift
    rad = line["rad"]
    weight = line["weight"]
    return {"lat": lat, "lng": lng, "rad": rad, "weight": g_weight, "type": "point"}
    
    
def random_point():
    global points
    c = []
    for i in range(len(points)):
        for n in range(points[i]["weight"]):
            c.append(i)
    return points[random.choice(c)]

def random_location(point):
    if point["type"] == "line":
        point = line_get_point(point)
    lat = point["lat"]
    lng = point["lng"]
    rad = point["rad"]
    angle = random.random()*2*math.pi
    lat += random.random()*rad*math.cos(angle)
    lng += random.random()*rad*math.sin(angle)
    return {"lat": lat, "lng": lng}

def read_and_process_file(filename):
    bata = open(filename, "r", encoding='utf-8')
    batanew = ""
    data = bata.readlines()
    length = len(data)
    i = 0
    for t in data:
        if round((i/length)*100,1)%5 == 0:
            print(filename, (i/length)*100)
        p = random_location(random_point())
        t = t.replace('"coordinates":null', '"coordinates": {"coordinates" : ['+str(p["lng"])+", "+str(p["lat"])+']}')
        batanew += (t)
        i+=1
    bata.close()
    return batanew

#Nijmegen
add_point(51.817423, 5.869934, 0.02, 10)
#Ulft
add_point(51.89302, 6.383987, 0.001)
#Barchem
add_point(52.130116, 6.448578, 0.001)
#Grolsch
add_point(52.207528, 6.817611, 0.001)
#Enschede
add_point(52.225907, 6.893867, 0.06, 10)
#NEEEEEEderland
add_point(52.196160, 5.442792, 1.5)
#Campus
add_point(52.242117, 6.854262, 0.01, 5)
#Campus sportcentrum
add_point(52.244215, 6.850565, 0.0004, 10)

#Route bata
add_line(51.818936, 5.857026, 51.806031, 6.159757, 0.001)
add_line(51.806031, 6.159757, 51.838044, 6.249087, 0.001)
add_line(51.838044, 6.249087, 51.877831, 6.252928, 0.001)
add_line(51.877831, 6.252928, 51.874342, 6.378135, 0.001)
add_line(51.874342, 6.378135, 51.865997, 6.489831, 0.001)
add_line(51.865997, 6.489831, 51.951742, 6.481014, 0.001)
add_line(51.951742, 6.481014, 52.011272, 6.395645, 0.001)
add_line(52.011272, 6.395645, 52.078711, 6.358775, 0.001)
add_line(52.078711, 6.358775, 52.120069, 6.438016, 0.001)
add_line(52.120069, 6.438016, 52.162609, 6.429909, 0.001)
add_line(52.162609, 6.429909, 52.157278, 6.609974, 0.001)
add_line(52.157278, 6.609974, 52.174501, 6.734290, 0.001)
add_line(52.174501, 6.734290, 52.244135, 6.850530, 0.001)

filenames = ["bata_2014.txt", "batatweets.txt", "p2000.txt"]

"""for i in range(199):
    p = random_location(random_point())
    print ("%s \t %s"%(p["lat"], p["lng"]))

"""
new_file = ""
for filename in filenames:
    print("processing: ", filename)
    new_file += read_and_process_file(filename)


batan = open("data.txt", "w", encoding='utf-8')
batan.write(new_file)
batan.close()
