# Bekijk de voorbeelden en verander de functies
# Maak vervolgens de opdracht hieronder
# Voorbeeld1
def rekenen1():
  getal1 = 50
  getal2 = 5
  return getal1 + getal2

def rekenen2():
  getal1 = 50
  getal2 = 5
  return getal1 - getal2

def rekenen3():
  getal1 = 50
  getal2 = 5
  return getal1 * getal2

getal = rekenen2()
TweedeGetal = rekenen1()
DerdeGetal = rekenen3()
print(getal)
print(TweedeGetal)
print(DerdeGetal)

# Voorbeeld2
def locatie(land):
  print("Ik kom uit " + land)

locatie("Nederland")

# Voorbeeld3
def kwadraat(getal):
  resultaat = getal * getal
  return resultaat

mijnKwadraat = kwadraat(4)
print(mijnKwadraat)


# Maak 5 functies die allemaal in een andere taal "Goedemorgen" printen.
# Roep daarna elke functie minimaal 2 keer aan (callen) waardoor er minimaal 10 keer "Goedemorgen" naar de console wordt geprint!

def Nederlands():
  groet = "Goedemorgen"
  return groet

def Engels():
  groet = "Good Morning"
  return groet

def Duits():
  groet = "Gute Morgen"
  return groet

def Frans():
  groet = "Bonjour"
  return groet

def Spaans():
  groet = "Buen dia"
  return groet

Nederlands = gegroet(*2)
print(gegroet)

Engels = gegroet1(*2)
Duits = gegroet2(*2)
Frans = gegroet3(*2)
Spaans = gegroet4(*2)
