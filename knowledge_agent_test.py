from autogen import UserProxyAgent
from agents.knowledge_base_agent import knowledge_agent
from tools.knowledge_base_tool import search_similar_solution


def get_user_agent():
    return UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        code_execution_config=False,
    )


def run_test():

    print("RUN_TEST STARTED")

    user = get_user_agent()

    user.register_for_execution(
        name="search_similar_solution"
    )(search_similar_solution)

    problem = "My VPN keeps disconnecting."

    print("STARTING CHAT")

    user.initiate_chat(
        knowledge_agent,
        message=f"Find a solution for this IT problem: {problem}",
        max_turns=5
    )


if __name__ == "__main__":
    run_test()