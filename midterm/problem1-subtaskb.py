from pulp import *

x1 = LpVariable('X1', lowBound = 0)
x2 = LpVariable('X2', lowBound = 0)
x3 = LpVariable('X3', lowBound = 0)

model = LpProblem('Problem1_subtaskb', LpMaximize)

model += 2 * x1 + 2 * x2 + 3 * x3, 'Revenue'
model += x1 + 2 * x2 - x3 <= 14, 'Rang buoc 1'
model += 2 * x1 - 2 * x2 + 3 * x3 <= 16, 'Rang buoc 2'
model += -1 * x1 + 4 * x2 + 2 * x3 <= 16, 'Rang buoc 3'

model.solve()

model.objective

model.objective.value()

for i in model.variables():
    print(i, i.value())