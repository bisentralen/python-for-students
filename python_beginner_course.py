# PYTHON Beginner Course, autumn 2022
# w/Fredrik E. Juell, fredrik.e.juell@bi.no


##########################################
# 1. VARIABLES and PRINT #################

# Variables - types
# Salmon data
price = 30 	# NOK pr. kilo
weight = 1350	# kilos
origin = "Norway"
is_frozen = False

# Simple calculator
# Calculating price x weight:
price_total = weight*price
print(price_total)
# Prettier print
print("The price of", weight, "kilos of salmon is NOK", price_total)


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
# 2. IF-TESTS ###########################

# Indentation is important

# Test if price is low enough
if price < 30:
	print("I will buy.")

# Test for price interval and boolean
if 10 < price < 40 and not is_frozen:
	print("Yes, give it to me!")

# Nested if-statements
if price < 30 and weight >= 1000:
	print("I will buy a lot.")
elif 30 < price < 40:
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
# 3.1. LISTS ############################
prices_salmon = [20, 25, 30, 35, 40]
prices_salmon.append(27)				# Adding one element
prices_salmon = prices_salmon+[43, 31]	# Adding two elements

# Print to screen, to view the list
print(prices_salmon)
# Print 2nd element
print(prices_salmon[1])
# Print elements from index 0 up to 3
print(prices_salmon[0:3])
# Print number of elements in the list
print(len(prices_salmon))

# EXERCISE
# Define a list called animals, that contains three animals of your choice.
# Print the last element in the list

# ANSWER:
animals = ["snake", "rabbit", "unicorn"]
print(animals[2])				# When we know how many elements in the list, len(animals)
print(animals[-1])				# Always the last element

# More examples:
more_animals = animals + ["dog", "turtle"]
print(more_animals)



###############################################
# 3.2. DICTIONARIES ###########################

# Example with prices for different qualities of salmon
prices_quality = {"superb":50, "high":35, "mid":30, "low":23, "catfood":9}
# Print/write the value for the key "high":
print(prices_quality["high"])

# Another dictionary example:
salmon_batch = {"origin": "Island",
				"weight": 30000,
              	"frozen": True,
              	"quality": "mid",
              	"price": prices_quality["mid"]
            	}

# If batch is frozen and price is under 40
if salmon_batch["frozen"] and salmon_batch["price"]<40:
	print("Yes, it's frozen and price is", salmon_batch["price"])
else:
	# If not:
	print("Not frozen and too expensive")


# EXERCISE:
# Define a dictionary called animals_fav, with three Key:Value-pairs.
# Let the Keys be the animals in your list in the previous exercise.
# Let Value be True if the animal could be your pet, and False if not.
# Write a test that prints your possible pets from animals_fav.

# ANSWER:
animals_fav = {"snake":False, "rabbit":True, "unicorn":True}
animals_fav = {animals[0]:True, animals[1]:True, animals[2]:False}
if animals_fav["snake"]:
  print("snake")
if animals_fav["rabbit"]:
  print("rabbit")
if animals_fav["unicorn"]:
  print("unicorn")





################################################
# 4. FOR-LOOPS #################################

# Test all prices in a for-loop, and answer each
for price in prices_salmon:
	if price < 30:
		print("I will buy at price", price)
	else:
		print("Too expensive at price", price)

# Alternative ANSWER to exercise with use of a for-loop
for key in animals_fav:
  if animals_fav[key]:
    print(key)


# EXERCISE:
# A list of the numbers from 0 to 50:
my_numbers = list(range(0,100))
# Make another list called quarters, that contain the numbers in my_numbers divided by 4. 
# View the result with print(quarters)
# Hint: Start by making an empty list quarters, and use a for-loop to add elements into it.

# ANSWER:
quarters = []
for x in my_numbers:
	quarters.append(x/4)
print(quarters)
	



##########################################
# 5. FUNCTIONS ###########################
# Defining a function to calculate total price of a volume of salmon
def total_price(volume, price):
	price_total = volume*price
	return(price_total)

# Use the function total_price, and save the result in a variable price_example
price_example = total_price(1600, 25)
print(price_example)

# EXERCISE:
# f(x) = x^2 + 5x - 1
# a) Write a Python function called f, that calculates f(x) and returns the answer.
# b) Test the function with print(f(2))

# ANSWER
def f(x):
	y = x*x + 5*x - 1
	return y

print("f(2) is",f(2))


##########################################
# 6. IMPORT ##############################
import math
print(math.pi)

# View the contents of the package math
dir(math)


