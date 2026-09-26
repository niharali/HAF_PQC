"""
threat_model.py

Security threat simulation framework
for HAF-PQC.

Evaluates:
- primitive compromise
- family compromise
- correlated failures
- dependency failures

This module performs simulation only.

It does not provide cryptographic
security proofs.
"""


from dataclasses import dataclass

from typing import List

import random





@dataclass
class FailureScenario:

    name: str

    compromised_components: List[str]

    description: str





@dataclass
class SimulationResult:

    scenario: str

    configuration: List[str]

    survived: bool

    remaining_components: List[str]

    survival_probability: float





class ThreatModelSimulator:
    """
    HAF-PQC threat simulation engine.
    """



    def __init__(
        self,
        trials=10000,
        seed=42
    ):

        self.trials = trials

        self.seed = seed

        random.seed(seed)





    # --------------------------------------------------
    # Scenario Definitions
    # --------------------------------------------------

    def scenarios(self):


        return [

            FailureScenario(

                name=
                "single_family_compromise",

                compromised_components=
                [
                    "ML-KEM"
                ],

                description=
                "Single lattice family failure"

            ),



            FailureScenario(

                name=
                "two_family_compromise",

                compromised_components=
                [
                    "ML-KEM",
                    "HQC"
                ],

                description=
                "Two independent families fail"

            ),



            FailureScenario(

                name=
                "correlated_failure",

                compromised_components=
                [
                    "shared_dependency"
                ],

                description=
                "Common dependency failure"

            ),



            FailureScenario(

                name=
                "implementation_failure",

                compromised_components=
                [
                    "implementation"
                ],

                description=
                "Implementation level failure"

            )

        ]





    # --------------------------------------------------
    # Failure Evaluation
    # --------------------------------------------------

    def evaluate_configuration(

        self,

        configuration:

        List[str],

        scenario:

        FailureScenario

    ) -> SimulationResult:


        failures = (
            scenario.compromised_components
        )


        remaining = []


        for component in configuration:


            failed = False


            for failure in failures:


                if failure in component:

                    failed = True



            if not failed:

                remaining.append(
                    component
                )



        survived = (
            len(remaining)
            >
            0
        )


        probability = (
            len(remaining)
            /
            len(configuration)
            if configuration
            else 0
        )



        return SimulationResult(

            scenario=scenario.name,

            configuration=configuration,

            survived=survived,

            remaining_components=remaining,

            survival_probability=probability

        )





    # --------------------------------------------------
    # Monte Carlo Simulation
    # --------------------------------------------------

    def run_simulation(

        self,

        configuration:

        List[str]

    ):


        results = []


        for scenario in self.scenarios():


            survival_count = 0


            for _ in range(
                self.trials
            ):


                result = (

                    self.evaluate_configuration(

                        configuration,

                        scenario

                    )

                )


                if result.survived:

                    survival_count += 1



            probability = (

                survival_count
                /
                self.trials

            )


            results.append(

                SimulationResult(

                    scenario=
                    scenario.name,

                    configuration=
                    configuration,

                    survived=
                    probability > 0,

                    remaining_components=
                    [],

                    survival_probability=
                    probability

                )

            )


        return results