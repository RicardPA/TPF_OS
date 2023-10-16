class Driver:
	def __init_(self, name, used, location, punctuation, houseLocation, dateInitApp):
		self.name = name
		self.used = used
		self.location = location
		self.punctuation = punctuation
		self.houseLocation = houseLocation
		self.dateInitApp =dateInitApp
		
	def driveToString(self):
		 print("Nome:" + self.name)
		 print("Utilizado:" + self.used)
		 print("Localização:" + self.location)
		 print("Pontuação:" + self.punctuation)
 		 print("Localização da casa:" + self.houseLocation)
  		 print("Horário de inicialização do aplicativo:" + self.dateInitApp)
