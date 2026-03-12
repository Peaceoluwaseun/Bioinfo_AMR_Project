import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("all_ecoli_AMR_results.tsv", sep="\t", header=None)

gene_counts = df[1].value_counts()

plt.figure(figsize=(14,7))
gene_counts.plot(kind="bar")
plt.xticks(rotation=45, ha='right')
plt.xlabel("AMR Genes")
plt.ylabel("Frequency")
plt.title("AMR Gene Distribution Across E. coli Genomes")
plt.tight_layout()
plt.savefig("amr_bar_chart.png", dpi=300)



