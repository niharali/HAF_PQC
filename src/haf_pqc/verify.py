"""
verify.py

Final validation module for HAF-PQC.

Checks:

1. Project structure
2. Experiment outputs
3. Dataset integrity
4. Figures
5. Tables
6. Metadata

Used before final ZIP packaging.
"""


from pathlib import Path

import json

import pandas as pd





class HAFPQCVerifier:
    """
    Validates HAF-PQC research package.
    """



    def __init__(

        self,

        root="."

    ):


        self.root = Path(root)


        self.results = Path(

            "results"

        )


        self.figures = Path(

            "figures"

        )


        self.report = {}





    # =================================================
    # Directory Validation
    # =================================================

    def check_directories(self):


        print(

            "\nChecking directories..."

        )


        required = [

            "src/haf_pqc",

            "results",

            "results/raw",

            "results/processed",

            "figures",

            "docs",

            "tests"

        ]



        status = {}



        for folder in required:


            exists = Path(folder).exists()


            status[folder] = exists



        self.report[

            "directories"

        ] = status



        return status





    # =================================================
    # Result File Validation
    # =================================================

    def check_result_files(self):


        print(

            "\nChecking result files..."

        )


        required_files = [

            "results/raw/session_metrics.csv",

            "results/raw/security_simulation.csv",

            "results/raw/recovery_metrics.csv",

            "results/processed/statistical_summary.json",

            "results/processed/ablation_results.csv",

            "results/final_metadata.json"

        ]



        status = {}



        for file in required_files:


            status[file] = Path(file).exists()



        self.report[

            "result_files"

        ] = status



        return status





    # =================================================
    # CSV Validation
    # =================================================

    def validate_csv(

        self,

        filename

    ):


        try:


            df = pd.read_csv(

                filename

            )


            return {

                "valid":

                True,


                "rows":

                len(df),


                "columns":

                list(df.columns)

            }



        except Exception as e:


            return {

                "valid":

                False,


                "error":

                str(e)

            }





    def check_csv_integrity(self):


        print(

            "\nChecking CSV integrity..."

        )


        files = [

            "results/raw/session_metrics.csv",

            "results/raw/security_simulation.csv",

            "results/processed/ablation_results.csv"

        ]


        validation = {}



        for file in files:


            if Path(file).exists():


                validation[file] = (

                    self.validate_csv(file)

                )


        self.report[

            "csv_validation"

        ] = validation



        return validation





    # =================================================
    # Figure Validation
    # =================================================

    def check_figures(self):


        print(

            "\nChecking generated figures..."

        )


        formats = [

            "png",

            "svg",

            "pdf"

        ]


        figure_status = {}



        for fmt in formats:


            folder = (

                self.figures /

                fmt

            )


            if folder.exists():


                files = list(

                    folder.glob(

                        "*."+fmt

                    )

                )


                figure_status[fmt] = {


                    "count":

                    len(files),


                    "files":

                    [

                        f.name

                        for f in files

                    ]

                }



        self.report[

            "figures"

        ] = figure_status



        return figure_status





    # =================================================
    # Table Validation
    # =================================================

    def check_tables(self):


        print(

            "\nChecking manuscript tables..."

        )


        table_folder = Path(

            "results/processed/tables"

        )


        result = {}



        if table_folder.exists():


            tables = list(

                table_folder.glob(

                    "*.csv"

                )

            )


            result = {


                "count":

                len(tables),


                "files":

                [

                    t.name

                    for t in tables

                ]

            }


        self.report[

            "tables"

        ] = result



        return result





    # =================================================
    # Metadata Validation
    # =================================================

    def check_metadata(self):


        print(

            "\nChecking metadata..."

        )


        file = Path(

            "results/final_metadata.json"

        )


        if not file.exists():


            self.report[

                "metadata"

            ] = False


            return False



        try:


            with open(file) as f:


                data = json.load(f)



            self.report[

                "metadata"

            ] = {


                "valid":

                True,


                "keys":

                list(data.keys())

            }


            return True



        except Exception:


            self.report[

                "metadata"

            ] = False


            return False





    # =================================================
    # Complete Verification
    # =================================================

    def run(self):


        print(

            """

================================

 HAF-PQC FINAL VERIFICATION

================================

"""

        )



        self.check_directories()


        self.check_result_files()


        self.check_csv_integrity()


        self.check_figures()


        self.check_tables()


        self.check_metadata()



        output = Path(

            "results/verification_report.json"

        )


        with open(

            output,

            "w"

        ) as file:


            json.dump(

                self.report,

                file,

                indent=4

            )



        print(

            """

Verification completed.

Report:

results/verification_report.json

"""

        )


        return self.report





def verify():


    checker = HAFPQCVerifier()


    return checker.run()