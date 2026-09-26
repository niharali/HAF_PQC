"""
fare.py

Family-Aware Robust Ensemble Selection (FARE)

Selects heterogeneous cryptographic
configurations.

Objective:

maximize:

Security Diversity
+
Security Level

while controlling:

Cost
+
Risk


FARE does not perform cryptography.
It performs configuration optimization.
"""


from dataclasses import dataclass

from typing import List

from itertools import combinations





@dataclass
class CryptoCandidate:

    name: str

    family: str

    security_level: int

    computational_cost: float

    communication_cost: float

    risk_score: float





class FamilyAwareRobustEnsembleSelector:
    """
    FARE optimizer.

    Selects heterogeneous
    cryptographic combinations.
    """



    def __init__(

        self,

        min_components=2,

        max_components=3

    ):


        self.min_components = min_components

        self.max_components = max_components





    # ======================================
    # Diversity Calculation
    # ======================================

    def diversity_score(

        self,

        configuration

    ):


        families = set(

            item.family

            for item in configuration

        )


        return len(families)





    # ======================================
    # Utility Function
    # ======================================

    def calculate_utility(

        self,

        configuration

    ):


        diversity = (

            self.diversity_score(

                configuration

            )

        )


        security = sum(

            item.security_level

            for item in configuration

        )


        cost = sum(

            item.computational_cost

            +

            item.communication_cost

            for item in configuration

        )


        risk = sum(

            item.risk_score

            for item in configuration

        )


        utility = (

            5 * diversity

            +

            3 * security

            -

            2 * cost

            -

            4 * risk

        )


        return utility





    # ======================================
    # Optimization
    # ======================================

    def optimize_configuration(

        self,

        candidates:

        List[CryptoCandidate]

    ):


        best = None

        best_score = float("-inf")



        all_configurations = []



        for size in range(

            self.min_components,

            self.max_components + 1

        ):


            all_configurations.extend(

                combinations(

                    candidates,

                    size

                )

            )



        for configuration in all_configurations:



            diversity = (

                self.diversity_score(

                    configuration

                )

            )


            # Mandatory heterogeneous rule

            if diversity < 2:

                continue



            utility = (

                self.calculate_utility(

                    configuration

                )

            )



            if utility > best_score:


                best_score = utility


                best = configuration





        if best is None:


            raise RuntimeError(

                "No valid heterogeneous configuration found"

            )



        return {


            "selected_algorithms":

            [

                item.name

                for item in best

            ],


            "utility":

            round(

                best_score,

                3

            ),


            "diversity_score":

            self.diversity_score(

                best

            ),


            "security_score":

            sum(

                x.security_level

                for x in best

            ),


            "cost_score":

            sum(

                x.computational_cost

                for x in best

            ),


            "risk_score":

            sum(

                x.risk_score

                for x in best

            )

        }