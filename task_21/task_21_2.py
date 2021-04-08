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


if __name__ == '__main__':
    foods = read_input('input.txt')
    all_ingredients = list({ingredient for food in foods for ingredient in food[0]})
    all_allergens = list({allergen for food in foods for allergen in food[1]})

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
    solver.Solve(model)
    all_allergens.sort()
    print(','.join([all_ingredients[solver.Value(variables[allergen])] for allergen in all_allergens]))
