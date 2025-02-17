from Project import ChatBook



cha = ChatBook()

lst = [1,2,3,3]
len(lst) ## calling function


cha = ChatBook()

#cha.menu() # calling methos using object
#print(cha.name)

#### Encapsulation
# we dont want to show all the methods and attributes of you 'CLASS' to user or team member we can use encapsulation

# Apply encapsulation
#print(cha.__name)  # see in the Project.py file and __name attribute you can see but you can access becuase it is encapsulated. you can access using (obj._classname__attributename

#print(cha._ChatBook__name) # type: ignore

## Getter and setter method

print(cha.get_name())

cha.set_name("vikas X")

print(cha.get_name())