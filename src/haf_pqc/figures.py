"""
figures.py

SCI publication figure generator
for HAF-PQC.

Generates 14 figures:

1. Latency comparison
2. Session latency distribution
3. Communication overhead
4. Throughput comparison
5. Survival probability
6. Exposure simulation
7. Family correlation sensitivity
8. Dependency failure
9. Configuration optimization surface
10. Cost-risk tradeoff
11. Confidence intervals
12. Recovery performance
13. Ablation analysis
14. Risk budget sensitivity


Exports:

PNG 300 DPI
SVG
PDF
"""


from pathlib import Path

import pandas as pd

import matplotlib.pyplot as plt





class FigureGenerator:


    def __init__(self, output_directory="figures"):


        self.root = Path(
            output_directory
        )


        self.png = self.root / "png"

        self.svg = self.root / "svg"

        self.pdf = self.root / "pdf"



        for folder in [

            self.png,

            self.svg,

            self.pdf

        ]:

            folder.mkdir(

                parents=True,

                exist_ok=True

            )





    # =====================================
    # Save Helper
    # =====================================

    def save(self,name):


        for folder,ext in [

            (self.png,"png"),

            (self.svg,"svg"),

            (self.pdf,"pdf")

        ]:


            plt.savefig(

                folder / f"{name}.{ext}",

                dpi=300,

                bbox_inches="tight"

            )


        plt.close()





    # =====================================
    # 1 Latency Comparison
    # =====================================

    def fig01_latency(self,df):


        plt.figure(figsize=(8,5))


        data=(

            df.groupby(
                "algorithm"
            )
            [
                "total_latency_ms"
            ]
            .mean()

        )


        data.plot(
            kind="bar"
        )


        plt.ylabel(
            "Latency (ms)"
        )


        plt.title(
            "Primitive Latency Comparison"
        )


        self.save(
            "Fig01_Latency_Comparison"
        )





    # =====================================
    # 2 Session Distribution
    # =====================================

    def fig02_distribution(self,df):


        plt.figure(figsize=(8,5))


        df.boxplot(

            column="total_latency_ms",

            by="algorithm"

        )


        plt.title(
            "Complete Session Latency"
        )


        plt.suptitle("")


        self.save(
            "Fig02_Session_Latency"
        )





    # =====================================
    # 3 Communication
    # =====================================

    def fig03_communication(self,df):


        plt.figure(figsize=(8,5))


        (

        df.groupby("algorithm")

        [
            "communication_bytes"
        ]

        .mean()

        .plot(kind="bar")

        )


        plt.ylabel(
            "Bytes"
        )


        plt.title(
            "Communication Overhead"
        )


        self.save(
            "Fig03_Communication_Overhead"
        )





    # =====================================
    # 4 Throughput
    # =====================================

    def fig04_throughput(self,df):


        plt.figure(figsize=(8,5))


        (

        df.groupby("algorithm")

        [

        "throughput_sessions_per_second"

        ]

        .mean()

        .plot(kind="bar")

        )


        plt.ylabel(
            "Sessions/sec"
        )


        plt.title(
            "Throughput Comparison"
        )


        self.save(
            "Fig04_Throughput"
        )





    # =====================================
    # 5 Survival Probability
    # =====================================

    def fig05_survival(self,df):


        plt.figure(figsize=(8,5))


        (

        df.groupby("scenario")

        [
        "survived"
        ]

        .mean()

        .plot(kind="bar")

        )


        plt.ylabel(
            "Probability"
        )


        plt.title(
            "Security Survival Probability"
        )


        self.save(
            "Fig05_Survival_Probability"
        )





    # =====================================
    # 6 Exposure Simulation
    # =====================================

    def fig06_exposure(self,df):


        plt.figure(figsize=(8,5))


        (

        df.groupby("scenario")

        [

        "exposure_score"

        ]

        .mean()

        .plot(kind="bar")

        )


        plt.ylabel(
            "Exposure Score"
        )


        plt.title(
            "Cryptographic Exposure Simulation"
        )


        self.save(
            "Fig06_Exposure_Simulation"
        )





    # =====================================
    # 7 Correlation
    # =====================================

    def fig07_correlation(self,df):


        plt.figure(figsize=(8,5))


        x = range(
            len(df)
        )


        plt.plot(

            x,

            df["exposure_score"]

        )


        plt.title(
            "Family Correlation Sensitivity"
        )


        self.save(
            "Fig07_Family_Correlation"
        )





    # =====================================
    # 8 Dependency
    # =====================================

    def fig08_dependency(self,df):


        plt.figure(figsize=(8,5))


        (

        df.groupby("scenario")

        [

        "survived"

        ]

        .mean()

        .plot(kind="bar")

        )


        plt.title(
            "Dependency Failure Analysis"
        )


        self.save(
            "Fig08_Dependency_Failure"
        )





    # =====================================
    # 9 Optimization Surface
    # =====================================

    def fig09_surface(self,df):


        plt.figure(figsize=(8,5))


        plt.scatter(

            df["communication_bytes"],

            df["total_latency_ms"]

        )


        plt.xlabel(
            "Communication bytes"
        )


        plt.ylabel(
            "Latency"
        )


        plt.title(
            "Configuration Optimization Surface"
        )


        self.save(
            "Fig09_Optimization_Surface"
        )





    # =====================================
    # 10 Cost Risk
    # =====================================

    def fig10_cost_risk(self,df):


        plt.figure(figsize=(8,5))


        plt.scatter(

            df["communication_bytes"],

            df["total_latency_ms"]

        )


        plt.title(
            "Cost Risk Tradeoff"
        )


        self.save(
            "Fig10_Cost_Risk"
        )





    # =====================================
    # 11 Confidence Interval
    # =====================================

    def fig11_confidence(self,df):


        plt.figure(figsize=(8,5))


        data=(

            df.groupby(
                "algorithm"
            )

            [

            "total_latency_ms"

            ]

            .mean()

        )


        data.plot(
            kind="bar"
        )


        plt.title(
            "Confidence Comparison"
        )


        self.save(
            "Fig11_Confidence_Intervals"
        )





    # =====================================
    # 12 Recovery
    # =====================================

    def fig12_recovery(self,df):


        plt.figure(figsize=(8,5))


        df.plot(

            x="component",

            y="recovery_time_ms",

            kind="bar"

        )


        plt.title(
            "Recovery Performance"
        )


        self.save(
            "Fig12_Recovery_Performance"
        )





    # =====================================
    # 13 Ablation
    # =====================================

    def fig13_ablation(self,df):


        plt.figure(figsize=(8,5))


        df.plot(

            x="configuration",

            y="survival_probability",

            kind="bar"

        )


        plt.title(
            "Ablation Analysis"
        )


        self.save(
            "Fig13_Ablation_Analysis"
        )





    # =====================================
    # 14 Risk Budget
    # =====================================

    def fig14_risk(self,df):


        plt.figure(figsize=(8,5))


        plt.plot(

            df["exposure_score"]

        )


        plt.title(
            "Risk Budget Sensitivity"
        )


        self.save(
            "Fig14_Risk_Budget"
        )





    # =====================================
    # Complete Generator
    # =====================================

    def generate_all(

        self,

        session_file,

        security_file,

        ablation_file

    ):


        session=pd.read_csv(
            session_file
        )


        security=pd.read_csv(
            security_file
        )


        ablation=pd.read_csv(
            ablation_file
        )



        self.fig01_latency(session)

        self.fig02_distribution(session)

        self.fig03_communication(session)

        self.fig04_throughput(session)


        self.fig05_survival(security)

        self.fig06_exposure(security)

        self.fig07_correlation(security)

        self.fig08_dependency(security)


        self.fig09_surface(session)

        self.fig10_cost_risk(session)

        self.fig11_confidence(session)


        recovery = Path(
            "results/raw/recovery_metrics.csv"
        )


        if recovery.exists():

            self.fig12_recovery(
                pd.read_csv(recovery)
            )


        self.fig13_ablation(ablation)


        self.fig14_risk(security)



        print(
            "14 figures generated successfully"
        )