from analysis import check_validity, calculate_average, calculate_min_max, compare_to_baseline
from models import Observation

def test_calculations():
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_min_max([10, 20, 30]) == (10, 30)
    assert compare_to_baseline(60, 75) == 15

def test_validity():
    valid = Observation(1, 80, 2.0, 32.5, 0.5, 0.9)
    invalid = Observation(1, 250, 2.0, 32.5, 0.5, 0.9)

    assert check_validity(valid)
    assert not check_validity(invalid)

if __name__ == "__main__":
    test_calculations()
    test_validity()
    print("All tests passed.")