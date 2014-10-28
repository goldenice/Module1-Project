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

#Nijmegen
add_point(51.817423, 5.869934, 0.02, 10)
#Marmelhorst
add_line(51.817423, 5.869934, 51.89069, 6.434845, 0.01)
#Ulft
add_point(51.89302, 6.383987, 0.001)
#Ulft - Barchem
add_line(51.89302, 6.383987, 52.130116, 6.448578, 0.01)
#Barchem
add_point(52.130116, 6.448578, 0.001)
#Grolsch
add_point(52.207528, 6.817611, 0.001)
#Enschede
add_point(52.225907, 6.893867, 0.06, 10)
#NEEEEEEderland
add_point(52.196160, 5.442792, 1.5)
#Campus
add_line(52.207528, 6.817611, 52.244215, 6.850565, 0.001)
add_point(52.242117, 6.854262, 0.01, 5)
#Campus sportcentrum
add_point(52.244215, 6.850565, 0.0004, 10)

"""for i in range(199):
    p = random_location(random_point())
    print ("%s \t %s"%(p["lat"], p["lng"]))

"""
bata = open("bata_2014.txt", "r", encoding='utf-8')
batanew = ""
points_orig = points[:]
data = bata.readlines()
total_length = len(data)

for t in data:
    p = random_location(random_point())
    batanew += (t.replace('"coordinates":null', '"coordinates": "'+str(p["lat"])+", "+str(p["lng"])+'"'))
bata.close()
batan = open("bata_2014_w_loc.txt", "w", encoding='utf-8')
batan.write(batanew)
batan.close()
   
    

