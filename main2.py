import requests

def main():
    url = "http://api-colombia.com/api/v1/TypicalDish"
    platos = requests.get(url).json()

    print("MENÚ ")
    for plato in platos:
        print(plato["id"], "-", plato["name"])

    while True:
        numero = input("Número del plato (o 'salir'): ")

        if numero == "salir":
            break

        for plato in platos:
            if plato["id"] == int(numero):
                print("Elegiste:", plato["name"])


if __name__ == "__main__":
    main()