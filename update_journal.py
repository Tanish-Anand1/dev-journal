import os
import datetime
import urllib.request
import json

def fetch_tech_fact():
    # Attempt to fetch a programming quote or random fact to keep the auto-generated log educational
    try:
        url = "https://programming-quotes-api.herokuapp.com/Quotes/random"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            return f'*" {data["en"]} "* — **{data["author"]}**'
    except Exception:
        pass

    try:
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            return f'**Did you know?** {data["text"]}'
    except Exception:
        return "**Tip:** Focus on deep work and continuous learning. Write code every day!"

def main():
    today = datetime.date.today()
    year_str = today.strftime("%Y")
    month_str = today.strftime("%m")
    day_str = today.strftime("%d")

    # Create directory structure logs/YYYY/MM
    dir_path = os.path.join("logs", year_str, month_str)
    os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, f"{day_str}.md")

    if os.path.exists(file_path):
        print(f"Log for {today} already exists. Skipping auto-generation.")
        return

    fact = fetch_tech_fact()

    content = f"""# Dev Log — {today.strftime("%B %d, %Y")}

## Summary of the Day
*Self-directed study, engineering iterations, or project updates.*

## Key Focus Area
- [ ] AI & NLP Benchmarking
- [ ] Hardware / Edge systems
- [ ] Web application architectures
- [ ] Security research / Disclosures

## What I Learned / Tech Insight
{fact}

## Today's Contributions
- Automated system check & status reporting.
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated new dev log at {file_path}")

if __name__ == "__main__":
    main()
