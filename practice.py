price = 9.99
discount = 0.2

finalPrice = price * ( 1- discount)

print(finalPrice)
print ("----------------------------------------------------------------------------------------")

######################################################################################################

name = "daddy"

greeting = "Hello {}"
with_name = greeting.format(name)

print (f"Hello, {name}")
print (with_name)
print ("----------------------------------------------------------------------------------------")
name = "mommmy"
print (f"Hello, {name}")
print (with_name)
print ("----------------------------------------------------------------------------------------")

######################################################################################################

name = input("Enter your name:")
print(name)
print ("----------------------------------------------------------------------------------------")

number = input("Enter your number:")
print(int(number)/ 10.8)
casted_number = int(number)
new_num = casted_number / 10
print(f"{casted_number} divided by 10 is {new_num:.2f}")

print ("----------------------------------------------------------------------------------------")

######################################################################################################

l = [ "Tom", "Mike", "Bob"] #list keep order elements can be added
t = ( "Timothy", "Michael", "Jimbo")  #tuple cannot be changed after initializing keep order
s = { "John", "Poe", "Lee"} #set cannot have duplicate values do not keep order

print(l[0])

l[0] = "Mom"

print(l[0])

l.append("Dad")
print(l)

s.add("John")
print(s)


friends = { "John", "Poe", "Lee"}
abroad = { "John", "Lee"}
siblings = {"Michael, Lee"}
local_friends = friends.difference(abroad)
print(local_friends)

sibs_friends = friends.union(siblings)

biz = {"Salene", "Phoebe", "Matt"}
science = {"Phoebe", "Harrison", "Kevin"}
biz_sci = biz.intersection(science)
print(biz_sci)

print ("----------------------------------------------------------------------------------------")
######################################################################################################

day = input("What is the day of the week:")
if day == "Monday":
    print("Have a great start to your week")
elif day == "Sunday":
    print("Praise da lord")
else:
    print("GG")

######################################################################################################

movies_watched = {"Batman", "Spider-Man" , "The Grinch"}
movie = input("What movie: ")
print(movie in movies_watched)



######################################################################################################

movies_watched = {"Batman", "Spider-Man" , "The Grinch"}
for movie in movies_watched:
    print(f"I watched {movie}")



######################################################################################################





######################################################################################################

