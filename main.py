import requests
import json 
import requests


def dish_fetch(num):
    url = f"http://api-colombia.com/api/v1/TypicalDish/{num}"
    response = requests.get(url)
    return response.json()


def main():
    print("Bienvenido al menú de platos típicos")

    while True:
        opcion = input("Ingrese el número del plato (o escriba 'salir'): ")

        if opcion == "salir":
            print("¡Hasta luego!")
            break

        if not opcion.isdigit():
            print("Por favor escriba un número válido.")
            continue

        plato = dish_fetch(int(opcion))

        if "name" in plato:
            print("Plato encontrado:", plato["name"])
        else:
            print("No se encontró ese plato.")


if __name__ == "__main__":
    main()