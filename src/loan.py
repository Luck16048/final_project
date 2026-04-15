class Loan:
    def __init__(self, amount, rate, months):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if rate <= 0:
            raise ValueError("Rate must be positive")
        if months <= 0:
            raise ValueError("Months must be positive")

        self.amount = amount
        self.rate = rate / 12
        self.months = months

    def monthly_payment(self):
        r = self.rate
        n = self.months
        return self.amount * r * (1 + r) ** n / ((1 + r) ** n - 1)

    def schedule(self):
        payment = self.monthly_payment()
        balance = self.amount
        result = []

        for month in range(1, self.months + 1):
            interest = balance * self.rate
            principal = payment - interest
            balance = balance - principal
            result.append({
                "month": month,
                "payment": round(payment, 2),
                "interest": round(interest, 2),
                "principal": round(principal, 2),
                "balance": round(max(balance, 0), 2),
            })

        return result

    def __str__(self):
        return f"Loan: {self.amount} for {self.months} months at {self.rate * 12 * 100}%"
    
    def save_history(self, filename="loan_history.json"):
        import json
        data = {
            "amount": self.amount,
            "months": self.months,
            "monthly_payment": round(self.monthly_payment(), 2),
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