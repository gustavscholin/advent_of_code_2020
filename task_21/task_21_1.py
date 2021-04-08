from itertools import permutations
from ortools.sat.python import cp_model


def read_input(path):
    foods = []
    with open(path, 'r') as f:
        for line in f.read().splitlines():
            ingredients, allergens = line.split(' (contains ')
            ingredients = ingredients.split()
            allergens = allergens.strip(')').split(', ')
            foods.append((ingredients, allergens))
    return foods


class VarArraySolutionCollector(cp_model.CpSolverSolutionCallback):

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.solution_list = set()

    def on_solution_callback(self):
        [self.solution_list.add(self.Value(v)) for v in self.__variables]


if __name__ == '__main__':
    foods = read_input('input.txt')
    all_ingredients = list({ingredient for food in foods for ingredient in food[0]})
    all_allergens = tuple({allergen for food in foods for allergen in food[1]})

    model = cp_model.CpModel()
    variables = {}
    for allergen in all_allergens:
        variables[allergen] = model.NewIntVar(0, len(all_ingredients) - 1, allergen)

    model.AddAllDifferent(variables.values())
    for food in foods:
        ingredients_indices = [(all_ingredients.index(ingredient), ) for ingredient in food[0]]
        allergens_vars = [variables[allergen] for allergen in food[1]]
        for allergens_var in allergens_vars:
            model.AddAllowedAssignments([allergens_var], ingredients_indices)

    solver = cp_model.CpSolver()
    solution_collector = VarArraySolutionCollector(variables.values())
    solver.SearchForAllSolutions(model, solution_collector)
    non_allergen_ingredients = {all_ingredients[idx] for idx in list(set(range(len(all_ingredients))).difference(solution_collector.solution_list))}
    appearances = 0
    for food in foods:
        appearances += len(non_allergen_ingredients.intersection(set(food[0])))

    print(appearances)
