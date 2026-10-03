from autogen import UserProxyAgent

from agents.classifier_agent import get_classifier_agent
from agents.knowledge_base_agent import knowledge_agent, tool_executor


def resolve_ticket(ticket):

    # -------------------------------
    # STEP 1: CLASSIFY THE TICKET
    # -------------------------------

    classifier = get_classifier_agent()

    user = UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        code_execution_config=False,
    )

    classification_result = user.initiate_chat(
        classifier,
        message=f"""
Classify this IT ticket:

{ticket}
""",
        max_turns=1
    )

    classification = classification_result.summary

    # -------------------------------
    # STEP 2: KNOWLEDGE BASE
    # -------------------------------

    knowledge_result = tool_executor.initiate_chat(
        knowledge_agent,
        message=f"""
The user submitted this IT ticket:

{ticket}

The ClassifierAgent classified it as:

{classification}

Now find the most relevant solution for this ticket.

You MUST use the search_similar_solution tool.
After retrieving the relevant information, provide a concise
solution to the user.
""",
        max_turns=3
    )

    solution = knowledge_result.summary

    # Return the results to Streamlit
    return {
        "classification": classification,
        "solution": solution
    }


if __name__ == "__main__":

    ticket = input("Enter your IT issue: ")

    result = resolve_ticket(ticket)

    print("\n=== CLASSIFICATION ===")
    print(result["classification"])

    print("\n=== FINAL SOLUTION ===")
    print(result["solution"])