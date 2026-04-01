from app.tools.parse_user_request import parse_user_request


class RecipeAgentOrchestrator:
    def run(self, user_query: str):
        intent = parse_user_request(user_query)
        return {
            "intent": intent
        }