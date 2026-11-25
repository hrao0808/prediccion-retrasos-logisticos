#1. Tus datos de entrada (Tu lista e camiones)
tiempos_reales = [50, 95, 60, 120, 45]
tiempo_estimado = 60

print("--- INICIANDO AUDITORÍA DE RUTAS ---")

#2. El bucle: 'tiempo' tomaráel valor de cada camión uno por uno
for tiempo in tiempos_reales:
    retraso = tiempo - tiempo_estimado

    if retraso > 0:
        print(f"ALERTA: El camión tardó {tiempo} min. Llegó tarde por {retraso} min.")
    else:
        print(f"PROCESO OK: El camión tardó {tiempo} min. Entregó a tiempo.")

print("--- AUDITORÍA TERMINADA ---")