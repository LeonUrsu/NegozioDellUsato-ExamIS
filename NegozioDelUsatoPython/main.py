from datetime import *


date_format = '%d/%m/%Y, %H/%M/%S '
today = datetime.today()
tomorrow = datetime.today() + timedelta(minutes=1)
if tomorrow >= today:
    print('ciao')
print(today, tomorrow)