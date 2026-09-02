#!/usr/bin/env python3
"""
Renders docs/assets/languages.svg from the real byte counts GitHub reports for
every public, non-fork repository.

Why this instead of one of the hosted stats cards: those run on somebody else's
free Vercel plan. At the time of writing github-readme-stats answers 503
(DEPLOYMENT_PAUSED) and both github-profile-trophy and
github-readme-activity-graph answer 402. A broken image on your profile is worse
than no image, so this repository generates its own and commits the result.

    python3 scripts/languages.py            # needs `gh` to be logged in
"""
import json
import pathlib
import subprocess
from collections import Counter

USER = "Mampiz"
OUT = pathlib.Path(__file__).resolve().parent.parent / "docs" / "assets" / "languages.svg"
TOP = 8

# GitHub's own language colours (github/linguist)
COLOURS = {
    "Go": "#00ADD8", "Python": "#3572A5", "TypeScript": "#3178c6",
    "JavaScript": "#f1e05a", "Shell": "#89e051", "Astro": "#ff5a03",
    "Makefile": "#427819", "Java": "#b07219", "CSS": "#663399",
    "HTML": "#e34c26", "C": "#555555", "C++": "#f34b7d",
    "Dockerfile": "#384d54", "Smarty": "#f0c040", "Mustache": "#724b3b",
    "Go Template": "#00ADD8", "Jinja": "#a52a22", "Nix": "#7e7eff",
}
FALLBACK = "#8b949e"


def gh(*args):
    return subprocess.run(["gh", *args], capture_output=True, text=True, check=True).stdout


def collect():
    repos = json.loads(gh("repo", "list", USER, "--limit", "100", "--no-archived",
                          "--source", "--json", "name,visibility,isFork"))
    totals = Counter()
    counted = 0
    for r in repos:
        if r["visibility"] != "PUBLIC" or r["isFork"]:
            continue
        try:
            totals.update(json.loads(gh("api", f"repos/{USER}/{r['name']}/languages")))
            counted += 1
        except subprocess.CalledProcessError:
            pass
    return totals, counted


def render(totals, repo_count):
    total = sum(totals.values())
    rows = totals.most_common(TOP)
    other = total - sum(v for _, v in rows)
    if other > 0:
        rows.append(("Other", other))

    W, BAR_Y, BAR_H, PAD = 860, 46, 14, 8
    cols, per_col = 3, (len(rows) + 2) // 3
    line_h, legend_y = 26, BAR_Y + BAR_H + 30
    H = legend_y + per_col * line_h + 6

    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" font-family="-apple-system,BlinkMacSystemFont,'
         f'Segoe UI,Helvetica,Arial,sans-serif">',
         f'<style>.t{{fill:#8b949e;font-size:13px}}.h{{fill:#8b949e;font-size:15px;'
         f'font-weight:600}}.p{{fill:#6e7681;font-size:12.5px}}</style>',
         f'<text x="0" y="18" class="h">Language mix</text>',
         f'<text x="0" y="18" class="p" text-anchor="end" transform="translate({W},0)">'
         f'{total/1e6:.1f} MB of code across {repo_count} public repositories</text>']

    # barra apilada, con esquinas redondeadas mediante clip
    p.append(f'<clipPath id="r"><rect x="0" y="{BAR_Y}" width="{W}" height="{BAR_H}" rx="7"/></clipPath>')
    p.append('<g clip-path="url(#r)">')
    x = 0.0
    for name, val in rows:
        w = val / total * W
        p.append(f'<rect x="{x:.2f}" y="{BAR_Y}" width="{w:.2f}" height="{BAR_H}" '
                 f'fill="{COLOURS.get(name, FALLBACK)}"/>')
        x += w
    p.append('</g>')

    col_w = W / cols
    for i, (name, val) in enumerate(rows):
        cx = (i // per_col) * col_w
        cy = legend_y + (i % per_col) * line_h
        pct = val / total * 100
        p.append(f'<circle cx="{cx+6:.1f}" cy="{cy:.1f}" r="6" fill="{COLOURS.get(name, FALLBACK)}"/>')
        p.append(f'<text x="{cx+20:.1f}" y="{cy+4.5:.1f}" class="t">{name}</text>')
        p.append(f'<text x="{cx+col_w-PAD-30:.1f}" y="{cy+4.5:.1f}" class="t" '
                 f'text-anchor="end">{pct:.1f}%</text>')
    p.append('</svg>')
    return "\n".join(p)


if __name__ == "__main__":
    totals, n = collect()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(totals, n))
    print(f"{OUT} written from {n} public repositories")
    for name, val in totals.most_common(TOP):
        print(f"  {name:14s} {val*100/sum(totals.values()):5.1f}%")
