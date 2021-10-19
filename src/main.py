from maps import GoogleMaps


def createInput(*input_messages):
    """
    """
    input_data = []
    for message in input_messages:
        value_input = input(message)
        input_data.append(value_input)
    return input_data


maps = GoogleMaps()  # Objeto

choose = input(
    "Cordernadas ou Endereço: | [1] Coordenadas || [2] Endereço | : ")

if int(choose) == 1:
    cord_one, cord_two = createInput(
        "Digite a latitude:  ", "Digite a longitude:  ")
    maps.cord(cord_one, cord_two)
elif int(choose) == 2:
    street, district, city, state = createInput(
        "Digite a rua:  ", "Digite o bairro:  ", "Digite a cidade:  ", "Digite o estado:  ")
    maps.addres(street, district, city, state)
else:
    print("Por favor, ponha um dado válido")
