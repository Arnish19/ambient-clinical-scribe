from pathlib import Path

import pandas as pd


class ICDCache:
    """
    Loads the ICD-10 dataset once and keeps it in memory.
    """

    _dataframe = None

    @classmethod
    def get_dataframe(cls) -> pd.DataFrame:

        if cls._dataframe is None:

            csv_path = (
                Path(__file__).resolve().parents[1]
                / "data"
                / "icd10.csv"
            )

            cls._dataframe = (
                pd.read_csv(
                    csv_path,
                    header=None,
                    dtype=str,
                )
                .fillna("")
            )

            cls._dataframe.columns = [
                "category",
                "billable",
                "code",
                "description",
                "long_description",
                "category_description",
            ]

        return cls._dataframe