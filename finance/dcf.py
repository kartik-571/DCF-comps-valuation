# Building the cost of equity code lines
def cost_of_equity(risk_free_rate:float, beta:float, equity_risk_premium:float):
    cost_of_equity = risk_free_rate + beta * equity_risk_premium
    return cost_of_equity


#Building cost of debt code lines
def after_tax_cost_of_debt(pre_tax_cost_of_debt:float, tax_rate:float):
    after_tax_cost_of_debt = pre_tax_cost_of_debt * (1 - tax_rate)
    return after_tax_cost_of_debt
