import requests
import json 
import requests

import requests


def dish_fetch(num):
    url = f"http://api-colombia.com/api/v1/TypicalDish/{num}"
    response = requests.get(url)
    return response.json()


def mostrar_menu():
    url = "http://api-colombia.com/api/v1/TypicalDish"
    response = requests.get(url)
    platos = response.json()

    print("MENÚ DE PLATOS TÍPICOS DE COLOMBIA ---")
    for plato in platos:
        print(plato["id"], "-", plato["name"])


def main():
    mostrar_menu()

    while True:
        opcion = input("Escriba número del plato (o 'salir'): ")

        if opcion == "salir":
            print("¡Hasta una proxima!")
            break

        if not opcion.isdigit():
            print("Escriba un número válido.")
            continue

        plato = dish_fetch(int(opcion))

        if "name" in plato:
            print("Plato:", plato["name"])
        else:
            print("No existe ese plato.")


if __name__ == "__main__":
    main()