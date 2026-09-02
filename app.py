# This DCF model was developed with the help of claude AI, and it was mainly used to help with understanding 
# financial terminology, equations and concepts as well as help with reviewing and pointing out potential bugs in code.
# All the code and script was written, and tested by me.

from flask import Flask, request, render_template

from finance.dcf import run_dcf_analysis, sensitivity_analysis
from finance.comps import comp_multiple_calculation,rank_comps, filter_comps

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
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
            if not (len(growth_rate) == len(ebit_margin) == len(da_pct_revenue) == len(capex_pct_revenue) == len(nwc_change_pct_revenue)):
                 raise ValueError("All input lists must have the same length.")
            sensitivity_table_result = sensitivity_analysis(wacc_values, terminal_growth_rate_values, tax_rate, base_revenue, growth_rate, ebit_margin, da_pct_revenue, capex_pct_revenue, nwc_change_pct_revenue, net_debt, shares_outstanding)
            dcf_result = run_dcf_analysis(tax_rate, wacc_value, base_revenue, growth_rate, ebit_margin, da_pct_revenue, capex_pct_revenue, nwc_change_pct_revenue, terminal_growth_rate, net_debt, shares_outstanding)
            return render_template("dcf_result.html", dcf_result=dcf_result, sensitivity_table_result=sensitivity_table_result)
        except ValueError as e:
            return render_template("error.html", error_message=str(e) + " Please ensure all inputs are valid numbers and lists are comma-separated.")

        
    return render_template('home.html')


@app.route('/comps', methods=["GET", "POST"])
def comps():
    if request.method == "POST":
        try:
            share_price = [float(x) for x in request.form["share_price"].split(",")]
            eps = [float(x) for x in request.form["eps"].split(",")]
            shares_outstanding = [float(x) for x in request.form["shares_outstanding"].split(",")]
            total_debt = [float(x) for x in request.form["total_debt"].split(",")]
            cash_and_cash_equivalents = [float(x) for x in request.form["cash_and_cash_equivalents"].split(",")]
            ebit = [float(x) for x in request.form["ebit"].split(",")]
            d_and_a = [float(x) for x in request.form["d_and_a"].split(",")]
            sort_by = request.form["sort_by"]
            filter_by = request.form["filter_by"]
            cut_off = float(request.form["cut_off"])
            if not (len(share_price) == len(eps) == len(shares_outstanding) == len(total_debt) == len(cash_and_cash_equivalents) == len(ebit)== len(d_and_a)):
                 raise ValueError("All input lists must have the same length.")
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
            sorted_comp_result = rank_comps(comp_result, sort_by)
            filtered_comp_result = filter_comps(comp_result, filter_by, cut_off)
            return render_template("comps_result.html", comp_result=comp_result, sorted_comp_result=sorted_comp_result, filtered_comp_result=filtered_comp_result)
        except ValueError as e:
            return render_template("error.html", error_message=str(e) + " Please ensure all inputs are valid numbers and lists are comma-separated.")
    return render_template('comps.html')


if __name__ == '__main__':
    app.run(debug=True)
