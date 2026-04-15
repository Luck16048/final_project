from src.investment import Investment
from src.loan import Loan
from src.currency import CurrencyConverter


def main():
    converter = CurrencyConverter()

    while True:
        print("\n=== Financial Calculator ===")
        print("1. Investment calculator")
        print("2. Loan calculator")
        print("3. Currency converter")
        print("4. Exit")

        choice = input("\nChoice: ")

        if choice == "1":
            try:
                amount = float(input("Amount: "))
                rate = float(input("Annual rate (e.g. 0.05 for 5%): "))
                years = int(input("Years: "))
                investment = Investment(amount, rate, years)
                print("Simple interest:", round(investment.simple_interest(), 2))
                print("Compound interest:", round(investment.compound_interest(), 2))
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            try:
                amount = float(input("Loan amount: "))
                rate = float(input("Annual rate (e.g. 0.05 for 5%): "))
                months = int(input("Months: "))
                loan = Loan(amount, rate, months)
                print("Monthly payment:", round(loan.monthly_payment(), 2))
            except ValueError as e:
                print("Error:", e)

        elif choice == "3":
            try:
                print("1. Add rate  2. Convert  3. Show rates")
                action = input("Choice: ")
                if action == "1":
                    currency = input("Currency (e.g. USD): ")
                    rate = float(input("Rate: "))
                    converter.add_rate(currency, rate)
                    print("Rate added!")
                elif action == "2":
                    amount = float(input("Amount: "))
                    from_c = input("From: ")
                    to_c = input("To: ")
                    print("Result:", converter.convert(amount, from_c, to_c), to_c)
                elif action == "3":
                    converter.show_rates()
            except (ValueError, KeyError) as e:
                print("Error:", e)

        elif choice == "4":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()