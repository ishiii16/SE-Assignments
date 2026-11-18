# Name: Ishika Jain | SRN: PES2UG24AM067
# Test cases to reach 90%+ line (code) coverage of credit_card_rewards.py
import pytest
from credit_card_rewards import reward_points, late_payment_fee, card_status


# ---- reward_points ----
def test_classic_grocery():
    assert reward_points("classic", 1000, "grocery", False) == 10

def test_unknown_tier():
    with pytest.raises(ValueError):
        reward_points("silver", 1000, "grocery", False)

def test_zero_amount():
    with pytest.raises(ValueError):
        reward_points("gold", 0, "grocery", False)

def test_fuel_gives_no_points():
    assert reward_points("platinum", 5000, "fuel", True) == 0

def test_gold_dining_weekend():
    # 2000 // 100 * 2 = 40, doubled for dining = 80, +50 weekend bonus = 130
    assert reward_points("gold", 2000, "dining", True) == 130


# ---- late_payment_fee ----
def test_paid_on_time():
    assert late_payment_fee(5000, 0) == 0

def test_small_outstanding():
    assert late_payment_fee(800, 10) == 100

def test_medium_outstanding_very_late():
    assert late_payment_fee(5000, 45) == 500 + 750

def test_large_outstanding():
    assert late_payment_fee(20000, 5) == 1000


# ---- card_status ----
def test_frozen():
    assert card_status(10, 0, True) == "frozen"

def test_blocked():
    assert card_status(10, 3, False) == "blocked"

def test_over_limit_risk():
    assert card_status(95, 0, False) == "over limit risk"

def test_watch():
    assert card_status(50, 0, False) == "watch"

def test_good():
    assert card_status(10, 0, False) == "good"
