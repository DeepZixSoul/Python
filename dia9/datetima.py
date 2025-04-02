from datetime import datetime, date


"""mi_hora = datetime.time(17, 33,50,166)

print(type(mi_hora))
print(mi_hora.minute)
print(mi_hora.hour)
print(mi_hora)"""

"""mi_dia = datetime.date(2025,10,17)
print(mi_dia)
print(mi_dia.year)
print(mi_dia.month)
print(mi_dia.ctime())
print(mi_dia.today())"""

"""mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 25000)

print(mi_fecha)

mi_fecha=mi_fecha.replace(month=11)

print(mi_fecha)
"""
"""nacimiento = date(1995, 3, 2)
defuncion = date(2095, 6, 19)

vida = defuncion - nacimiento
# Tiempo que viviste
print(vida)
print(vida.days)"""

# Tiempo despierta

despierta = datetime(2022, 10, 5, 7,30)
duerme = datetime(2022, 10, 5, 23, 45)
vigilia = duerme - despierta
print(vigilia)
print(vigilia.seconds)

hoy = datetime.today()
print(hoy)