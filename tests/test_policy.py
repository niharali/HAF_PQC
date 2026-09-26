"""
Policy controller tests
"""


from src.haf_pqc.policy import CryptoPolicyController





def test_policy_creation():


    policy = CryptoPolicyController()


    assert policy.policy is not None





def test_policy_hash_generation():


    policy = CryptoPolicyController()


    value = policy.generate_policy_hash()


    assert len(value) > 0





def test_configuration_validation():


    policy = CryptoPolicyController()


    result = policy.validate_configuration(

        [

        "ML-KEM-768",

        "HQC",

        "X25519"

        ]

    )


    assert result["valid"] is True