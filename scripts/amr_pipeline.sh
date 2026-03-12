#!/bin/bash

# Loop through genomes
for genome in ecoli_*.fasta
do
  name=$(basename $genome .fasta)

  # BLAST
  blastn -query $genome \
  -db CARD_db \
  -out ${name}_CARD.tsv \
  -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore" \
  -evalue 1e-30

  # Filter hits >=90% identity
  awk '$3 >= 90' ${name}_CARD.tsv > ${name}_filtered.tsv

  # Add column header
  echo -e "ID\tARO_Index\tGene\t%identity\talignment_length\tmismatches\tgap_opens\tq_start\tq_end\ts_start\ts_end\tevalue\tbit_score" | cat - ${name}_filtered.tsv > final_${name}_filtered.tsv
done

# Combine all filtered results
cat final_*_filtered.tsv > all_ecoli_AMR_results.tsv
