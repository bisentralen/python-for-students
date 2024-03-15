# PYTHON NYBEGYNNERKURS, vår 2024
# v/Fredrik E. Juell, fredrik.e.juell@bi.no


##########################################
print("---------- 1. VARIABLES ----------")

# Variabler - typer
# Eksempel: Leilighetskjøp
size = 55 # kvm
price_per_m2 = 75000
location = "Nydalen i Oslo"
has_balcony = True


# Enkel kalkulator
# Regner ut volum:
price = size * price_per_m2
print(price)
# Mer utførlig print
print(f"Leiligheten i {location} koster kr {price:_}.")


# OPPGAVE:
# Lag en variabel price_old, med verdi 4_000_000. 
# Regn ut hva prisen blir etter en prisøkning på 3%, og lagre i variabel price_new
# Skriv ut price_new på skjermen.
# Divisjon: /

# SVAR:
price_old = 4_000_000
price_new = price_old + (price_old * 3) / 100  # Or price_old * 1.03
print(price_new)

 

#########################################
print("---------- 2. IF-TESTS ----------")

# Innrykk er viktig

price = 4_000_000

# Hvis under prisgrense
if price <= 4_000_000:
    print(f"I will bid {price+25000}.")

# Og har balkong
if price < 4_000_000 and has_balcony:
    print(f"My bid is {price+50000}")
elif price < 4_000_000 and not has_balcony:
    print(f"My bid is {price+25000}")
else:
    print(f"No bid over {price}.")


# OPPGAVE: (Fra Matte-olympiaden 2023)
a = 2**31
b = 3**21
# Skriv en if-test som finner det største tallet av a og b. 
# Skriv ut svaret på skjermen.

# SVAR:
if a > b:
    print(f"{a = } er størst")
#elif a==b:
#  print("a og b er like")
else:
    print(f"{b = } er størst")

#print(f"{a = :_} og {b = :_}")


#########################################
print("---------- 3. LISTS ----------")
locations = ["Nydalen", "Storo", "Sagene"]
locations.append("Torshov")	 # Legger til element
locations = locations + ["Bjølsen", "Ullevål", "Korsvoll"]  # Legger til to elementer, alternativ metode

# Print til skjerm for å se på listen.
print(locations)
# Print 2. element
print(locations[1])
# Print elementene fom. index 0 til 3 (dvs. element 1, 2, 3)
print(locations[0:3])
# Fjern et element
locations.pop(-1)
# Sorter listen
locations.sort()
print(f"Sortert liste: {locations}")
# Print antall elementer i listen
print(len(locations))


# OPPGAVE:
# Definer en liste kalt campuses, med navnene på de fire BI-campusene.
# Skriv ut det siste elementet i listen

### --- PAUSE --- ###

# SVAR:
campuses = ["BI Oslo", "BI Bergen", "BI Trondheim", "BI Stavanger"]
print(campuses[2])	                # Når vi vet listens lengde
print(campuses[len(campuses)-1])    # Komplisert alternativ
print(campuses[-1])			        # Beste alternativ




###############################################
print("---------- 4. DICTIONARIES ----------")

# Kvadratmeterpriser for ulike områder
location_prices = {'Bjølsen':70000, 'Nydalen':75000, 'Sagene':60000, 'Storo':73000, 'Torshov':82000, 'Ullevål':90000}
# Skriv ut verdien for nøkkelen "Sagene"
print(location_prices["Sagene"])

# Eksempel på annen dictionary
flat_nydalen = {"location": "Nydalen",
			     "size": 55,
            	 "has_balcony": True,
            	 "price_per_m2": location_prices['Nydalen']    # or "price": prices_fish[species]
            	 }

# Hvis leiligheten har balkong og koster under 5 mill:
if flat_nydalen['has_balcony'] and flat_nydalen['size']>=50:
    print("Yes, I am interested.")
else:
	print("Not interested.")


# OPPGAVE:
# Definer en dictionary campuses_visited, med tre Key:Value-par.
# La Key være byene fra forrige oppgave.
# La Value være True hvis du har vært der, og False hvis ikke.
# Lag en test som printer ut de campusene du har vært på.

# SVAR:
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
# Skriv ut mine interesseområder. Skriv ut elementene i en liste.
for loc in locations:
    print(loc)

# Finn områder som passer mine preferanser (balkong + 50 kvm)
# Behandle key, value i en dict
for area, price_per_m2 in location_prices.items():
    my_size_limit = 50  # kvm
    price = price_per_m2 * my_size_limit
    if price < 4_000_000 and has_balcony:
        print(f"{area}, with price {price}")



# To alternative svar på forrige oppgave med bruk av for-løkke:
for key in campuses_visited:
  if campuses_visited[key]:
    print(key)
# Eller
for key,value in campuses_visited.items():
  if value:
    print(key)


# OPPGAVE:
# Her er en liste med hele tall fra 0 til 100:
whole_numbers = list(range(0,100))
# Lag en ny liste quarters, som inneholder tallene i wholes, delt på 4. 
# Skriv ut listen quarters på skjermen.
# Hint: Lag først en tom liste quarters, og bruk en for-loop for å legge elementer til denne.

# SVAR:
quarters = []
for x in whole_numbers:
  quarters.append(x/4)
print(quarters)





##########################################
print("---------- 6. FUNCTIONS ----------")
# Definerer en funksjon som regner ut prisen på en leilighet
def flat_price(size, price_per_m2):
	price = size * price_per_m2
	return price

# Bruk funksjonen total_price, og lagre resultat i en variabel price_example
price_example = flat_price(45, 79000)
print(price_example)

# OPPGAVE:
# Lag en funksjon som øker en pris en valgfri prosent.
# Kall funksjonen raise_price, og la den ta imot argumentene price og percent 
# Test funksjonen ved å f.eks kalle raise_price(3_500_000, 2.5)

# SVAR:
def raise_price(price, percent):
    new_price = price + (price * percent)/100
    return new_price

print(raise_price(3_500_000, 2.5))

""" EKSTRA: SCOPE 
Variabel-scope: Der en variabel er synlig og tilgjengelig
Scope rekkefølge: Local (En funksjon) -> Enclosed -> Global -> Built-in
"""
 



