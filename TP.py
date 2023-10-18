class Driver:
    def __init__(self, identifier, name, user, location, punctuation, house_location, date_init_app, travel_time, travel_history):
        self.identifier = identifier
        self.name = name
        self.user = user
        self.location = location
        self.punctuation = punctuation
        self.house_location = house_location
        self.travel_time = travel_time
        self.date_init_app = date_init_app
        self.travel_history = travel_history

    def driver_to_string(self):
        print("Nome: " + self.name)
        print("Utilizado: " + self.used)
        print("Localização: " + self.location)
        print("Pontuação: " + self.punctuation)
        print("Tempo de locomoção: " + self.travel_time)
        print("Localização da casa: " + self.house_location)
        print("Horário de inicialização do aplicativo: " + self.date_init_app)


class User:
    def __init__(self, identifier, name, location, search, destiny, driver):
        self.identifier = identifier
        self.name = name
        self.location = location
        self.search = search
        self.destiny = destiny
        self.driver = driver

    def user_to_string(self):
        print("Nome: " + self.name)
        print("Localização: " + self.location)
        print("Busca: " + self.search)
        print("Destino: " + self.destiny)


import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

# Coordenadas geográficas de pontos extremos
points = [
    {'name': 'C', 'latitude': 90, 'longitude': 180},
    {'name': 'D', 'latitude': -90, 'longitude': 180},
    {'name': 'A', 'latitude': 90, 'longitude': -180},
    {'name': 'B', 'latitude': -90, 'longitude': -180}
]

# Extrair as coordenadas dos pontos extremos
extreme_points = [(point['longitude'], point['latitude']) for point in points]

# Separar as coordenadas x e y
x_coords, y_coords = zip(*extreme_points)

plt.figure(figsize=(10, 6))

# Adicionar os pontos no mapa
for i in range(len(points)):
    plt.text(points[i]['longitude'], points[i]['latitude'], points[i]['name'])

# Adicionar a reta conectando os pontos extremos
plt.plot(x_coords, y_coords, linestyle='--', color='blue', label='Reta entre pontos extremos')

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Mapa com Reta entre Pontos Extremos')

plt.legend()
plt.grid(True)
plt.show()


