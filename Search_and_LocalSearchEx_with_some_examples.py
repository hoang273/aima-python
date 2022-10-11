import sys 
sys.path.append('aima-python')
from search import *

#Graph search examples using uninformed search and a* on graphs
#Tree search examples using depth first tree search breadth first tree search


class FRAME:
    def __init__(self, prob=None):
        self.prob = GraphProblem('Arad', 'Bucharest', romania_map)
    def problem_1(self):
        print("======breadth_first_graph_search=======")
        ans = breadth_first_graph_search(self.prob)
        print("goal was found: ", ans)
        print("path cost: ",ans.path_cost)
        print("path found: ", ans.path())
        return ""
        return ""
    def problem_2(self):
        print("======depth_first_graph_search=======")
        return ""
    def problem_3(self):
        print("======uniform_cost_search=======")
        return ""
    def problem_4(self):
        print("======astar_search=======")
        return ""
    def problem_5(self):
        print("======depth_first_tree_search=======")
        return ""
    def problem_6(self):
        print("======breadth_first_tree_search=======")
        tree = Graph(dict(A=dict(B=1, C=1, D=1), B=dict(E=1, F=1)))
        graph2 = GraphProblem('A', 'F', tree)
        ans = depth_first_tree_search(graph2)
        print("goal was found: ", ans)
        print("path cost: ",ans.path_cost)
        print("path found: ", ans.path())
        return ""
    def problem_7(self):
        print("======compare_graph_searchers=======")
        return ""

#The following functions examine the behavior of hill climbing and
#simulated annealing on various peak problems represented by a 2-D grid

#redefine simulated_annealing_full with debug print statements to
#illustrate what is going on
def simulated_annealing_full(problem, schedule=exp_schedule()):
    """ This version returns all the states encountered in reaching 
    the goal state. The last tuple in the list is the goal state it found"""
    states = []
    current = Node(problem.initial)
    print("range: ", sys.maxsize)#debug
    for t in range(sys.maxsize):
        states.append(current.state)
        T = schedule(t)
        print("t: ",t,"T: ",T) #debug
        if T == 0:
            return states
        neighbors = current.expand(problem)
        if not neighbors:
            return current.state
        next_choice = random.choice(neighbors)
        delta_e = problem.value(next_choice.state) - problem.value(current.state)
        print("delta: ",delta_e) #debug
        print("exp(delta_e/T): ",np.exp(delta_e / T)," prob: ",probability(np.exp(delta_e / T)))  #debug
        if delta_e > 0 or probability(np.exp(delta_e / T)):
            current = next_choice


def test_hill_climbing():
    prob1 = PeakFindingProblem((0, 0), [[0, 5, 10, 20],
                                       [-3, 7, 11, 5]])
    print("Problem 1 Max coords: ",hill_climbing(prob1))
    
    prob2 = PeakFindingProblem((0, 0), [[0, 5, 10, 8],
                                       [-3, 7, 9, 999],
                                       [1, 2, 5, 11]])
    print("Problem 2 Max coords: ",hill_climbing(prob2))
    
    prob3 = PeakFindingProblem((2, 0), [[0, 5, 10, 8],
                                       [-3, 7, 9, 999],
                                       [1, 2, 5, 11]])
    print("Problem 3 Max coords: ",hill_climbing(prob3))


def test_simulated_annealing():
   prob4 = PeakFindingProblem((0, 0), [[0, 5, 10, 20],
                                       [-3, 7, 11, 5]], directions4)
   #sols = {prob4.value(simulated_annealing(prob4)) for _ in range(100)}
   #print("Solutions, Simulated Annealing Problem 4: ", sols)
   #print("Maximum = ", max(sols))
   
   sol = simulated_annealing_full(prob4)
   print("states visited by full simulated annealing = ", sol)

   check_ele = (0,3)
   x=list(filter(lambda i:(i==check_ele),sol))
   print("optimal tuple (0, 3) occurs: ",len(x),"times")
   print("out of: ", len(sol), " items")
   
#main function to test all the graph search problems out:

def main():
    frame1 = FRAME()
    print("Problem 1:", frame1.problem_1())
    print("Problem 2:", frame1.problem_2())
    print("Problem 3:", frame1.problem_3())
    print("Problem 4:", frame1.problem_4())
    print("Problem 5:", frame1.problem_5())
    print("Problem 6:", frame1.problem_6())
    print("Problem 7:", frame1.problem_7())

    #add calls to test simulated annealing

