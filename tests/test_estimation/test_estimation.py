from estimation.estimation import calculate_estimate

def test_calculate_estimate():
    assert(calculate_estimate(1,2,3)) == 2
    assert(calculate_estimate(1,2,3)) != 3
