import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv
load_dotenv()
llm_config = {

    "config_list": [

        {

            "model": "gpt-4o",

            "api_key": os.environ.get("OPENAI_API_KEY")

        }

    ]

}
assistant=AssistantAgent("assistant",llm_config=llm_config)
user_proxy=UserProxyAgent("user_proxy",code_execution_config=False)
user_proxy.initiate_chat(
    assistant,
    message="Tell me a joke on data scientist"
)