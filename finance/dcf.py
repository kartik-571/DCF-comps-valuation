# Building the cost of equity code lines
def cost_of_equity(risk_free_rate:float, beta:float, equity_risk_premium:float):
    cost_of_equity = risk_free_rate + beta * equity_risk_premium
    return cost_of_equity


#Building cost of debt code lines
def after_tax_cost_of_debt(pre_tax_cost_of_debt:float, tax_rate:float):
    after_tax_cost_of_debt = pre_tax_cost_of_debt * (1 - tax_rate)
    return after_tax_cost_of_debt

#Building wacc code lines
def wacc(cost_of_equity:float, cost_of_debt:float, market_value_of_equity:float, market_value_of_debt:float):
    total_value = market_value_of_equity + market_value_of_debt
    if total_value == 0:
        raise ValueError("Total value of equity and debt cannot equal 0")
    wacc = (cost_of_equity * (market_value_of_equity / total_value) + cost_of_debt * (market_value_of_debt / total_value))
    return wacc
