from autogen import AssistantAgent, UserProxyAgent

from utility.llm_config import llm_config
from utility.prompt import knowledge_base_prompt
from tools.knowledge_base_tool import search_similar_solution


knowledge_agent = AssistantAgent(
    name="KnowledgeAgent",
    system_message=knowledge_base_prompt,
    llm_config=llm_config,
    code_execution_config=False,
)

tool_executor = UserProxyAgent(
    name="ToolExecutor",
    human_input_mode="NEVER",
    code_execution_config=False,
)

knowledge_agent.register_for_llm(
    name="search_similar_solution",
    description=(
        "Search the IT knowledge base for solutions similar "
        "to the user's problem."
    )
)(search_similar_solution)

tool_executor.register_for_execution(
    name="search_similar_solution"
)(search_similar_solution)