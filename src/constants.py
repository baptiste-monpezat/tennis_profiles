"""constants we used in the project"""

TABLE_URL_DICT = {
    "serve":
    "https://tennisabstract.com/reports/mcp_leaders_serve_men_career.html",
    "return":
    "https://tennisabstract.com/reports/mcp_leaders_return_men_career.html",
    "rally":
    "https://tennisabstract.com/reports/mcp_leaders_rally_men_career.html",
    "tactics":
    "https://tennisabstract.com/reports/mcp_leaders_tactics_men_career.html",
}
# to scrap 
HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


COLUMNS_NAME = [
    "Unret%",
    "<=3 W%",
    "SvImpact",
    "1st: Unret%",
    "<=3 W%.1",
    "SvImpact.1",
    "2nd: Unret%",
    "<=3 W%.2",
    "RiP%",
    "RetWnr%",
    "1st: RiP%",
    "RetWnr%.1",
    "2nd: RiP%",
    "RetWnr%.2",
    "Wnr FH%",
    "FH Wnr%",
    "FH DTL Wnr%",
    "FHP/100",
    "BH Wnr%",
    "BH DTL Wnr%",
    "BHP/100",
    "Net W%",
    "Net Freq",
    "Drop Freq",
    "Drop Wnr%",
    "SnV Freq",
    "SnV W%"

]

MAPPING_DICT = {
    "serve":{
            "Unret%",
            "<=3 W%",
            "SvImpact",
            "1st: Unret%",
            "<=3 W%.1",
            "SvImpact.1",
            "2nd: Unret%",
            "<=3 W%.2"
    },
    "return":{
         "RiP%",
         "RetWnr%",
         "1st: RiP%",
         "RetWnr%.1",
         "2nd: RiP%",
         "RetWnr%.2"
    },
    "forehand":{
        "Wnr FH%",
        "FH Wnr%",
        "FH DTL Wnr%",
        "FHP/100"
    },
    "backhand":{
        "BH Wnr%",
        "BH DTL Wnr%",
        "BHP/100"
    },
    "volley":{
        "Net W%",
        "Net Freq"

    },
    "dropshots":{
        "Drop Freq",
        "Drop Wnr%"        
    },
    "agressivity":{
        "SnV Freq",
        "SnV W%"
    }
}