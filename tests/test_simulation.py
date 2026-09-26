"""
Security simulation tests
"""


from src.haf_pqc.simulation import (
    SecuritySimulationEngine
)





def test_simulation_initialization():


    engine = SecuritySimulationEngine()


    assert engine is not None





def test_independent_failure_model():


    engine = SecuritySimulationEngine(

        trials=10

    )


    failed = engine.independent_failure(

        [

        "ML-KEM",

        "HQC"

        ],

        0.5

    )


    assert isinstance(

        failed,

        list

    )





def test_correlated_failure_model():


    engine = SecuritySimulationEngine()



    failed = engine.correlated_failure(

        [

        "ML-KEM",

        "HQC"

        ],

        1.0

    )


    assert len(failed) == 2





def test_exposure_calculation():


    engine = SecuritySimulationEngine()



    score = engine.calculate_exposure(

        [

        "A",

        "B",

        "C"

        ],

        [

        "A"

        ]

    )


    assert score == (

        1/3

    )