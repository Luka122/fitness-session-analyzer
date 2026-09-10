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
    def __init__(self, participant, observation):
        self.participant = participant
        self.observation = observation

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
            }