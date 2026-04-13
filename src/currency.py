class CurrencyConverter:
    def __init__(self):
        self.rates = {}
        self.history = []

    def add_rate(self, currency, rate):
        if rate <= 0:
            raise ValueError("Rate must be positive")
        self.rates[currency] = rate

    def convert(self, amount, from_currency, to_currency):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if from_currency not in self.rates:
            raise KeyError(f"Currency {from_currency} not found")
        if to_currency not in self.rates:
            raise KeyError(f"Currency {to_currency} not found")

        amount_in_base = amount / self.rates[from_currency]
        result = amount_in_base * self.rates[to_currency]

        self.history.append({
            "from": from_currency,
            "to": to_currency,
            "amount": amount,
            "result": round(result, 2),
        })

        return round(result, 2)

    def show_rates(self):
        for currency, rate in self.rates.items():
            print(f"{currency}: {rate}")

    def __str__(self):
        return f"CurrencyConverter with {len(self.rates)} currencies"