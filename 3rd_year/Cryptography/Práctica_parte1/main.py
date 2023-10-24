import hashlib
import json
import rsa

#Función recurrente
def username_used(users, usr_statement):
    chosen_username = input(usr_statement)
    for i in users:
        if (i["username"] == chosen_username):
            chosen_username = username_used(users, "Nombre de usuario ya en uso, prueba otro: ")
    return chosen_username
    

def register_user():
    #Abrir usuarios para checkear posobles repeticiones
    with open("data.json") as read_file:
        data = json.load(read_file)
        read_file.close()

    #Crear nuevo usuario y checkear que no esté repetido
    usr = username_used(data["users"], usr_statement = "Introduce un nuevo nombre de usuario: ")

    #Pedir contraseña y asegurarse que tiene mínimo 10 carácteres (normalmente también se debería asegurar que se utilizan un mínimo de carácteres especiales)
    local_password = str(input("Introduce una contraseña (con un mínimo de 10 carácteres): "))
    while (len(local_password) < 10):
        local_password = str(input("Longitud de contraseña inválida, pureba otra: ")) 

    #Usar función Hash para encriptar (aunque con una función hash no se puede desencriptar) la contraseña
    usrPassword = hashlib.pbkdf2_hmac('sha512', local_password.encode(), usr[-4:].encode(), len(usr))
    print(usrPassword.hex())

    #Crear pareja de claves para rsa
    public_key, private_key = rsa.newkeys(3072)
    with open(usr + ".pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))
        f.close()
    #k = public_key.save_pkcs1("PEM").hex
    #kk = bytes.fromhex(k)

    #Añadir nuevo usuario
    data["users"].append({"username": usr, "password": usrPassword.hex(), "public_key": public_key.save_pkcs1("PEM").hex()})

    #sobreescribir JSON
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    #Go to the main page
    main()

def access_user():
    #Abrir usuarios para checkear posobles repeticiones
    with open("data.json") as read_file:
        data = json.load(read_file)
        read_file.close()

    #Log in
    access_username = input("Cual es tu nombre de usuario?: ")
    for i in data["users"]:
        if i["username"] == access_username:
            access_password_local = input("Cual es tu contraseña ?: ")
            access_password = hashlib.pbkdf2_hmac('sha512', access_password_local.encode(), access_username[-4:].encode(), len(access_username))
            if (access_password.hex() == i["password"]):
                user_action()
                print("Serás redirigido al menu principal")
                main()
                exit()

    #If user doesn't exist go to home
    print("Nombre de usuario no existe, serás redirigido al menu principal")
    main()

def user_action():
    

def main():
    print("Presiona 1 para crear un usuario nuevo")
    print("Presiona 2 para acceder a un usuario")
    print("Presiona 3 para salir de la aplicación")

    x = input("Number pressed: ")
    while (x != "1" and x != "2" and x != "3"):
        x = input("Número inválido, purba de nuevo: ")
    if (x == "1"):
        register_user()
    elif(x == "2"):
        access_user()
    elif(x == "3"):
        exit()

if __name__ == "__main__":
    print("Bienvenido al programa de Cryptografía")
    main()