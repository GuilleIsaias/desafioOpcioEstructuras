#librerias importadas
import requests
import json


#funcion a utilizar
def request_get(url):
    return json.loads(requests.get(url).text)

#requerimiento 1 - obtener informacion de los usuarios
users_data = request_get("https://reqres.in/api/users")
print(users_data)

#requerimiento 2 - crear usuario

payload = {
    "name": "Ignacio",
    "job": "Profesor"
}
created_user = requests.post("https://reqres.in/api/users",
data = payload)

print(created_user)

#requerimiento 3 - actualizar usuario

payload = {
    "name": "morpheus",
    "job": "zion resident"
}
updated_user = requests.put("https://reqres.in/api/users/2",
data = payload)
print(updated_user)

#requerimiento 4 - eliminar usuario

payload = {
    "name": "Tracey",
}
deleted_user = requests.delete("https://reqres.in/api/users/2",
data = payload)
print(deleted_user)
