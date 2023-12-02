import requests
import json


def get_data(url):
    response = requests.get(url)
    return response.json()


def main():
    base_url = "https://swapi.dev/api/"
    starship_url = base_url + "starships/10/"
    starship_data = get_data(starship_url)

    # Вывод основной информации о корабле
    print("\nStarship Info:")
    print(f"Name: {starship_data['name']}")
    print(f"Max Speed: {starship_data['max_atmosphering_speed']}")
    print(f"Class: {starship_data['starship_class']}")

    # Вывод информации о пилотах
    print("\nPilots:")
    for pilot_url in starship_data['pilots']:
        pilot_data = get_data(pilot_url)
        print("\nPilot Info:")
        print(f"Name: {pilot_data['name']}")
        print(f"Height: {pilot_data['height']}")
        print(f"Weight: {pilot_data['mass']}")
        homeworld_data = get_data(pilot_data['homeworld'])
        print(f"Homeworld: {homeworld_data['name']}")
        print(f"Homeworld URL: {pilot_data['homeworld']}")

    # Запись данных в JSON-файл
    with open("millennium_falcon_info.json", "w") as outfile:
        json.dump(starship_data, outfile)


if __name__ == "__main__":
    main()
