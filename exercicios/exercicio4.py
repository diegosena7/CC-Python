inputSegundos = int(input("Digite os segundos: "))

segundos = inputSegundos % 60
minutos = (inputSegundos // 60) % 60
horas = (inputSegundos // 60 // 60) % 24
dias = inputSegundos // 60 // 60 // 24

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")