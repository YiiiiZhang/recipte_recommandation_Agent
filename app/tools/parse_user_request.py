import json

from app.agent.prompts import PARSE_USER_REQUEST_PROMPT
from app.agent.schemas import UserIntent
from app.llm.base import BaseLLM


def extract_json_block(text: str) -> str:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end < start:
        raise ValueError(f"No valid JSON object found in model output: {text}")
    return text[start:end + 1]


def parse_user_request(user_query: str, llm: BaseLLM) -> UserIntent:
    messages = [
        {"role": "system", "content": PARSE_USER_REQUEST_PROMPT},
        {"role": "user", "content": user_query},
    ]

    raw_output = llm.chat(messages)
    json_text = extract_json_block(raw_output)
    data = json.loads(json_text)

    return UserIntent(
        meal_type=data.get("meal_type"),
        diet_goal=data.get("diet_goal"),
        preferred_ingredients=data.get("preferred_ingredients", []),
        excluded_ingredients=data.get("excluded_ingredients", []),
        allergies=data.get("allergies", []),
        max_cook_time=data.get("max_cook_time"),
        max_calories=data.get("max_calories"),
    )