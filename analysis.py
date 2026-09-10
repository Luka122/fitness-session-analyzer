def check_validity(observation): # Assumptions in README.md
    # Check if required observations are present
    required = ["timestamp", "heart_rate", "skin_response", "temperature", "activity_level", "signal_quality"]

    for key in required:
        if key not in observation:
            return False

    if observation["heart_rate"] < 30 or observation["heart_rate"] > 220:
        return False

    if observation["heart_rate"] < 30 or observation["heart_rate"] > 220:
        return False

    if observation["skin_response"] < 0:
        return False

    if observation["temperature"] < 25 or observation["temperature"] > 42:
        return False

    if observation["activity_level"] < 0 or observation["activity_level"] > 1:
        return False

    if observation["signal_quality"] < 0 or observation["signal_quality"] > 1:
        return False

    return True

def calculate_average(values):
    if values:
        return sum(values) / len(values)
    else:
        return False

def calculate_min_max(values):
    if values:
        return min(values), max(values)
    else:
        return False

def compare_to_baseline(baseline_heart_rate, session_heart_rate):
        return session_heart_rate - baseline_heart_rate
