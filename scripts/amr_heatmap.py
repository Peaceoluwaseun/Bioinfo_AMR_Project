import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("all_ecoli_AMR_results.tsv", sep="\t", header=None)

heat = pd.crosstab(df[1], df[0])

sns.heatmap(heat)

plt.title("AMR Gene Distribution Across E. coli Genomes")

plt.savefig("amr_heatmap.png")
