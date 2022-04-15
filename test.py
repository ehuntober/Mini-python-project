
# import time , sys

# name = input("Enter your name: ")
# print(f"Hi {name}, How are you doing")
# feedback = input("What do you want to do now? ")
# print("I do not want to do that. Good bye!")
# time.sleep(3)
# sys.exit()

# Copy 
# the copy module provides shallow and deep object copying operations for lists, tuples ,dictionaries, and class instances 

# import copy
# x = [1,2, 3, [4,5,6]]
# y = copy.copy(x)
# print(y)
# print(y==x)


# import copy

# listone = [{ "name":"Andre"} , 3, 2]
# listtwo = copy.copy(listone)
# listthree = copy.deepcopy(listone)
# listone[0]["name"] = "Renata"
# listone.append("Python")
# print(listone)
# print(listtwo)
# print(listthree)


import os
os.rename(learns.txt,lesr.txt)

"""

rotor
The rotor module implements a permutation-based encryption and decryption engine. (The design is 
derived from the Enigma device, a machine used by the Germans to encrypt messages during WWII.)
 
>>> import rotor
>>> message = raw_input("Enter the message")
>>> key = raw_input("Enter the key")
>>> newr = rotor.newrotor(key)
>>> enc = newr.encrypt(message)
>>> print "The encoded message is: ", repr(enc)
>>> dec = newr.decrypt(enc)
>>> print "The decoded message is: ", repr(dec)


"""iices print 'the decoded print """"
