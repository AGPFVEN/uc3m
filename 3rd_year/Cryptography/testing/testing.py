import rsa
import time
from OpenSSL import crypto

#Get public key
#2d2d2d2d2d424547494e20525341205055424c4943204b45592d2d2d2d2d0a4d49494269674b43415945416c4138414b2f312b55545735694a5976324146324c4d5a397a43796452506a356332446769352f50463356776f322b36432f71710a3942625a486241544e5358363845675456557a3834464f71645338774c2f5145587644613546436673786e6b536d395a506b2f2f3572696b6d6d44725354716b0a6d6e3670484f54515a446e46676556712b644a2f796e5876745959626f3231312f727a3756394b6e556777544347534f41694a4a754e794a75454166736c4e550a64764149357068596e4e4a41386f742f5144766b73394634787a6d31684851656459786b5966306c51386e46612b4753446674386136506953454c324a6e382f0a54656473473937487146367a687047745846413456564e5a662f5a786f47327a6c7932514c4874572f30486e45396e6b527a70443047704c77334967783656460a5363457753727459394e5451416f4f44335765764f7236384157565a7a4e6d7747694e7a326f444e367967586b4b6d63536468474d70797173514f31432b566d0a6162793236304767436a7a712f416f31307464363334546a4156474e4c666e576a36734d6d55727745344b55314a4574316538504b74766956586b2f63585a460a33335779522b2f7a71365574376b34325a744d6e4949484939495a54484d34694533674a574936347931422f38466c4d76417333385050794a683136785269300a4d55426a54446c567758594c41674d424141453d0a2d2d2d2d2d454e4420525341205055424c4943204b45592d2d2d2d2d0a
publicKey ="2d2d2d2d2d424547494e20525341205055424c4943204b45592d2d2d2d2d0a4d49494269674b43415945416c4138414b2f312b55545735694a5976324146324c4d5a397a43796452506a356332446769352f50463356776f322b36432f71710a3942625a486241544e5358363845675456557a3834464f71645338774c2f5145587644613546436673786e6b536d395a506b2f2f3572696b6d6d44725354716b0a6d6e3670484f54515a446e46676556712b644a2f796e5876745959626f3231312f727a3756394b6e556777544347534f41694a4a754e794a75454166736c4e550a64764149357068596e4e4a41386f742f5144766b73394634787a6d31684851656459786b5966306c51386e46612b4753446674386136506953454c324a6e382f0a54656473473937487146367a687047745846413456564e5a662f5a786f47327a6c7932514c4874572f30486e45396e6b527a70443047704c77334967783656460a5363457753727459394e5451416f4f44335765764f7236384157565a7a4e6d7747694e7a326f444e367967586b4b6d63536468474d70797173514f31432b566d0a6162793236304767436a7a712f416f31307464363334546a4156474e4c666e576a36734d6d55727745344b55314a4574316538504b74766956586b2f63585a460a33335779522b2f7a71365574376b34325a744d6e4949484939495a54484d34694533674a574936347931422f38466c4d76417333385050794a683136785269300a4d55426a54446c567758594c41674d424141453d0a2d2d2d2d2d454e4420525341205055424c4943204b45592d2d2d2d2d0a"
publicKeyRSAObj = rsa.PublicKey.load_pkcs1(bytes.fromhex(publicKey))
publicK_obj = crypto.load_publickey(crypto.FILETYPE_PEM, publicKeyRSAObj._save_pkcs1_pem())

#Get private key
with open("test2.pem", "rt") as f:
    privateK = f.read()
privateK_obj = crypto.load_privatekey(crypto.FILETYPE_PEM, privateK)

#crear solicitud de certificado
cert_req = crypto.X509Req()
cert_req.get_subject().CN = "mi dominio"
cert_req.set_pubkey(publicK_obj)
cert_req.sign(privateK_obj, "sha256")

# Exportar la solicitud de certificado a un archivo
with open("mi_solicitud.csr", "wt") as f:
    f.write(crypto.dump_certificate_request(crypto.FILETYPE_PEM, cert_req).decode("utf-8"))

# Importar la solicitud de certificado desde un archivo
with open("mi_solicitud.csr", "rt") as f:
    cert_req_imported = crypto.load_certificate_request(crypto.FILETYPE_PEM, f.read())

with open("agpfven.pem", "rt") as f:
    privateK = f.read()
    privateK_obj = crypto.load_privatekey(crypto.FILETYPE_PEM, privateK)

# Crear un certificado
cert = crypto.X509()
cert.set_subject(cert_req.get_subject())
cert.set_issuer(cert_req.get_subject())
cert.set_pubkey(cert_req.get_pubkey())
cert.sign(privateK_obj, "sha256")

# Convertir el certificado a formato PEM
cert_pem = crypto.dump_certificate(crypto.FILETYPE_PEM, cert)

# Guardar el certificado en un archivo----------------------------------------------
with open("mi_certificado_firmado.pem", "wt") as f:
    f.write(cert_pem.decode("utf-8"))
    
# Obtener el período de validez del certificado-----------------------------
not_before = time.strptime(cert.get_notBefore().decode('ascii'), '%Y%m%d%H%M%SZ')
not_after = time.strptime(cert.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')

# Convertir a tiempo en segundos desde la época
not_before = time.mktime(not_before)
not_after = time.mktime(not_after)

# Obtener el tiempo actual en segundos desde la época
now = time.time()

# Verificar el período de validez del certificado
if not_before <= now <= not_after:
    print("El certificado está dentro de su período de validez.")
else:
    print("El certificado no está dentro de su período de validez.")

# Verificar la firma del certificado------------------------------------------------
try:
    store = crypto.X509Store()
    store.add_cert(cert)
    store_ctx = crypto.X509StoreContext(store, cert)
    store_ctx.verify_certificate()
    print("El certificado está correctamente firmado.")
except crypto.X509StoreContextError:
    print("La firma del certificado no es válida.")

print(cert_req_imported.get_subject())