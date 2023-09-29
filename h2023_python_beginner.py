# PYTHON BEGINNER COURSE, autumn 2023
# v/Fredrik E. Juell, fredrik.e.juell@bi.no


##########################################
print("---------- 1. VARIABLES ----------")

# Variables - types
# Fish example
price = 30 		# price per kilo
weight = 1350	# kilo
origin = "Norway"
is_frozen = False

# Simple calculation
price_total = price*weight
print(price_total)
# Prettier print
print("The price of", weight, "kilos of fish is NOK", price_total)


# EXERCISE:
a = 1
b = 5
# Switch the values of a and b
#
# ANSWER:
x = a
a = b
b = x
print(a,b)
# Alternative: 
a,b = b,a



#########################################
print("---------- 2. IF-TESTS ----------")

# Indentation is important

# Test if price is low enough
if price < 30:
  print("I will buy.")

# Test for price interval and boolean
if 10 < price < 40 and not is_frozen:
  print("Yes, give it to me!")

# Nested if-statements
if price < 30:
  print("I will buy a lot.")
elif price < 40:
  print("I will buy less.")
else:
  print("Too expensive.")

# EXERCISE:
a = 3**12 # 3 to the power of 12
b = 2**19
# Write an if-test which prints the biggest number of a and b.

# ANSWER:
if a > b:
  print("a is biggest")
else:
  print("b is biggest")





#########################################
print("---------- 3. LISTS ----------")
species_fish = ["salmon", "cod", "shark"]
species_fish.append("halibut")				# Adds an element
species_fish = species_fish+["herring", "tuna"]	# Adds two elements

# Print to screen, to view the list.
print(species_fish)
# Print 2nd element
print(species_fish[1])
# Print elements fom. index 0 til 3 (e.g. element 1, 2, 3)
print(species_fish[0:3])
# Sort the list
species_fish.sort()
# Print number of elements in the list
print(len(species_fish))


# EXERCISE
# Define a list called music, that contains three genres of music of your choice.
# Print the last element in the list.

### --- BREAK --- ###

# ANSWER:
music = ["techno", "punk", "yacht rock"]
print(music[2])				# WHen length is known
print(music[len(music)-1])	# Complicated
print(music[-1])				# Best alternative




###############################################
print("---------- 4. DICTIONARIES ----------")

# Prices for species of fish
prices_fish = {"tuna":50, "cod":35, "herring":29, "salmon":23, "shark":25, "halibut":30}
# Extract price of "cod"
print(prices_fish["cod"])

# Another dict
fish_batch = {"species": "cod",
			        "weight": 30000,
            	"frozen": True,
            	"price": prices_fish["cod"]    # or "price": prices_fish[species]
            	}

# If batch is frozen and price under 40
if fish_batch["frozen"] and fish_batch["price"]<40:
  print("Yes, batch is frozen and price is", fish_batch["price"]*fish_batch["weight"])
else:
	print("Not frozen and/or too expensive")

# EXERCISE:
# Define a dictionary called mymusic, with three Key:Value-pairs.
# Let the Keys be the music genres in your list in the previous exercise.
# Let Value be True if you like this music genre, and False if not.
# Write a test that prints your liked genres from mymusic.

# SVAR:
mymusic = {"techno":True, "punk":True, "yacht rock":False}
mymusic = {music[0]:True, music[1]:True, music[2]:False}
if mymusic["techno"]:
  print("techno")
if mymusic["punk"]:
  print("punk")
if mymusic["yacht rock"]:
  print("yacht rock")




##########################################
print("---------- 5. FOR-LOOPS ----------")
# Test all prices in a for-loop, and answer each
for species in prices_fish:
	if prices_fish[species] < 30:
		print(f"I will buy {species} at price at {prices_fish[species]}")
	else:
		print(f"{species} is too expensive")

# Test all genres in a for-loop, and answer each
for key in mymusic:
  if mymusic[key]:
    print(key)
# Or alternativly
for key,value in mymusic.items():
  if value:
    print(key)


# EXERCISE:
# Here is a list of whole numbers from 0 to 100:
wholes = list(range(0,100))
# Make another list called quarters, that contain the numbers in wholes divided by 4. 
# View the result with print(quarters)
# Hint: Start by making an empty list quarters, and use a for-loop to add elements into it.

# ANSWER:
quarters = []
for x in wholes:
  quarters.append(x/4)
print(quarters)



##########################################
print("---------- 6. FUNCTIONS ----------")
# Defining a function to calculate total price of a batch of fish
def total_price(weight, price):
	price_total = weight*price
	return(price_total)

# Bruk funksjonen total_price, og lagre resultat i en variabel price_example
price_example = total_price(1600, 25)
print(price_example)

# EXERCISE:
# f(x) = x^2 + 5x - 1
# a) Write a Python function called f, that calculates f(x) and returns the answer.
# b) Test the function with print(f(2))

# SVAR
def f(x):
	y = x*x + 5*x - 1
	return y

print(f(2))





