
from datetime import datetime

dia_jogo = "08/07/2014"
data = datetime.strptime(dia_jogo, '%d/%m/%Y')
print(datetime.today() - data)