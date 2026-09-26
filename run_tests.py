"""
run_tests.py

HAF-PQC complete test runner.

Executes:

- unit tests
- integration tests
- validation tests

Uses pytest.
"""


import subprocess

import sys





def run_tests():


    print(

        """

=================================

 HAF-PQC TEST EXECUTION

=================================

"""

    )



    command = [

        sys.executable,

        "-m",

        "pytest",

        "-v",

        "--tb=short"

    ]



    result = subprocess.run(

        command

    )



    if result.returncode == 0:


        print(

            """

=================================

 ALL TESTS PASSED

=================================

"""

        )


    else:


        print(

            """

=================================

 TEST FAILURE DETECTED

=================================

"""

        )



    return result.returncode





if __name__ == "__main__":


    exit_code = run_tests()


    sys.exit(

        exit_code

    )