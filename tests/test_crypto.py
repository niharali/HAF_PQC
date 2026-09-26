"""
Crypto module tests
"""


from src.haf_pqc.crypto import CryptoEngine





def test_crypto_engine_initialization():


    engine = CryptoEngine()


    assert engine is not None





def test_x25519_execution():


    engine = CryptoEngine()


    result = engine.execute(

        "X25519"

    )


    assert result.algorithm == "X25519"





def test_unknown_algorithm_failure():


    engine = CryptoEngine()


    result = engine.execute(

        "UNKNOWN"

    )


    assert result.success is False