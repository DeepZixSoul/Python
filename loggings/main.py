import requests

def get_curren_price(id):
    print('Entramos en la funcion')

    response = requests.get(f'https://www.udemy.com/{id}')

    if response.status_code == 200:
        print("Exito")

        return response.json()

    return None


if __name__ == '__main__':

    response = get_curren_price('courses')

    print('obtenemos respuestas')

    print(response)
