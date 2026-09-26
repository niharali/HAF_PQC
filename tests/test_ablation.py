"""
Ablation study tests
"""


from src.haf_pqc.ablation import (
    AblationStudy
)





def test_ablation_initialization():

    study = AblationStudy()

    assert study is not None





def test_ablation_configuration_generation():

    study = AblationStudy()


    configs = study.generate_configurations()


    assert len(configs) > 0





def test_ablation_contains_baseline():

    study = AblationStudy()


    configs = study.generate_configurations()


    names = [

        item["name"]

        for item in configs

    ]


    assert "Full HAF-PQC" in names