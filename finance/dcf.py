# This DCF model was developed with the help of claude AI, and it was mainly used to help with understanding 
# financial terminology, equations and concepts as well as help with reviewing and pointing out potential bugs in code.
# All the code and script was written, and tested by me.

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

# multi-year FCF calculation code lines
def project_fcf(ebit_margin: list, revenue: list, tax_rate: float, da_pct_revenue: list, capex_pct_revenue: list, nwc_change_pct_revenue: list):
    fcf = []
    for year_revenue, year_ebit_margin, year_da_pct_revenue, year_capex_pct_revenue, year_nwc_change_pct_revenue in zip(revenue, ebit_margin, da_pct_revenue, capex_pct_revenue, nwc_change_pct_revenue):
        fcf_multi_years = calculate_fcf_single_year(year_ebit_margin, year_revenue, tax_rate, year_da_pct_revenue, year_capex_pct_revenue, year_nwc_change_pct_revenue)
        fcf.append(fcf_multi_years)
    return fcf

# terminal value calculation code lines
def terminal_value(fcf_final_year: float, terminal_growth_rate: float, wacc: float):
    if wacc <= terminal_growth_rate:
        raise ValueError("WACC must be greater than the terminal growth rate to calculate terminal value")
    terminal_value = fcf_final_year * (1 + terminal_growth_rate) / (wacc - terminal_growth_rate)
    return terminal_value

# DCF calculation code lines
def calculate_dcf(fcf:list, wacc:float):
    dcf = []
    for t, cash_flow in enumerate(fcf, start=1):
        pv = cash_flow / (1 + wacc)**t
        dcf.append(pv)
    return dcf


# run_dcf_analysis function to combine all calculations and return the final results
def run_dcf_analysis(tax_rate:float, wacc_value:float, base_revenue:float,
                        growth_rate:list, ebit_margin: list, da_pct_revenue:list, capex_pct_revenue: list,
                          nwc_change_pct_revenue: list, terminal_growth_rate: float, net_debt:float, shares_outstanding:float):
    # Project revenue
    projected_revenue = project_revenue(base_revenue, growth_rate)
    # Project FCF 
    projected_fcf = project_fcf(ebit_margin, projected_revenue, tax_rate, da_pct_revenue, capex_pct_revenue, nwc_change_pct_revenue)
    # Calculate dcf
    dcf_values = calculate_dcf(projected_fcf, wacc_value)
    # Calculate terminal value  
    terminal_value_result = terminal_value(projected_fcf[-1], terminal_growth_rate, wacc_value)
    # Discount terminal value to present value
    discounted_terminal_value = calculate_dcf([terminal_value_result], wacc_value)[0]
    # Calculate total enterprise value
    total_enterprise_value = sum(dcf_values) + discounted_terminal_value
    # Calculate equity value
    equity_value = total_enterprise_value - net_debt
    # Calculate intrinsic value per share
    intrinsic_value_per_share = equity_value / shares_outstanding
    return {
        "total_enterprise_value": total_enterprise_value,
        "equity_value": equity_value,
        "intrinsic_value_per_share": intrinsic_value_per_share}

# creation of sensitivity analysis function to analyze the impact of changes 
# in the key assumptions on the DCF valuation (WACC and terminal growth rate)
def sensitivity_analysis(wacc_values: list, terminal_growth_rate_values: list, tax_rate: float, base_revenue: float,
                          growth_rate: list, ebit_margin: list, da_pct_revenue: list, capex_pct_revenue: list,
                          nwc_change_pct_revenue: list, net_debt: float, shares_outstanding: float):
    results = {}
    for wacc_val in wacc_values:
        results[wacc_val] = {}
        for terminal_growth_rate_val in terminal_growth_rate_values:
            try:
                dcf_result = run_dcf_analysis(tax_rate, wacc_val, base_revenue, growth_rate,
                                                  ebit_margin, da_pct_revenue, capex_pct_revenue,
                                                  nwc_change_pct_revenue, terminal_growth_rate_val,
                                                  net_debt, shares_outstanding)
                dcf_result = {"intrinsic_value_per_share" : dcf_result["intrinsic_value_per_share"]}
            except ValueError:
                dcf_result = "Invalid"
            
            results[wacc_val][terminal_growth_rate_val] = dcf_result
    return results

# Creating function to automatically produce range for different wacc and terminal growth rate values for sensitivity table
def generate_range(centre, step, number_of_steps=2):
        values=[]
        for i in range(-number_of_steps, number_of_steps +1):
            values.append(centre + (i * step))
        return values


