import os
from dotenv import load_dotenv
from openai import OpenAI

# Always load .env from the current file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=ENV_PATH)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_patent_abstract(raw_description: str) -> str:
    """
    Version 1: simple improved patent-style abstract.
    """
    prompt = f"""
You are an experienced patent attorney.

The user will give you a rough, informal description of a technical invention.

Rewrite it as a clear, formal patent-style abstract (150–250 words).
Use precise, technical language, but keep it understandable.

Rough description:
\"\"\"{raw_description}\"\"\"

Now write the improved abstract:
"""
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    # Extract text from the response
    return response.output[0].content[0].text

def generate_structured_patent_abstract(raw_description: str) -> str:
    """
    Version 2: structured abstract with explicit sections.
    """
    prompt = f"""
You are an experienced patent attorney.

Rewrite the user's rough description as a structured, formal patent-style abstract.

Follow this structure exactly:

Title:
Field:
Background:
Summary of the Invention:
Technical Advantages:

Rough description:
\"\"\"{raw_description}\"\"\"

Now produce the structured abstract:
"""
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )
    return response.output[0].content[0].text

if __name__ == "__main__":
    raw = """
I built this system that monitors smart home usage data and can detect patterns that suggest
the user forgot to turn off the stove or left a high-risk appliance plugged in. When it detects
an anomaly, it sends a real-time alert to the user’s phone.
"""

    abstract_v1 = generate_patent_abstract(raw)
    abstract_v2 = generate_structured_patent_abstract(raw)

    print("=== Version 1 (plain abstract) ===")
    print(abstract_v1)
    print("\n=== Version 2 (structured abstract) ===")
    print(abstract_v2)

