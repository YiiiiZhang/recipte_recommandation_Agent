from app.agent.schemas import UserIntent, Recipe
from app.data.seed_recipes import SEED_RECIPES


def _matches_constraints(recipe: Recipe, intent: UserIntent) -> bool:
    if intent.meal_type and recipe.meal_type.lower() != intent.meal_type.lower():
        return False

    if intent.max_cook_time and recipe.cook_time_min > intent.max_cook_time:
        return False

    if intent.max_calories and recipe.calories > intent.max_calories:
        return False

    recipe_ingredients = {item.lower() for item in recipe.ingredients}

    for item in intent.excluded_ingredients:
        if item.lower() in recipe_ingredients:
            return False

    for item in intent.allergies:
        if item.lower() in recipe_ingredients:
            return False

    return True


def retrieve_recipes(intent: UserIntent) -> list[Recipe]:
    candidates = []
    for recipe in SEED_RECIPES:
        if _matches_constraints(recipe, intent):
            candidates.append(recipe)
    return candidates