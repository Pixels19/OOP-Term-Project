# Scenarios and Contraints 
# Devloping Functions 

import random 

def getScenario():
    """
    Randomly chooses a scenario and legal complications.

    Returns:
        int: An integer representing the scenario (00-22).
             Tens digit: Legal complications (0, 1, or 2).
             Ones digit: Scenario type (0, 1, or 2).
    """
    scenario = random.randint(0, 2)  # 0, 1, or 2
    legal = random.randint(0, 2)     # 0, 1, or 2
    return legal * 10 + scenario

# Example usage
current_scenario = getScenario() 
print(f"Current Scenario Code: {current_scenario}") 