# import random
import random 

# Listas de planetas y distancias:
planetas = ("Mercurio", "Venus",  "Tierra", "Marte", "Jupiter",  "Saturno", "Urano", "Neptuno", "Plutón")
distancias = [57_900_000, 108_200_000, 149_600_000, 227_900_000, 778_600_000, 1_433_500_000, 2_872_500_000, 4_495_100_000, 5_234_234_230]

planeta_1 = random.choice(planetas[:]) # Escoge un primer planeta de la lista planetas
planeta_2 = random.choice(planetas[:]) # Escoge un segundo planeta de la lista planetas

indice_1 = planetas.index(planeta_1)
indice_2 = planetas.index(planeta_2)

distancia_1 = distancias[indice_1]
distancia_2 = distancias[indice_2]


print("El primer planeta escogido es: ", planeta_1)
print("El segundo planeta escogido es: ", planeta_2)

# Plantilla de ejemplo:

plantilla = """La distancia entre {} y {} es de: {} Km
""".format(planeta_1, planeta_2, abs(distancia_1 - distancia_2))

print(plantilla)

