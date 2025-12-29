def assess_hazards(detected_objects):
    """
    Assess hazards and prioritize them.
    Returns a list of tuples: (hazard_message, risk_score)
    """
    hazard_rules = {
        "staircase": (10, "Warning: stairs ahead!"),
        "vehicle": (9, "Caution: vehicle nearby!"),
        "wet floor": (7, "Alert: slippery surface!"),
        "pole": (5, "Caution: obstacle at head level!"),
        "open drain": (8, "Danger: open drain ahead!")
    }

    warnings = []

    for obj in detected_objects:
        if obj in hazard_rules:
            score, msg = hazard_rules[obj]
            warnings.append((msg, score))

    warnings.sort(key=lambda x: x[1], reverse=True)

    if not warnings:
        warnings.append(("No immediate hazards detected.", 0))

    return warnings
