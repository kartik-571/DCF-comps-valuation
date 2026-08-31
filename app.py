from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        revenue = request.form["revenue"]
        tax_rate = request.form["tax_rate"]
        wacc_value = request.form["wacc"]
        base_revenue = request.form["base_revenue"]
        growth_rate = request.form["growth_rate"]
        ebit_margin = request.form["ebit_margin"]
        da_pct_revenue = request.form["da_pct_revenue"]
        capex_pct_revenue = request.form["capex_pct_revenue"]
        nwc_change_pct_revenue = request.form["nwc_change_pct_revenue"]
        terminal_growth_rate = request.form["terminal_growth_rate"]
        net_debt = request.form["net_debt"]
        shares_outstanding = request.form["shares_outstanding"]
        return f"You entered: Revenue:{revenue} Tax Rate:{tax_rate} WACC:{wacc_value} Base Revenue:{base_revenue} Growth Rate:{growth_rate} EBIT Margin:{ebit_margin} DA % Revenue:{da_pct_revenue} Capex % Revenue:{capex_pct_revenue} NWC Change % Revenue:{nwc_change_pct_revenue} Terminal Value Growth Rate:{terminal_growth_rate} Net Debt:{net_debt} Shares Outstanding:{shares_outstanding}"
    return '''
        <form method="POST">
            Revenue: <input type="text" name="revenue">
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
            <input type="submit" value="Submit">
            

            </form>
            '''
if __name__ == '__main__':
    app.run(debug=True)
