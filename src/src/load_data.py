from pathlib import Path
import pandas as pd


def load_annotation_metrics(csv_path: str | Path) -> pd.DataFrame:
    """Load annotation metrics from a CSV file."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_csv(path)
