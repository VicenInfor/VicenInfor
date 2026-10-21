#Datos
print("Primer set")
P1J1= int(input('Jugador 1, dime tu puntuacion:'))
P1J2= int(input('Jugador 2, dime tu puntuacion:'))
print("Segundo set")
P2J1= int(input('Jugador 1, dime tu puntuacion:'))
P2J2= int(input('Jugador 2, dime tu puntuacion:'))
print("Tercer set")
P3J1= int(input('Jugador 1, dime tu puntuacion:'))
P3J2= int(input('Jugador 2, dime tu puntuacion:'))
#Calculo
J1 = P1J1+P2J1+P3J1
J2 = P1J2+P2J2+P3J2
#Resultado
print(f"J1. Juegos a favor/Juegos en contra: {J1}/{J2}")
print(f"J1. Juegos a favor/Juegos en contra: {J2}/{J1}")