from models import *
from fitness_assignment.data_generator import generate_fitness_data

profile, observation_data = generate_fitness_data()

#testing scenarios
#profile, observation_data = generate_fitness_data(scenario="resting", seed=1)
#profile, observation_data = generate_fitness_data(scenario="moderate_activity", seed=1)
#profile, observation_data = generate_fitness_data(scenario="high_activity", seed=1)
#profile, observation_data = generate_fitness_data(scenario="recovery", seed=1)
#profile, observation_data = generate_fitness_data(scenario="poor_quality", seed=1)

participant = Participant(
    profile["participant_id"],
    profile["baseline_heart_rate"],
    profile["baseline_skin_response"],
    profile["baseline_temperature"]
)

observations = []

for data in observation_data:
    observation = Observation(
        data["timestamp"],
        data["heart_rate"],
        data["skin_response"],
        data["temperature"],
        data["activity_level"],
        data["signal_quality"]
    )
    observations.append(observation)

session = FitnessSession(participant, observations)
analyzer = FitnessAnalyzer(session)

print("Summary:", analyzer.calculate_summary())
print("Classification:", analyzer.classify())