# PYTHON BEGINNER COURSE, spring 2024
# by Fredrik E. Juell, fredrik.e.juell@bi.no


##########################################
print("---------- 1. VARIABLES ----------")

# Variabler - types
# Example: Apartment description
size = 55 # kvm
price_per_m2 = 75000
location = "Nydalen in Oslo"
has_balcony = True


# Simple calculator
# Calculating price:
price = size * price_per_m2
print(price)
# Formatted print
print(f"The apartment in {location} has price NOK {price:_}.")


# EXERCISE:
# Make a variable price_old, with value 4_000_000. 
# Calculate the price after a price raise of 3%, and store it in a variable price_new.
# Print price_new on the screen.
# Division: /

# ANSWER:
price_old = 4_000_000
price_new = price_old + (price_old * 3) / 100  # Or price_old * 1.03
print(price_new)

 

#########################################
print("---------- 2. IF-TESTS ----------")

# Indentation is important

price = 4_000_000

# If below a price limit
if price <= 4_000_000:
    print(f"I will bid {price+25000}.")

# And if it has balcony
if price < 4_000_000 and has_balcony:
    print(f"My bid is {price+50000}")
elif price < 4_000_000 and not has_balcony:  # If not balcony
    print(f"My bid is {price+25000}")
else:
    print(f"No bid over {price}.")


# EXERCISE: (From Math-olympiade 2023)
a = 2**31
b = 3**21
# Write an if-test that finds the largest number of a and b, and print it to screen. 

# ANSWER:
if a > b:
    print(f"a is largest")
#elif a==b:
#  print("a and b are equal")
else:
    print(f"b is largest")

#print(f"{a = :_} og {b = :_}")


#########################################
print("---------- 3. LISTS ----------")
locations = ["Nydalen", "Storo", "Sagene"]
locations.append("Torshov")	 # Adding an element
locations = locations + ["Bjølsen", "Ullevål", "Korsvoll"]  # Joining two lists

# Use print() to view the list.
print(locations)
# Print 2nd element
print(locations[1])
# Print elements from index 0 to 3 (element 1, 2, 3)
print(locations[0:3])
# Remove an element
locations.pop(-1)
# Sort list
locations.sort()
print(f"Sorted list: {locations}")
# Print number of elements in the list
print(len(locations))


# EXERCISE:
# Define a list called campuses, containing the four BI campuses.
# Print the last element to screen

### --- BREAK --- ###

# ANSWER:
campuses = ["BI Oslo", "BI Bergen", "BI Trondheim", "BI Stavanger"]
print(campuses[3])	                # When list length is known
print(campuses[len(campuses)-1])    # Complicated
print(campuses[-1])			        # Best alternative




###############################################
print("---------- 4. DICTIONARIES ----------")

# Price per square meter for for some areas
location_prices = {'Bjølsen':70000, 'Nydalen':75000, 'Sagene':60000, 'Storo':73000, 'Torshov':82000, 'Ullevål':90000}
# Print the value for key "Sagene"
print(location_prices["Sagene"])

# Another dictionary
flat_nydalen = {"location": "Nydalen",
			     "size": 55,
            	 "has_balcony": True,
            	 "price_per_m2": location_prices['Nydalen']
            	 }

# If apartment has balcony and is larger or equal to 50 square meters:
if flat_nydalen['has_balcony'] and flat_nydalen['size']>=50:
    print("Yes, I am interested.")
else:
	print("Not interested.")


# EXERCISE:
# Define a dictionary campuses_visited, with three Key:Value-pairs.
# Let Key be the BI campuses from previous exercise.
# Let Value be True if you have been on the campus, or False if not.
# Make a test that prints the campuses with True.

# ANSWER:
campuses_visited = {"BI Oslo":True, "BI Bergen":False, "BI Trondheim":True, "BI Stavanger":False}
campuses_visited = {campuses[0]:True, campuses[1]:False, campuses[2]:True, campuses[3]:False}
if campuses_visited["BI Oslo"]:
    print("BI Oslo")
if campuses_visited["BI Bergen"]:
    print("BI Bergen")
if campuses_visited["BI Trondheim"]:
    print("BI Trondheim")
if campuses_visited["BI Stavanger"]:
    print("BI Stavanger")





##########################################
print("---------- 5. FOR-LOOPS ----------")
# Process all elements in a list.
for loc in locations:
    print(loc)

# Process all elements in a dictionary
for area, price_per_m2 in location_prices.items():
    my_size_limit = 50  # square meters
    price = price_per_m2 * my_size_limit
    if price < 4_000_000 and has_balcony:
        print(f"{area}, with price {price}")



# Two alternative answers to previous exercise using for-loop:
for key in campuses_visited:
  if campuses_visited[key]:
    print(key)
# Or:
for key,value in campuses_visited.items():
  if value:
    print(key)


# EXERCISE:
# Here is a list with integers from 0 to 100:
whole_numbers = list(range(0,100))
# Make a new list quarters, that contains the elements in whole_numbers divided by 4
# Print the list to screen.
# Tip: First, make an empty list. Then use a for-loop to add elements to it

# ANSWER:
quarters = []
for x in whole_numbers:
  quarters.append(x/4)
print(quarters)





##########################################
print("---------- 6. FUNCTIONS ----------")
# Define a function for apartment price calculation.
def apart_price(size, price_per_m2):
	price = size * price_per_m2
	return price

# Call the function, and save the result in a variable.
price_example = apart_price(45, 79000)
print(price_example)

# EXERCISE:
# Make a function raise_price, that takes two arguments: price, percent
# The function should calculate and return the new price.
# Test the function by calling raise_price(3_500_000, 2.5)

# ANSWER:
def raise_price(price, percent):
    new_price = price + (price * percent)/100
    return new_price

print(raise_price(3_500_000, 2.5))






