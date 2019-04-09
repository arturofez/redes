#############################################
#											#
# Ejercicio 9, práctica 1, versión PYTHON	#
# (Redes y Sistemas Distribuidos, UMA)		#
# Autor: Arturo Fernández Pérez				#
#											#
#############################################

import psutil

addrs = psutil.net_if_addrs() #Para obtener las interfaces y sus direcciones MAC
stats = psutil.net_if_stats() #Para saber si la interfaz esta activa

#print(addrs.keys())
#print(stats.keys())

#Para cada interfaz i en el diccionario
for i in addrs:
	#Para cada elemento t de la tupla en el valor que corresponde a i
	for t in addrs[i]:
		#Si tiene asignada IP, guardo los datos de la (sub)red
		if t.family == 2:
			ip = t.address
			nm = t.netmask
			bc = t.broadcast

		#Compruebo si tiene direccion MAC
		if t.family == 18:
			mac = t.address
			#Muestro el nombre de la interfaz y su direccion MAC
			print(i + ": " + str.upper(mac), end =" ")

			#Muestro si es local o globalmente administrada
			#(penultimo bit del primer byte)
			firstByte = mac[:2]
			binByte = '{0:08b}'.format(int(firstByte,16))
			if int(binByte[6]) == 0:
				print("- global", end =" ")
			else:
				print("- local", end =" ")

			#Muestro si la interfaz esta activa
			if stats[i].isup:
				print("- (up)")
			else:
				print("- (down)")

			#Muestra (si tiene asingadas) la IP, la máscara de red
			#y la dirección de broadcast
			if ip != None:
				print("- IP: " + ip)
				print("- Netmask: " + nm)
				print("- Broadcast: " + bc)

			#Muestro si la interfaz es full-duplex o half-duplex, o desconocido
			if stats[i].duplex == 2:
				print("- Duplex mode: FULL-DUPLEX")
			elif stats[i].duplex == 1:
				print("- Duplex mode: HALF-DUPLEX")
			else:
				print("- Duplex mode: unknown")
			#Muestro la velocidad de la interfaz
			print("- Speed (MB/s): " + str(stats[i].speed))
			#Muestro el MTU
			print("- MTU: " + str(stats[i].mtu))

			print()
			ip = None

