import pandas as pd

from src.metrics import compute_summary_statistics, group_by_taxonomy


def sample_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "family": ["F1", "F1", "F2"],
            "completeness_score": [90.0, 95.0, 80.0],
            "protein_coding_genes": [20000, 21000, 18000],
            "transcripts": [40000, 42000, 35000],
            "mean_exons_per_transcript": [8.0, 8.5, 6.0],
            "mean_gene_length": [24000, 25000, 20000],
            "mean_transcript_length": [1800, 1900, 1500],
        }
    )


def test_compute_summary_statistics_returns_expected_columns() -> None:
    df = sample_df()
    summary = compute_summary_statistics(df)
    assert "mean" in summary.columns
    assert "std" in summary.columns


def test_group_by_taxonomy_returns_grouped_frame() -> None:
    df = sample_df()
    grouped = group_by_taxonomy(df, "family")
    assert "F1" in grouped.index
    assert "F2" in grouped.index
