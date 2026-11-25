# Asi se crean las 'Cajas' con datos de tu ruta
cliente = "Walmart Torres"
distancia_km = 45
clima = "Lluvia"
tiempo_estimado_minutos = 60
tiempo_real_minutos = 95

# Claculmos la diferencia del tiempo
retraso = tiempo_real_minutos - tiempo_estimado_minutos

# Creamos la regla de decision
if retraso > 0:
    print("Alerta: El camión llegó tarde con el cliente.")
    print("Minutos de retraso:", retraso)
else:
    print("PROCESO OK: El camión entregó a tiempo.")