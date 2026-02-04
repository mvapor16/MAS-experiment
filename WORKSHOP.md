# Multi-Agent Systems Workshop

Build your own AI-powered multi-agent system using ChatGPT and GitHub.

**Duration:** 1–1.5 hours hands-on  
**Requirements:** Browser, email address, credit card (for OpenAI API billing)

---

## Part A: Technical Setup

### Step 1: Create a GitHub Account (5 min)

Skip this step if you already have a GitHub account.

1. Go to [github.com](https://github.com)
2. Click **Sign up**
3. Enter your email, create a password, and choose a username
4. Complete the verification puzzle
5. Check your email and enter the verification code
6. You can skip the personalization questions

---

### Step 2: Fork the Workshop Repository (2 min)

Forking creates your own copy of the code that you can modify freely.

1. Go to the workshop repo:  
   **[github.com/marcodalessio80/MAS-experiment](https://github.com/marcodalessio80/MAS-experiment)**
2. Click the **Fork** button (top-right of the page)
3. On the "Create a new fork" page, keep the defaults and click **Create fork**
4. You now have your own copy at `github.com/YOUR-USERNAME/MAS-experiment`

---

### Step 3: Launch GitHub Codespaces (3 min)

Codespaces gives you a complete development environment in your browser — no installation needed.

1. In your forked repo, click the green **Code** button
2. Select the **Codespaces** tab
3. Click **Create codespace on main**
4. Wait 1-2 minutes for the environment to load
5. You'll see a VS Code-like editor in your browser

---

### Step 4: Get an OpenAI API Key (5 min)

You need an API key to let your agents call ChatGPT.

1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Click your profile icon (top-right) → **View API keys**
4. Click **Create new secret key**
5. Give it a name (e.g., "MAS Workshop") and click **Create**
6. **Copy the key immediately** — you won't see it again

**Important:** You also need to add billing:
1. Go to **Settings** → **Billing**
2. Click **Add payment method**
3. Add a credit card and set a usage limit (e.g., $5-10 for the workshop)

---

### Step 5: Configure Your Environment (2 min)

Back in your Codespace:

1. In the file explorer (left panel), right-click and select **New File**
2. Name it exactly: `.env`
3. Add this content (paste your actual API key):

```
OPENAI_API_KEY=sk-paste-your-key-here
```

4. Save the file (Ctrl+S or Cmd+S)

---

### Step 6: Install Dependencies and Run (2 min)

In the terminal at the bottom of Codespaces (if you don't see it, press Ctrl+` or go to View → Terminal):

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Run the multi-agent system:
```bash
python main.py
```

3. Enter a question when prompted, for example:
   - "What are the pros and cons of remote work?"
   - "Explain how solar panels work"

4. Watch the Manager, Researcher, and Writer agents collaborate!

---

## Part B: Design Your Own MAS

Now that you've seen the skeleton work, it's time to build your own multi-agent system. Use ChatGPT to help you design and implement it.

### Step 7: Choose a Use Case

Think about a task that could benefit from multiple specialized agents working together. Examples:

| Use Case | Possible Agents |
|----------|-----------------|
| Content creation | Researcher, Outliner, Writer, Editor |
| Decision support | Data Gatherer, Analyst, Devil's Advocate, Summarizer |
| Learning assistant | Explainer, Quiz Master, Feedback Coach |
| Code review | Reviewer, Security Checker, Documentation Writer |
| Travel planning | Destination Expert, Budget Analyst, Itinerary Builder |

---

### Step 8: Use ChatGPT to Design Your Agents

Open [chatgpt.com](https://chatgpt.com) and use prompts like these:

**To brainstorm agent roles:**
```
I want to build a multi-agent system that helps with [YOUR USE CASE].

Suggest 3-4 specialized agent roles. For each agent, tell me:
- Its name
- Its responsibility (one sentence)
- The tone/style of its output
```

**To generate the code for a new agent:**
```
Here's my current agents.py file:

[PASTE YOUR agents.py CONTENT]

Add a new agent called [AGENT NAME] that [DESCRIPTION OF WHAT IT DOES].
Keep the same code style and structure.
```

**To modify the orchestration flow:**
```
Here's my current main.py file:

[PASTE YOUR main.py CONTENT]

Modify the workflow so that:
- [DESCRIBE THE NEW FLOW, e.g., "the Editor reviews the Writer's output and sends feedback back to the Writer for revision"]
```

---

### Step 9: Implement Your Changes

Based on ChatGPT's suggestions:

1. **Edit `agents.py`** to add or modify agent functions
2. **Edit `main.py`** to change how agents interact
3. **Test frequently** — run `python main.py` after each change

**Tips:**
- Start small: add one agent at a time
- Keep system prompts short and specific
- If something breaks, ask ChatGPT to help debug by pasting the error message

---

### Step 10: Experiment and Iterate

Ideas to try:

- **Change agent personalities** — make the Writer formal vs. casual
- **Add a review loop** — have the Manager check the final output and request revisions
- **Create agent debate** — have two agents argue different perspectives before a Synthesizer combines them
- **Adjust the model** — try `gpt-4o` instead of `gpt-4o-mini` for more sophisticated responses (costs more)

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "No module named openai" | Run `pip install -r requirements.txt` |
| "Invalid API key" | Check your `.env` file — no quotes around the key, no extra spaces |
| "Rate limit exceeded" | Wait a minute and try again, or check your OpenAI billing/limits |
| Codespace won't start | Try refreshing the page or creating a new Codespace |
| Agents give unhelpful responses | Make the system prompts more specific |

---

## Quick Reference

**Files you'll edit:**
- `agents.py` — define agent roles and behaviors
- `main.py` — control the workflow between agents

**Commands you'll use:**
```bash
pip install -r requirements.txt   # Install packages (once)
python main.py                    # Run your MAS
```

**Useful ChatGPT prompts:**
- "Suggest agent roles for a MAS that does [X]"
- "Add a new agent to this code: [paste code]"
- "This error occurred: [paste error]. How do I fix it?"

---

## Next Steps After the Workshop

- Explore [OpenAI's function calling](https://platform.openai.com/docs/guides/function-calling) to give agents tools
- Look into [LangChain](https://python.langchain.com/) or [CrewAI](https://www.crewai.com/) for more advanced orchestration
- Add memory so agents remember previous interactions

---

**Questions?** Ask your facilitator or use ChatGPT to help troubleshoot!
