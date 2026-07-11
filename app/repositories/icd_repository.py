from rapidfuzz import fuzz

from app.core.icd_cache import ICDCache


class ICDRepository:
    """
    Repository for ICD-10 search.
    """

    def __init__(self):
        self.df = ICDCache.get_dataframe()

    def search(
        self,
        diagnosis: str,
        limit: int = 5,
    ):

        diagnosis = diagnosis.lower().strip()

        results = []

        for _, row in self.df.iterrows():

            description = row["description"]

            score = max(
                fuzz.partial_ratio(
                    diagnosis,
                    description.lower(),
                ),
                fuzz.token_sort_ratio(
                    diagnosis,
                    description.lower(),
                ),
            )

            if score >= 65:

                results.append(
                    {
                        "code": row["code"],
                        "description": description,
                        "confidence": int(score),
                    }
                )

        results.sort(
            key=lambda x: x["confidence"],
            reverse=True,
        )

        return results[:limit]