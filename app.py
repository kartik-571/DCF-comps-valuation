# This DCF model was developed with the help of claude AI, and it was mainly used to help with understanding 
# financial terminology, equations and concepts as well as help with reviewing and pointing out potential bugs in code.
# All the code and script was written, and tested by me.

from flask import Flask, request

from finance.dcf import run_dcf_analysis, sensitivity_analysis
from finance.comps import comp_multiple_calculation,rank_comps, filter_comps

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        tax_rate = float(request.form["tax_rate"])
        wacc_value = float(request.form["wacc"])
        base_revenue = float(request.form["base_revenue"])
        growth_rate = [float (x) for x in request.form["growth_rate"].split(",")]
        ebit_margin = [float (x) for x in request.form["ebit_margin"].split(",")]
        da_pct_revenue = [float (x) for x in request.form["da_pct_revenue"].split(",")]
        capex_pct_revenue = [float (x) for x in request.form["capex_pct_revenue"].split(",")]
        nwc_change_pct_revenue = [float (x) for x in request.form["nwc_change_pct_revenue"].split(",")]
        terminal_growth_rate = float(request.form["terminal_growth_rate"])
        net_debt = float(request.form["net_debt"])
        shares_outstanding = float(request.form["shares_outstanding"])
        wacc_values = [float (x) for x in request.form["wacc_values"].split(",")]
        terminal_growth_rate_values = [float (x) for x in request.form["terminal_growth_rate_values"].split(",")]
        sensitivity_table_result = sensitivity_analysis(wacc_values, terminal_growth_rate_values, tax_rate, base_revenue, growth_rate, ebit_margin, da_pct_revenue, capex_pct_revenue, nwc_change_pct_revenue, net_debt, shares_outstanding)
        dcf_result = run_dcf_analysis(tax_rate, wacc_value, base_revenue, growth_rate, ebit_margin, da_pct_revenue, capex_pct_revenue, nwc_change_pct_revenue, terminal_growth_rate, net_debt, shares_outstanding)

        return f"DCF Result: {dcf_result} Sensitivity Analysis Result: {sensitivity_table_result}"
    return '''
        <form method="POST">
            Tax Rate: <input type="text" name="tax_rate">
            WACC: <input type="text" name="wacc">
            Base Revenue: <input type="text" name="base_revenue">
            Growth Rate (comma-separated): <input type="text" name="growth_rate">
            EBIT Margin (comma-separated): <input type="text" name="ebit_margin">
            DA % Revenue (comma-separated): <input type="text" name="da_pct_revenue">
            Capex % Revenue (comma-separated): <input type="text" name="capex_pct_revenue">
            NWC Change % Revenue (comma-separated): <input type="text" name="nwc_change_pct_revenue">
            Terminal Growth Rate: <input type="text" name="terminal_growth_rate">
            Net Debt: <input type="text" name="net_debt">
            Shares Outstanding: <input type="text" name="shares_outstanding">
            WACC Values (comma-separated): <input type="text" name="wacc_values">
            Terminal Growth Rate Values (comma-separated): <input type="text" name="terminal_growth_rate_values">
            <input type="submit" value="Submit">
            

            </form>
            '''


@app.route('/comps', methods=["GET", "POST"])
def comps():
    if request.method == "POST":
        share_price = [float(x) for x in request.form["share_price"].split(",")]
        eps = [float(x) for x in request.form["eps"].split(",")]
        shares_outstanding = [float(x) for x in request.form["shares_outstanding"].split(",")]
        total_debt = [float(x) for x in request.form["total_debt"].split(",")]
        cash_and_cash_equivalents = [float(x) for x in request.form["cash_and_cash_equivalents"].split(",")]
        ebit = [float(x) for x in request.form["ebit"].split(",")]
        d_and_a = [float(x) for x in request.form["d_and_a"].split(",")]
        companies = []
        for sp, e, so, to, cace, eb, da in zip(share_price, eps, shares_outstanding, total_debt, cash_and_cash_equivalents, ebit, d_and_a):
            companies.append({
                "share_price": sp,
                "eps": e,
                "shares_outstanding": so,
                "total_debt": to,
                "cash_and_cash_equivalents": cace,
                "ebit": eb,
                "d_and_a": da
            })
        comp_result = comp_multiple_calculation(companies)
        return f"Comps inputs processed successfully: {comp_result}"

    return '''
<form method="POST">
            Share Price (comma-separated): <input type="text" name="share_price">
            EPS (comma-separated): <input type="text" name="eps">
            Shares Outstanding(comma-separated): <input type="text" name="shares_outstanding">
            Total Debt(comma-separated): <input type="text" name="total_debt">
            Cash and Cash Equivalents(comma-separated): <input type="text" name="cash_and_cash_equivalents">
            EBIT (comma-separated): <input type="text" name="ebit">
            D and A (comma-separated): <input type="text" name="d_and_a">
            <input type="submit" value="Submit">
            </form>
            '''

if __name__ == '__main__':
    app.run(debug=True)
