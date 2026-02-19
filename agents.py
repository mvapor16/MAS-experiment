import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
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
You are a TCM Planner agent.

Create a structured lesson plan.

Output format:

Domain:
Subskill:
Learning Objective:
Audience Level:
Instructions for Lesson Builder:
"""
    messages = [{"role": "user", "content": query}]
    return call_agent(system_prompt, messages)


def researcher(plan):
    system_prompt = """
You are a Lesson Builder agent.

Create lesson content.

Output format:

Concept Explanation:
Example Scenario:
Try This:
Reflection Question:
"""
    messages = [{"role": "user", "content": plan}]
    return call_agent(system_prompt, messages)


def writer(draft_lesson):
    system_prompt = """
You are an Editor.

Format lesson:

Title:
Why This Matters:
Concept:
Example in Practice:
Try This:
Reflection:
"""
    messages = [{"role": "user", "content": draft_lesson}]
    return call_agent(system_prompt, messages)


def qa_agent(final_lesson):
    system_prompt = """
You are QA.

Check:
- TCM relevance
- Scenario present
- Actionable
- Under 250 words

Respond PASS or REVISE.
"""
    messages = [{"role": "user", "content": final_lesson}]
    return call_agent(system_prompt, messages)
