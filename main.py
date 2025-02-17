from Project import ChatBook



# cha = ChatBook()

# lst = [1,2,3,3]
# len(lst) ## calling function


# cha = ChatBook()

#cha.menu() # calling methos using object
#print(cha.name)

#### Encapsulation
# we dont want to show all the methods and attributes of you 'CLASS' to user or team member we can use encapsulation

# Apply encapsulation
#print(cha.__name)  # see in the Project.py file and __name attribute you can see but you can access becuase it is encapsulated. you can access using (obj._classname__attributename

#print(cha._ChatBook__name) # type: ignore

## Getter and setter method

# print(cha.get_name())

# cha.set_name("vikas X")

# print(cha.get_name())


#Static method 

'''
obj = ChatBook()
print(">>>>>>>obj>>>>>>",obj.id)

obj.id
obj1 = ChatBook()
print(">>>>>>obj1>>>>>>>",obj1.id)

obj2 = ChatBook()
print(">>>>>>obj2>>>>>>>",obj2.id)'''

obj = ChatBook()

print(obj.id)

# adding id as 10 using static method now start point is 10
ChatBook.set_id(10) 
obj2=ChatBook()
print(obj2.id)

#ChatBook.set_id(10) # so now count will be 11 bcz stating at 10 id
obj3=ChatBook()
print(obj3.id)