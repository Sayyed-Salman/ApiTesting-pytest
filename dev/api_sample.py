import requests
import json

# URL
url = 'https://data.police.uk/api'

"""
UK Police API
https://data.police.uk/docs/

1) list of forces
    GET
    /forces

2) neighbourhoods
    GET
    /{nighbourhood_name}/neighbourhoods

"""

# Get list of forces


def get_forces():
    r = requests.get(url + '/forces')
    return r


def get_neighbourhoods(neighbourhood_name):
    r = requests.get(url + f'/{neighbourhood_name}/' + '/neighbourhoods')
    return r


def make_json_file(data, filename):
    with open("data/"+filename, 'w+') as f:
        f.write(data)


if __name__ == '__main__':
    # Get list of forces
    forces = get_forces()
    forces_data = json.dumps(forces.json(), indent=4)
    with open('data/forces.json', 'w+') as f:
        f.write(forces_data)
    print(forces_data)

    # Get list of neighbourhoods
    neighbourhoods = [
        "avon-and-somerset", "bedfordshire", "cambridgeshire", "cheshire"
    ]
    for neighbourhood in neighbourhoods:
        res = get_neighbourhoods(neighbourhood)
        nighood = json.dumps(res.json(), indent=4)
        make_json_file(nighood, f'{neighbourhood}.json')
        print(res.status_code)
        print(nighood)
