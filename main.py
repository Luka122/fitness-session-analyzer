class Participant:
    def __init__(self, participant_id, baseline_heart_rate, baseline_skin_response, baseline_temperature):
        self.participant_id = participant_id
        self.baseline_heart_rate = baseline_heart_rate
        self.baseline_skin_response = baseline_skin_response
        self.baseline_temperature = baseline_temperature

class Observation:
    def __init__(self, timestamp, heart_rate, skin_response, temperature, activity_level, signal_quality):
        self.timestamp = timestamp
        self.heart_rate = heart_rate
        self.skin_response = skin_response
        self.temperature = temperature
        self.activity_level = activity_level
        self.signal_quality = signal_quality

class FitnessSession:
    def __init__(self, participant, observation):
        self.participant = participant
        self.observation = observation

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
