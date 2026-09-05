# This DCF model was developed with the help of claude AI, and it was mainly used to help with understanding 
# financial terminology, equations and concepts as well as help with reviewing and pointing out potential bugs in code.
# All the code and script was written, and tested by me.
from dotenv import load_dotenv
import os
from flask import Flask, request, render_template
from finance.data_fetch import fetch_company_data
from finance.dcf import generate_range, run_dcf_analysis, sensitivity_analysis
from finance.comps import comp_multiple_calculation,rank_comps, filter_comps
load_dotenv()
api_key = os.getenv("FMP_API_KEY")

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "centre" in request.form:
            centre = float(request.form["centre"])
            step = float(request.form["step"])
            number_of_steps = int(request.form["number_of_steps"]) if "number_of_steps" in request.form else 2
            generated_range = generate_range(centre, step, number_of_steps)
            return render_template("home.html", generated_range=generated_range)
        else:
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
            except (ValueError, KeyError) as e:
                return render_template("error.html", error_message=str(e) + " Please ensure all inputs are valid numbers and lists are comma-separated.")    
    return render_template('home.html')


@app.route('/comps', methods=["GET", "POST"])
def comps():
    if request.method == "POST":
        if "ticker" in request.form:
            ticker = request.form["ticker"]
            fetched_data = fetch_company_data(ticker, api_key)
            return render_template("comps.html", fetched_data=fetched_data)
        else:
            try:
                sort_by = request.form["sort_by"]
                filter_by = request.form["filter_by"]
                cut_off = float(request.form["cut_off"])
                companies = []
                company_count = int(request.form["company_count"])
                for i in range(1, company_count + 1):
                    companies.append({
                    "company_name": request.form[f"company_name_{i}"],
                    "share_price": float(request.form[f"share_price_{i}"]),
                    "eps": float(request.form[f"eps_{i}"]),
                    "shares_outstanding": float(request.form[f"shares_outstanding_{i}"]),
                    "total_debt": float(request.form[f"total_debt_{i}"]),
                    "cash_and_cash_equivalents": float(request.form[f"cash_and_cash_equivalents_{i}"]),
                    "ebit": float(request.form[f"ebit_{i}"]),
                    "d_and_a": float(request.form[f"d_and_a_{i}"])
                    })
                comp_result = comp_multiple_calculation(companies)
                for original, result in zip(companies, comp_result):
                    result["company_name"] = original["company_name"]
                sorted_comp_result = rank_comps(comp_result, sort_by)
                filtered_comp_result = filter_comps(comp_result, filter_by, cut_off)
                return render_template("comps_result.html", comp_result=comp_result, sorted_comp_result=sorted_comp_result, filtered_comp_result=filtered_comp_result)
            except (ValueError, KeyError) as e:
                return render_template("error.html", error_message=str(e) + " Please ensure all inputs are valid numbers.")
    return render_template('comps.html')


if __name__ == '__main__':
    app.run(debug=True)
    