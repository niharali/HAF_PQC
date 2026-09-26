"""
baseline_models.py

Baseline comparison framework for HAF-PQC.

Contains:
- Classical baseline
- PQC single primitive baselines
- Static combinations
- Proposed adaptive HAF-PQC model

All measurements must come from actual backend execution.
"""


from dataclasses import dataclass
import time


@dataclass
class SessionResult:
    """
    Stores one cryptographic session result.
    """

    algorithm: str

    latency_ms: float

    communication_bytes: int

    success: bool

    metadata: dict



class BaselineModel:
    """
    Abstract baseline model.
    """


    name = "Base"


    def __init__(self, backend=None):

        self.backend = backend



    def run_session(self):

        raise NotImplementedError(
            "Each baseline must implement run_session()"
        )



    def measure(self, operation):

        start = time.perf_counter()

        result = operation()

        end = time.perf_counter()


        latency = (
            end-start
        ) * 1000


        return latency, result





class MLKEMBaseline(BaselineModel):

    name = "ML-KEM-768"


    def run_session(self):

        """
        ML-KEM only baseline.

        Real operation will call backend KEM.
        """

        latency, result = self.measure(
            lambda: True
        )


        return SessionResult(

            algorithm=self.name,

            latency_ms=latency,

            communication_bytes=0,

            success=result,

            metadata={
                "family":"Lattice",
                "mode":"single"
            }

        )





class HQCBaseline(BaselineModel):

    name="HQC"


    def run_session(self):

        latency, result = self.measure(
            lambda: True
        )


        return SessionResult(

            algorithm=self.name,

            latency_ms=latency,

            communication_bytes=0,

            success=result,

            metadata={
                "family":"Code-based",
                "mode":"single"
            }

        )





class ClassicMcElieceBaseline(BaselineModel):

    name="Classic-McEliece"


    def run_session(self):

        latency, result = self.measure(
            lambda: True
        )


        return SessionResult(

            algorithm=self.name,

            latency_ms=latency,

            communication_bytes=0,

            success=result,

            metadata={
                "family":"Code-based",
                "mode":"single"
            }

        )





class X25519PQCHybrid(BaselineModel):

    name="X25519+PQC"


    def run_session(self):

        latency, result = self.measure(
            lambda: True
        )


        return SessionResult(

            algorithm=self.name,

            latency_ms=latency,

            communication_bytes=0,

            success=result,

            metadata={
                "family":
                "Classical + PQC",

                "mode":
                "hybrid"
            }

        )





class StaticSameFamilyCombination(BaselineModel):

    name="Static-Same-Family"


    def run_session(self):

        latency, result = self.measure(
            lambda: True
        )


        return SessionResult(

            algorithm=self.name,

            latency_ms=latency,

            communication_bytes=0,

            success=result,

            metadata={
                "diversity":
                "low"
            }

        )





class StaticHeterogeneousPair(BaselineModel):

    name="Static-Heterogeneous-Pair"


    def run_session(self):

        latency, result = self.measure(
            lambda: True
        )


        return SessionResult(

            algorithm=self.name,

            latency_ms=latency,

            communication_bytes=0,

            success=result,

            metadata={
                "diversity":
                "medium"
            }

        )





class StaticHeterogeneousTriple(BaselineModel):

    name="Static-Heterogeneous-Triple"


    def run_session(self):

        latency, result = self.measure(
            lambda: True
        )


        return SessionResult(

            algorithm=self.name,

            latency_ms=latency,

            communication_bytes=0,

            success=result,

            metadata={
                "diversity":
                "high"
            }

        )





class StaticFallbackPolicy(BaselineModel):

    name="Static-Fallback"


    def run_session(self):

        latency, result = self.measure(
            lambda: True
        )


        return SessionResult(

            algorithm=self.name,

            latency_ms=latency,

            communication_bytes=0,

            success=result,

            metadata={
                "adaptive":
                False
            }

        )





class HAFPQCAdaptive(BaselineModel):

    """
    Proposed framework.

    Uses:
    - FARE selection
    - PBSF fusion
    - CIR recovery
    """


    name="HAF-PQC"


    def __init__(
        self,
        backend=None,
        selector=None,
        fusion=None,
        recovery=None
    ):

        super().__init__(backend)

        self.selector = selector

        self.fusion = fusion

        self.recovery = recovery




    def run_session(self):


        latency, result = self.measure(
            lambda: True
        )


        return SessionResult(

            algorithm=self.name,

            latency_ms=latency,

            communication_bytes=0,

            success=result,

            metadata={

                "adaptive":
                True,

                "components":
                [
                    "FARE",
                    "PBSF",
                    "CIR"
                ]

            }

        )





def get_all_baselines(backend=None):

    """
    Returns all evaluation models.
    """


    return [

        MLKEMBaseline(backend),

        HQCBaseline(backend),

        ClassicMcElieceBaseline(backend),

        X25519PQCHybrid(backend),

        StaticSameFamilyCombination(backend),

        StaticHeterogeneousPair(backend),

        StaticHeterogeneousTriple(backend),

        StaticFallbackPolicy(backend),

        HAFPQCAdaptive(backend)

    ]