"""
statistics.py

Statistical analysis utilities
for HAF-PQC experiments.
"""


import statistics

import math





class StatisticalAnalyzer:
    """
    Provides statistical processing.
    """



    # =====================================
    # Mean
    # =====================================

    def mean(

        self,

        values

    ):


        return statistics.mean(

            values

        )





    # =====================================
    # Median
    # =====================================

    def median(

        self,

        values

    ):


        return statistics.median(

            values

        )





    # =====================================
    # Standard Deviation
    # =====================================

    def standard_deviation(

        self,

        values

    ):


        return statistics.stdev(

            values

        )





    # =====================================
    # Confidence Interval
    # =====================================

    def confidence_interval(

        self,

        values,

        confidence=0.95

    ):


        mean_value = self.mean(

            values

        )


        std = self.standard_deviation(

            values

        )


        margin = (

            1.96 *

            std /

            math.sqrt(

                len(values)

            )

        )


        return (

            mean_value-margin,

            mean_value+margin

        )





    # =====================================
    # Summary
    # =====================================

    def summarize(

        self,

        values

    ):


        return {


            "mean":

            self.mean(values),


            "median":

            self.median(values),


            "standard_deviation":

            self.standard_deviation(values),


            "confidence_interval":

            self.confidence_interval(values)

        }