import hashlib
import json
import rsa
import sys

from cryptography.fernet import Fernet

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

    #Añadir nuevo usuario
    data["users"].append({"username": usr, "password": usrPassword.hex(), "public_key": public_key.save_pkcs1("PEM").hex()})

    #sobreescribir JSON
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    #Go to the main page
    main()
    sys.exit()

def access_user():
    #Abrir usuarios para checkear que el usuario existe
    with open("data.json") as read_file:
        data = json.load(read_file)
        read_file.close()

    #Log in
    access_username = input("Cual es tu nombre de usuario?: ")
    access_password = ""
    for i in data["users"]:
        if i["username"] == access_username:
            access_password_local = input("Cual es tu contraseña ?: ")
            access_password = hashlib.pbkdf2_hmac('sha512', access_password_local.encode(), access_username[-4:].encode(), len(access_username))
            if (access_password.hex() == i["password"]):
                user_action(access_username)
            else:
                print("Contraseña incorrecta serás redirigido al menú principal")
                main()
                sys.exit()


    #Si usuario no existe ir al menú principal
    if access_password == "":
        print("Nombre de usuario no existe, serás redirigido al menú principal")
        main()
        sys.exit()

#Post, see intended, see message
def user_action(active_user:str):
    #Post message
    print("Bienvenido " + active_user)
    print("Presiona 1 para ver tus mensajes")
    print("Presiona 2 para descifrar mensaje")
    print("Presiona 3 para crear un mensaje")
    print("Presiona 4 para volver al menú principal")

    x = input("Number pressed: ")
    print("")
    while (x != "1" and x != "2" and x != "3" and x != "4"):
        x = input("Número inválido, purba de nuevo: ")
    if (x == "1"):
        see_user_messages(active_user)
    elif(x == "2"):
        decrypt_message(active_user)
    elif(x == "3"):
        create_message(active_user)
    elif(x == "4"):
        main()
        sys.exit()

#Posible mejora, mensajes con sender público y privado
def create_message(sender):
    #Abrir usuarios para checkear posobles destinos
    with open("data.json") as read_file:
        data = json.load(read_file)
        read_file.close()

    #Checkear si destinatario existe y pillar clave pública
    destination_username = input("A quien le quieres mandar un mensaje?: ")
    destination_publicKey = ""
    while(destination_publicKey == ""):
        for i in data["users"]:
            if i["username"] == destination_username:
                destination_publicKey = i["public_key"]

        if (destination_publicKey == ""):
            destination_username = input("Destinatario no existente, prueba otro: ")

    #Encriptar mensaje con Fernet
    fernet_key = Fernet.generate_key()
    fernet_object = Fernet(fernet_key)
    encrypted_message = fernet_object.encrypt(input("Contenido del mensaje: ").encode())
    print("Mensaje encriptado: ", encrypted_message)

    #Encriptar la llave de fernet con RSA
    encrypted_fernet_key = rsa.encrypt(fernet_key, rsa.PublicKey.load_pkcs1(bytes.fromhex(destination_publicKey)))
    print("Llave de Fernet encriptada con RSA: ", encrypted_fernet_key)

    #Modificar JSON
    data["mensajes"].append({
        "ID": data["mensajes"][-1]["ID"] + 1,
        "para": destination_username,
        "mensaje": encrypted_message.hex(),
        "llave": encrypted_fernet_key.hex()
    })

    #sobreescribir JSON
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
        json_file.close()

    #Go to the main page
    user_action(sender)

def see_user_messages(sender):
    #Abrir usuarios para checkear posobles destinos
    with open("data.json") as read_file:
        data = json.load(read_file)
        read_file.close()

    print("Estos son los IDs de los mensajes que son para ti: ")    
    for i in data["mensajes"]:
        if sender == i["para"]:
            print(i["ID"])

    #Volver a menú selección de acciones
    user_action(sender)

def decrypt_message(sender):
    #Abrir archivo para obtener datos
    with open("data.json") as read_file:
        data = json.load(read_file)
        read_file.close()
    
    #Select message
    message_id = input("Introduce el ID del mensaje que quieres ver: ")
    while(message_id.isdigit() != True):
        message_id = input("Los IDs son números, itroduce un número: ")

    #Obtener mensaje del json
    for i in data["mensajes"]:
        if int(message_id) == i["ID"]:
            #Desencriptar llave 
            encrypted_key = i["llave"]
            print("Llave encriptado: " + encrypted_key)
            encrypted_message = i["mensaje"]
            print("Mensaje encriptado: " + encrypted_message)
    
    decrypted_key = rsa.decrypt(bytes.fromhex(encrypted_key), rsa.PrivateKey.load_pkcs1(open(sender + ".pem", "rb").read()))
    print("Llave desencriptada: " + decrypted_key.decode())
    cipher_suite = Fernet(decrypted_key)
    print("Mensaje desencriptado: " + cipher_suite.decrypt(bytes.fromhex(encrypted_message)).decode() + "\n")
    user_action(sender)

def main():
    print("Presiona 1 para crear un usuario nuevo")
    print("Presiona 2 para acceder a un usuario")
    print("Presiona 3 para salir de la aplicación")

    x = input("Number pressed: \n")
    while (x != "1" and x != "2" and x != "3"):
        x = input("Número inválido, purba de nuevo: ")
    if (x == "1"):
        register_user()
    elif(x == "2"):
        access_user()
    elif(x == "3"):
        sys.exit()

if __name__ == "__main__":
    print("Bienvenido al programa de Cryptografía")
    main()
    sys.exit()