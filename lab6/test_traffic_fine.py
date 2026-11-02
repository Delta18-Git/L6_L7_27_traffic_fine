import pytest
from traffic_fine import speeding_fine, license_action, total_penalty

#Example test cases:
def test_no_speeding():
    assert speeding_fine(50, 60, "city") == 0

def test_clean_record():
    assert license_action(2, False, False) == "none"

# Code coverage: exercise every line of speeding_fine
def test_school_high_excess():
    assert speeding_fine(110, 60, "school") == 6000

def test_highway_mid_excess():
    assert speeding_fine(85, 60, "highway") == 2000

def test_other_low_excess():
    assert speeding_fine(70, 60, "city") == 500

# Code coverage: exercise every line of license_action
def test_license_revoke_commercial():
    assert license_action(13, True, False) == "revoke"

def test_license_suspend_points():
    assert license_action(13, False, False) == "suspend"

def test_license_warning():
    assert license_action(9, False, False) == "warning"

def test_license_suspend_repeat():
    assert license_action(9, False, True) == "suspend"

def test_license_notice():
    assert license_action(5, False, False) == "notice"

# Code coverage: exercise every line of total_penalty
def test_total_normal():
    assert total_penalty([100, 200]) == 300

def test_total_cap():
    assert total_penalty([6000, 6000]) == 10000

def test_total_negative_raises():
    with pytest.raises(ValueError):
        total_penalty([100, -1])