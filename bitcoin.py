import requests
from pprint import pprint
def main():
    data = api_call()
    pprint(data)
    bitcoin = user_input()
    bitcoin_value_in_dollars = get_exchange_rate(data, bitcoin)
    display_exchange_rate(bitcoin, bitcoin_value_in_dollars)


def api_call():
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    try:
        response = requests.get(coindesk_url)
        data = response.json()
        return data
    except Exception as e:
        print('Error in the connecting please try again' + e)

def user_input():
    bitcoin = float(input('Enter the number of bitcoin: '))
    return bitcoin

def get_exchange_rate(data, bitcoin):
    dollars_exchange_rate = data['bpi']['USD']['rate_float']    
    bitcoin_value_in_dollars = bitcoin * dollars_exchange_rate
    return bitcoin_value_in_dollars

def display_exchange_rate(bitcoin, bitcoin_value_in_dollars):
    print(f'{bitcoin} Bitcoin is equivalent to ${bitcoin_value_in_dollars}')

if __name__ == '__main__':
    main()