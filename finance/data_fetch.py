import requests
#producing the company data fetching function
def fetch_company_data(ticker, api_key):
#pulling live stock critical data (share price at current time)
    quote_url = f"https://financialmodelingprep.com/stable/quote?symbol={ticker}&apikey={api_key}"
    quote_response = requests.get(quote_url).json()
    quote = quote_response[0]
#pulling income statement data
    income_url = f"https://financialmodelingprep.com/stable/income-statement?symbol={ticker}&apikey={api_key}"
    income_response = requests.get(income_url).json()
    income = income_response[0]
#pulling balance sheet data
    balance_url = f"https://financialmodelingprep.com/stable/balance-sheet-statement?symbol={ticker}&apikey={api_key}"
    balance_response = requests.get(balance_url).json()
    balance = balance_response[0]

    return {
        "share_price": quote["price"],
        "eps": income["eps"],
        "shares_outstanding": income["weightedAverageShsOut"],
        "ebit": income["ebit"],
        "d_and_a": income["depreciationAndAmortization"],
        "total_debt": balance["totalDebt"],
        "cash_and_cash_equivalents": balance["cashAndCashEquivalents"]
    }
