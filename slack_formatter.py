def format_for_slack(lesson_text, domain, subskill):
    slack_message = f"""
🧠 *TCM Micro-Lesson*

*Domain:* {domain}  
*Focus:* {subskill}

{lesson_text}

—
_Reply in thread with a moment you applied this 👇_
"""
    return slack_message
