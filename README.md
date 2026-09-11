# Smart Fitness Session Analyzer

## Student Information

* Student Name: Luka Dordevic
* Student Number: s374915

## Description

Option A — Smart Fitness Session Analyzer 

This project analyzes fitness session data by validating observations, 
calculating summary statistics, comparing session heart rate with the participant's baseline, 
and classifying the session.

## Project Structure

- `models.py` — contains the classes and session analysis logic.
- `analysis.py` — contains validation and calculation functions.
- `main.py` — generates the data, creates the objects and runs the analysis.
- `fitness_assignment/data_generator.py` — provides the simulated fitness data.

## Assumptions

- Reasonable heart rate is within 30–220 bpm for data validation.
- Skin response cannot be negative.
- Temperature is considered valid between 25–42 °C.
- Sessions with fewer than 3 valid observations are classified as having "insufficient data".
- Activity level ≤ 0.25 is classified as resting, > 0.25 to ≤ 0.65 as moderate activity, and > 0.65 as high activity.
- A session is classified as recovering when both heart rate and activity level decline from the first to the last valid observation, with heart rate decreasing by at least 10%.

## Class design

- Participant
  - Stores the participant ID and baseline measurements such as heart rate, skin response and temperature.
- Observation
  - Represents one measurement window from a fitness session and stores its timestamp, heart rate, skin response, temperature, activity level and signal quality.
- FitnessSession 
  - Groups a participant with a list of observations, representing one complete fitness session.
- FitnessAnalyzer 
  - Processes a session by validating observations, calculating summaries, comparing measurements with the participant's baseline and classifying the session.

## Object oriented design
- Composition: FitnessSession contains a Participant object and a list of Observation objects.
- Encapsulation: FitnessAnalyzer stores valid observations in the protected style _valid_observations attribute and provides access through the valid_observations property.
- Inheritance and overriding: Inheritance is not used because the application does not require subclasses. Composition better represents the relationship between a session, participant and observations.
- Static method: FitnessAnalyzer.classify_activity_level() is a static method because it classifies an activity level using only the supplied value and does not require access to a specific analyzer instance.


## Installation and running
Clone the repository and run the program from the repository root:

git clone https://github.com/Luka122/fitness-session-analyzer.git

cd fitness-session-analyzer (root)

python main.py

The project uses only the Python standard library.


## Example Output
Formatted for readability
```text
Summary:
  Heart rate average:       106.25 bpm
  Heart rate min/max:       74 / 134 bpm
  Skin response average:    2.03
  Skin response min/max:    1.81 / 2.33
  Temperature average:      32.81 °C
  Temperature min/max:      32.64 / 33.05 °C
  Activity level average:   0.465
  Activity level min/max:   0.17 / 0.81
  Signal quality average:   0.91
  Signal quality min/max:   0.86 / 0.98
  Session average HR:       106.25 bpm
  Baseline HR difference:   +36.25 bpm

Classification: recovering
```
### known limitations
The classification rules are manually defined, and recovery detection compares the first and last valid heart rate and activity measurements.