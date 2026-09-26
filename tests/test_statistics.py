"""
Statistics module tests
"""


from src.haf_pqc.statistics import (
    StatisticalAnalyzer
)





def test_statistics_initialization():

    analyzer = StatisticalAnalyzer()

    assert analyzer is not None





def test_mean_calculation():

    analyzer = StatisticalAnalyzer()


    values = [

        10,

        20,

        30

    ]


    result = analyzer.mean(values)


    assert result == 20





def test_median_calculation():

    analyzer = StatisticalAnalyzer()


    values = [

        10,

        20,

        30

    ]


    result = analyzer.median(values)


    assert result == 20





def test_standard_deviation():

    analyzer = StatisticalAnalyzer()


    values = [

        10,

        20,

        30

    ]


    result = analyzer.standard_deviation(values)


    assert result > 0





def test_summary_generation():

    analyzer = StatisticalAnalyzer()


    values = [

        1,

        2,

        3,

        4,

        5

    ]


    result = analyzer.summarize(values)


    assert "mean" in result

    assert "median" in result