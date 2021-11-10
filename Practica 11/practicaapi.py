# LLAMADA A GITHUB API
import requests
import json
import time

# La Función hace 2 llamadas por usuario
# La segunda llamada en basada en la primera


def llamadas_api(user, llamada):
    # LLAMADA 1 -- Información de un Usuario
    url = "https://api.github.com/users/" + user + "/repos"
    response = requests.get(url)
    data = json.loads(response.content)
    print()
    # print(llamada)
    # print(data)
    # print(type(data))

    # Recopilación Importante de la Llamada
    print("----LLAMADA" + str(llamada) + "----")
    repo = 1
    for i in range(0, len(data)):
        # FILA - COLUMNA
        print("Repositorio" + str(repo))
        print("Usuario: ", data[i]["owner"]["login"])
        print("Nombre Repositorio: ", data[i]["name"])
        print("Descripción: ", data[i]["description"])
        print("Created Date: ", data[i]["created_at"])
        print("Updated Date: ", data[i]["updated_at"])
        print("Tamaño: ", data[i]["size"])
        print()
        repo += 1

    # LLAMADA
    llamada += 1
    listadata2 = []
    for i in range(0, len(data)):
        lang = data[i]["languages_url"]
        response2 = requests.get(lang)
        data2 = json.loads(response2.content)
        listadata2.append(data2)
        # print(data2)
        time.sleep(3)

    repo2 = 1
    print("----LLAMADA" + str(llamada) + "----")
    print("Información Obtenida de la llamada anterior: ")
    for i in range(0, len(listadata2)):
        print("Repositorio" + str(repo2))
        print("Usuario: ", data[i]["owner"]["login"])
        print("Lenguaje de Programación: ", listadata2[i])
        repo2 += 1


# LLAMADA 1 Y 2
user = "LicPlatano"
llamada = 1
llamadas_api(user, llamada)

# LLAMADA 3 Y 4
user = "Raycrowbel"
llamada = 3
llamadas_api(user, llamada)

# LLAMADA 5 Y 6
user = "Gil22"
llamada = 5
llamadas_api(user, llamada)
