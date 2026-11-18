# Name: Ishika Jain | SRN: PES2UG24AM067
# Test cases to reach 90%+ branch coverage of credit_card_rewards.py.
# Every if / elif is tested both True and False, every part of the
# "and" / "or" conditions is tested on its own, and boundary values are checked.
import pytest
from credit_card_rewards import reward_points, late_payment_fee, card_status


# ---- reward_points ----
def test_unknown_tier():
    with pytest.raises(ValueError):
        reward_points("silver", 1000, "grocery", False)

def test_zero_amount():
    with pytest.raises(ValueError):
        reward_points("gold", 0, "grocery", False)

def test_negative_amount():
    with pytest.raises(ValueError):
        reward_points("gold", -500, "grocery", False)

def test_fuel_gives_no_points():
    assert reward_points("platinum", 5000, "fuel", True) == 0

def test_classic_grocery_weekday():                 # no double, no bonus
    assert reward_points("classic", 1000, "grocery", False) == 10

def test_amount_below_100_gives_zero():             # boundary: 99 // 100 = 0
    assert reward_points("platinum", 99, "grocery", False) == 0

def test_amount_exactly_100():
    assert reward_points("gold", 100, "grocery", False) == 2

def test_dining_doubles_points():                   # first half of the "or"
    assert reward_points("gold", 1000, "dining", False) == 40

def test_travel_doubles_points():                   # second half of the "or"
    assert reward_points("platinum", 1000, "travel", False) == 80

def test_weekend_bonus_for_gold():                  # weekend and not classic
    assert reward_points("gold", 1000, "grocery", True) == 70

def test_no_weekend_bonus_for_classic():            # weekend but classic
    assert reward_points("classic", 1000, "grocery", True) == 10

def test_platinum_travel_weekend():                 # everything together
    assert reward_points("platinum", 2000, "travel", True) == 2000 // 100 * 4 * 2 + 50


# ---- late_payment_fee ----
def test_paid_on_time():                            # days_late <= 0
    assert late_payment_fee(5000, 0) == 0

def test_negative_days():
    assert late_payment_fee(5000, -3) == 0

def test_nothing_outstanding():                     # outstanding <= 0, days_late > 0
    assert late_payment_fee(0, 10) == 0

def test_outstanding_exactly_1000():                # boundary of first band
    assert late_payment_fee(1000, 10) == 100

def test_outstanding_1001():
    assert late_payment_fee(1001, 10) == 500

def test_outstanding_exactly_10000():               # boundary of second band
    assert late_payment_fee(10000, 10) == 500

def test_outstanding_10001():
    assert late_payment_fee(10001, 10) == 1000

def test_exactly_30_days_late():                    # 30 is not > 30
    assert late_payment_fee(800, 30) == 100

def test_31_days_late():                            # extra 750
    assert late_payment_fee(800, 31) == 850

def test_large_outstanding_very_late():
    assert late_payment_fee(20000, 60) == 1750


# ---- card_status ----
def test_frozen_overrides_everything():
    assert card_status(99, 5, True) == "frozen"

def test_blocked_at_3_missed():
    assert card_status(10, 3, False) == "blocked"

def test_two_missed_is_watch():                     # second half of the "or"
    assert card_status(10, 2, False) == "watch"

def test_one_missed_is_watch():
    assert card_status(10, 1, False) == "watch"

def test_over_limit_risk():
    assert card_status(95, 0, False) == "over limit risk"

def test_utilisation_exactly_90_is_watch():         # 90 is not > 90
    assert card_status(90, 0, False) == "watch"

def test_high_utilisation_is_watch():               # first half of the "or"
    assert card_status(50, 0, False) == "watch"

def test_utilisation_exactly_30_is_good():          # 30 is not > 30
    assert card_status(30, 0, False) == "good"

def test_good():
    assert card_status(10, 0, False) == "good"
