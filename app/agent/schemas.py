from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class UserIntent:
    meal_type: Optional[str] = None
    diet_goal: Optional[str] = None
    preferred_ingredients: List[str] = field(default_factory=list)
    excluded_ingredients: List[str] = field(default_factory=list)
    allergies: List[str] = field(default_factory=list)
    max_cook_time: Optional[int] = None
    max_calories: Optional[int] = None