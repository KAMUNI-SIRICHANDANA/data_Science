#3.  mehfil(1,1) upto 7km but have to check the coordinator(6,7)

import math

def mehfilRestaurant(mehf1, mehf2, dist1, dist2, radius):
    distance = math.sqrt(((dist1 - mehf1) ** 2) + ((dist2 - mehf2) ** 2))
    
    if distance <= radius:
        print("The order can be delivered. Within", radius, "kms from the Mehfil Restaurant.")
    else:
        print("The order can't be delivered.As the distance is", distance, "kms")

mehfilRestaurant(1, 1, 6, 7, 7)
