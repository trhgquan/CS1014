from pulp import *

def main():
    x1 = LpVariable('x1', lowBound = 0)
    x2 = LpVariable('x2', lowBound = 0)
    x3 = LpVariable('x3', lowBound = 0)
    x4 = LpVariable('x4', lowBound = 0)

    beta = [0]
    for i in range(1, 5):
        beta.append(100**(i - 1))

    model = LpProblem('ExtraCredit', LpMaximize)

    model += 8 * x1 + 4 * x2 + 2 * x3 + x4 - 4*beta[1] - 2*beta[2] - beta[3] - .5*beta[4], 'fmax'

    model += x1 <= beta[1], 'First constraint'
    model += 4 * x1 + x2 <= 2*beta[1] + beta[2], 'Second constraint'
    model += 8 * x1 + 4 * x2 + x3 <= 4 * beta[1] + 2 * beta[2] + beta[3], 'Third coinstraint'
    model += 16 * x1 + 8 * x2 + 4 * x3 + x4 <= 8 * beta[1] + 4 * beta[2] + 2 * beta[3] + beta[4], 'Fourth coinstraint'

    model.solve()

    print('Objective' , model.objective)
    print('Fmax', model.objective.value())

    for i in model.variables():
        print(i, i.value())

if __name__ == '__main__':
    main()