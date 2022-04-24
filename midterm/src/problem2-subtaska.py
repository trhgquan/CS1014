from pulp import *

def main():
    x = LpVariable('x', lowBound = 0)
    y = LpVariable('y', lowBound = 0)

    model = LpProblem('recheck problem b', LpMaximize)

    model += 29 * x + 4 * y, 'target'
    model += 9 * x - 3 * y <= 23, 'first requirement'
    model += 3 * x - 8 * y >= -22, 'second requirement'
    model += x + y >= 5, 'third requirement'

    model.solve()

    print('Target:', model.objective.value())

    for i in model.variables():
        print(i, i.value())

if __name__ == '__main__':
    main()