#code for comp evaluation
def comp_single_calculation(company:dict):
    if company["eps"] == 0:
            raise ValueError("eps of a company cannot be 0 ")
    pe_ratio = company["share_price"]/ company["eps"]
    market_value_of_equity = company["share_price"]* company["shares_outstanding"]
    enterprise_value = market_value_of_equity + company["total_debt"] - company["cash_and_cash_equivalents"]
    ebitda = company["ebit"] + company["d_and_a"]
    if ebitda == 0:
            raise ValueError("ebitda of company cannot be 0")
    ev_ebitda_ratio = enterprise_value / ebitda
    return {
        "pe_ratio": pe_ratio,
        "ev_ebitda_ratio": ev_ebitda_ratio,
    }
    
    






