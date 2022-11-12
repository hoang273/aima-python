import sys 
sys.path.append('aima-python')
from logic import *

class HW3:
    def __init__(self):
        pass

    def problem_1(self):
        problem_1_list = [ 'A==>A','(A ==> B) ==> (~ A ==> ~ B)','A | B | ~ B','A | B | ~ B','(A ==> B) ==> (B ==> C)','(A ==> C) ==> ((A & B) ==> C)'] #placeholder, populate this with your statements
        results = [] # iteratively append the results to this
        #iterate over the problems and append the tt_true result to the list 
        for statement in problem_1_list:
            results.append(tt_true(statement))
        #return the list of results
        return results

    def problem_2(self):
        problem_2_list = [(expr('E ==> E')),(expr('E ==> F')),(expr('(E & F) | ~ F')),(expr('((G | B) & (~ B | A)) ==> (G | A)')),(expr('(A ==> B) ==> (B ==> C)'))] #placeholder, populate this with your statements
        results = [] # iteratively append the results to this
        #iterate over the problems and append the dpll_satisfiable result to the list
        for statement in problem_2_list:
            results.append(dpll_satisfiable(statement))
        #return the list of results
        return results

    def problem_3(self):
        KB = PropKB() 
        for clause in ['My ==> ~ Mo','~ My ==> Mo & Ma','~ Mo | Ma ==> H','H ==> Ma']:
            KB.tell(expr(clause)) #placeholder, populate this with your statements
        alpha = expr('H') #placeholder, populate this with your statements
        #pass in your KB and alpha and return the pl_resolution result
        result= pl_resolution(KB,alpha)
        return result #placeholder

    def problem_4(self):
        KB = None
        alpha = None
        #return the pl_resolution result
        return None #placeholder


def main():

    hw = HW3()

    #problem 1
    print(hw.problem_1())

    #problem 2
    print(hw.problem_2())

    #problem 3
    print(hw.problem_3())

    #problem 4
    print(hw.problem_4())
    

if __name__ == '__main__':
    main()