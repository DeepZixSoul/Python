"""diccionar por defecto"""
from collections import defaultdict

mi_dic = {'uno': 'verde', 'dos':'rojo', 'tres':'azul' }

print(mi_dic['tres'])
#falla
#print(mi_dic['cautr'])

#añade un nuevo valor a una nueva clave valor='nada'
mi_dic1 = defaultdict(lambda : 'nada')
# clave nueva 'dos'
mi_dic1['uno'] = 'verde'
print(mi_dic1['dos'])

print(mi_dic1)

