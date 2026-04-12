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