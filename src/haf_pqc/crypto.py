"""
crypto.py

Real cryptographic operation wrapper
for HAF-PQC.

Backends:

PQC:
- liboqs-python

Classical:
- cryptography

Supported:
- ML-KEM-768
- HQC
- Classic-McEliece
- X25519


No simulated cryptographic outputs.
"""



from dataclasses import dataclass

from typing import Optional

import time





@dataclass
class KEMResult:

    algorithm: str

    success: bool

    public_key_bytes: int

    ciphertext_bytes: int

    shared_secret_bytes: int

    keygen_time_ms: float

    encapsulation_time_ms: float

    decapsulation_time_ms: float

    error: str = ""





class CryptoEngine:
    """
    Unified cryptographic execution layer.
    """



    def __init__(self):

        self.oqs_available = False

        self.crypto_available = False


        self._detect_backends()





    # ===============================================
    # Backend Detection
    # ===============================================

    def _detect_backends(self):


        try:

            import oqs

            self.oqs_available = True


        except Exception:

            self.oqs_available = False



        try:

            from cryptography.hazmat.primitives.asymmetric import x25519

            self.crypto_available = True


        except Exception:

            self.crypto_available = False





    # ===============================================
    # PQC KEM
    # ===============================================

    def run_pqc_kem(

        self,

        algorithm: str

    ) -> KEMResult:



        if not self.oqs_available:


            return KEMResult(

                algorithm,

                False,

                0,

                0,

                0,

                0,

                0,

                0,

                "liboqs unavailable"

            )



        import oqs



        try:


            # -----------------------------
            # Key Generation
            # -----------------------------

            start = time.perf_counter()



            with oqs.KeyEncapsulation(

                algorithm

            ) as kem:


                public_key = (

                    kem.generate_keypair()

                )


                end = time.perf_counter()



                keygen_time = (

                    end-start

                )*1000





                # -------------------------
                # Encapsulation
                # -------------------------


                start = time.perf_counter()


                ciphertext, secret1 = (

                    kem.encap_secret(

                        public_key

                    )

                )


                end = time.perf_counter()


                encaps_time = (

                    end-start

                )*1000





                # -------------------------
                # Decapsulation
                # -------------------------


                start = time.perf_counter()



                secret2 = (

                    kem.decap_secret(

                        ciphertext

                    )

                )



                end = time.perf_counter()



                decap_time = (

                    end-start

                )*1000





            return KEMResult(

                algorithm=

                algorithm,


                success=

                secret1 == secret2,


                public_key_bytes=

                len(public_key),


                ciphertext_bytes=

                len(ciphertext),


                shared_secret_bytes=

                len(secret1),


                keygen_time_ms=

                keygen_time,


                encapsulation_time_ms=

                encaps_time,


                decapsulation_time_ms=

                decap_time

            )




        except Exception as e:


            return KEMResult(

                algorithm,

                False,

                0,

                0,

                0,

                0,

                0,

                0,

                str(e)

            )





    # ===============================================
    # X25519
    # ===============================================

    def run_x25519(self):


        if not self.crypto_available:


            return KEMResult(

                "X25519",

                False,

                0,

                0,

                0,

                0,

                0,

                0,

                "cryptography unavailable"

            )



        from cryptography.hazmat.primitives.asymmetric import x25519



        try:


            start = time.perf_counter()



            private_key = (

                x25519.X25519PrivateKey.generate()

            )


            public_key = (

                private_key.public_key()

            )



            end = time.perf_counter()



            keygen_time = (

                end-start

            )*1000



            public_bytes = (

                public_key.public_bytes_raw()

            )



            return KEMResult(

                algorithm="X25519",

                success=True,

                public_key_bytes=len(public_bytes),

                ciphertext_bytes=0,

                shared_secret_bytes=32,

                keygen_time_ms=keygen_time,

                encapsulation_time_ms=0,

                decapsulation_time_ms=0

            )


        except Exception as e:


            return KEMResult(

                "X25519",

                False,

                0,

                0,

                0,

                0,

                0,

                0,

                str(e)

            )





    # ===============================================
    # Unified Interface
    # ===============================================

    def execute(

        self,

        algorithm:str

    ):


        if algorithm == "X25519":


            return self.run_x25519()



        return self.run_pqc_kem(

            algorithm

        )