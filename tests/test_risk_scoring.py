from src.risk_scoring import calculate_risk


def test_high_risk():
    assert calculate_risk(3, 2) == "High"


def test_medium_risk():
    assert calculate_risk(1, 1) == "Medium"


def test_low_risk():
    assert calculate_risk(0, 1) == "Low"


def test_chronic_condition_rule():
    assert calculate_risk(0, 3) == "Medium"