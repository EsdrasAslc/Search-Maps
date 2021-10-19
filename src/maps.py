import webbrowser


class GoogleMaps():

    def __init__(self) -> None:
        self.maps_url = "https://www.google.com/maps/search/?api=1&query="
        self.alert_message = "Veja seu local em seu navegador padrão!"

    def cord(self, cord1, cord2):
        print(self.alert_message)
        full_url = f"{self.maps_url}{cord1}%2C{cord2}"
        webbrowser.open(full_url)

    def addres(self, street, district, city, state):
        print(self.alert_message)
        full_url = f"{self.maps_url}{street}+{district}+{city}+{state}"
        webbrowser.open(full_url)


if __name__ == "__main__":
    maps = GoogleMaps()
    # maps.addres("Rua Angelo Ferreira Fagundes",
    #             "Jardim Trianom", "Taboão da Serra", "São Paulo")
    maps.cord(-12.984103447198363, -38.43574894294015)
