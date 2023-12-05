import sys
import random
import os

from OpenSSL import crypto

def main():
    print("Presiona 1 para crear una nueva autoridad de certificado")
    print("Presiona 2 para actualizar el estado de los certificados de una autoridad de certificados")
    print("Presiona 3 para gestionar los certificados de una autoridad de certificados")
    print("Presiona 4 para salir")

    x = input("Number pressed: \n")
    while (x != "1" and x != "2" and x != "3" and x != "4"):
        x = input("Número inválido, purba de nuevo: ")
    if (x == "1"):
        set_up_CA()
    elif(x == "2"):
        print("actualizar")
    elif(x == "3"):
        CA_review()
    elif(x == "4"):
        sys.exit()

#Verificar primero las solicitudes de certificados y después las inválidos (rechazados y caducados)
def CA_review():
    CA_id = input("Introduce el ID de la CA que quieres gestionar: ")

    #Verifica si la ruta existe
    if not os.path.exists("./CA_" + CA_id):
        print("CA no existe")
        main()

    #Importar llave privada de la CA
    with open("CA_" + CA_id + ".pem", "rt") as f:
        CA_private_key = crypto.load_privatekey(crypto.FILETYPE_PEM, f.read())
        f.close()
    
    #Importar certificado de la CA
    with open("CA_" + CA_id + "/certificados/CA_" + CA_id + "certificado.pem", "rt") as f:
        CA_certificate = crypto.load_certificate(crypto.FILETYPE_PEM, f.read())
        f.close()

    #Obtener lista de solicitudes de certificados
    certicates_path = os.listdir("CA_" + CA_id + "/solicitudes")
    for i in certicates_path:
        print(i) 
        #Importar solicitudes de certificados
        request_path = "CA_" + CA_id + "/solicitudes/" + i
        
        with open(request_path, 'rb') as f:
            request = crypto.load_certificate_request(crypto.FILETYPE_PEM, f.read())
            f.close()

        #Mostrar info
        print("Subject:", request.get_subject())
        print("Public Key:", request.get_pubkey())

        #Gestionar solicitud
        x = input("Presiona [y] para garantizar certificado \nPresiona [n] para negar certificado\n")
        while (x != "y" and x != "n"):
            x = input("Número inválido, purba de nuevo: ")
        if (x == "y"):
            certificate = crypto.X509()
            certificate.set_subject(request.get_subject())
            certificate.set_pubkey(request.get_pubkey())
            certificate.gmtime_adj_notBefore(0)
            certificate.gmtime_adj_notAfter(31536000)  # 1 year
            certificate.set_issuer(CA_certificate.get_subject())
            certificate.sign(CA_private_key, "sha256")

            #Guardar certificado
            with open("CA_" + CA_id + "/certificados/" + i[:-4] + ".pem", "wb") as f:
                f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, certificate))
        
        #Borrar solicitud
        os.remove(request_path)

def set_up_CA():
    #Esta parte es la menos realista, ya que el proceso es mucho más complejo que generar ids random y tres subdirectorios
    AC_id = ''.join([str(random.randint(0, 9)) for _ in range(4)]) #Crear id random para CA
    ruta_CA = "./CA_" + AC_id + "/"
    os.makedirs(ruta_CA + "certificados", exist_ok=True) #Crear subdirectorios
    os.makedirs(ruta_CA + "inválidos", exist_ok=True)
    os.makedirs(ruta_CA + "solicitudes", exist_ok=True) 

    # Generar una clave privada para la CA
    ca_private_key = crypto.PKey()
    ca_private_key.generate_key(crypto.TYPE_RSA, 2048)

    # Crear un certificado autofirmado para la CA
    ca_cert = crypto.X509()
    ca_cert.get_subject().CN = AC_id
    ca_cert.set_serial_number(1)
    ca_cert.gmtime_adj_notBefore(0)
    ca_cert.gmtime_adj_notAfter(365*24*60*60)  # Un año de validez
    ca_cert.set_issuer(ca_cert.get_subject())
    ca_cert.set_pubkey(ca_private_key)
    ca_cert.sign(ca_private_key, 'sha256')

    # Guardar el certificado en un archivo
    with open(ruta_CA + "certificados/CA_" + AC_id + "certificado.pem", "wt") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, ca_cert).decode("utf-8"))
        f.close()
    
    #Guardar la clave privada de la CA (en teoría solo la tendría la CA en local)
    with open("CA_" + AC_id + ".pem", "wt") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, ca_private_key).decode("utf-8"))
        f.close()
    
    #Ir a main
    main()

if __name__ == "__main__":
    print("Bienvenido al programa de la Autoridad de certificación")
    main()
    sys.exit()