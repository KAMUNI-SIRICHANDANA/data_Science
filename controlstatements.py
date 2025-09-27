#1.WAFunction which takes any two no.s as the input and the operation as the input
#a+b --> 2+2=4

# def calulator(a,b,opt):
#     if opt=="+":
#         result = a+b
#     elif opt=="-":
#         result = a-b
#     elif opt=="*":
#         result = a*b
#     return result
# print(calulator(1,2,"+"))




#2.WAF person(1,2) D1(2,3) D2(8,11)   
#--> find euclidean distance between person --> D1 and D2


# import math 
# def cabbooking(per_Q1,per_Q2,cab1_Q1,cab1_Q2,cab2_Q1,cab2_Q2):
#     dist1 = math.sqrt(((cab1_Q1-per_Q1)**2) + ((cab1_Q2 - per_Q2)**2))
    
#     dist2 = math.sqrt(((cab2_Q1-per_Q1)**2) + ((cab2_Q2-per_Q2)**2))

#     if dist1 < dist2:
#         print("The nearest distance is ",dist1, "So,the cab confirmed for the Distance1")
#     else:
#         print("The nearest distance is ",dist2, "So, the cab confirmed for the Distance2")
        
# cabbooking(1,2,2,3,8,11)

user_loc = (10,15)
d1_loc = (12,18)
d2_loc = (2,5)

# def dist(point_1,point_2):
#     total_dist = ((point_2[0]-point_1[0])**2) + ((point_2[1]-point_1[1])**2)**0.5
#     return total_dist

# def driverAssign(user, d1, d2):
#     if dist(user, d1) < dist(user, d2):
#         print("Driver 1 Assigned")
#     else:
#         print("Driver 2 Assigned")

# driverAssign(user_loc, d1_loc, d2_loc)


#Method 3
import math

print(math.dist(user_loc,d1_loc))
print("---------------------")
print(math.dist(user_loc,d2_loc))


#3.even or odd



# def evenodd(n):
#     if n%2==0:
#         print("The number is even ")
#     else:
#         print("The number is odd ")

# evenodd(2)


#4.Given 3 angles of triangle check if it is a valid triangle
#a+b+c=180 
# def triangle(a,b,c,angle):
#     result = a+b+c
#     if result == angle:
#         print("The triangle is valid triangle")
#     else:
#         print("The triangle is not valid triangle")
# triangle(60,60,60,180)


#5.









    