import persistencia_pickle as pp
import car_class
import random as rd

FILE = 'coches.obj.txt'
lista_coches = pp.retrieve(FILE)
if lista_coches == None:
    lista_coches = []
while True:
    marca = input('Marca:')
    if marca == ('fin'):
        break
    modelo = input('Modelo:')
    combustible = input('Combustible:')
    cilindrada = input('Cilindrada:')
    ancho= input('Ancho:')
    rodadura= input('Rodadura:')
    diametro= input('Diametro:')
    presion= input('Presion:')

    wheel = car_class.Wheel(ancho, rodadura, diametro)
    wheel.set_pressure(presion)
    coche = car_class.Car(marca, modelo, combustible, cilindrada)
    coche.set_wheel(wheel)

    lista_coches.append(coche)
    coche.move_pos(rd.random() * 100, rd.random() * 600)
    print('posicion:', coche.get_pos())
    coche.move_incr(rd.random() * 10, rd.random() * 60)
    print('posicion:', coche.get_pos())
    del (coche)
pp.store(lista_coches, FILE)
lista_coches = []
lista_coches = pp.retrieve(FILE)
for car in lista_coches:
    print('Marca, modelo, combustible, cilindrada:', car.marca, car.modelo, car.combustible, car.cilindrada)
    print('posición:', car.get_pos(), '\n')
    print('Rueda: ', car.wheel.print_info(), 'Presion:', car.wheel.presion)
