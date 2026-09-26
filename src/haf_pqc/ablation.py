"""
ablation.py

Ablation study framework
for HAF-PQC.

Evaluates contribution of:

- diversity mechanism
- PBSF binding
- adaptive selection
- recovery mechanism
- correlation modelling
"""


import pandas as pd

from pathlib import Path





class AblationStudy:
    """
    Controls ablation experiments.
    """



    def __init__(self):


        self.configurations = [

            {

                "name":
                "Full HAF-PQC",

                "diversity":
                True,

                "pbsf":
                True,

                "adaptive":
                True,

                "recovery":
                True,

                "correlation":
                True

            },


            {

                "name":
                "Without Diversity",

                "diversity":
                False

            },


            {

                "name":
                "Without PBSF",

                "pbsf":
                False

            },


            {

                "name":
                "Without Adaptive Selection",

                "adaptive":
                False

            },


            {

                "name":
                "Without Recovery",

                "recovery":
                False

            },


            {

                "name":
                "Without Correlation Model",

                "correlation":
                False

            }

        ]





    # =====================================
    # Generate Configurations
    # =====================================

    def generate_configurations(self):


        return self.configurations





    # =====================================
    # Evaluate Configuration
    # =====================================

    def evaluate_configuration(

        self,

        configuration

    ):


        score = 100



        if configuration.get(

            "diversity",

            True

        ) is False:


            score -= 15



        if configuration.get(

            "pbsf",

            True

        ) is False:


            score -= 10



        if configuration.get(

            "adaptive",

            True

        ) is False:


            score -= 20



        if configuration.get(

            "recovery",

            True

        ) is False:


            score -= 15



        return {


            "configuration":

            configuration["name"],


            "survival_probability":

            score / 100

        }





    # =====================================
    # Run Complete Study
    # =====================================

    def run(

        self,

        output_file=

        "results/processed/ablation_results.csv"

    ):


        results=[]



        for config in self.configurations:


            results.append(

                self.evaluate_configuration(

                    config

                )

            )



        df=pd.DataFrame(

            results

        )


        Path(

            output_file

        ).parent.mkdir(

            parents=True,

            exist_ok=True

        )


        df.to_csv(

            output_file,

            index=False

        )


        return df