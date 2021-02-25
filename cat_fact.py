import requests
try:
    response = requests.get('https://catfact.ninja/fact')
    print(response.status_code)
    response.raise_for_status() # raise an expection
    print(response.text)
    print(response.json())

    data = response.json()
    fact = data['fact']
    print(f'A random cat fact is {fact}')
except Exception as e:
    print(e)
    print('Error making request')