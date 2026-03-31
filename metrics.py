import pandas as pd


NUMERIC_COLUMNS = [
    "completeness_score",
    "protein_coding_genes",
    "transcripts",
    "mean_exons_per_transcript",
    "mean_gene_length",
    "mean_transcript_length",
]


def compute_summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Return summary statistics for selected numeric columns."""
    return df[NUMERIC_COLUMNS].describe().T


def group_by_taxonomy(df: pd.DataFrame, rank: str) -> pd.DataFrame:
    """Group data by a taxonomy rank and compute mean metrics."""
    if rank not in df.columns:
        raise ValueError(f"Taxonomy rank '{rank}' not found in dataframe.")
    return df.groupby(rank)[NUMERIC_COLUMNS].mean(numeric_only=True)
