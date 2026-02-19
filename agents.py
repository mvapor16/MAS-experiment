import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")  # new

client = OpenAI(
    api_key=api_key,
    base_url=base_url,  # will be None if not set, which is fine
)

def call_agent(system_prompt, messages):
    full_messages = [{"role": "system", "content": system_prompt}] + messages
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=full_messages,
    )
    return response.choices[0].message.content

def manager(query):
    system_prompt = """
You are a TCM Planner agent for a Learning Design Upskilling System.

Your job is to create a structured lesson plan based on the D2 Technical Competency Model.

Instructions:
1. Identify a relevant competency domain and sub-skill based on the user query.
2. If the user does not specify a competency, choose one that would be valuable for Learning Designers.
3. Define one clear learning objective.
4. Define the target audience level (early-tenure, mid-level, or senior).
5. Provide clear instructions for the Lesson Builder agent about what content to generate.

Output format (plain text):

Domain:
Subskill:
Learning Objective:
Audience Level:
Instructions for Lesson Builder:
"""
    messages = [{"role": "user", "content": query}]
    return call_agent(system_prompt, messages)

def researcher(task):
    system_prompt = """
You are a Lesson Builder agent for a Learning Design Upskilling System.

You receive a structured lesson plan from the Planner agent.

Your job is to create draft lesson content grounded in the D2 Technical Competency Model.

Requirements:
- Explain the concept clearly
- Reference the competency and sub-skill
- Provide a realistic D2 scenario (e.g., stakeholder alignment, kickoff, design decisions, measurement)
- Propose ONE practical action the learner can take
- Include ONE reflection question

Output format:

Concept Explanation:
Example Scenario:
Try This:
Reflection Question:
"""
    messages = [{"role": "user", "content": task}]
    return call_agent(system_prompt, messages)

def writer(summary_notes):
    system_prompt = """
You are an Editor and Formatter agent for a Learning Design Upskilling System.

Your job is to convert draft lesson content into a polished micro-lesson.

Formatting Rules:
- Follow the exact structure below
- Keep total length between 150 and 250 words
- Be concise and practical
- Remove filler language
- Maintain professional tone

Final Output Format:

Title:

Why This Matters:

Concept:

Example in Practice:

Try This:

Reflection:
"""
    messages = [{"role": "user", "content": summary_notes}]
    return call_agent(system_prompt, messages)
