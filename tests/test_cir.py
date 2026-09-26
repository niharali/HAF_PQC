"""
CIR recovery tests
"""


from src.haf_pqc.cir import (
    ConstrainedIncidentRecovery
)





def test_cir_initialization():


    cir = ConstrainedIncidentRecovery()


    assert cir is not None





def test_epoch_increment():


    cir = ConstrainedIncidentRecovery()


    old = cir.security_epoch


    new = cir.increase_epoch()



    assert new == old + 1





def test_component_blacklist():


    cir = ConstrainedIncidentRecovery()



    cir.blacklist_component(

        "HQC"

    )


    assert (

        "HQC"

        in

        cir.blacklist

    )





def test_blacklisted_component_rejected():


    cir = ConstrainedIncidentRecovery()



    cir.blacklist_component(

        "ML-KEM"

    )


    result = cir.is_allowed(

        "ML-KEM"

    )


    assert result is False