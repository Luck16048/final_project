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