"""
Reproducibility tests
"""


from src.haf_pqc.reproducibility import (
    ReproducibilityManager
)





def test_reproducibility_initialization(tmp_path):


    file = tmp_path / "metadata.json"


    manager = ReproducibilityManager(

        output_file=file

    )


    assert manager is not None





def test_system_information():

    manager = ReproducibilityManager()


    result = (

        manager.collect_system_information()

    )


    assert "python_version" in result





def test_seed_recording():

    manager = ReproducibilityManager()


    manager.record_seed(

        42

    )


    assert (

        manager.metadata["random_seed"]

        ==

        42

    )





def test_configuration_recording():

    manager = ReproducibilityManager()


    manager.record_configuration(

        {

            "test":

            True

        }

    )


    assert (

        manager.metadata["configuration"]["test"]

        is True

    )