"""
PBSF module tests

Validates:

- session binding
- transcript integrity
- policy binding
"""



import pytest


from src.haf_pqc.pbsf import (
    PolicyBoundSessionFusion
)





def create_test_context():


    return {

        "protocol_version":
        "1.0",


        "algorithm_ids":

        [

            "ML-KEM-768",

            "HQC",

            "X25519"

        ],


        "public_keys":

        [

            b"key1",

            b"key2"

        ],


        "ciphertexts":

        [

            b"cipher1"

        ],


        "session_id":

        "SESSION001",


        "policy_hash":

        "abc123",


        "epoch":

        1,


        "sender_role":

        "client",


        "receiver_role":

        "server"

    }





def test_pbsf_initialization():


    pbsf = PolicyBoundSessionFusion()


    assert pbsf is not None





def test_session_binding_creation():


    pbsf = PolicyBoundSessionFusion()


    context = create_test_context()


    result = pbsf.create_session_binding(

        context

    )


    assert result is not None





def test_policy_binding_changes_output():


    pbsf = PolicyBoundSessionFusion()



    context1 = create_test_context()



    context2 = create_test_context()


    context2["policy_hash"] = "different"



    binding1 = (

        pbsf.create_session_binding(

            context1

        )

    )


    binding2 = (

        pbsf.create_session_binding(

            context2

        )

    )


    assert binding1 != binding2





def test_modified_transcript_detection():


    pbsf = PolicyBoundSessionFusion()



    context = create_test_context()



    binding = (

        pbsf.create_session_binding(

            context

        )

    )


    context["ciphertexts"] = [

        b"modified"

    ]



    valid = (

        pbsf.verify_binding(

            context,

            binding

        )

    )


    assert valid is False