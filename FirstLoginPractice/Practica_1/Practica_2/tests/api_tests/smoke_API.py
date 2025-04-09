import requests

# URL del endpoint
url = "https://admin-demo.nopcommerce.com/login?returnurl=%2Fadmin%2F"

# Datos del formulario
data = {
    "Email": "admin@yourstore.com",  # Reemplaza con el email
    "Password": "admin",            # Reemplaza con la contraseña
    "__RequestVerificationToken": "CfDJ8OLWedOnyOZDsfP51Y0TlDTVkhiKYWU5asskZSYT5zNuvaeLlcv8yxn7TCZY7Qg_HSVtrK_KIx3UqpRLEFic_DJJOrEBrCGjICktjd7fLRuLshSwNT_-owEgzZ4ZqM1KhXnlAtlKoz705VSvPNd9xqc"  # Copia el valor del token de la página
}

# Cabeceras (opcional)
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

# Enviar solicitud POST
response = requests.post(url, data=data, headers=headers)

# Mostrar la respuesta
print(f"Status Code: {response.status_code}")
print("Response Body:")
print(response.text)