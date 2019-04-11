#############################################
#                                           #
# Ejercicio 9, practica 1, version PYTHON   #
# (Redes y Sistemas Distribuidos, UMA)      #
# Autor: Arturo Fernandez Perez             #
#                                           #
#############################################

import psutil, socket

addrs = psutil.net_if_addrs() #Para obtener las interfaces y sus direcciones MAC
stats = psutil.net_if_stats() #Para saber si la interfaz esta activa

#print(addrs.keys())
#print(stats.keys())

#Para cada interfaz i en el diccionario
for i in addrs:
	#Para cada elemento t de la tupla en el valor que corresponde a i
	for t in addrs[i]:
		#Si tiene asignada IP, guardo los datos de la (sub)red
		if t.family == socket.AF_INET:
			ip = t.address
			nm = t.netmask
			bc = t.broadcast

		#Compruebo si tiene direccion MAC
		if t.family == psutil.AF_LINK:
			mac = t.address
			#Muestro el nombre de la interfaz y su direccion MAC
			print(f"{i}: {mac}", end =" ")

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
				print(f"- IP: {ip}")
				print(f"- Netmask: {nm}")
				print(f"- Broadcast: {bc}")

			#Muestro si la interfaz es full-duplex o half-duplex, o desconocido
			if stats[i].duplex == psutil.NIC_DUPLEX_FULL:
				print("- Duplex mode: FULL-DUPLEX")
			elif stats[i].duplex == psutil.NIC_DUPLEX_HALF:
				print("- Duplex mode: HALF-DUPLEX")
			else:
				print("- Duplex mode: Unknown")
			#Muestro la velocidad de la interfaz
			print(f"- Speed (MB/s): {stats[i].speed}")
			#Muestro el MTU
			print(f"- MTU: {stats[i].mtu}")

			print()
			ip = None

