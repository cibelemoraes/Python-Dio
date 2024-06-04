from datetime import datetime
import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/SãoPaulo"))

print (data)

