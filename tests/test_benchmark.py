"""
Benchmark engine tests
"""


from pathlib import Path


from src.haf_pqc.benchmark_engine import (
    BenchmarkEngine
)





def test_benchmark_initialization(tmp_path):


    engine = BenchmarkEngine(

        output_directory=str(tmp_path),

        sessions=1,

        warmup=0

    )


    assert engine is not None





def test_single_measurement(tmp_path):


    engine = BenchmarkEngine(

        output_directory=str(tmp_path),

        sessions=1,

        warmup=0

    )


    result = engine.measure_session(

        "X25519",

        1,

        0

    )


    assert (

        "algorithm"

        in

        result

    )


    assert (

        result["algorithm"]

        ==

        "X25519"

    )





def test_benchmark_output(tmp_path):


    engine = BenchmarkEngine(

        output_directory=str(tmp_path),

        sessions=1,

        warmup=0,

        seeds=[1]

    )


    engine.run(

        [

            "X25519"

        ]

    )


    file = (

        Path(tmp_path)

        /

        "session_metrics.csv"

    )


    assert file.exists()