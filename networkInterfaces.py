#############################################
#											#
# Ejercicio 9, practica 1, version PYTHON	#
# (Redes y Sistemas Distribuidos, UMA)		#
# Autor: Arturo Fernandez Perez				#
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
		if t.family == 18 or t.family == 17:
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

			#Muestra (si tiene asingadas) la IP, la mascara de red
			#y la direccion de broadcast
			if ip != None:
				print("- IP: " + ip)
				if nm != None:
					print("- Netmask: " + nm)
				if bc != None:
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

