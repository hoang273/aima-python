import sys
sys.path.append('aima-python')
from search import *
import math

class HW2:

    def __init__(self):
        pass

    def example_problem_1(self, eight_puzzle, searcher):
        #EightPuzzle example with A*
        return searcher(eight_puzzle).solution()

    def problem_1a(self):
        '''
        problem 1a
        1. The start state of the 8 puzzle is (1, 0, 3, 4, 6, 8, 2, 7, 5)
        2. The goal state of the 8 puzzle is (1, 2, 3, 4, 5, 6, 7, 8, 0)
        3. Pass in the EightPuzzle object and use the A* search to solve.
        4. Return the solution.
        '''
        eight_puzzle = EightPuzzle(initial=(1, 0, 3, 4, 6, 8, 2, 7, 5),goal=(1, 2, 3, 4, 5, 6, 7, 8, 0))
        return astar_search(eight_puzzle).solution()
    
    def problem_1b(self):
        '''
        problem 1b
        1. The start state of the 8 puzzle is (2, 1, 3, 4, 0, 6, 5, 7, 8)
        2. The goal state of the 8 puzzle is (1, 2, 3, 4, 0, 5, 6, 7, 8)
        3. Pass in the EightPuzzle object and use the A* search to solve.
        4. Return the solution.
        '''
        eight_puzzle = EightPuzzle(initial=(2, 1, 3, 4, 0, 6, 5, 7, 8),goal=(1, 2, 3, 4, 0, 5, 6, 7, 8))
        return astar_search(eight_puzzle).solution()

    def problem_2a(self):
        '''
        problem 2a - Example of code with question to answer in homework
        1.  A* with 8-Puzzle and different heuristics (default and manhattan)
        2.  Return the solutions using same start state
            and goal.
        3.  Answer the question for this problem in your HW2_YourName.pdf
        '''

        puzzle = EightPuzzle((2, 4, 3, 1, 5, 6, 7, 8, 0))

        default_solution = astar_search(puzzle).solution()
        manhattan_solution = astar_search(puzzle,self.manhattan).solution()

        # Do not change this return statement
        return default_solution, manhattan_solution

    def problem_2b(self,searcher=None,heuristic=None):
        '''
        problem 2b - Use different start state
        1.  A* with 8-Puzzle and different heuristics (default and manhattan)
        2.  Return the solution and print the result using same start state
        3.  Answer the question for this problem in your HW2_YourName.pdf
        '''
        eight_puzzle = EightPuzzle(initial=(1, 0, 3, 4, 6, 8, 2, 7, 5),goal=(1, 2, 3, 4, 5, 6, 7, 8, 0))
        default_solution = searcher(eight_puzzle).solution()
        manhattan_solution = searcher(eight_puzzle,heuristic).solution()

        # Do not change this return statement
        return default_solution, manhattan_solution

    def problem_3a(self):
        '''
        problem 3a
        1. create the two romania graph problems
        2. create the list of search algorithms
        3. run each search algorithm on each problem and append the results to a list
        4. return each result list
        '''
        # HINT: Fill in the missing pieces in these comments
        r_graph1 = GraphProblem('Arad', 'Bucharest', romania_map)
        r_graph2 = GraphProblem('Iasi', 'Sibiu', romania_map)
        search_algos = [depth_first_graph_search,iterative_deepening_search,breadth_first_graph_search,uniform_cost_search,astar_search]

        results1 = []
        results2 = []
        for search in search_algos:
            results1.append(search(r_graph1))
            results2.append(search(r_graph2))
        # Do not change this return statement
        return results1, results2

    def problem_3b(self):
        '''
        1. read the documentation from: 
https://github.com/aimacode/aima-python/blob/master/search.py to compare
        2. return the result from the comparison tool
        '''
        header = ['Search Algorithm', 'Iasi->Sibiu']
        r_graph = [GraphProblem('Iasi', 'Sibiu', romania_map)] # Replace None with the romania graph problem (Note this sould be a 1 element list, see documentation)
        search_algos = [depth_first_graph_search,iterative_deepening_search,breadth_first_graph_search,uniform_cost_search,astar_search]
        return compare_searchers(problems=r_graph, searchers=search_algos, header=header)


    # This assumes that the goal state is (1, 2, 3, 4, 5, 6, 7, 8, 0)
    def manhattan(self,node):
        state = node.state
        index_goal = {0:[2,2], 1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1]}

        index_state = {}
        index = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
        x, y = 0, 0
 
        for i in range(len(state)):
            index_state[state[i]] = index[i]
    
        mhd = 0
        for i in range(8):
            for j in range(2):
                mhd = abs(index_goal[i][j] - index_state[i][j]) + mhd
    
        return mhd

def main():
    
    # Create object, hw2, of datatype HW2.
    hw2 = HW2()
 
    #=======================
    # A* with 8-Puzzle 
    # An example for you to follow to get you started on the EightPuzzle
    puzzle = EightPuzzle((2, 4, 3, 1, 5, 6, 7, 8, 0))
    # Checks whether the initialized configuration is solvable or not
    puzzle.check_solvability((2, 4, 3, 1, 5, 6, 7, 8, 0))
    print("A* with default heuristic")
    print(hw2.example_problem_1(puzzle, astar_search))
    #=======================

    print("\nProblem 1a")
    print(hw2.problem_1a())

    print("\nProblem 1b")
    print(hw2.problem_1b())

    print("\nProblem 2a")
    default_solution_2a, manhattan_solution_2a = hw2.problem_2a()
    print("Default Heuristic Solution: ", default_solution_2a)
    print("Manhattan Heuristic Solution: ", manhattan_solution_2a)

    print("\nProblem 2b")
    default_solution_2b, manhattan_solution_2b = hw2.problem_2b()
    print("Default Heuristic Solution: ", default_solution_2b)
    print("Manhattan Heuristic Solution: ", manhattan_solution_2b)

    print("\nProblem 3a")
    results1, results2 = hw2.problem_3a()
    print("Results for Arad -> Bucharest: ", results1)
    print("Results for Iasi -> Sibiu: ", results2)

    print("\nProblem 3b")
    print(hw2.problem_3b())
    
    
if __name__ == "__main__":
    main()


