# even_list =[]
# for i in range(100):
#     if i%2==0:
#         even_list.append(i)
# print(even_list)


#1.WAF which takes input of no. and calculates the sum of n natural no.s

# num = int(input("Enter number: "))
# sum=0
# for i in range(1,num+1):
#     sum = sum+i

# print(sum)


#2.input =     output = 9,14,14,27,60

# L1 = [1,2,5,7,10]
# L2 = [8,12,9,20,50]
# result = []
# for i in range(5):
#     add = L1[i] + L2[i]
#     result.append(add)
# print(result)



#3

# word = "mississippi"
# word_1 = list(word)
# word_2 = {}
# for i in word_1:
#     if i in word_1:
#        word_2[i] = word_1.count(i)
    
# print(word_2)


#4.    

# word = ["Dog","F","Horn","Fight"]
# count_word = {}
# for i in word:
#     count_word[i] = len(i)
# print(count_word)




#22/09/2025

#1.4,9,16,25,36,49,64,81,100

# list_ = [2,3,5,6,7,8,9,10]
# result = []
# for i in list_:
#     if i%2==0:
#         even_square = i**2
#         result.append(even_square)
# print(result)



#2.generate a list of squares of all the no.s from 1 to 50

# list_ = []
# for i in range(1,51):
#     list_.append(i**2)
# print(list_)


#square comprehence
# squares = [num**2 for num in range(1,51)]
# print(squares)

# dict_ = {}
# for i in range(1,5):
#     dict_[i] = i**2
# print(dict_)

#Dictionary comprehence
# sq_dict = {num:num**2 for num in range(10)}
# print(sq_dict)


# cities = ["Venice","Tokyo","Delhi","Dubai","Chennai","Bengaluru","Surat","Mumbai"]
# upper = []
# for i in cities:
#     upper.append(i.lower())
# print(upper)


# upper = [i.upper() for i in cities]
# print(upper)

# ones = [100 for i in range(10)]
# print(ones)

# ones = {i:0 for i in range(10)}
# print(ones)

# print([x **2 for x in range(20) if x%2==0])



 
# cities = ["Venice","Tokyo","Delhi","Dubai","Chennai","Bengaluru","Surat","Mumbai"]
# for i in cities:
#     print(i)
#     if i=="Chennai":
#         print("City found")
#         break 

# cities = ["Venice","Tokyo","Delhi","Dubai","Chennai","Bengaluru","Surat","Mumbai"]
# for i in cities:
#     print(i)
#     if i=="Chennai":
#         continue



#Q) Input = [[10,20,30],50,[20,10],[20]]   output = [10,20,30,50,20,10,20]
Input = [[10,20,30],"Tokyo",[20,10],[20]]
for i in Input:
    if type(i) == str:
        print(i)
    else:
        for j in i:
            print(j)

