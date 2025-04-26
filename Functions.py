# Scenarios and Groups
# Devloping Functions 
import random

def getScenario():  # 10,
    """
    This function randomly chooses a scenario for the vehicle and determines if there are legal complications.

    Returns:
        int: A two digit integer that represents the scenario and legal context.

        Tens digit -> legal complications (0, 1, 2)

        legal complication 0 = There are no legal complications

        legal complicaion 1 = The crossing signal in the car's current lane is green 
        (meaning the pedestrians are legally crossing)
        but the signal in the other lane is red 
        (meaning the pedestrians should not be crossing)

        legal compication 2 =  The crossing signal in the car's current lane is red
        (meaning the pedestrians should not be crossing)
        but the signal in the other lane is green 
        (meaning the pedestrians are legally crossing)

        
        Ones digit -> the scenario (0, 1, 2)

        scenario 0 =  The car can either stay in its current lane and hit one group of pedestrians 
        or swerve into the other lane and hit a different group of pedestrians.

        scenario 1 =  The car can either stay in its lane and hit a group of pedestrians 
        or swerve into the other lane and hit a concrete barricade
        which will result in the death of the car's passengers

        scenario 2 =  The car can either stay in its lane and hit a concrete barricade, killing the passengers
        or swerve into the other lane and hit a group of pedestrians.

    """
    # Scenario -> (12, 13, 14, 15, 16, 17, 18, 19, 20)
    scenario = random.randint(0,2)

    # Legal -> (21, 22, 23, 24, 25, 26)
    legal = random.randint(0,2) 

    # Calculates the scenario and legal into a two-digit int
    result = legal * 10 + scenario

    return result

# scenario_result = getScenario()
# print(f"Get Scenario Results: {scenario_result}")

"""
For print results for example lets say the result is 20:

it would mean the SCENARIO = 0 

The car must choose to stay in the lane and hit one group of pedestrians 
or sway into the other lane and hit a different group of pedestrians


it would mean the LEGAL = 2 

The crossing in the current lane is red (indicating that the group should not be crossing) 
but the other lane is green (indicating that the group can legally cross)
"""

def getGroup():
    """
    This function randomly determines the number of people/animals in a group 
    and assigns a character to each one representing thier type
    
    a - Man
    b - Woman
    c - Boy
    d - Girl
    e - Elderly Man
    f - Elderly Woman
    g - Obese Man
    h - Obese Woman
    i - Male Executive
    j - Female Executive
    k - Male Doctor
    l - Female Doctor
    m - Male Jogger
    n - Female Jogger
    o - Pregnant Woman
    p - Homeless Person
    q - Criminal
    r - Baby
    s - Dog
    t - Cat


    Returns:
        str: a string consisting of concatenated characters representing the group members
    """
    # Determines Group Size 
    group_size = random.randint(1, 5) # Randomly chooses between 1 - 5 

    # Define the possible characters for group members 
    characters = 'abcdefghijklmnoprst' # 'a'- 't' to represent the diff types of ppl

    # Builds the group string
    group_str = " " # Starts with an empty string 

    for _ in range(group_size): # Loop for each member in a group 
        random_char = random.choice(characters) # Randomly chooses a character
        group_str += random_char # Adds the character to the string
    return group_str

# group_result = getGroup()
# print(f"Get Group results: {group_result}")

"""
For print results for example lets say the results were 'btoms': 

This means the function randomly generated the group of 5 ppl and assigned them letter 
corresponding to the list above

b - Woman 
t - Cat  
o - Male Jogger  
m - Male Doctor  
s - Criminal

"""