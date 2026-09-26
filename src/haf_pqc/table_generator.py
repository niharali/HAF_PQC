"""
table_generator.py

Automatic manuscript table generator
for HAF-PQC.

Creates SCI paper ready tables.

Generated:

Table 1:
Baseline performance

Table 2:
Communication overhead

Table 3:
Security resilience

Table 4:
Recovery performance

Table 5:
Statistical summary

Table 6:
Ablation study
"""


from pathlib import Path

import pandas as pd

import json





class TableGenerator:
    """
    Generates manuscript tables
    from experimental outputs.
    """



    def __init__(

        self,

        output_directory=
        "results/processed/tables"

    ):


        self.output = Path(
            output_directory
        )


        self.output.mkdir(

            parents=True,

            exist_ok=True

        )





    # ============================================
    # Table 1
    # Baseline Performance
    # ============================================

    def baseline_table(

        self,

        benchmark_file

    ):


        df = pd.read_csv(

            benchmark_file

        )


        table = (

            df.groupby(

                "algorithm"

            )

            [

            [

            "total_latency_ms",

            "keygen_ms",

            "encapsulation_ms",

            "decapsulation_ms"

            ]

            ]

            .mean()

            .reset_index()

        )


        table.to_csv(

            self.output /

            "Table1_Baseline_Performance.csv",

            index=False

        )


        return table





    # ============================================
    # Table 2
    # Communication
    # ============================================

    def communication_table(

        self,

        benchmark_file

    ):


        df = pd.read_csv(

            benchmark_file

        )


        table = (

            df.groupby(

                "algorithm"

            )

            [

            [

            "public_key_bytes",

            "ciphertext_bytes",

            "communication_bytes",

            "throughput_sessions_per_second"

            ]

            ]

            .mean()

            .reset_index()

        )


        table.to_csv(

            self.output /

            "Table2_Communication_Overhead.csv",

            index=False

        )


        return table





    # ============================================
    # Table 3
    # Security
    # ============================================

    def security_table(

        self,

        security_file

    ):


        df = pd.read_csv(

            security_file

        )


        table = (

            df.groupby(

                "scenario"

            )

            [

            [

            "survived",

            "exposure_score"

            ]

            ]

            .mean()

            .reset_index()

        )


        table.rename(

            columns={

            "survived":

            "survival_probability"

            },

            inplace=True

        )


        table.to_csv(

            self.output /

            "Table3_Security_Resilience.csv",

            index=False

        )


        return table





    # ============================================
    # Table 4
    # Recovery
    # ============================================

    def recovery_table(

        self,

        recovery_file

    ):


        path = Path(

            recovery_file

        )


        if not path.exists():


            return None



        df = pd.read_csv(

            path

        )


        table = df[

            [

            "component",

            "old_epoch",

            "new_epoch",

            "recovery_time_ms",

            "successful"

            ]

        ]



        table.to_csv(

            self.output /

            "Table4_Recovery_Performance.csv",

            index=False

        )


        return table





    # ============================================
    # Table 5
    # Statistics
    # ============================================

    def statistics_table(

        self,

        statistics_file

    ):


        path = Path(

            statistics_file

        )


        if not path.exists():

            return None



        with open(

            path

        ) as file:


            data=json.load(

                file

            )



        table=pd.DataFrame(

            [data]

        )



        table.to_csv(

            self.output /

            "Table5_Statistical_Summary.csv",

            index=False

        )


        return table





    # ============================================
    # Table 6
    # Ablation
    # ============================================

    def ablation_table(

        self,

        ablation_file

    ):


        path=Path(

            ablation_file

        )


        if not path.exists():

            return None



        df=pd.read_csv(

            path

        )


        df.to_csv(

            self.output /

            "Table6_Ablation_Study.csv",

            index=False

        )


        return df





    # ============================================
    # Complete Generation
    # ============================================

    def generate_all(

        self,

        benchmark_file,

        security_file,

        recovery_file,

        statistics_file,

        ablation_file

    ):


        print(

            "\nGenerating manuscript tables..."

        )



        self.baseline_table(

            benchmark_file

        )


        self.communication_table(

            benchmark_file

        )


        self.security_table(

            security_file

        )


        self.recovery_table(

            recovery_file

        )


        self.statistics_table(

            statistics_file

        )


        self.ablation_table(

            ablation_file

        )



        print(

            "Tables generated successfully"

        )