import datetime
from time import ctime
import ntplib
import os
from subprocess import call
t1=datetime.datetime.now()
print("Hora de inicio de la peticion: %s" % t1)
sdt="time-a-wwv.nist.gov"
print("\nObteniendo la hora del servidor NTP:")
clntp=ntplib.NTPClient()
respuesta=clntp.request(sdt)
ha=datetime.datetime.strptime(ctime(respuesta.tx_time),"%a %b %d %H:%M:%S %Y")
print("respuesta de " +sdt +  ": "+ str(ha)+ "\n")
t2=datetime.datetime.now()
print("Hora de llegada de la peticion: %s" % t2)
aj=(t2-t1)/2
print("El ajuste es %s" % aj)
rel=ha+aj
call("date \""+rel.strftime("%m%d%H%M%Y.%S") + "\"", shell = True)
call("hwclock --systohc", shell =True)
print("Hora cambiada: %s" % rel)
