"""
policy.py

Cryptographic Policy Controller

Responsible for:

- defining security requirements
- validating cryptographic configurations
- controlling allowed algorithms
- enforcing risk limits
- generating policy hash

The policy controller does not implement
cryptography. It controls selection rules.
"""


from dataclasses import dataclass, field

from typing import List, Dict

import hashlib

import json





@dataclass
class SecurityPolicy:
    """
    Defines HAF-PQC security policy.
    """


    security_level: str


    allowed_algorithms: List[str]


    max_components: int


    risk_threshold: float


    require_diversity: bool


    allow_classical_component: bool


    version: str = "1.0"





class CryptoPolicyController:
    """
    Policy management layer of HAF-PQC.
    """



    def __init__(

        self,

        security_level="high",

        risk_threshold=0.3,

        max_components=3

    ):


        self.policy = SecurityPolicy(

            security_level=
            security_level,


            allowed_algorithms=[

                "ML-KEM-768",

                "HQC",

                "Classic-McEliece",

                "X25519"

            ],


            max_components=
            max_components,


            risk_threshold=
            risk_threshold,


            require_diversity=True,


            allow_classical_component=True

        )





    # ==================================================
    # Policy Export
    # ==================================================

    def get_policy(self):

        return {

            "security_level":

            self.policy.security_level,


            "allowed_algorithms":

            self.policy.allowed_algorithms,


            "max_components":

            self.policy.max_components,


            "risk_threshold":

            self.policy.risk_threshold,


            "require_diversity":

            self.policy.require_diversity,


            "allow_classical_component":

            self.policy.allow_classical_component,


            "version":

            self.policy.version

        }





    # ==================================================
    # Policy Hash
    # ==================================================

    def generate_policy_hash(self):

        """
        Creates deterministic policy identifier.

        Used by PBSF transcript binding.
        """


        serialized = json.dumps(

            self.get_policy(),

            sort_keys=True

        ).encode()



        return hashlib.sha3_256(

            serialized

        ).hexdigest()





    # ==================================================
    # Algorithm Validation
    # ==================================================

    def validate_algorithm(

        self,

        algorithm: str

    ):


        return (

            algorithm

            in

            self.policy.allowed_algorithms

        )





    # ==================================================
    # Configuration Validation
    # ==================================================

    def validate_configuration(

        self,

        configuration: List[str]

    ):


        result = {


            "valid":

            True,


            "violations":

            []

        }



        # Check component count

        if len(configuration) > self.policy.max_components:


            result["valid"] = False


            result["violations"].append(

                "Maximum component limit exceeded"

            )



        # Check algorithm availability

        for algorithm in configuration:


            if not self.validate_algorithm(

                algorithm

            ):


                result["valid"] = False


                result["violations"].append(

                    f"Algorithm not allowed: {algorithm}"

                )



        # Diversity requirement

        if self.policy.require_diversity:


            if len(configuration) > 1:


                families = self.classify_families(

                    configuration

                )


                if len(families) < 2:


                    result["valid"] = False


                    result["violations"].append(

                        "Insufficient algorithm diversity"

                    )



        return result





    # ==================================================
    # Family Classification
    # ==================================================

    def classify_families(

        self,

        configuration: List[str]

    ):


        families = set()



        mapping = {


            "ML-KEM-768":

            "Lattice",


            "HQC":

            "Code",


            "Classic-McEliece":

            "Code",


            "X25519":

            "ECC"

        }



        for algorithm in configuration:


            if algorithm in mapping:


                families.add(

                    mapping[algorithm]

                )



        return families





    # ==================================================
    # Risk Validation
    # ==================================================

    def validate_risk(

        self,

        risk_score: float

    ):


        """

        Checks whether selected configuration
        satisfies risk budget.

        """


        return (

            risk_score

            <=

            self.policy.risk_threshold

        )





    # ==================================================
    # Downgrade Protection
    # ==================================================

    def prevent_downgrade(

        self,

        old_configuration:

        List[str],


        new_configuration:

        List[str]

    ):


        """
        Prevents replacing a strong
        configuration with a weaker one.
        """


        old_score = len(

            self.classify_families(

                old_configuration

            )

        )


        new_score = len(

            self.classify_families(

                new_configuration

            )

        )


        if new_score < old_score:


            return False



        return True





    # ==================================================
    # Policy Update
    # ==================================================

    def update_policy(

        self,

        **kwargs

    ):


        """

        Controlled policy modification.

        """


        for key,value in kwargs.items():


            if hasattr(

                self.policy,

                key

            ):


                setattr(

                    self.policy,

                    key,

                    value

                )



        return self.get_policy()