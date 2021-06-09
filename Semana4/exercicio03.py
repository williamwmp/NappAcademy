from datetime import datetime

nasc = input('Digite quando nasceu? ')
nasc = datetime.strptime(nasc, '%d/%m/%Y')
hoje = datetime.today()

anos = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))

print(anos)