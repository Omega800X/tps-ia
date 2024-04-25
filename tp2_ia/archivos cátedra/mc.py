class Estado(object):
	def __init__(self, estado, canoa):
		self.estado = estado
		self.canoa = canoa

		if not self.es_valido():
			raise ValueError("estado no valido")

	def es_valido(self):
		#
		# Explicar el objetivo de "es_valido"
		#

		for gente in self.estado:
			for persona in gente:
				if persona > 3 or persona < 0:
					return False

		for mis, can in self.estado:
			if mis and can > mis:
				return False

		return True

	def viaja(self, gente):
		#
		# Explicar el objetivo de "viaja"
		#

		estado = copy.deepcopy(self.estado)
		canoa = self.canoa

		estado[canoa][0] -= gente[0]
		estado[canoa][1] -= gente[1]
		canoa = 0 if canoa else 1
		estado[canoa][0] += gente[0]
		estado[canoa][1] += gente[1]

		return Estado(estado, canoa)

	def __str__(self):
		"""Muestra el estado como una representacion en texto."""
		return "M: %d C: %d | %s\\___/%s | M: %d C: %d" % (
			   self.estado[0][0], self.estado[0][1],
			   '~' * 8 * self.canoa, '~' * (8 - 8 * self.canoa),
			   self.estado[1][0], self.estado[1][1]
			   )

	def __eq__(self, other):
		return self.estado == other.estado and self.canoa == other.canoa

	def __ne__(self, other):
		return not self.__eq__(other)

def main():
	# donde empezamos
	#
	# Completar con el código correspondiente
	#
	inicio = 
	# a donde queremos llegar
	#
	# Completar con el código correspondiente
	#
	final = 

	# los viaje posibles ( legales )
	#
	# Completar con el código correspondiente
	#	
	viajes = 

	# los viajes que probamos desde cada estado
	viajes_posibles = list(viajes)

	# guardamos el recorrido y las opciones que no hemos usado
	# para poder 'volver atras' si hay problemas (backtracking)
	recorrido = []
	viajes_restantes = []

	while inicio != final and viajes_posibles:
		while viajes_posibles:
			# probamos un viaje cualquiera
			viaje = viajes_posibles.pop()

			try:
				nuevo = inicio.viaja(viaje)

				# si no hemos estado nunca alla
				if nuevo not in recorrido:
					# guarda el estado y las opciones restantes
					recorrido.append(inicio)
					viajes_restantes.append(viajes_posibles)

					# continuamos desde la nueva posicion
					inicio = nuevo
					viajes_posibles = list(viajes)
			except ValueError:
				# no es valido, probamos el siguiente
				pass

		# si no hemos encontrado nada, backtracking
		if not viajes_posibles and recorrido:
			inicio = recorrido.pop()
			viajes_posibles = viajes_restantes.pop()

	if inicio == final:
		print ("Tenemos un resultado!")
		for estado in recorrido:
			print (estado)
		print (inicio)
	else:
		# no va a pasar ;)
		print ("No hemos encontrado un resultado :(")

if __name__ == "__main__":
	main()