dias = int(input('digite a quantidade de dias: '))
horas = int(input('digite a quantidade de horas: '))
segundos = int(input('digite a quantidade de segundos: '))

total_segundos = (dias * 86400) + (horas * 3600) + (segundos)
print(f' o total em segundos é {total_segundos}')
