import pytest
from traffic_fine import speeding_fine, license_action, total_penalty

#Example test cases:
def test_no_speeding():
    assert speeding_fine(50, 60, "city") == 0

def test_clean_record():
    assert license_action(2, False, False) == "none"

# --- speeding_fine: no speeding (equality boundary) ---
def test_no_speeding_at_limit():
    assert speeding_fine(60, 60, "city") == 0

# --- speeding_fine: school zone, all excess tiers ---
def test_school_low_excess():
    assert speeding_fine(70, 60, "school") == 2000

def test_school_mid_excess():
    assert speeding_fine(85, 60, "school") == 4000

def test_school_high_excess():
    assert speeding_fine(110, 60, "school") == 6000

# --- speeding_fine: highway zone, all excess tiers ---
def test_highway_low_excess():
    assert speeding_fine(70, 60, "highway") == 1000

def test_highway_mid_excess():
    assert speeding_fine(85, 60, "highway") == 2000

def test_highway_high_excess():
    assert speeding_fine(110, 60, "highway") == 3000

# --- speeding_fine: other zone, all excess tiers ---
def test_other_low_excess():
    assert speeding_fine(70, 60, "city") == 500

def test_other_mid_excess():
    assert speeding_fine(85, 60, "city") == 1000

def test_other_high_excess():
    assert speeding_fine(110, 60, "city") == 1500

# --- speeding_fine: exact thresholds ---
def test_excess_exactly_20():
    assert speeding_fine(80, 60, "city") == 500

def test_excess_exactly_40():
    assert speeding_fine(100, 60, "city") == 1000

# --- license_action: all branches ---
def test_license_none():
    assert license_action(2, False, False) == "none"

def test_license_notice():
    assert license_action(5, False, False) == "notice"

def test_license_warning():
    assert license_action(9, False, False) == "warning"

def test_license_suspend_repeat():
    assert license_action(9, False, True) == "suspend"

def test_license_suspend_points():
    assert license_action(13, False, False) == "suspend"

def test_license_revoke_commercial():
    assert license_action(13, True, False) == "revoke"

# --- license_action: boundaries ---
def test_license_points_exactly_4():
    assert license_action(4, False, False) == "notice"

def test_license_points_exactly_8():
    assert license_action(8, False, False) == "warning"

def test_license_points_exactly_12():
    assert license_action(12, False, False) == "suspend"

# --- total_penalty ---
def test_total_empty():
    assert total_penalty([]) == 0

def test_total_normal():
    assert total_penalty([100, 200]) == 300

def test_total_cap():
    assert total_penalty([6000, 6000]) == 10000

def test_total_under_cap():
    assert total_penalty([4000, 4000]) == 8000

def test_total_negative_raises():
    with pytest.raises(ValueError):
        total_penalty([100, -1])

def test_total_exact_cap():
    assert total_penalty([5000, 5000]) == 10000