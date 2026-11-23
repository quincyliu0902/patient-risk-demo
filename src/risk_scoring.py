def calculate_risk(ed_visits, chronic_conditions):
    """
    Assign a patient risk category using simple rules.

    Parameters
    ----------
    ed_visits : int
        Number of ED visits in the past 6 months.
    chronic_conditions : int
        Number of chronic conditions.

    Returns
    -------
    str
        High, Medium, or Low.
    """
    if ed_visits >= 2:
        return "High"
    elif ed_visits >= 1 or chronic_conditions >= 2:
        return "Medium"
    else:
        return "Low"