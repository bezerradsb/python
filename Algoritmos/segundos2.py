segs_str  = input("Por favor, entre com o número de segundos que deseja converter: ")

segs_int = int(segs_str)

dias = segs_int // 86400
segs_rest1 = segs_int % 86400
horas = segs_rest1 // 3600
segs_rest2 = segs_rest1 % 3600
minutos = segs_rest2 // 60
segs_final = segs_rest2 % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_final, "segundos.")



