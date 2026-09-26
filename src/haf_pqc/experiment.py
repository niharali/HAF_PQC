"""
experiment.py

Complete HAF-PQC Research Execution Pipeline

Workflow:

Environment
    |
    v
Crypto Backend
    |
    v
Policy Controller
    |
    v
FARE Selection
    |
    v
Real Crypto Benchmark
    |
    v
Threat Simulation
    |
    v
CIR Recovery
    |
    v
Statistics
    |
    v
Ablation
    |
    v
Figures
    |
    v
Tables
    |
    v
Validation
"""


from pathlib import Path

import json
import time



from .crypto_backend import PQCBackend


from .crypto import CryptoEngine


from .policy import CryptoPolicyController


from .fare import (
    FamilyAwareRobustEnsembleSelector,
    CryptoCandidate
)


from .benchmark_engine import BenchmarkEngine


from .simulation import SecuritySimulationEngine


from .statistics import StatisticalAnalyzer


from .ablation import AblationStudy


from .figures import FigureGenerator


from .table_generator import TableGenerator


from .reproducibility import ReproducibilityManager


from .cir import ConstrainedIncidentRecovery


from .recovery_engine import RecoveryEngine





class HAFPQCExperiment:
    """
    Main HAF-PQC experiment controller.
    """



    def __init__(self):


        self.results = Path(
            "results"
        )


        self.raw = (

            self.results /
            "raw"

        )


        self.processed = (

            self.results /
            "processed"

        )


        self.raw.mkdir(
            parents=True,
            exist_ok=True
        )


        self.processed.mkdir(
            parents=True,
            exist_ok=True
        )


        self.metadata = {}





    # =================================================
    # 1. ENVIRONMENT
    # =================================================

    def initialize_environment(self):


        print(
            "\n[1] Detecting environment"
        )


        self.backend = PQCBackend()


        self.crypto = CryptoEngine()


        self.metadata["backend"] = (

            self.backend.get_status()

        )





    # =================================================
    # 2. REPRODUCIBILITY
    # =================================================

    def initialize_reproducibility(self):


        print(
            "\n[2] Recording reproducibility information"
        )


        manager = ReproducibilityManager()



        manager.collect_system_information()


        manager.collect_dependencies()



        manager.record_seed(
            42
        )


        manager.record_configuration(

            {

            "framework":
            "HAF-PQC",


            "benchmark_sessions":
            3000,


            "algorithms":

            [

                "ML-KEM-768",

                "HQC",

                "Classic-McEliece",

                "X25519"

            ]

            }

        )


        manager.collect_git_information()


        manager.save()





    # =================================================
    # 3. POLICY CONTROLLER
    # =================================================

    def initialize_policy(self):


        print(
            "\n[3] Initializing policy controller"
        )


        self.policy = CryptoPolicyController(

            security_level="high",

            risk_threshold=0.3,

            max_components=3

        )


        self.metadata["policy_hash"] = (

            self.policy.generate_policy_hash()

        )





    # =================================================
    # 4. FARE
    # =================================================

    def run_fare(self):


        print(
            "\n[4] Running FARE selection"
        )


        candidates = [

            CryptoCandidate(

                "ML-KEM-768",

                "Lattice",

                5,

                2.0,

                3.0,

                0.2

            ),


            CryptoCandidate(

                "HQC",

                "Code",

                5,

                4.0,

                5.0,

                0.15

            ),


            CryptoCandidate(

                "X25519",

                "ECC",

                1,

                1.0,

                1.0,

                0.5

            )

        ]



        fare = FamilyAwareRobustEnsembleSelector()



        self.configuration = (

            fare.optimize_configuration(

                candidates

            )

        )


        print(

            self.configuration

        )





    # =================================================
    # 5. REAL BENCHMARK
    # =================================================

    def run_benchmark(self):


        print(
            "\n[5] Running real cryptographic benchmark"
        )


        algorithms = [

            "ML-KEM-768",

            "HQC",

            "Classic-McEliece",

            "X25519"

        ]



        engine = BenchmarkEngine(

            output_directory=

            str(self.raw),


            sessions=3000,


            warmup=50,


            seeds=[1,2,3]

        )


        self.records = engine.run(

            algorithms

        )





    # =================================================
    # 6. THREAT SIMULATION
    # =================================================

    def run_security_simulation(self):


        print(
            "\n[6] Running security simulation"
        )


        simulator = SecuritySimulationEngine(

            trials=10000

        )


        records = simulator.run(

            [

            "ML-KEM",

            "HQC",

            "X25519"

            ]

        )


        simulator.save_results(

            records

        )





    # =================================================
    # 7. CIR RECOVERY
    # =================================================

    def run_recovery(self):


        print(
            "\n[7] Running CIR recovery"
        )


        cir = ConstrainedIncidentRecovery()


        recovery = RecoveryEngine(

            cir=cir

        )


        recovery.recover(

            [

            "ML-KEM",

            "HQC",

            "X25519"

            ],


            "HQC",


            [

            "Classic-McEliece"

            ]

        )


        recovery.export_metrics()





    # =================================================
    # 8. STATISTICS
    # =================================================

    def run_statistics(self):


        print(
            "\n[8] Statistical analysis"
        )


        analyzer = StatisticalAnalyzer()



        latency = []


        import pandas as pd


        df = pd.read_csv(

            self.raw /
            "session_metrics.csv"

        )


        latency = (

            df

            [

            "total_latency_ms"

            ]

            .tolist()

        )



        result = analyzer.summarize(

            latency

        )


        with open(

            self.processed /

            "statistical_summary.json",

            "w"

        ) as file:


            json.dump(

                result,

                file,

                indent=4

            )





    # =================================================
    # 9. ABLATION
    # =================================================

    def run_ablation(self):


        print(
            "\n[9] Running ablation study"
        )


        study = AblationStudy()


        study.run()





    # =================================================
    # 10. FIGURES
    # =================================================

    def generate_figures(self):


        print(
            "\n[10] Generating figures"
        )


        generator = FigureGenerator()



        generator.generate_all(

            str(

            self.raw /

            "session_metrics.csv"

            ),


            str(

            self.raw /

            "security_simulation.csv"

            ),


            str(

            self.processed /

            "ablation_results.csv"

            )

        )





    # =================================================
    # 11. TABLES
    # =================================================

    def generate_tables(self):


        print(
            "\n[11] Generating tables"
        )


        generator = TableGenerator()



        generator.generate_all(

            str(

            self.raw /

            "session_metrics.csv"

            ),


            str(

            self.raw /

            "security_simulation.csv"

            ),


            str(

            self.raw /

            "recovery_metrics.csv"

            ),


            str(

            self.processed /

            "statistical_summary.json"

            ),


            str(

            self.processed /

            "ablation_results.csv"

            )

        )





    # =================================================
    # 12. FINAL METADATA
    # =================================================

    def save_metadata(self):


        self.metadata["completed"] = True


        self.metadata["time"] = time.time()



        with open(

            self.results /

            "final_metadata.json",

            "w"

        ) as file:


            json.dump(

                self.metadata,

                file,

                indent=4

            )





    # =================================================
    # COMPLETE EXECUTION
    # =================================================

    def run(self):


        print(

            """

=================================
 HAF-PQC EXPERIMENT STARTED
=================================

"""

        )


        self.initialize_environment()


        self.initialize_reproducibility()


        self.initialize_policy()


        self.run_fare()


        self.run_benchmark()


        self.run_security_simulation()


        self.run_recovery()


        self.run_statistics()


        self.run_ablation()


        self.generate_figures()


        self.generate_tables()


        self.save_metadata()



        print(

            """

=================================
 HAF-PQC COMPLETED SUCCESSFULLY
=================================

Generated:

✓ Real benchmark data
✓ Security simulation
✓ Recovery metrics
✓ Statistical analysis
✓ Figures
✓ Tables
✓ Metadata

"""

        )





def run():

    experiment = HAFPQCExperiment()

    experiment.run()