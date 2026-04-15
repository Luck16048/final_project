import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.investment import Investment
from src.loan import Loan
from src.currency import CurrencyConverter



def test_investment_simple_interest():
    inv = Investment(1000, 0.05, 3)
    assert inv.simple_interest() == 1150.0

def test_investment_compound_interest():
    inv = Investment(1000, 0.05, 3)
    assert round(inv.compound_interest(), 2) == 1157.63

def test_investment_negative_amount():
    with pytest.raises(ValueError):
        Investment(-1000, 0.05, 3)

def test_investment_negative_rate():
    with pytest.raises(ValueError):
        Investment(1000, -0.05, 3)

def test_investment_zero_years():
    with pytest.raises(ValueError):
        Investment(1000, 0.05, 0)



def test_loan_monthly_payment():
    loan = Loan(10000, 0.12, 12)
    assert round(loan.monthly_payment(), 2) == 888.49

def test_loan_schedule_length():
    loan = Loan(10000, 0.12, 12)
    assert len(loan.schedule()) == 12

def test_loan_negative_amount():
    with pytest.raises(ValueError):
        Loan(-1000, 0.05, 12)

def test_loan_zero_months():
    with pytest.raises(ValueError):
        Loan(1000, 0.05, 0)



def test_currency_add_rate():
    converter = CurrencyConverter()
    converter.add_rate("USD", 4.0)
    assert converter.rates["USD"] == 4.0

def test_currency_convert():
    converter = CurrencyConverter()
    converter.add_rate("USD", 4.0)
    converter.add_rate("EUR", 4.3)
    result = converter.convert(100, "USD", "EUR")
    assert result == round(100 / 4.0 * 4.3, 2)

def test_currency_negative_rate():
    converter = CurrencyConverter()
    with pytest.raises(ValueError):
        converter.add_rate("USD", -1.0)

def test_currency_unknown_currency():
    converter = CurrencyConverter()
    converter.add_rate("USD", 4.0)
    with pytest.raises(KeyError):
        converter.convert(100, "USD", "GBP")

def test_currency_history():
    converter = CurrencyConverter()
    converter.add_rate("USD", 4.0)
    converter.add_rate("EUR", 4.3)
    converter.convert(100, "USD", "EUR")
    assert len(converter.history) == 1