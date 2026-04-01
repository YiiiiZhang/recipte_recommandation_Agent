from app.llm.transformers_qwen import LocalQwenLLM
from app.tools.parse_user_request import parse_user_request
from app.tools.retrieve_recipes import retrieve_recipes
from app.tools.rank_candidates import rank_candidates


class RecipeAgentOrchestrator:
    def __init__(self):
        self.llm = LocalQwenLLM()

    def run(self, user_query: str):
        intent = parse_user_request(user_query, self.llm)
        candidates = retrieve_recipes(intent)
        ranked_results = rank_candidates(candidates, intent)

        return {
            "intent": intent,
            "ranked_results": ranked_results,
        }