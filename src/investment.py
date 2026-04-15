class Investment:
    def __init__(self, amount, rate, years):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if rate < 0:
            raise ValueError("Rate cannot be negative")
        if years <= 0:
            raise ValueError("Years must be positive")

        self.amount = amount
        self.rate = rate
        self.years = years

    def simple_interest(self):
        return self.amount * (1 + self.rate * self.years)

    def compound_interest(self):
        return self.amount * (1 + self.rate) ** self.years

    def __str__(self):
        return f"Investment: {self.amount} for {self.years} years at {self.rate * 100}%"
    
    def save_history(self, filename="investment_history.json"):
        import json
        data = {
            "amount": self.amount,
            "rate": self.rate,
            "years": self.years,
            "simple_interest": round(self.simple_interest(), 2),
            "compound_interest": round(self.compound_interest(), 2),
        }
        history = []
        from pathlib import Path
        if Path(filename).exists():
            with open(filename, "r") as f:
                history = json.load(f)
        history.append(data)
        with open(filename, "w") as f:
            json.dump(history, f, indent=4)
        print("Saved to", filename)