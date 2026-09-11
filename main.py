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

summary = analyzer.calculate_summary()

print("Summary:")

if summary["usable_observations"] == 0:
    print("  No usable observations.")
else:
    print(f"  Heart rate average:       {summary['heart_rate_average']:.2f} bpm")
    print(f"  Heart rate min/max:       {summary['heart_rate_min_max']}")
    print(f"  Skin response average:    {summary['skin_response_average']:.2f}")
    print(f"  Skin response min/max:    {summary['skin_response_min_max']}")
    print(f"  Temperature average:      {summary['temperature_average']:.2f} °C")
    print(f"  Temperature min/max:      {summary['temperature_min_max']}")
    print(f"  Activity level average:   {summary['activity_level_average']:.3f}")
    print(f"  Activity level min/max:   {summary['activity_level_min_max']}")
    print(f"  Signal quality average:   {summary['signal_quality_average']:.2f}")
    print(f"  Signal quality min/max:   {summary['signal_quality_min_max']}")
    print(f"  Session average HR:       {summary['session_avg_heart_rate']:.2f} bpm")
    print(f"  Baseline HR difference:   {summary['base_session_comparison']:.2f} bpm")
    print(f"  Baseline skin difference: {summary['skin_response_comparison']:.2f}")
    print(f"  Baseline temp difference: {summary['temperature_comparison']:.2f} °C")

print(f"  Usable observations:      {summary['usable_observations']}/{len(observation_data)}")

classification = analyzer.classify()
print(f"Classification: {classification}")

if classification == "recovering":
    print("Reason: heart rate and activity level declined near the end of the session.")
elif classification == "resting":
    print("Reason: average activity level was 0.25 or lower.")
elif classification == "moderate activity":
    print("Reason: average activity level was between 0.25 and 0.65.")
elif classification == "high activity":
    print("Reason: average activity level was above 0.65.")
else:
    print("Reason: fewer than 3 valid observations were available.")