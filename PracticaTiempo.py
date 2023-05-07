print("Hola como estas! Por favor indica la Hora, Minutos y duracion de tu Curso")
hora = int(input("Hora de inicio de tu curso: "))
minutos = int(input("Minutos: "))
duracion = int(input("Duracion de tu Curso en Minutos: "))

hora_entrada = hora
minutos_entrada = minutos
duracion_curso = duracion

duracion_hora = 60
horas_dia = 24

minutos = minutos + duracion
hora = hora + minutos // duracion_hora
minutos = minutos % duracion_hora
hora = hora % horas_dia

print(
    "Tu curso inicia a la(s): ",
    hora_entrada,
    ":",
    minutos_entrada,
    "y dura: ",
    duracion_curso,
    "Minutos.",
    "Saldras a la siguiente hora: ",
    hora,
    ":",
    minutos,
    ",Mucha Suerte!!!",
    sep=" ",
)
