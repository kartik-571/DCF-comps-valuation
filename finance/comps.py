# This DCF model was developed with the help of claude AI, and it was mainly used to help with understanding 
# financial terminology, equations and concepts as well as help with reviewing and pointing out potential bugs in code.
# All the code and script was written, and tested by me.

#code for comp evaluation
def comp_single_calculation(company:dict):
    if company["eps"] == 0:
            raise ValueError("eps of a company cannot be 0 ")
    pe_ratio = company["share_price"]/ company["eps"]
    market_value_of_equity = company["share_price"]* company["shares_outstanding"]
    enterprise_value = market_value_of_equity + company["total_debt"] - company["cash_and_cash_equivalents"]
    ebitda = company["ebit"] + company["d_and_a"]
    if ebitda == 0:
            raise ValueError("ebitda of company cannot be 0")
    ev_ebitda_ratio = enterprise_value / ebitda
    return {
        "pe_ratio": pe_ratio,
        "ev_ebitda_ratio": ev_ebitda_ratio,
    }

def comp_multiple_calculation(companies:list[dict]):
    comps = []
    for company in companies:
        results = comp_single_calculation(company)
        comps.append(results)
    return comps


# ranking based on p_e
def rank_comps(comps_list:list,sort_by:str  ):
      companies_sorted = sorted(comps_list, key= lambda company: company[sort_by])
      for x, ordered_companies in enumerate(companies_sorted, start=1):
            ordered_companies["rank"] = x
      return companies_sorted
            
          
# filtering companies based on conditions 
def filter_comps(companies_sorted:list,filter_by:str, cut_off:float ):
            filtered_companies = []
            for company in companies_sorted:
                  if company[filter_by] < cut_off:
                        filtered_companies.append(company)
            return filtered_companies
    