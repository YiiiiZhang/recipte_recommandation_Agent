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

            print("\n[Parsed Intent]")
            print(f"meal_type: {intent.meal_type}")
            print(f"diet_goal: {intent.diet_goal}")
            print(f"preferred_ingredients: {intent.preferred_ingredients}")
            print(f"excluded_ingredients: {intent.excluded_ingredients}")
            print(f"allergies: {intent.allergies}")
            print(f"max_cook_time: {intent.max_cook_time}")
            print(f"max_calories: {intent.max_calories}")
            print()

        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()