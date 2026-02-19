import os
from dotenv import load_dotenv
load_dotenv()

import argparse
from datetime import datetime

from agents import manager, researcher, writer, qa_agent
from catalog import get_random_domain_and_subskill
from slack_formatter import format_for_slack


def run_workflow():
    parser = argparse.ArgumentParser(description="TCM Upskilling Engine")
    parser.add_argument("--level", type=str)
    args = parser.parse_args()

    # 🎲 Random competency
    domain, subskill = get_random_domain_and_subskill()

    user_query = f"""
Generate a micro-lesson.

Domain: {domain}
Subskill: {subskill}
Level: {args.level or "general"}
"""

    print("\n=== USER REQUEST ===")
    print(user_query.strip())

    print("\n[PLANNER]")
    plan = manager(user_query)
    print(plan)

    print("\n[LESSON BUILDER]")
    draft = researcher(plan)
    print(draft)

    print("\n[EDITOR]")
    final_lesson = writer(draft)
    print("\n=== FINAL LESSON ===")
    print(final_lesson)

    print("\n[QA]")
    qa_result = qa_agent(final_lesson)
    print(qa_result)

    # Save lesson
    os.makedirs("outputs", exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"outputs/{date_str}_{domain.replace(' ','_')}_{subskill.replace(' ','_')}.md"

    with open(filename, "w") as f:
        f.write(final_lesson)

    print(f"\nSaved to {filename}")

    # Slack output
    slack_message = format_for_slack(final_lesson, domain, subskill)

    print("\n=== SLACK READY ===")
    print(slack_message)


if __name__ == "__main__":
    run_workflow()
