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
    detected_language: str = "en"


@dataclass
class Recipe:
    recipe_id: str
    title: str
    cuisine: str
    meal_type: str
    ingredients: List[str]
    cook_time_min: int
    calories: int
    protein_g: int
    tags: List[str]
    summary: str


@dataclass
class RankedRecipe:
    recipe: Recipe
    score: float
    reason: str