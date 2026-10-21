import os, json, glob, urllib.request, urllib.error, datetime

TOKEN = os.environ["GITHUB_TOKEN"]
MODEL = "openai/gpt-4o-mini"
changed = []

for path in glob.glob("**/SKILL.md", recursive=True):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        continue
    end = text.find("\n---", 3)
    if end == -1 or "minutes_saved:" in text[:end]:
        continue
    prompt = (
        "You estimate the time value of an AI skill at a 250-person software company. "
        "Read the skill below. Estimate how many minutes a competent employee takes to do this task by hand, "
        "and how many minutes it takes using this skill with an AI assistant, including time to review the output. "
        "Be conservative. Reply with only JSON in this shape: "
        '{"manual_minutes": 0, "assisted_minutes": 0, "estimate_basis": "one sentence on your assumptions"}'
        "\n\nSKILL:\n" + text
    )
    body = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
    }).encode()
    req = urllib.request.Request(
        "https://models.github.ai/inference/chat/completions",
        data=body,
        headers={
            "Authorization": "Bearer " + TOKEN,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        out = json.load(urllib.request.urlopen(req, timeout=60))
    except urllib.error.HTTPError as e:
        print("Model call failed:", e.code, e.read().decode())
        raise
    reply = out["choices"][0]["message"]["content"]
    data = json.loads(reply[reply.find("{"): reply.rfind("}") + 1])
    manual = int(data["manual_minutes"])
    assisted = int(data["assisted_minutes"])
    basis = str(data["estimate_basis"]).replace('"', "'")
    fields = (
        f"\nmanual_minutes: {manual}"
        f"\nassisted_minutes: {assisted}"
        f"\nminutes_saved: {max(manual - assisted, 0)}"
        f'\nestimate_basis: "{basis}"'
        f"\nestimated_by: {MODEL} via GitHub Actions"
        f"\nestimated_on: {datetime.date.today()}"
    )
    open(path, "w", encoding="utf-8").write(text[:end] + fields + text[end:])
    changed.append(path)
    print("Estimated", path, manual, "->", assisted)

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"count={len(changed)}\n")
