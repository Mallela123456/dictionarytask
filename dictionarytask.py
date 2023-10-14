#1.Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

#dict_1 = {0: 10, 1: 20}
#dict_1.update({2:30})
#print(dict_1) 

#2.Write a Python script to check whether a given key already exists in a dictionary.
#dict_1 = {2:30,3:40,4:90}
#def key_1(l):
 #   if l in dict_1:
  #      print("Yes")
   # else:
    #    print("No")
#key_1(2)
#key_1(10)

#3.Write a Python program to iterate over dictionaries using for loops
#dict_1 = {1:20,2:30,3:40,4:50}
#for k,v in dict_1.items():
 #   print(k,v)
 
 
 
#4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

#dict_1 =  {}
#for x in range(1,16):
 #   dict_1[x] = (x**2)
#print(dict_1)


#5.Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#Sample string : 'marolix technology'
#Expected output: {'m': 1, 'a': 1, 'o': 3, 'l': 2, 'i': 1, 'x': 1, 't': 1, 'e': 1,'c': 1, 'h': 1, 'n': 1, 'g': 1,'y':1}

#string_1 = "marolix technology"
#dict_1 = {}
#for char in string_1:
 #   if char in dict_1:
  #      dict_1[char] += 1
   # else:
    #    dict_1[char] =1
#print(dict_1)

#6. Write a Python program to sum all the items in a dictionary.
#dict_1 = {1:20,2:30,3:40}
#print(sum(dict_1.values()))

#7.Write a Python program to combine two dictionary by adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#d3 = d2
#for i,j in d1.items():
 #   if i in d2:
  #      d3[i] = j + d2[i]
   # else:
    #    d3[i] = j 
#print(d3)   

#8.Write a Python program to access dictionary key's element by index.
#Expected Output:
#physics
#math
#chemistry 

#dict_1 = {"physics": 100,"math":90,"chemistry":90}
#print(dict_1.keys())

#9.Write a Python program to remove a key from a dictionary.

#keys = {"name":"srikanth","age" : 22,"address" : "guntur"}
#print(keys.pop("name"))
#print(keys)


#10.Write a Python script to merge two Python dictionaries.
dict_1 = {"name":"srikanth","address":"guntur"}
dict_2 = {2:30,4:60,5:90}
dict_3 = dict_1.copy()
dict_3.update(dict_2)
print(dict_3) 
