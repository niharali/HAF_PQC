"""
recovery_engine.py

Operational recovery controller for HAF-PQC.

Works with:
- CIR
- FARE
- Policy Controller

Responsibilities:

- incident handling
- secure reconfiguration
- recovery metrics
- downgrade prevention

Recovery is policy-driven.
It does not claim automatic detection
of cryptographic compromise.
"""



from dataclasses import dataclass

from typing import List, Dict

import time





@dataclass
class RecoveryMetric:

    incident_component: str

    old_configuration: List[str]

    new_configuration: List[str]

    old_epoch: int

    new_epoch: int

    recovery_time_ms: float

    successful: bool





class RecoveryEngine:
    """
    Executes constrained recovery workflow.
    """



    def __init__(

        self,

        cir=None,

        fare=None

    ):


        self.cir = cir

        self.fare = fare


        self.recovery_history = []





    # --------------------------------------------------
    # Incident Validation
    # --------------------------------------------------

    def validate_incident(

        self,

        component: str

    ) -> bool:


        """
        Checks whether recovery
        action is required.
        """


        if component is None:

            return False


        return True





    # --------------------------------------------------
    # Recovery Execution
    # --------------------------------------------------

    def recover(

        self,

        current_configuration:

        List[str],


        failed_component:

        str,


        replacement_candidates:

        List[str]

    ) -> RecoveryMetric:


        start = time.perf_counter()



        if not self.validate_incident(

            failed_component

        ):


            raise ValueError(

                "Invalid incident"

            )



        old_epoch = (

            self.cir.security_epoch

            if self.cir

            else 0

        )



        # Remove failed algorithm

        new_configuration = [

            item

            for item

            in current_configuration

            if item != failed_component

        ]



        # Add replacement

        for candidate in replacement_candidates:


            if candidate not in new_configuration:


                new_configuration.append(

                    candidate

                )


        # CIR update

        if self.cir:


            self.cir.blacklist_component(

                failed_component

            )


            new_epoch = (

                self.cir.increase_epoch()

            )


        else:


            new_epoch = old_epoch + 1





        # Validate downgrade

        successful = (

            len(new_configuration)

            >=

            len(current_configuration)

        )



        end = time.perf_counter()



        metric = RecoveryMetric(

            incident_component=

            failed_component,


            old_configuration=

            current_configuration,


            new_configuration=

            new_configuration,


            old_epoch=

            old_epoch,


            new_epoch=

            new_epoch,


            recovery_time_ms=

            (end-start)*1000,


            successful=

            successful

        )



        self.recovery_history.append(

            metric

        )


        return metric





    # --------------------------------------------------
    # Metrics Export
    # --------------------------------------------------

    def export_metrics(

        self,

        filename=

        "results/raw/recovery_metrics.csv"

    ):


        import csv


        with open(

            filename,

            "w",

            newline=""

        ) as file:


            writer = csv.writer(file)



            writer.writerow(

                [

                "component",

                "old_epoch",

                "new_epoch",

                "recovery_time_ms",

                "successful"

                ]

            )



            for item in self.recovery_history:


                writer.writerow(

                    [

                    item.incident_component,

                    item.old_epoch,

                    item.new_epoch,

                    item.recovery_time_ms,

                    item.successful

                    ]

                )
                