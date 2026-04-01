import json

from app.agent.prompts import PARSE_USER_REQUEST_PROMPT
from app.agent.schemas import UserIntent
from app.llm.transformers_qwen import LocalQwenLLM


def parse_user_request(user_query: str) -> UserIntent:
    llm = LocalQwenLLM()

    messages = [
        {"role": "system", "content": PARSE_USER_REQUEST_PROMPT},
        {"role": "user", "content": user_query},
    ]

    raw_output = llm.chat(messages)

    data = json.loads(raw_output)

    return UserIntent(
        meal_type=data.get("meal_type"),
        diet_goal=data.get("diet_goal"),
        preferred_ingredients=data.get("preferred_ingredients", []),
        excluded_ingredients=data.get("excluded_ingredients", []),
        allergies=data.get("allergies", []),
        max_cook_time=data.get("max_cook_time"),
        max_calories=data.get("max_calories"),
    )