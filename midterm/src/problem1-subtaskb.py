from pulp import *

x1 = LpVariable('X1', lowBound = 0)
x2 = LpVariable('X2', lowBound = 0)
x3 = LpVariable('X3', lowBound = 0)

model = LpProblem('Problem1_subtaskb', LpMaximize)

model += 2 * x1 + 2 * x2 + 3 * x3, 'Revenue'
model += x1 + 2 * x2 - x3 <= 14, 'First constraint'
model += 2 * x1 - 2 * x2 + 3 * x3 <= 16, 'Second constraint'
model += -1 * x1 + 4 * x2 + 2 * x3 <= 16, 'Third constraint'

model.solve()

print('Objective:', model.objective)

print('Maximum revenue:', model.objective.value())

for i in model.variables():
    print(i, i.value())