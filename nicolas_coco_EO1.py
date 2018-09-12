#La duración en segundos de un intervalo dado en horas, minutos y segundos.

def pedir_intervalo ():
    hora=int(input("Ingrese la hora del intervalo "))
    minuto=int(input("Ingrese los minutos del intervalo "))
    segundo=int(input("Ingrese los segundos del intervalo "))
    intervalo_en_segundos= (hora*3600)+(minuto*60)+segundo
    return intervalo_en_segundos

intervalo_en_segundos= pedir_intervalo()
print(intervalo_en_segundos)

#b) La duración en horas, minutos y segundos de un intervalo dado en segundos.

def pedir_intervalo_en_segundos ():
    segundos=int(input("Ingrese el valor del intervalo en segundos"))
    hora_a_segundos = (int(segundos / 3600))
    minutos_a_segundos = int((segundos - (hora_a_segundos * 3600)) / 60)
    segundos_a_segundos = segundos - ((hora_a_segundos * 3600) + (minutos_a_segundos* 60))
    intervalo_hora_minuto_segundo= hora_a_segundos, minutos_a_segundos, segundos_a_segundos
    return intervalo_hora_minuto_segundo

intervalo_hh_mm_ss= pedir_intervalo_en_segundos()
print(intervalo_hh_mm_ss)







