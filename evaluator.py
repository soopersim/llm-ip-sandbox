import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from main import (
    generate_patent_abstract,
    generate_structured_patent_abstract,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=ENV_PATH)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def score_abstract(abstract: str) -> dict:
    """
    Ask the LLM to score the abstract on several dimensions.
    Returns a dict like:
    {
      "clarity": 4,
      "formality": 5,
      "technical_specificity": 4,
      "structure": 5
    }
    """
    prompt = f"""
You are evaluating a patent abstract.

Rate the following on a scale from 1 (very poor) to 5 (excellent):

- Clarity
- Formal tone
- Technical specificity
- Structure

Return your answer as strict JSON with keys:
clarity, formality, technical_specificity, structure

Do NOT include any explanation, only JSON.

Abstract:
\"\"\"{abstract}\"\"\"
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    # Get the raw text from the model
    raw = response.output[0].content[0].text.strip()

    # Try to parse it as JSON
    try:
        scores = json.loads(raw)
    except json.JSONDecodeError:
        print("Failed to parse JSON, got:")
        print(raw)
        # Fallback: return empty dict or something safe
        scores = {}

    return scores

if __name__ == "__main__":
    raw = """
I built this system that monitors smart home usage data and can detect patterns that suggest
the user forgot to turn off the stove or left a high-risk appliance plugged in. When it detects
an anomaly, it sends a real-time alert to the user’s phone.
"""

    print("Generating abstracts...")
    abs1 = generate_patent_abstract(raw)
    abs2 = generate_structured_patent_abstract(raw)

    print("\n=== Abstract 1 (plain) ===")
    print(abs1)
    scores1 = score_abstract(abs1)
    print("Scores:", scores1)

    print("\n=== Abstract 2 (structured) ===")
    print(abs2)
    scores2 = score_abstract(abs2)
    print("Scores:", scores2)
