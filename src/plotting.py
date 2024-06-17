import pandas as pd
import matplotlib.pyplot as plt
from src.utils import entropy
import seaborn as sns 

def set_size(width, fraction=1):
    """Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float
            Document textwidth or columnwidth in pts
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    # Width of figure (in pts)
    fig_width_pt = width * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    # https://disq.us/p/2940ij3
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio

    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim

def plot_barplot(column_names, *datasets):
    # Calculate Spearman correlation
    
    corrs = [dataset.corr(method="spearman")['Improvement in NDCG@10']
             for dataset in datasets] 
    # Combine correlations into a single DataFrame
    df = pd.concat(corrs, axis=1)
    df.columns = column_names
    # Dropping unnecessary indices
    df = df.drop(index=['Improvement in NDCG@10'])

    # Create the figure and axes
    fig, ax = plt.subplots()
    l = ["Number of Test Documents", 
        "Overlap of Generated Query to Source Document Vocabulary", 
        "Overlap of Generated to Source Query Vocabulary",
        "Overlap of Test Document to Generated Query Vocabulary",
        "Overlap of Test to Generated Query Vocabulary",
        "Entropy between Test and Generated Query Type Distributions",
        "Generated Query Type Distribution Entropy"]
    
    l.reverse()
    # Plot the bar chart
    df.loc[l].plot.barh(ax=ax, width=0.7, edgecolor='black', alpha=0.75, legend=False)

    # Set axis labels and title
    ax.set_xlabel('Spearman Correlation', fontsize=14, labelpad=20, weight='bold')
    ax.set_ylabel('Factors', fontsize=14, labelpad=20, weight='bold')
    ax.set_title('Correlation of Factors with Improvement in NDCG@10', fontsize=14, pad=20, weight='bold')

    # Customizing and positioning the legend
    ax.legend(fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    # Grid and layout adjustments
    ax.grid(axis='x', linestyle='--', linewidth=0.7)

    # Save the figure as a high-resolution PNG
    fig.savefig("corr.pdf", bbox_inches="tight")
    fig.savefig("corr.png", bbox_inches="tight")

def plot_query_types(data):
    fig = plt.figure()
    df = pd.DataFrame.from_dict(data).transpose()
    df['Entropy'] = df.apply(lambda x: entropy(x), axis=1)
    sns.heatmap(df, annot=True, fmt=".2f")
    fig.savefig("query_types.png", bbox_inches="tight")
    fig.savefig("query_types.pdf", bbox_inches="tight") 
   
def plot_overlap_test_document(data_1, data_2):
    # Create the figure and axes
    fig, ax = plt.subplots()

    # Plot the barplot
    sns.barplot(data = data_1, x="Dataset", y="Overlap of Test Document to Generated Query Vocabulary", color = "r", label = "GPL")
    sns.barplot(data = data_2, x="Dataset", y="Overlap of Test Document to Generated Query Vocabulary", color = "b", label = "InPars")

    # Set axis labels and title
    ax.set_xlabel('', fontsize=14, labelpad=20, weight='bold')
    ax.set_ylabel('', fontsize=14, labelpad=20, weight='bold')
    ax.tick_params(axis='x', labelrotation=90)
    ax.set_title('Overlap of Test Document to Generated Query', fontsize=14, pad=20, weight='bold')
    # Save the figure as a high-resolution PNG
    # Customizing and positioning the legend
    ax.legend(fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    # Grid and layout adjustments
    ax.grid(axis='x', linestyle='--', linewidth=0.7)
    fig.savefig("overlap_test_domain.pdf", bbox_inches="tight")
    fig.savefig("overlap_test_domain.png", bbox_inches="tight")

    
def plot_overlap_test_query(data_1, data_2):
    # Create the figure and axes
    fig, ax = plt.subplots()

    # Plot the barplot
    sns.barplot(data = data_1, x="Dataset", y="Overlap of Test to Generated Query Vocabulary", color = "r", label = "GPL")
    sns.barplot(data = data_2, x="Dataset", y="Overlap of Test to Generated Query Vocabulary", color = "b", label = "InPars")

    # Set axis labels and title
    ax.set_xlabel('', fontsize=14, labelpad=20, weight='bold')
    ax.set_ylabel('', fontsize=14, labelpad=20, weight='bold')
    ax.tick_params(axis='x', labelrotation=90)
    ax.set_title('Overlap of Test to Generated Query', fontsize=14, pad=20, weight='bold')
    # Save the figure as a high-resolution PNG
    # Customizing and positioning the legend
    ax.legend(fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
 
    # Grid and layout adjustments
    ax.grid(axis='x', linestyle='--', linewidth=0.7)
    fig.savefig("overlap_test_query.pdf", bbox_inches="tight")
    fig.savefig("overlap_test_query.png", bbox_inches="tight")
    
    
def plot_generated_query_type_entropy(data_1, data_2):
    # Create the figure and axes
    fig, ax = plt.subplots()
    # Plot the barplot
    sns.barplot(data = data_1, x="Dataset", y="Generated Query Type Distribution Entropy", color = "r", label = "GPL")
    sns.barplot(data = data_2, x="Dataset", y="Generated Query Type Distribution Entropy", color = "b", label = "InPars")
    # Set axis labels and title
    ax.set_xlabel('', fontsize=14, labelpad=20, weight='bold')
    ax.set_ylabel('', fontsize=14, labelpad=20, weight='bold')
    ax.tick_params(axis='x', labelrotation=90)
    ax.set_title('Generated Query Type Distribution Entropy', fontsize=14, pad=20, weight='bold')
    # Save the figure as a high-resolution PNG
    # Customizing and positioning the legend
    ax.legend(fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    # Grid and layout adjustments
    ax.grid(axis='x', linestyle='--', linewidth=0.7)
    fig.savefig("gen_query_types.pdf", bbox_inches="tight")
    fig.savefig("gen_query_types.png", bbox_inches="tight")
     
    