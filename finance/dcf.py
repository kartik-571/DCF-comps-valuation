# Building the cost of equity code lines
def cost_of_equity(risk_free_rate, beta, equity_risk_premium):
    cost_of_equity = risk_free_rate + beta * equity_risk_premium
    return cost_of_equity