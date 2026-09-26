"""
benchmark_engine.py

Real cryptographic benchmark engine
for HAF-PQC.

Generates:

results/raw/session_metrics.csv

Measurements:

- key generation latency
- encapsulation latency
- decapsulation latency
- total latency
- communication overhead
- throughput
- success status
"""


from pathlib import Path

import csv
import json
import random
import time

from .crypto import CryptoEngine





class BenchmarkEngine:
    """
    Executes reproducible cryptographic experiments.
    """



    def __init__(

        self,

        output_directory="results/raw",

        sessions=3000,

        warmup=50,

        seeds=None

    ):


        self.output_directory = Path(
            output_directory
        )


        self.output_directory.mkdir(

            parents=True,

            exist_ok=True

        )


        self.sessions = sessions

        self.warmup = warmup


        self.seeds = (

            seeds

            if seeds

            else

            [1,2,3]

        )


        self.crypto = CryptoEngine()





    # ==========================================
    # Warmup
    # ==========================================

    def warmup_algorithm(self, algorithm):


        for _ in range(self.warmup):

            self.crypto.execute(
                algorithm
            )





    # ==========================================
    # Single Experiment
    # ==========================================

    def measure_session(

        self,

        algorithm,

        seed,

        session_id

    ):


        random.seed(

            seed + session_id

        )


        start = time.perf_counter()


        result = self.crypto.execute(

            algorithm

        )


        end = time.perf_counter()



        total_latency = (

            end-start

        ) * 1000



        communication = (

            result.public_key_bytes

            +

            result.ciphertext_bytes

        )



        throughput = (

            1000 /

            total_latency

            if total_latency > 0

            else 0

        )



        return {


            "algorithm":

            algorithm,


            "seed":

            seed,


            "session_id":

            session_id,


            "success":

            result.success,


            "keygen_ms":

            result.keygen_time_ms,


            "encapsulation_ms":

            result.encapsulation_time_ms,


            "decapsulation_ms":

            result.decapsulation_time_ms,


            "total_latency_ms":

            total_latency,


            "public_key_bytes":

            result.public_key_bytes,


            "ciphertext_bytes":

            result.ciphertext_bytes,


            "shared_secret_bytes":

            result.shared_secret_bytes,


            "communication_bytes":

            communication,


            "throughput_sessions_per_second":

            throughput,


            "error":

            result.error

        }





    # ==========================================
    # Run Benchmark
    # ==========================================

    def run(self, algorithms):


        records = []



        for seed in self.seeds:


            execution_order = list(
                algorithms
            )


            random.shuffle(
                execution_order
            )


            for algorithm in execution_order:


                print(

                    f"Benchmarking {algorithm}"

                )


                self.warmup_algorithm(

                    algorithm

                )



                for session in range(

                    self.sessions

                ):


                    record = (

                        self.measure_session(

                            algorithm,

                            seed,

                            session

                        )

                    )


                    records.append(

                        record

                    )



        self.save_results(

            records

        )


        return records





    # ==========================================
    # Save CSV
    # ==========================================

    def save_results(self, records):


        filename = (

            self.output_directory

            /

            "session_metrics.csv"

        )



        with open(

            filename,

            "w",

            newline=""

        ) as file:


            writer = csv.DictWriter(

                file,

                fieldnames=

                records[0].keys()

            )


            writer.writeheader()


            writer.writerows(

                records

            )



        print(

            f"Benchmark saved: {filename}"

        )



        self.save_metadata()





    # ==========================================
    # Metadata
    # ==========================================

    def save_metadata(self):


        metadata = {


            "sessions":

            self.sessions,


            "warmup_runs":

            self.warmup,


            "random_seeds":

            self.seeds,


            "measurement":

            "real cryptographic execution"

        }



        with open(

            self.output_directory /

            "benchmark_metadata.json",

            "w"

        ) as file:


            json.dump(

                metadata,

                file,

                indent=4

            )