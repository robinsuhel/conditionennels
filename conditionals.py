name = input("What's your name: ")
age = int(input("How old are you: "))
year = str(2017-age)
print(name + " you born in the year "+ year)

if age > 17:
	print("You are adult! You can see a rated R movie")
elif age < 17 and age > 12:
	print("You are teenager! You can see a rated PG-13 movie")
else:
	print("You are a child! You can only see rated PG movies")