correo = "cesarserranobenitez@gmail.com"
nuevoDominio = "ceu.es"
pos1 = correo.find("@")
dominio = correo[pos1+1::1]

correo = correo.replace(dominio,nuevoDominio)

print(correo)