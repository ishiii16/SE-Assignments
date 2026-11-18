# Name: Ishika Jain | SRN: PES2UG24AM067
# Hypothesis fuzz tests: each function gets random text (and None) and must
# not crash. If it returns something, the result must also make sense.
from hypothesis import given, strategies as st
from credit_card_rewards_parser import mask_card_number, parse_transaction, parse_statement_total


@given(st.text() | st.none())
def test_mask_card_number_no_crash(s):
    try:
        result = mask_card_number(s)
    except Exception as e:
        assert False, f"mask_card_number crashed with: {e!r}"
    # either rejected, or 12 stars followed by exactly 4 digits
    if result is not None:
        assert result[:12] == "*" * 12 and len(result) == 16 and result[12:].isdigit()


@given(st.text() | st.none())
def test_parse_transaction_no_crash(s):
    try:
        result = parse_transaction(s)
    except Exception as e:
        assert False, f"parse_transaction crashed with: {e!r}"
    # either rejected, or (non-empty category, positive whole amount)
    if result is not None:
        category, amount = result
        assert category != "" and isinstance(amount, int) and amount > 0


@given(st.text() | st.none())
def test_parse_statement_total_no_crash(s):
    try:
        result = parse_statement_total(s)
    except Exception as e:
        assert False, f"parse_statement_total crashed with: {e!r}"
    # either rejected, or a whole number that is not negative
    if result is not None:
        assert isinstance(result, int) and result >= 0
