import random
from Functions import getGroup, getScenario
class MoralMachine:
    """
    This class contains the algorithm that makes the moral decisions in a vehicle 

    """

    def __init__(self):
        """
        Contructor for MoralMachine class (empty for now but might add initialization here for later)
        
        """
        pass

    def decideSwerve(self, scenario, group1, group2):
        """
        This function decides whether the vehicle should swerve or not based on the scenario 
        and types of groups being affected

        Args:
            scenario (int): an integer representing the scenario (00 - 22)
            group1 (str):   a string representing the group of people/animals in current lane
            group2 (str )   a string representing the group of people/animals in other lane

        Returns:
            bool: True if car should swerve, False if it stays in current lane 

        Goal: I want to prioritize 4 things (I will mark in Parts by order of importance) 1. saving more lives, 2. uphold the law, 3. age preference
        whilst 4. protecting passengers to an extent
        """

        # Part 1: Saving More Lives 
        num_group1 = len(group1) # Number of ppl in group 1 
        num_group2 = len(group2) # Number of ppl in group 2 
        if num_group2 < num_group1: # if less ppl will die by swerving 
            swerve = True # then we swerve 
        elif num_group1 < num_group2: # if less ppl die if we DONT swerve
            swerve = False # we dont swerve 
        else:
            swerve = False # Defaults to not swerve if else (or saving lives is the same regardless)


        # Part 2: Upholding the Law 
        legal_complications = scenario // 10 # get the tens digit 
        if legal_complications == 1: # if it is legal to cross in current lane, but illegal in the other 
            swerve = False # we do not swerve
        elif legal_complications == 2: # if it is illegal to cross in current lane, but legal in the other 
            swerve = True # we swerve 

        # Part 3: Age Preference <-- prioritize the little ones ('c' = Boy , 'd' = Girl , 'r' = Baby)
        child_group1 = group1.count('c') + group1.count('d') + group1.count('r')
        child_group2 = group2.count('c') + group2.count('d') + group2.count('r') 
        if child_group2 > child_group1: # if more children in group 2 
            swerve = False  # we dont swerve 
        if child_group1 > child_group2: # if more children in group 1 
            swerve = True # we swerve

        # Part 4: Protecting Passengers <-- tie breaker should some (scenarios == False) kill some passengers 
        if swerve == False and scenario in [1, 2, 10, 12, 20, 22]: # scenarios in which swerving kills passengers <--- (this)
            swerve = False # dont swerve if it kills passenger <-- reinforced False to make sure no lives are lost 
        return swerve
    
    def testAlgorithm(self, num_tests):
        """
        Tests the moral algorithmn over a specified number of scenarios
        and returns the kill rates for each type of person/animal

        Args:
            num_tests (int): Number of test scenarios to run

        Returns:
            list: A list of floats representing the kill percentage for each type of person/animal
                    the order of percentage corresponds to order of characters -> 'a' - 't'

        """
        kill_counts = [0] * 20 # Initialize a list to count kills for each type
        total_counts = [0] * 20 # Initialize a list to count the total number of each type
        characters = 'abcdefghijklmnopqrst' # 'a' - 't' for person/animal type

        for _ in range(num_tests):
            scenario = getScenario() # calls getScenario() to get a scenario
            group1 = getGroup() # calls getGroup() to get group 1 
            group2 = getGroup() # calls getGroup() to get group 2 

            swerve = self.decideSwerve(scenario, group1, group2) # get the decision
            killed_group = group2 if swerve else group1 # determine who got killed

            for i, char in enumerate(characters):
                count1 = group1.count(char)
                count2 = group2.count(char)
                total_counts[i] += count1 + count2
                kill_counts[i] += killed_group.count(char)
            
            kill_percentage = [(kill_counts[i] / total_counts[i] if total_counts[i] > 0 else 0 for i in range(20))]
            return kill_percentage
        
    def getScenario():
        # Scenario -> (12, 13, 14, 15, 16, 17, 18, 19, 20)
        scenario = random.randint(0,2)

        # Legal -> (21, 22, 23, 24, 25, 26)
        legal = random.randint(0,2) 

        # Calculates the scenario and legal into a two-digit int
        result = legal * 10 + scenario

        return result
    
    def getScenario():
        return random.randint(0, 22)


    def getGroup():
        group_size = random.randint(1, 5) # Determines group size 
        characters = 'abcdefghijklmnopqrst' # defines possible characters 
        return ''.join(random.choice(characters) for _ in range(group_size)) # builds group string
        

if __name__ == "__main__":
    moral_machine = MoralMachine()
    num_tests = 1000
    results = moral_machine.testAlgorithm(num_tests)
    print("Kill percentages:", list(results))




        
