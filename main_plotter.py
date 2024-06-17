import matplotlib 
import matplotlib.pyplot as plt
import pandas as pd
from src.plotting import set_size, plot_barplot, \
plot_overlap_test_document, plot_overlap_test_query,\
plot_generated_query_type_entropy, plot_query_types
import json 


matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'font.weight' : 'bold',
    'font.size' : 12,
    'text.usetex': True,
    'pgf.rcfonts': False,
})

figsize = set_size(455.24411, fraction = 0.8)
plt.rcParams["figure.figsize"] = figsize


d_beir_gpl = pd.read_csv("data/GPL_BEIR.csv")
d_lotte_gpl = pd.read_csv("data/GPL_LoTTE.csv")
d_beir_inpars = pd.read_csv("data/InPars_BEIR.csv")
d_lotte_gpl['type'] = d_lotte_gpl['Dataset'].apply(lambda x: "search" if "Search" in x else "forum")


gpl_generated_beir = "shared_json/BEIR/GPL/generated_query_types_gpl.json"
inpars_generated_beir = "shared_json/BEIR/InPars/generated_query_types.json"
with open(gpl_generated_beir, 'r') as file:
    gpl_generated_beir = json.load(file)
with open(inpars_generated_beir, 'r') as file:
    inpars_generated_beir = json.load(file)
    

if __name__ == "__main__":
    
    # For Bar Plots we need to drop the columns with String values!
    column_names = ["BEIR", "LoTTE Search", "LoTTE Forum"]
    plot_barplot(column_names,
                 d_beir_gpl.drop(columns = ["Dataset"]), d_lotte_gpl[d_lotte_gpl['type'] == "search"].drop(columns = ["Dataset", "type"]), 
                 d_lotte_gpl[d_lotte_gpl['type'] == "forum"].drop(columns = ["Dataset", "type"]))
    column_names = ["GPL", "InPars"]
    plot_barplot(column_names,
                d_beir_gpl.drop(columns = ["Dataset"]), 
                d_beir_inpars.drop(columns = ["Dataset"]))
    
    # Plot Overlaps
    plot_overlap_test_document(d_beir_gpl, d_beir_inpars)
    plot_overlap_test_query(d_beir_gpl, d_beir_inpars)
    plot_generated_query_type_entropy(d_beir_gpl, d_beir_inpars)
    
    
    # Plot Generated Query Types
    plot_query_types(gpl_generated_beir)
    plot_query_types(inpars_generated_beir)
    
    
