from app.agent.prompts import EXPLAIN_RESULTS_PROMPT
from app.agent.schemas import UserIntent, RankedRecipe
from app.llm.base import BaseLLM


def _format_ranked_results(ranked_results: list[RankedRecipe]) -> str:
    lines = []
    for i, item in enumerate(ranked_results, start=1):
        r = item.recipe
        lines.append(
            f"{i}. "
            f"title={r.title}; "
            f"summary={r.summary}; "
            f"cuisine={r.cuisine}; "
            f"meal_type={r.meal_type}; "
            f"time={r.cook_time_min} min; "
            f"calories={r.calories}; "
            f"protein={r.protein_g}g; "
            f"ingredients={', '.join(r.ingredients)}; "
            f"rule_reason={item.reason}"
        )
    return "\n".join(lines)


def explain_results(
    user_query: str,
    intent: UserIntent,
    ranked_results: list[RankedRecipe],
    llm: BaseLLM,
) -> str:
    if not ranked_results:
        return "未找到符合条件的菜谱。" if intent.detected_language == "zh" else "No matching recipes found."

    prompt = f"""
User original query:
{user_query}

Parsed intent:
meal_type={intent.meal_type}
diet_goal={intent.diet_goal}
preferred_ingredients={intent.preferred_ingredients}
excluded_ingredients={intent.excluded_ingredients}
allergies={intent.allergies}
max_cook_time={intent.max_cook_time}
max_calories={intent.max_calories}
detected_language={intent.detected_language}

Ranked recipes:
{_format_ranked_results(ranked_results)}

Generate the final user-facing recommendation in the detected language.
"""

    messages = [
        {"role": "system", "content": EXPLAIN_RESULTS_PROMPT},
        {"role": "user", "content": prompt},
    ]

    return llm.chat(messages).strip()