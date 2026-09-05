# DCF and COMPS valuation tool 

#### Video Demo: <URL HERE>

#### Description:

This project aimed to combine two of the core methods used in equity research and investment banking - a Discounted Cash Flow (DCF) model and a Comparable Companies (“comps”) screener- into a single application so the two methods can be used together and evaluated against each other in the same way real analysts would use them. It is a web-based tool built with Python, Flask and Jinja templates.

What does it do?

The DCF calculator on the homepage takes a set of financial assumptions (revenue, growth rates, margins, WACC, terminal growth rate, net debt, shares outstanding) and calculates a company’s intrinsic enterprise value, equity value and value per share. It also includes a sensitivity analysis in the form of a table so a user can see how the valuation calculated changes with different WACC and terminal growth rate combinations. This was done as a user can take their assumptions and see how sensitive their result is to them rather than just trusting a single calculation is accurate.

The comps screener takes several peer companies financial data – share price, EPS, shares outstanding, total debt, cash, EBIT and D&A- and calculated two ratios for each: P/E ratio and EV/EBITDA ratio. It then ranks companies (if the user chooses) by a chosen ratio and filters companies above a chosen cut off. The selection for companies is dynamic, and they can be added/removed with a button rather than being limited in number. Additionally, a company’s data can be pulled automatically from live financial data API by typing in a company’s ticker rather than manually typing information.

Another feature I added later to the DCF calculator was to allow the user to auto-generate a WACC range for the sensitivity table instead of having to hand type a fully comma separated list. By entering a centred value and an incremental step size, the calculator will generate a symmetric range around it and will prefill the WACC values for you. 

Why did I Build this? 

I had already created a DCF by hand using Excel and found the process to be much slower and more likely for errors to occur than I thought it needed to be. The main errors were almost always re-typing formulae across years, checking references and rebuilding the same structure for every new company you wanted to value. After taking CS50 It almost became obvious that most of these errors that occurred could be easily skipped over by simply writing the formulae into code instead of rebuilding each time which is why I wanted to make this project as it represented a much faster and more efficient method to calculate intrinsic value and other valuation ratios.

How the project was structured

•	Finance/dcf.py – This code was the main DCF itself and included all the standalone functions for cost of equity(CAPM), after-tax cost of debt, WACC, revenue projection, free cash flow projection(both single and multi-year), terminal value, discounting cash flows to present value, a run_dcf_analysis function that tied all of the DCF formulae together and a sensitivity analysis function that created a table showing the sensitivity of the calculated value to changes in WACC and Terminal growth values. I also added a generate_range function that helped generated a symmetric range of values around a centre value for the sensitivity table.

•	Finance/data_fetch.py – this code fetched live company data (share price, EPS, shares outstanding, total debt, cash, EBIT, D&A) from the Financial Modelling Prep API given the user enters a valid Ticker for a stock currently on the market.

•	App.py – This was the flask application and defined two routes, / was for the DCF calculator and was the default page opened when the application was loaded. /comps was the page for the comps screener.

•	Templates/ - these formed all the Jinja HTML templates. I decide to use a base.html template that held a shared page layout for each template which reduced the amount of identical code I had to write for each template. I also added a navigation bar to switch between the comp and DCF pages. I also added an error.html template which displayed a standard error message across both submission forms. Finally, I created two HTML pages to display results for the DCF (dcf_result.html) and comps (comps_result.html) with the results showing as tables.

•	Static/style.css – this includes the styles and features chosen for the website 

•	Tests/test_dcf.py and tests/test_comps.py – this contains all the pytest suites that I used to test every function within finance/dcf.py and finance/comps.py

Design decisions

•	The comps enterprise value was calculated from market data and not from the DCF’s output because the whole point of the comps screener was to show what the market is currently actually paying for similar companies, which is effectively an outsider check for the DCF models estimated value. If I had made the comps screener use the DCF calculated value it would be checking against itself which would be useless.

•	Run_dcf_analysis takes WACC directly from the users input rather than computing it directly from a calculation. Originally, I had the model calculate WACC internally using inputted data (risk-free rate, beta, equity risk premium) but I had to change this once I had built the sensitivity analysis feature. This was because there was no way to test different WACC values without duplicating all the WACC inputs as parameters. By passing the WACC as a single value made the function reusable in the sensitivity table.

•	There were occasionally some equations that included division where the denominators value could have resulted in being 0 or the user input being blank in which case the calculation couldn’t work and the app would crash. To get around this I wrapped each route in a try/except (ValueError, KeyError) as e block. This caught input errors, missing form fields and validation checks on formulae (e.g WACC couldn’t be less than terminal value growth rate as this would result in the terminal value formula dividing by a zero/negative number). I also created an error page rather than generic error messages so a user could understand exactly what was wrong.

•	I made sure to use tests for every standalone function to make sure they were working before combining functions into one overall function in the DCF calculation and the Comps calculation. Each function has a corresponding pytest that I checked against my own calculated values to ensure the code was working exactly how the formula would work.

Limitations

•	Companies that were added via the button to the total number of comps don’t survive/appear if you press the browsers back button, or if a full page reload occurs (like looking up a second ticker). The page automatically resets to the original Jinja template which is one empty company row. This is because added rows only currently exist in the browser, they are built by JavaScript and therefore Flask never sees them. HTTP requests are stateless and therefore nothing about a previous page’s state persists on the server unless its deliberately carried forward. 

•	A similar limitation was that the live-data ticker lookup feature only pre-fills found information for the first company in the form, currently I haven’t made it possible to bring real data into specific extra added companies.

•	The auto-generate range feature for the sensitivity table is currently only available to generate the WACC field ranges. Although it would involve the same code just slightly modified for the terminal growth rate values, I had decided not to include it for now.

•	The API key that I used to find and receive live company data only has a limited number of free-tier requests that can be made in a day. If this site were to be used simultaneously by many people, the limit would be reached quite quickly. To address this the easiest way, I could think of was for each user of the site to use their own key. I had thought to add the ability to register for accounts however I thought it would be best to keep it as a freely useable and accessible calculator for now.

AI Usage 

I used Claude AI throughout this project as a learning tool. It was mainly used to help me understand financial terms and formulae alongside some unfamiliar Python and Jinja syntax I had not come across before. It was also used as a final check for code I had already written to point out any bugs if there were any. All the code and all the fixes and modifications were all written and tested by me. I have disclosed the usage of AI per the CS50 guidelines at the top of the files.

