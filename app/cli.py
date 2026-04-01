from app.agent.orchestrator import RecipeAgentOrchestrator


def main():
    agent = RecipeAgentOrchestrator()

    print("Recipe Agent CLI")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("> ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break
        if not user_input:
            continue

        try:
            result = agent.run(user_input)
            intent = result["intent"]
            ranked = result["ranked_results"]
            explanation = result["explanation"]

            print("\n[Parsed Intent]")
            print(f"meal_type: {intent.meal_type}")
            print(f"diet_goal: {intent.diet_goal}")
            print(f"preferred_ingredients: {intent.preferred_ingredients}")
            print(f"excluded_ingredients: {intent.excluded_ingredients}")
            print(f"allergies: {intent.allergies}")
            print(f"max_cook_time: {intent.max_cook_time}")
            print(f"max_calories: {intent.max_calories}")
            print(f"response_language: {intent.response_language}")

            print("\n[Top Recommendations]")
            if not ranked:
                print("No matching recipes found.\n")
                continue

            for i, item in enumerate(ranked, start=1):
                recipe = item.recipe
                print(f"\n{i}. {recipe.title}")
                print(f"   score: {item.score:.2f}")
                print(f"   cuisine: {recipe.cuisine}")
                print(f"   time: {recipe.cook_time_min} min")
                print(f"   calories: {recipe.calories} kcal")
                print(f"   protein: {recipe.protein_g} g")
                print(f"   ingredients: {', '.join(recipe.ingredients)}")
                print(f"   rule-based why: {item.reason}")

            print("\n[LLM Explanation]")
            print(explanation)
            print()

        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()