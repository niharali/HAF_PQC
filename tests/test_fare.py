"""
FARE algorithm tests
"""


from src.haf_pqc.fare import (
    CryptoCandidate,
    FamilyAwareRobustEnsembleSelector
)





def test_fare_selects_diverse_configuration():


    candidates=[


        CryptoCandidate(

            "ML-KEM-768",

            "Lattice",

            5,

            2,

            3,

            0.2

        ),


        CryptoCandidate(

            "HQC",

            "Code",

            5,

            4,

            5,

            0.15

        ),


        CryptoCandidate(

            "X25519",

            "ECC",

            1,

            1,

            1,

            0.5

        )

    ]



    selector = (

        FamilyAwareRobustEnsembleSelector()

    )


    result = selector.optimize_configuration(

        candidates

    )


    assert (

        result["diversity_score"]

        >=

        2

    )