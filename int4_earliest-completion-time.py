"""
** Construction task management program **

Contractors on the field must be allowed to coordinate their work in the form of "tasks".
Each task has a size expressed in "days of work" to be completed. Ex: ["painting", 2]  ["masonry", 5], etc.
Dependencies between tasks are modeled by an array of pairs. A pair ["task1", "task2"] implies that task1 is dependent on task2 and cannot run before task2 is completed.

Implement a construction task management program that allows:
-The initial input of tasks and their dependencies
-The ability to ask for the "earliest completion time" for any given task

Example:

Inputs:
tasks = [["painting", 2], ["drywall", 3], ["plumbing", 4], ["electrical", 1], ["HVAC", 2]]
dependencies = [["painting", "drywall"], ["drywall", "plumbing"], ["drywall", "electrical"], ["drywall", "HVAC"]]

Explanation:
Painting (2 days)  =>  drywall (3 days)   =>  |  plumbing (4 days)
                                              |  electrical (1 day)
                                              |  HVAC (2 days)

The contruction task management should allow for the following usage scenario:
task_manager.init(tasks, dependencies)
task_manager.get_earliest_completion_time("painting") => returns 9
(that's 2 + 3 + max(4,1,2) )
"""

debug = False

tasks = [["painting", 2], ["drywall", 3], ["plumbing", 4], ["electrical", 1], ["HVAC", 2]]
dependencies = [["painting", "drywall"], ["drywall", "plumbing"], ["drywall", "electrical"], ["drywall", "HVAC"]]

# Construction task management class
class task_manager:
    # Class member variables
    tasks = {}  # Task dictionary defining individual task completion times
    dependencies = []  # List of dependencies in ["task", "dependency"] format

    def calc_earliest_completion_time(self, li: list) -> int:
        time = 0
        max = 0

        # Find the task in the list that takes longest to complete
        for el in li:
            # If el is a string, include it in consideration for the current max
            if isinstance(el,str):
                if self.tasks[el] > max:
                    max = self.tasks[el]
            # Otherwise, it's a list and we'll need to call this function recursively
            else:
                time += self.calc_earliest_completion_time(el)

        if debug:
            print("Max in li {} is %d".format(li) %(max))

        # Add the time it takes to complete the longest task
        time += max

        return time

    # Get the list of dependencies for a given task
    def get_dependency_list(self, task: str) -> list:
        dependencyChain = []  # List of dependencies

        # Construct the list of dependencies in the format:
        #   ["dep1", "dep2", ["dep3", "dep4",["dep5"]]]
        for i in dependencies:
            if i[0] == task:
                dependencyChain.append(i[1])
                additionalDependecies = self.get_dependency_list(i[1])
                if additionalDependecies:
                    dependencyChain.append(additionalDependecies)

        return dependencyChain

    # Calculate earliest completion time for a given task
    def get_earliest_completion_time(self, task: str) -> int:
        # Initialize to the time it takes to complete the given task
        completion_time = self.tasks[task]

        # Get the dependency chain so we can calculate its completion time
        dependencyChain = self.get_dependency_list(task)

        # Add the time needed to complete all dependencies as well
        completion_time += self.calc_earliest_completion_time(dependencyChain)

        return completion_time

    # Class initializer
    def __init__(self, t: dict, d: dict):
        self.dependencies =  d

        # Convert the list to a dictionary, for easier lookup
        for i in t:
            self.tasks[i[0]] = i[1]
    
# Instantiate the object using our class
tm = task_manager([["painting", 2], ["drywall", 3], ["plumbing", 4], ["electrical", 1], ["HVAC", 2]], [["painting", "drywall"], ["drywall", "plumbing"], ["drywall", "electrical"], ["drywall", "HVAC"]])

# Test
print(tm.get_earliest_completion_time("painting"))