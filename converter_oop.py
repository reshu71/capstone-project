import requests

class CurrencyConverter:
    def __init__(self, base_url):
        self._base_url = base_url
        # Create the session once when the object is born
        self._session = requests.Session()

    def fetch_rate(self, currency_code):
        try:
            response = self._session.get(self._base_url)
            
            response.raise_for_status()

            data = response.json()
            
            if currency_code not in data.get('rates', {}):
                raise ValueError(f"Currency {currency_code} not found in API.")

            return data['rates'][currency_code]
    
        except requests.RequestException as e:
            print(f"Network Error: {e}")
            raise 

    def convert(self, amount, rate):
        return amount * rate

if __name__ == "__main__":
    converter = CurrencyConverter('https://api.exchangerate-api.com/v4/latest/USD')
    
    try:
        # Fetch rate once
        eur_rate = converter.fetch_rate('EUR')
        print(f"Current EUR Rate: {eur_rate}")
        
        # Do math
        total = converter.convert(10, eur_rate)
        print(f"10 USD = {total} EUR")
        
    except Exception as e:
        print(f"Program failed: {e}")