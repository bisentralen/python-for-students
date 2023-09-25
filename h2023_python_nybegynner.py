# PYTHON NYBEGYNNERKURS, høst 2023
# v/Fredrik E. Juell, fredrik.e.juell@bi.no


##########################################
# 1. VARIABLES ###########################

# Variabler - typer
# Fish example
price = 30 		# kilopris
weight = 1350	# kilo
origin = "Norway"
is_frozen = False

# Enkel kalkulator
# Regner ut pris x vekt:
price_total = price*weight
print(price_total)
# Mer utførlig print
print("The price of", weight, "kilos of fish is NOK", price_total)


# OPPGAVE:
a = 1
b = 5
# Bytt om verdiene på a og b
#
# SVAR:
x = a
a = b
b = x
print(a,b)
# Alternativt: 
a,b = b,a




#########################################
# 2. IF-TESTS ###########################

# Innrykk er viktig

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

# OPPGAVE:
a = 3**12
b = 2**19
# Skriv en if-test som finner det største tallet av a og b. 
# Skriv ut svaret på skjermen.

# SVAR:
if a > b:
  print("a er størst")
#elif a==b:
#  print("a og b er like")
else:
  print("b er størst")



#########################################
# 3. LISTS ############################
types_fish = ["salmon", "cod", "shark"]
types_fish.append("halibut")				# Legger til element
types_fish = types_fish+["herring", "tuna"]	# Legger til to elementer, alternativ metode

# Print til skjerm for å se på listen.
print(types_fish)
# Print 2. element
print(types_fish[1])
# Print elementene fom. index 0 til 3 (dvs. element 1, 2, 3)
print(types_fish[0:3])
# Sorter listen
types_fish.sort()
# Print antall elementer i listen
print(len(types_fish))


# OPPGAVE
# Definer en liste kalt candy, som inneholder tre valgfrie elementer av godteri.
# Skriv ut det siste elementet i listen

### --- PAUSE --- ###

# SVAR:
candy = ["lakrispipe", "lakrisbåter", "Panda lakris"]
print(candy[2])				# Når vi vet listens lengde
print(candy[len(candy)-1])	# Komplisert alternativ
print(candy[-1])				# Beste alternativ



###############################################
# 4. DICTIONARIES ###########################

# Eksempel med priser for ulike kvaliteter
prices_fish = {"tuna":50, "cod":35, "herring":29, "salmon":23, "shark":25, "halibut":30}
# Skriv ut verdien for nøkkelen "high"
print(prices_fish["cod"])

# Eksempel på annen dictionary
fish_batch = {"species": "cod",
			        "weight": 30000,
            	"frozen": True,
            	"price": prices_fish["cod"]    # or "price": prices_fish[type]
            	}

# Hvis batch er frossen og pris er under 40
if fish_batch["frozen"] and fish_batch["price"]<40:
  print("Yes, batch is frozen and price is", fish_batch["price"]*fish_batch["weight"])
else:
	print("Not frozen and too expensive")


# OPPGAVE:
# Definer en dictionary candy_fav, med tre Key:Value-par.
# La Key være godteriene fra forrige oppgave.
# La Value være True hvis godteriet er en av dine favoritter, og False hvis
# du kan greie deg uten.
# Lag en test som printer ut favorittcandy fra candy_fav

# SVAR:
candy_fav = {"lakrispipe":True, "lakrisbåter":True, "Panda lakris":False}
candy_fav = {candy[0]:True, candy[1]:True, candy[2]:False}
if candy_fav["lakrispipe"]:
  print("lakrispipe")
if candy_fav["lakrisbåter"]:
  print("lakrisbåter")
if candy_fav["Panda lakris"]:
  print("Panda lakris")




##########################################
# 5. FOR-LOOPS ###########################
# Test all prices in a for-loop, and answer each
for species in prices_fish:
	if prices_fish[species] < 30:
		print(f"I will buy {species} at price at {prices_fish[species]}")
	else:
		print(f"{species} is too expensive")

# To alternative svar på forrige oppgave med bruk av for-løkke:
for key in candy_fav:
  if candy_fav[key]:
    print(key)
# Eller
for key,value in candy_fav.items():
  if value:
    print(key)




##########################################
# 6. FUNCTIONS ###########################
# Defining a function to calculate total price of a volume of fish
def total_price(volume, price):
	price_total = volume*price
	return(price_total)

# Bruk funksjonen total_price, og lagre resultat i en variabel price_example
price_example = total_price(1600, 25)
print(price_example)

# OPPGAVE:
# f(x) = x^2 + 5x - 1
# a) Skriv en funksjon f, som regner ut f(x).
# b) Test funksjonen med print(f(2))

# SVAR
def f(x):
	y = x*x + 5*x - 1
	return y

print(f(2))





