from fastapi import FastAPI, HTTPException
from converter_oop import CurrencyConverter

# 1. Initialize the FastAPI Application
app = FastAPI()

# 2. Initialize the Logic (The Singleton)
# We create this ONCE. It lives as long as the server is running.
# This reuses the internal requests.Session, making your API fast.
converter = CurrencyConverter('https://api.exchangerate-api.com/v4/latest/USD')

@app.get("/")
def health_check():
    """
    Root Endpoint.
    Used to verify the server is running.
    """
    return {
        "status": "online",
        "service": "Currency Converter API",
        "version": "1.0.0"
    }

@app.get("/convert")
def convert_route(amount: float, target: str):
    """
    The Conversion Endpoint.
    Example: GET /convert?amount=100&target=EUR
    """
    try:
        # Step A: Get the rate using your OOP class
        rate = converter.fetch_rate(target)
        
        # Step B: Do the math
        result = converter.convert(amount, rate)
        
        # Step C: Return the JSON response
        return {
            "base_currency": "USD",
            "target_currency": target,
            "amount": amount,
            "converted_amount": round(result, 2),
            "rate_used": rate
        }
        
    except Exception as e:
        # If anything goes wrong (e.g., Invalid Currency), send a 400 Error.
        # "str(e)" converts the Python error message into text for the user.
        raise HTTPException(status_code=400, detail=str(e))