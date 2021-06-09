from datetime import datetime


nasc = input('Quando voce nasceu? ')

nasc = datetime.strptime(nasc, '%d/%m/%Y')
print(f'voce tem {datetime.today() - nasc} de vida')
