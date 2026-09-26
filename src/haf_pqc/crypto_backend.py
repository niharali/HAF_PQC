"""
crypto_backend.py

Cryptographic backend abstraction layer for HAF-PQC.

Responsibilities:
- Detect available PQC algorithms
- Provide unified KEM interface
- Maintain reproducibility metadata
- Avoid simulated cryptographic outputs

Supported backends:
- liboqs-python (PQC)
- cryptography (X25519)

No fake cryptographic operations are permitted.
"""

from dataclasses import dataclass
import platform
import sys
import time


@dataclass
class AlgorithmInfo:
    name: str
    family: str
    available: bool
    backend: str
    notes: str = ""


class PQCBackend:
    """
    Unified cryptographic backend manager.
    """

    def __init__(self):
        self.algorithms = {}
        self._detect_environment()
        self.detect_algorithms()


    def _detect_environment(self):
        """
        Collect execution environment information.
        """

        self.environment = {
            "python_version": sys.version,
            "platform": platform.platform()
        }


    def detect_algorithms(self):
        """
        Detect available cryptographic algorithms.

        Returns:
            Dictionary containing algorithm availability.
        """

        self.algorithms = {

            "ML-KEM-768": AlgorithmInfo(
                name="ML-KEM-768",
                family="Lattice",
                available=False,
                backend="liboqs",
                notes=""
            ),

            "HQC": AlgorithmInfo(
                name="HQC",
                family="Code-based",
                available=False,
                backend="liboqs",
                notes=""
            ),

            "Classic-McEliece": AlgorithmInfo(
                name="Classic-McEliece",
                family="Code-based",
                available=False,
                backend="liboqs",
                notes=""
            ),

            "X25519": AlgorithmInfo(
                name="X25519",
                family="Elliptic Curve",
                available=False,
                backend="cryptography",
                notes=""
            )
        }


        # Detect liboqs
        try:
            import oqs

            enabled = oqs.get_enabled_KEM_mechanisms()

            for alg in [
                "ML-KEM-768",
                "HQC",
                "Classic-McEliece"
            ]:

                if alg in enabled:
                    self.algorithms[alg].available = True


        except Exception as e:

            for alg in [
                "ML-KEM-768",
                "HQC",
                "Classic-McEliece"
            ]:

                self.algorithms[alg].notes = (
                    f"liboqs unavailable: {str(e)}"
                )


        # Detect cryptography X25519

        try:

            from cryptography.hazmat.primitives.asymmetric import x25519

            self.algorithms[
                "X25519"
            ].available = True


        except Exception as e:

            self.algorithms[
                "X25519"
            ].notes = str(e)


        return self.get_status()



    def get_status(self):
        """
        Return algorithm availability report.
        """

        result = {}

        for name, info in self.algorithms.items():

            result[name] = {
                "family": info.family,
                "available": info.available,
                "backend": info.backend,
                "notes": info.notes
            }

        return result



    def available_algorithms(self):

        return [
            name
            for name, info
            in self.algorithms.items()
            if info.available
        ]



    def benchmark_placeholder(self, algorithm):
        """
        Timing wrapper.

        Actual cryptographic operations
        will be connected in the next layer.
        """

        start = time.perf_counter()

        # Real operation will be inserted here.

        end = time.perf_counter()

        return {
            "algorithm": algorithm,
            "latency_seconds": end - start
        }