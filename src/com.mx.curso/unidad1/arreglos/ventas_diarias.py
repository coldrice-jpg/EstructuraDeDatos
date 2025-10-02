# Dias de la semana
periodo_semanal = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ingresos_semana = []

print("Registro de Ingresos de la Semana ")

# Bucle para registrar los datos
for dia in periodo_semanal:
    monto_str = input(f"Monto para el día {dia}: $")
    monto_dia = float(monto_str)
    ingresos_semana.append(monto_dia)

# Calculos de las ventas
ingreso_total = sum(ingresos_semana)
ingreso_promedio = ingreso_total / len(ingresos_semana)
ingreso_superior = max(ingresos_semana)
ingreso_inferior = min(ingresos_semana)

indice_superior = ingresos_semana.index(ingreso_superior)
indice_inferior = ingresos_semana.index(ingreso_inferior)

# Se obtienen los nombres de los días correspondientes
dia_mayor_rendimiento = periodo_semanal[indice_superior]
dia_menor_rendimiento = periodo_semanal[indice_inferior]

# Se muestra un resumen de los ingresos de cada día
print("\nResumen de Ingresos por Día:")
for i in range(len(periodo_semanal)):
    nombre_dia = periodo_semanal[i]
    monto_dia = ingresos_semana[i]
    print(f" - {nombre_dia}: ${monto_dia}")

# Imprimir los resultados
print(f"Ingreso Total de la Semana: ${ingreso_total}")
print(f"Ingreso Promedio Diario: ${ingreso_promedio}")
print(f"Día de Mayor Rendimiento: {dia_mayor_rendimiento} (${ingreso_superior})")
print(f"Día de Menor Rendimiento: {dia_menor_rendimiento} (${ingreso_inferior})")