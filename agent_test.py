from autogen import UserProxyAgent
from agents.classifier_agent import get_classifier_agent

sample_tickets=[
    "The VPN isn't connecting since morning.",
    "My mouse is not working."
]
def get_user_agent():
    user=UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        code_execution_config=False,
    )
    return user

def run_test():
    user= get_user_agent()
    classifier=get_classifier_agent()

    for ticket in sample_tickets:
        print(f"\n Ticket: {ticket}")
        user.initiate_chat(
            recipient=classifier, #who will respond to the ticket
            message=f"Classify this ticket: {ticket}",
            max_turns=1
        )
    return

if __name__=="__main__":
    run_test()