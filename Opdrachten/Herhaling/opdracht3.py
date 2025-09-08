'''
Gegeven is een lijst met games. Doe het volgende:

  - Voeg Super Mario Bros toe aan de lijst
  - Vraag de gebruiker om een **getal** tussen de 0 en de 5
  - Print de game die op deze plek in de lijst staat
  - Vraag de gebruiker om een game met een input
  - Voeg deze game toe aan de lijst
  - Print de lijst met games
'''

games = ["Minecraft", "Rust", "GTA V", "Hayday", "Clash of clans", "Super Mario Bros"]

Gamekeuze = float(input("Geef een getal tussen 0 en 5"))

if Gamekeuze == 0:
  print(games[0])

elif Gamekeuze == 1:
  print(games[1])

elif Gamekeuze == 2:
  print(games[2])

elif Gamekeuze == 3:
  print(games[3])

elif Gamekeuze == 4:
  print(games[4])

elif Gamekeuze == 5:
  print(games[5])

else:
  print("Dat cijfer is niet geldig. Probeer het nog eens")