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

# building project revenue code lines
def project_revenue(base_revenue:float, growth_rate:float):
    growth = []
    current = base_revenue
    for rate in growth_rate:
        current = current * (1 + rate)
        growth.append(current) 
    return growth 


# single year FCF calculation code lines
def calculate_fcf_single_year(ebit_margin: float, revenue: float, tax_rate: float,da_pct_revenue:float, capex_pct_revenue: float,nwc_change_pct_revenue: float):
    ebit = revenue * ebit_margin
    nopat = ebit * (1 - tax_rate)
    da = revenue * da_pct_revenue
    capex = revenue * capex_pct_revenue
    change_in_nwc = revenue * nwc_change_pct_revenue
    fcf = nopat + da - capex - change_in_nwc
    return fcf