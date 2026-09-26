"""
reproducibility.py

Reproducibility metadata manager
for HAF-PQC.

Records:

- OS information
- Python version
- CPU information
- Package versions
- Git commit
- Random seeds
- Experiment configuration

Designed for SCI reproducibility.
"""


from pathlib import Path

import json

import platform

import sys

import subprocess

import importlib.metadata

import hashlib

import shutil





class ReproducibilityManager:
    """
    Collects experiment reproducibility metadata.
    """



    def __init__(

        self,

        output_file=
        "results/experiment_metadata.json"

    ):


        self.output_file = Path(

            output_file

        )


        self.output_file.parent.mkdir(

            parents=True,

            exist_ok=True

        )


        self.metadata = {}





    # ==========================================
    # System Information
    # ==========================================

    def collect_system_information(self):


        self.metadata["system"] = {


            "operating_system":

            platform.platform(),


            "machine":

            platform.machine(),


            "processor":

            platform.processor(),


            "python_version":

            sys.version,


            "python_executable":

            sys.executable


        }


        return self.metadata["system"]





    # ==========================================
    # CPU Information
    # ==========================================

    def collect_hardware_information(self):


        hardware = {}


        try:


            import psutil


            hardware["cpu_count"] = (

                psutil.cpu_count()

            )


            hardware["memory_gb"] = round(

                psutil.virtual_memory().total

                /

                (1024**3),

                2

            )


        except Exception:


            hardware["cpu_count"] = (

                "unavailable"

            )


            hardware["memory_gb"] = (

                "unavailable"

            )



        self.metadata["hardware"] = hardware



        return hardware





    # ==========================================
    # Dependencies
    # ==========================================

    def collect_dependencies(

        self,

        packages=None

    ):


        if packages is None:


            packages = [

                "numpy",

                "pandas",

                "scipy",

                "matplotlib",

                "cryptography",

                "pytest",

                "liboqs-python"

            ]



        versions = {}



        for package in packages:


            try:


                versions[package] = (

                    importlib.metadata.version(

                        package

                    )

                )


            except Exception:


                versions[package] = (

                    "not_installed"

                )



        self.metadata["dependencies"] = versions



        return versions





    # ==========================================
    # Git Information
    # ==========================================

    def collect_git_information(self):


        git_path = shutil.which(

            "git"

        )



        if git_path is None:


            self.metadata["git_commit"] = (

                "git_not_installed"

            )


            return self.metadata["git_commit"]




        try:


            check = subprocess.run(

                [

                    "git",

                    "rev-parse",

                    "--is-inside-work-tree"

                ],


                capture_output=True,

                text=True,

                timeout=5

            )


            if check.returncode != 0:


                self.metadata["git_commit"] = (

                    "not_available"

                )


                return "not_available"



            commit = subprocess.run(

                [

                    "git",

                    "rev-parse",

                    "HEAD"

                ],


                capture_output=True,

                text=True,

                timeout=5

            )


            self.metadata["git_commit"] = (

                commit.stdout.strip()

            )



        except Exception:


            self.metadata["git_commit"] = (

                "not_available"

            )



        return self.metadata["git_commit"]





    # ==========================================
    # Seed
    # ==========================================

    def record_seed(

        self,

        seed

    ):


        self.metadata["random_seed"] = seed





    # ==========================================
    # Configuration
    # ==========================================

    def record_configuration(

        self,

        configuration

    ):


        self.metadata["configuration"] = configuration





    # ==========================================
    # File Checksum
    # ==========================================

    def calculate_checksum(

        self,

        filename

    ):


        sha256 = hashlib.sha256()



        with open(

            filename,

            "rb"

        ) as file:


            for chunk in iter(

                lambda:

                file.read(4096),

                b""

            ):


                sha256.update(

                    chunk

                )



        return sha256.hexdigest()





    # ==========================================
    # Save
    # ==========================================

    def save(self):


        with open(

            self.output_file,

            "w"

        ) as file:


            json.dump(

                self.metadata,

                file,

                indent=4

            )


        print(

            f"Metadata saved: {self.output_file}"

        )


        return self.output_file