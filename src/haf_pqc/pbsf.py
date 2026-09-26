"""
pbsf.py

Policy Bound Session Fusion (PBSF)

Provides:

- canonical transcript binding
- policy binding
- session integrity verification
"""


import hashlib

import json





class PolicyBoundSessionFusion:
    """
    Secure session fusion layer.
    """



    def __init__(self):

        self.domain_separator = (

            "HAF-PQC-PBSF-v1"

        )





    # =====================================
    # Canonical Serialization
    # =====================================

    def serialize_context(

        self,

        context

    ):


        return json.dumps(

            context,

            sort_keys=True,

            default=str

        ).encode()





    # =====================================
    # Create Binding
    # =====================================

    def create_session_binding(

        self,

        context

    ):


        serialized = (

            self.domain_separator.encode()

            +

            self.serialize_context(

                context

            )

        )


        return hashlib.sha3_256(

            serialized

        ).hexdigest()





    # =====================================
    # Verify Binding
    # =====================================

    def verify_binding(

        self,

        context,

        binding

    ):


        calculated = (

            self.create_session_binding(

                context

            )

        )


        return (

            calculated

            ==

            binding

        )





    # =====================================
    # Key Fusion
    # =====================================

    def fuse_shared_secrets(

        self,

        secrets,

        context

    ):


        data = (

            b""

            .join(secrets)

            +

            self.serialize_context(

                context

            )

        )


        return hashlib.sha3_256(

            data

        ).digest()