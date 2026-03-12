# AMR Gene Identification in Escherichia coli Genomes

# Project Overview
This project identifies antimicrobial resistance (AMR) genes in assembled Escherichia coli genomes using the Comprehensive Antibiotic Resistance Database (CARD). The workflow involves sequence similarity searches using BLAST, filtering high-confidence hits, and visualizing AMR gene distribution across genomes.

# Objectives
- Download assembled E. coli genomes from NCBI
- Identify antimicrobial resistance genes using the CARD database
- Filter significant hits based on identity and E-value thresholds
- Compare AMR gene profiles across genomes
- Visualize AMR gene distribution using bar charts and heatmaps

## Tools and Software
- BLAST+  
- CARD Database (v3.3.0)  
- Bash scripting  
- Python (Pandas, Matplotlib, Seaborn)  
- Git/GitHub for version control

## Project Structure
Bioinfo_AMR_Project/
│
├── data/
│ ├── ecoli_genomes/
│ └── CARD_database/
│
├── scripts/
│ ├── amr_pipeline.sh
│ ├── amr_barplot.py
│ └── amr_heatmap.py
│
├── analysis/
│ ├── BLAST_results
│ ├── filtered_results
│ └── all_ecoli_AMR_results.tsv
│
└── README.md


# Workflow

# 1. Genome Download
Assembled E. coli genomes were downloaded from NCBI in FASTA format.

# 2. CARD Database Preparation
The CARD database was downloaded and the nucleotide FASTA file was converted into a BLAST database.

# 3. BLAST Search
Each genome was searched against the CARD database using BLASTn.

Parameters used:
- E-value ≤ 1e-30
- Tabular output format

# 4. Filtering
BLAST results were filtered to retain hits with:
- ≥ 90% sequence identity

# 5. Data Processing
Filtered results were combined into a single table containing:
- Query ID
- ARO index
- Gene name
- % identity
- Alignment length
- Mismatches
- Gap opens
- Query start/end
- Subject start/end
- E-value
- Bit score

# 6. Visualization
Python scripts were used to generate:

- Bar charts showing AMR gene frequencies
- Heatmaps comparing AMR gene presence across genomes


# AMR Gene Distribution
Bar charts illustrate the frequency of detected AMR genes across genomes.

# Comparative AMR Profiles
Heatmaps visualize resistance gene distribution among different E. coli strains.

# Reproducibility	

To reproduce the workflow:
bash scripts/amr_pipeline.sh


Then generate visualizations:
python scripts/amr_barplot.py
python scripts/amr_heatmap.py





AUTHOR: PEACE OKUNADE
