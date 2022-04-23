from pulp import *

def original():
    x1 = LpVariable('x1', upBound = 0)
    x2 = LpVariable('x2')
    x3 = LpVariable('x3', lowBound = 0)

    model = LpProblem('problem3-subtaska', LpMinimize)
    model += 2 * x1 - x2 + 4 * x3, 'target'
    model += x1 - x2 + 2 * x3 == 5, 'first requirement'
    model += 2 * x1 - x2 + x3 <= 3, 'second requirement'

    model.solve()

    print('Original')

    print(model.objective.value())

    for i in model.variables():
        print(i, i.value())

def new():
    y1 = LpVariable('y1')
    y2 = LpVariable('y2', upBound = 0)

    model = LpProblem('problem3-subtaska', LpMaximize)
    model += 5 * y1 + 3 * y2, 'target'
    model += y1 + 2 * y2 >= 2, 'first requirement'
    model += -y1 - y2 == -1, 'second requirement'
    model += 2 * y1 + y2 <= 4, 'third requirement'

    model.solve()

    print('New')

    print(model.objective.value())

    for i in model.variables():
        print(i, i.value())

if __name__ == '__main__':
    original()
    new()