import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_event(question: str, outcomes: list[str]) -> float:
    """Ask LLM for probability estimation"""
    prompt = f"""
    Analyze this Polymarket event:
    Question: "{question}"
    Possible outcomes: {outcomes}
    Estimate the probability that the first outcome will occur (as a percentage).
    """
    resp = client.chat.completions.create(
        model="gpt-4o-mini",  # можно заменить на DeepSeek, Gemini и т.д.
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    text = resp.choices[0].message.content
    # простейший парсинг процента
    import re
    m = re.search(r"(\d{1,3})%", text)
    return float(m.group(1)) / 100 if m else 0.5
