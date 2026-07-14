import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def parse_command(user_input):
    prompt = f"""
You are an automation parser.

Convert this command into JSON:
"{user_input}"

Only return JSON in this format:
{{
  "action": "organize_files | create_folder | move_file",
  "parameters": {{
    "source": "",
    "destination": ""
  }}
}}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    content = response.choices[0].message.content.strip()
    return eval(content)  # improve this later 