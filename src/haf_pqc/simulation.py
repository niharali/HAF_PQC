"""
simulation.py

Monte Carlo security simulation engine
for HAF-PQC.

Evaluates resilience under:
- independent failures
- correlated failures
- dependency failures

Simulation results are not security proofs.
They represent modeled scenarios.
"""


from dataclasses import dataclass

from typing import List, Dict

import random

import csv

from pathlib import Path





@dataclass
class SimulationRecord:

    scenario: str

    configuration: str

    trial: int

    survived: bool

    failure_probability: float

    exposure_score: float





class SecuritySimulationEngine:
    """
    Monte Carlo based security evaluator.
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
    # Independent Failure Model
    # --------------------------------------------------

    def independent_failure(

        self,

        components:

        List[str],

        failure_probability:

        float

    ):


        failed = []


        for component in components:


            if random.random() < failure_probability:

                failed.append(component)



        return failed





    # --------------------------------------------------
    # Correlated Failure Model
    # --------------------------------------------------

    def correlated_failure(

        self,

        components:

        List[str],

        correlation_probability:

        float

    ):


        failed = []


        common_event = (

            random.random()
            <
            correlation_probability

        )


        if common_event:


            return components.copy()



        return failed





    # --------------------------------------------------
    # Dependency Failure Model
    # --------------------------------------------------

    def dependency_failure(

        self,

        components:

        List[str],

        dependency_probability:

        float

    ):


        if random.random() < dependency_probability:

            return components


        return []





    # --------------------------------------------------
    # Survival Evaluation
    # --------------------------------------------------

    def evaluate_survival(

        self,

        configuration:

        List[str],

        failed:

        List[str]

    ):


        remaining = [

            c

            for c in configuration

            if c not in failed

        ]


        return len(remaining) > 0





    # --------------------------------------------------
    # Exposure Calculation
    # --------------------------------------------------

    def calculate_exposure(

        self,

        configuration:

        List[str],

        failed:

        List[str]

    ):


        if len(configuration)==0:

            return 1.0



        return (

            len(failed)

            /

            len(configuration)

        )





    # --------------------------------------------------
    # Complete Simulation
    # --------------------------------------------------

    def run(

        self,

        configuration:

        List[str],

        failure_probability=0.1

    ):


        records = []


        scenarios = {


            "independent":

            self.independent_failure,



            "correlated":

            self.correlated_failure,



            "dependency":

            self.dependency_failure

        }



        for scenario, function in scenarios.items():


            for trial in range(

                self.trials

            ):


                failed = function(

                    configuration,

                    failure_probability

                )


                survived = (

                    self.evaluate_survival(

                        configuration,

                        failed

                    )

                )


                exposure = (

                    self.calculate_exposure(

                        configuration,

                        failed

                    )

                )


                records.append(

                    SimulationRecord(

                        scenario=scenario,

                        configuration=

                        "+".join(configuration),


                        trial=trial,


                        survived=survived,


                        failure_probability=

                        failure_probability,


                        exposure_score=

                        exposure

                    )

                )


        return records





    # --------------------------------------------------
    # CSV Export
    # --------------------------------------------------

    def save_results(

        self,

        records:

        List[SimulationRecord],

        filename=

        "results/raw/security_simulation.csv"

    ):


        path = Path(filename)

        path.parent.mkdir(

            parents=True,

            exist_ok=True

        )


        with open(

            path,

            "w",

            newline=""

        ) as file:


            writer = csv.DictWriter(

                file,

                fieldnames=

                [

                    "scenario",

                    "configuration",

                    "trial",

                    "survived",

                    "failure_probability",

                    "exposure_score"

                ]

            )


            writer.writeheader()


            for record in records:


                writer.writerow(

                    {

                    "scenario":
                    record.scenario,


                    "configuration":
                    record.configuration,


                    "trial":
                    record.trial,


                    "survived":
                    record.survived,


                    "failure_probability":
                    record.failure_probability,


                    "exposure_score":
                    record.exposure_score

                    }

                )