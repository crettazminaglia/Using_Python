#Usando las funciones del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados en
# horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.

def pedir_y_sumar_intervalo ():
    hora_inicial=int(input("Ingrese la hora del intervalo inicial "))
    minuto_inicial=int(input("Ingrese los minutos del intervalo inicial "))
    segundo_inicial=int(input("Ingrese los segundos del intervalo inicial "))
    hora_final = int(input("Ingrese la hora del intervalo final "))
    minuto_final = int(input("Ingrese los minutos del intervalo final "))
    segundo_final = int(input("Ingrese los segundos del intervalo final "))
    suma_hora= (hora_inicial+hora_final)*3600
    suma_minuto= (minuto_inicial+minuto_final)*60
    suma_segundo= segundo_inicial+segundo_final
    suma_total_en_segundos= suma_hora+suma_minuto+suma_segundo
    return suma_total_en_segundos

def transformar_segundos_a_formato_hora (suma_total_en_segundos):
    hora_a_segundos = (int(suma_total_en_segundos / 3600))
    minutos_a_segundos = int((suma_total_en_segundos - (hora_a_segundos * 3600)) / 60)
    segundos_a_segundos = suma_total_en_segundos - ((hora_a_segundos * 3600) + (minutos_a_segundos* 60))
    intervalo_hora_minuto_segundo= hora_a_segundos, minutos_a_segundos, segundos_a_segundos
    return intervalo_hora_minuto_segundo

intervaloensegundos=pedir_y_sumar_intervalo()
devolver_formato_hora= transformar_segundos_a_formato_hora(intervaloensegundos)
print(devolver_formato_hora)








