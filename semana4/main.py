adversario = 'Iron-man'

def saludo():
    return 'hola'

LOKI_DISFRACES = {
    'Iron-man': saludo,
    'Thor': 'Odin',
    'Hulk':'Thanos'
}

loki = LOKI_DISFRACES[adversario]
print(loki)
