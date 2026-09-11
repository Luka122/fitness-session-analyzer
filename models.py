from analysis import check_validity, calculate_average, calculate_min_max, compare_to_baseline

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
    def __init__(self, participant, observations):
        self.participant = participant
        self.observations = observations

class FitnessAnalyzer:
    def __init__(self, session):
        self.session = session
        self.valid_observations = []

        for observation in session.observations:
            if check_validity(observation):
                self.valid_observations.append(observation)

    def calculate_summary(self):
        heart_rates = []
        skin_responses = []
        temperatures = []
        activity_levels = []
        signal_qualities = []

        for observation in self.valid_observations:
            heart_rates.append(observation.heart_rate)
            skin_responses.append(observation.skin_response)
            temperatures.append(observation.temperature)
            activity_levels.append(observation.activity_level)
            signal_qualities.append(observation.signal_quality)

        session_avg_heart_rate = calculate_average(heart_rates)
        base_session_comparison = compare_to_baseline(self.session.participant.baseline_heart_rate, session_avg_heart_rate)

        return {
            "heart_rate_average": calculate_average(heart_rates),
            "heart_rate_min_max": calculate_min_max(heart_rates),
            "skin_response_average": calculate_average(skin_responses),
            "skin_response_min_max": calculate_min_max(skin_responses),
            "temperature_average": calculate_average(temperatures),
            "temperature_min_max": calculate_min_max(temperatures),
            "activity_level_average": calculate_average(activity_levels),
            "activity_level_min_max": calculate_min_max(activity_levels),
            "signal_quality_average": calculate_average(signal_qualities),
            "signal_quality_min_max": calculate_min_max(signal_qualities),
            "session_avg_heart_rate": session_avg_heart_rate,
            "base_session_comparison": base_session_comparison,
            }

    def classify(self):
        if len(self.valid_observations) < 3:
            return "insufficient_data"

        summary = self.calculate_summary()
        activity_level_average = summary["activity_level_average"]

        first_observation = self.valid_observations[0]
        last_observation = self.valid_observations[-1]

        if last_observation.heart_rate <= first_observation.heart_rate * 0.9:
            return "recovering"

        if activity_level_average <= 0.25:
            return "resting"
        elif activity_level_average <= 0.65:
            return "moderate activity"
        else:
            return "high activity"