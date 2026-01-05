#converter
import argparse
import requests
import sys


def fetch_rate(currency):

    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        if response.status_code == 200:
            print('connection done !')
        
        print(f'ready to exchange rates based on the {currency}')

        rates = response.json()
        
        rate = rates['rates'][currency]

        return rate
    
    except requests.ConnectionError:
        return 'failed to setup a connection at the moment'
    

def convert_currency(amount, rate):
    return amount*rate

def main():
    parser = argparse.ArgumentParser(description='process a currency conversion')

    parser.add_argument("--amount",type=float,required=True,help='Monetery amount (float)')

    parser.add_argument("--currency",type=str,required=True,help='Currency Code i.e (USD,EUR,AED etc)')

    args = parser.parse_args()

    amount = args.amount
    currency = args.currency

    print(f"Amount: {amount}")
    print(f"Currency: {currency}")

    rate = fetch_rate(currency) 

    if rate:
        amount = convert_currency(amount,rate)
        print( f'amount {amount}')
    
    else:
        print("Error: Could not fetch rate.")
        
if __name__ == "__main__":
    main()
