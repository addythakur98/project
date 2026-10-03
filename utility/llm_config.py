import os
from dotenv import load_dotenv

load_dotenv()


llm_config = {

    "config_list": [

        {

            "model": "openrouter/free",

            "api_key": os.environ.get("OPENROUTER_API_KEY"),

            "base_url": "https://openrouter.ai/api/v1"

        }

    ]

}