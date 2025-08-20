import os
from dotenv import load_dotenv
import openai
import json

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def interpret_career_goal(goal_text):
    prompt = (
        f"Given the following career goal: '{goal_text}', "
        "suggest 2-3 personalized learning paths (courses, certifications) and 1-2 job rotation options. "
        "Respond in JSON with keys 'learning_paths' and 'job_rotations'."
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.7,
    )
    try:
        content = response.choices[0].message.content
        start = content.find('{')
        end = content.rfind('}') + 1
        json_str = content[start:end]
        return json.loads(json_str)
    except Exception:
        return {
            "learning_paths": ["Could not parse GenAI response."],
            "job_rotations": []
        }