from app.agent.schemas import UserIntent, Recipe, RankedRecipe


def _score_recipe(recipe: Recipe, intent: UserIntent) -> tuple[float, str]:
    score = 0.0
    reasons = []

    if intent.max_cook_time and recipe.cook_time_min <= intent.max_cook_time:
        score += 0.25
        reasons.append(f"ready in {recipe.cook_time_min} minutes")

    if intent.max_calories and recipe.calories <= intent.max_calories:
        score += 0.20
        reasons.append(f"{recipe.calories} kcal fits your calorie target")

    if intent.diet_goal == "high_protein" and recipe.protein_g >= 25:
        score += 0.30
        reasons.append(f"high in protein ({recipe.protein_g}g)")

    preferred = {x.lower() for x in intent.preferred_ingredients}
    ingredients = {x.lower() for x in recipe.ingredients}
    overlap = preferred.intersection(ingredients)
    if overlap:
        score += 0.25
        reasons.append(f"matches your preferred ingredients: {', '.join(sorted(overlap))}")

    if not reasons:
        reasons.append("generally matches your request")

    return score, "; ".join(reasons)


def rank_candidates(candidates: list[Recipe], intent: UserIntent) -> list[RankedRecipe]:
    ranked = []
    for recipe in candidates:
        score, reason = _score_recipe(recipe, intent)
        ranked.append(RankedRecipe(recipe=recipe, score=score, reason=reason))

    ranked.sort(key=lambda x: x.score, reverse=True)
    return ranked[:3]