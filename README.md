# Genome Annotation Metrics Exploration

This repository is a small exploratory project related to genome annotation metrics reporting and comparative analysis.

Its purpose is to demonstrate a backend-first approach to:
- loading structured genome annotation metrics
- computing per-genome summary statistics
- grouping genomes by taxonomy rank
- detecting simple outliers
- generating basic visual summaries

This work is intentionally small in scope. It is not a production implementation of the Ensembl Assembly/Annotation tracking app. Instead, it is a lightweight prototype to explore the kinds of analysis workflows that could support annotation quality reporting.

## Project goals

This prototype currently focuses on:

- loading genome annotation metrics from CSV
- computing summary statistics for selected metrics
- grouping genomes by taxonomic ranks
- identifying possible outliers using robust z-scores
- generating simple plots for exploratory analysis

## Repository structure

```text
.
├── data/
│   └── sample_annotation_metrics.csv
├── outputs/
├── src/
│   ├── load_data.py
│   ├── metrics.py
│   ├── outliers.py
│   ├── plotting.py
│   └── main.py
├── tests/
│   ├── test_metrics.py
│   └── test_outliers.py
├── requirements.txt
└── README.md
