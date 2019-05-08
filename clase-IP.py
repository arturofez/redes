import sys, string

#Comprueba que un IP es válida
def validarIP(ip):
	s = ip.split(".", 3)
	for p in s:
		if not p.isdigit() or int(p) < 0 or int(p) > 255:
			return False
	return True

#Dada la IP devuelve su clase
def claseIP(ip):
	fb = ip.b1
	if 0 <= fb < 128:
		return "A"
	elif 127 < fb < 192:
		return "B"
	elif 191 < fb < 224:
		return "C"
	elif 223 < fb < 240:
		return "D"
	else:
		return "E"

#Dado el prefijo devuelve la máscata en decimal punto
def mascdp(pref):
	if pref < 0 or pref > 32:
		raise Exception()
	mascdp = ""
	for i in range(0, pref):
		mascdp = mascdp + "1"
	for j in range(0, 32-pref):
		mascdp = mascdp + "0"
	m1 = str(int(mascdp[0:8], 2))
	m2 = str(int(mascdp[8:16], 2))
	m3 = str(int(mascdp[16:24], 2))
	m4 = str(int(mascdp[24:32], 2))
	mascdp = m1 + "." + m2 + "." + m3 + "." + m4
	return Ip(mascdp)

#Dada la IP y la máscara de red devuelve el ID de red
def id(ip, mascdp):
	i1 = str(ip.b1 & mascdp.b1)
	i2 = str(ip.b2 & mascdp.b2)
	i3 = str(ip.b3 & mascdp.b3)
	i4 = str(ip.b4 & mascdp.b4)
	id = i1 + "." + i2 + "." + i3 + "." + i4
	return Ip(id)

#Dado el prefijo, calcula el número de hosts
def nips(pref):
	if pref > 30:
		return 0
	else:
		return 2**(32-pref)-2

#Dada la ip, y la máscara en decimal punto y en prefijo calcula la dirección de broadcast
def broadcast(ip, mascdp, pref):
	b1 = str(bin(ip.b1)[2:10]).zfill(8)
	b2 = str(bin(ip.b2)[2:10]).zfill(8)
	b3 = str(bin(ip.b3)[2:10]).zfill(8)
	b4 = str(bin(ip.b4)[2:10]).zfill(8)
	b = b1 + b2 + b3 + b4

	bc = ""
	for i in range(0, pref):
		bc = bc + b[i]
	for i in range(pref, 32):
		bc = bc + "1"

	m1 = str(int(bc[0:8], 2))
	m2 = str(int(bc[8:16], 2))
	m3 = str(int(bc[16:24], 2))
	m4 = str(int(bc[24:32], 2))
	bc2 = m1 + "." + m2 + "." + m3 + "." + m4

	return Ip(bc2)

#Clase IP
class Ip():
	def __init__(self, ip):
		if not validarIP(ip):
			raise Exception()
		self.dir = ip
		s = ip.split(".", 3)
		self.b1 = int(s[0])
		self.b2 = int(s[1])
		self.b3 = int(s[2])
		self.b4 = int(s[3])

	def __str__(self):
		return self.dir


if __name__ == "__main__":
	if len(sys.argv) < 3:
		print(f"Uso: {sys.argv[0]} <Dirección IP> <Máscara de red>")
		print("Introduzca la IP en formato punto decimal y la máscara de red como prefijo.\n")
	else:
		try: #Compruebo si la IP es válida y muestro su clase
			ip = Ip(sys.argv[1])
			print(f"La IP {ip} es válida y es de clase {claseIP(ip)}")
		except: #Si no es válida:
			print(f"{sys.argv[1]} no es una dirección IP válida")
			print("Introduzca la IP en formato decimal punto.\n")
			exit(-1)
		
		try: #Comprueba si la máscara de red es válida y la transformo a decimal punto
			pref = int(sys.argv[2])
			mascdp = mascdp(pref)
		except: #Si no es válida:
			print(f"{sys.argv[2]} no es una máscara de red válida")
			print("Introduzca la máscara de red como prefijo.\n")
			exit(-1)

		#Cálculo el ID de red y lo muestro
		id = id(ip, mascdp)
		print(f"ID de red: {id}")
		#Muestro la máscara de red
		print(f"Máscara de red: {mascdp}")
		#Cálculo la direción de broadcast y la muestro
		bc = broadcast(ip, mascdp, pref)
		print(f"Broadcast: {bc}")
		print(f"Número de IPs para host: {nips(pref)}")

		#Muestro el rango de hosts
		if pref > 30:
			print(f"Rango: - ")
		else:
			r1 = id.dir.split(".", 3)
			r1[3] = str(int(r1[3]) + 1)
			r2 = bc.dir.split(".", 3)
			r2[3] = str(int(r2[3]) - 1)
			r1 = Ip(".".join(r1))
			r2 = Ip(".".join(r2))
			print(f"Rango: {r1}-{r2}")
