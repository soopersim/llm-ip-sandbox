# LLM Patent Abstract Assistant

A small end-to-end AI system that transforms rough invention ideas into formal patent-style abstracts — and evaluates them using an automated LLM judge.

## What This Project Is (Non-Technical Explanation)
This project uses AI to rewrite that into something a patent lawyer would write:
formal, structured, and technical.

But it doesn’t stop there.
A second AI acts like a reviewer, scoring the generated patent abstract based on:

- Clarity

- Professional tone

- Technical detail

- Structure

So this project is:
AI that writes patent-style descriptions + AI that grades them.

This is a simple prototype showing how AI can help with legal writing, safety reviews, and technical document drafting.

## What I Learned

While building this project, I practiced and strengthened several key skills:

### 1. Prompt Engineering

How different instructions change the tone, structure, and quality of AI output

How to design prompts for formal, domain-specific writing

How to compare two prompt versions scientifically

### 2. Evaluation Pipelines

Building an LLM-as-judge system

Designing a scoring rubric (clarity, formality, specificity, structure)

Parsing JSON and handling imperfect model outputs

### 3. Python + Project Structure

Organizing a real small-scale AI project

Using .env files, virtual environments, and clean imports

Writing reusable functions instead of single long scripts

### 4. Working With Domain Formats (Patents)

Understanding the typical structure of a patent abstract

Rewriting informal descriptions into formal technical language

Structuring prompts for legal/technical writing

### 5. Version Control & Clean Coding Habits

Creating a GitHub repository from scratch

Writing a readable README

Using .gitignore correctly

Committing meaningful increments

Overall, this project taught me how to build, structure, and evaluate a mini LLM system end-to-end — something I can expand into larger tools later.

## Features
### 1. Patent Abstract Generator — Version 1

Turns messy invention ideas into a formal 150–250 word abstract

Uses a single structured prompt

Great for baseline comparisons

### 2. Structured Patent Abstract Generator — Version 2

Outputs an abstract with clear sections:

- Title

- Field

- Background

- Summary of the Invention

- Technical Advantages

Useful for seeing how structured prompting affects output quality.

### 3. LLM-as-Judge Evaluation System

Scores abstracts using a rubric, returning JSON like:

{
  "clarity": 5,
  "formality": 5,
  "technical_specificity": 4,
  "structure": 5
}


This helps compare prompt versions and test consistency.

## Setup Instructions

### 1. Clone the repo
git clone https://github.com/soopersim/llm-ip-sandbox.git
cd llm-ip-sandbox

### 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install openai python-dotenv

### 4. Add your API key (.env file)
OPENAI_API_KEY=your_real_api_key_here

### Run the abstract generator
python main.py


This prints:

Plain patent abstract

Structured patent abstract

Both created from the same raw idea.

### Run the evaluation pipeline
python evaluator.py


This prints:

Abstract 1 + evaluation

Abstract 2 + evaluation

And uses the JSON-parsed results for comparison.

## Potential Future Improvements

Add retrieval (RAG) to ground abstracts in prior art

Add claims generation

Add multi-model evaluation

Add a simple UI in React for comparing outputs

Add automated benchmark datasets

Add token usage reporting + cost analysis
