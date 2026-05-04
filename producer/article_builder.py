"""
Article builder for One Happy Table producer.
Takes a pipeline article + loaded data, calls Claude, returns a markdown string.
"""

import anthropic
import json
import os
import yaml
from datetime import date
from pathlib import Path

def _get_amazon_tag() -> str:
    """AMAZON_TAG env var overrides site.config.yaml — matches Astro build behaviour."""
    if tag := os.environ.get("AMAZON_TAG"):
        return tag
    cfg_path = Path(__file__).parent.parent / "site.config.yaml"
    with open(cfg_path) as f:
        cfg = yaml.safe_load(f)
    return cfg["affiliate"]["amazon_tracking_id"]

AMAZON_TAG = _get_amazon_tag()


# ── Type-specific H2 templates ────────────────────────────────────────────────

H2_STRUCTURES = {
    "roundup":      "Our Top Picks → How We Chose → Full Reviews → What to Look For → FAQ",
    "review":       "Quick Verdict → What We Tested → Performance → Pros & Cons → Who Should Buy → FAQ",
    "comparison":   "Head-to-Head Verdict → Side-by-Side → Testing Notes → Who Each Is Best For → FAQ",
    "informational":"The Short Answer → What You Need to Know → Step-by-Step → Common Mistakes → FAQ",
    "buyer_guide":  "What to Look For → Our Top Picks → [3-5 specific criteria sections] → How to Choose → FAQ",
    # Title-case aliases
    "Roundup":      "Our Top Picks → How We Chose → Full Reviews → What to Look For → FAQ",
    "Review":       "Quick Verdict → What We Tested → Performance → Pros & Cons → Who Should Buy → FAQ",
    "Comparison":   "Head-to-Head Verdict → Side-by-Side → Testing Notes → Who Each Is Best For → FAQ",
    "Buyer Guide":  "What to Look For → Our Top Picks → [3-5 specific criteria sections] → How to Choose → FAQ",
}

TYPE_WORD_COUNTS = {
    "roundup": "2,000–2,500",
    "review": "1,800–2,200",
    "comparison": "1,800–2,200",
    "informational": "1,500–2,000",
    "buyer_guide": "2,200–2,800",
    "Roundup": "2,000–2,500",
    "Review": "1,800–2,200",
    "Comparison": "1,800–2,200",
    "Buyer Guide": "2,200–2,800",
}

SYSTEM = """You are a ghostwriter for One Happy Table, writing as Wendy Collins.

PERSONA: Wendy Collins. Interior design background, twenty years styling tables for events and private clients in Charleston, South Carolina. Hosts everything from casual weeknight dinners to large celebrations. Late 40s. She believes the right table makes every meal feel like a celebration, but she has zero patience for things that look good in a showroom and fall apart after two dinner parties.

VOICE:
- Direct and evaluative. She's tasted, handled, and hosted with these things. She tells you what she actually thinks.
- Specific: brand names, material names, care instructions. Never vague about quality.
- Comfortable saying something isn't worth it — a beautiful tablecloth that wrinkles in the wash is not worth it.
- Warm but not gushing. She genuinely loves hosting, but she's not going to overclaim about a dinner plate.
- Peer-voice — assumes the reader is a capable adult who sets a nice table and wants honest guidance.

VOICE TECHNIQUES — use these actively, not occasionally:

1. USE PRICE BANDS, NOT DOLLAR FIGURES. Amazon pricing changes constantly and showing specific dollar amounts violates affiliate program terms. Instead: reference budget / mid-range / premium framing in plain language. "At the budget end of the market" or "mid-range pricing for what you get" or "one of the more expensive options here." For comparisons, use relative language: "costs roughly twice as much as the Threshold set." Never write "$85" or "around $120-$150" or any specific dollar figure. If price matters to the verdict, say so. Direct readers to Amazon for current pricing ("check current price on Amazon").

2. SELF-AWARE ASIDES. Wendy occasionally steps back from the review voice with a brief aside. Dry, never cute. "(I've hosted forty guests on these)" or "(learned this the hard way)" or "which is, I admit, a very specific complaint" or "your guests will not notice this, but you will." One or two per article.

3. ADDRESS THE READER'S ACTUAL SITUATION. Not "great for dinner parties" but "if you've ever served guests on plates that look slightly wrong together because you bought different sets at different times, this solves that." Frame features as solutions to specific hosting moments the reader will recognise.

4. CATCH YOURSELF. Occasionally Wendy starts prescriptively and qualifies it. "If that matters to you" or "though I appreciate not everyone hosts at that scale." Not hedging a verdict, just a person with one dining room acknowledging other people have different ones.

5. COMPETITOR SPECIFICITY. Name the competing product she's comparing against. "Compared to the Williams Sonoma Brasserie collection, which I've used for years." Not generic "other options" — actual product names where she'd know them.

BANNED WORDS: unlock, navigate, navigating, journey, transformative, holistic, robust, seamless, dive deep, elevate, game-changer, genuinely, truly, certainly, impressive, comprehensive, nuanced, leverage, crucial, essential, vital

BANNED PHRASES: "the key is", "here's what", "moving forward", "you're not alone", "the good news is", "research shows", "studies show", "it's worth noting", "with that in mind", "at its core", "when it comes to", "in terms of", "not only... but also", "whether you're a", "one thing to keep in mind", "that said", "all in all", "now let's", "let's take a look"

AVOID THESE PATTERNS — they mark AI-generated text:
- False balance: never hedge a clear verdict. If one product is better, say so.
- Transition announcements: never write a sentence whose only job is to announce the next section.
- Pre-explaining obvious context: do not explain what a tablecloth is to someone shopping for tablecloths.
- Summarising conclusions: do not recap what you just wrote. End sections on a specific opinion or detail.
- Parallel list padding: not every section needs 3 items. Vary list lengths.
- Overusing "This": avoid starting consecutive sentences with "This means...", "This makes...", "This allows...".
- "You'll want to..." / "You'll find that...": Wendy doesn't narrate the reader's experience.

FORMATTING:
- H1: article title only (do not include in body)
- H2 for all main sections
- H3 for subsections under H2
- ABSOLUTELY NO em dashes (—) or double dashes (--) anywhere in the text. This is a hard rule. Instead: use a period and start a new sentence, use a comma, or use parentheses.
- No colons to introduce lists or clauses mid-sentence. Use a period instead.
- No semicolons joining two clauses. Use "but", "and", or a period instead.
- No horizontal rules.
- FAQ section: exactly 5 Q&A pairs.

LANGUAGE: American English throughout. No exceptions.
- color, flavor, honor, neighbor (not colour, flavour, honour, neighbour)
- realize, recognize, organize, prioritize (not realise, recognise, organise, prioritise)
- center, meter, fiber (not centre, metre, fibre)
- gray (not grey)
- while (not whilst), among (not amongst), toward (not towards)
- traveling, canceled, labeled (not travelling, cancelled, labelled)

OUTPUT FORMAT: Return the article body only (no frontmatter). Start with the intro paragraph directly. Use markdown headings."""


def build_products_brief(article: dict, products: dict) -> str:
    """Build a concise product brief for the prompt."""
    lines = []
    for key in article.get("products", []):
        p = products.get(key)
        if not p:
            continue
        lines.append(
            f"- **{p['name']}** (slug: `{key}`)\n"
            f"  Brand: {p.get('brand','')} | Price band: {p.get('price_band','')} | Link: [product:{key}]\n"
            f"  Pros: {'; '.join(p.get('default_pros',[]))}\n"
            f"  Cons: {'; '.join(p.get('default_cons',[]))}\n"
            f"  Writer notes: {p.get('notes_for_writers','')}"
        )
    return "\n\n".join(lines) if lines else "No products assigned."


def build_eeat_brief(eeat: dict) -> str:
    lines = []
    if eeat.get("experiences"):
        lines.append("WENDY'S RELEVANT EXPERIENCES:")
        for e in eeat["experiences"]:
            lines.append(f"- {e.get('story','')}")
    if eeat.get("failures"):
        lines.append("\nWENDY'S FAILURES TO REFERENCE:")
        for f in eeat["failures"]:
            lines.append(f"- {f.get('lesson','')}")
    if eeat.get("opinions"):
        lines.append("\nWENDY'S STRONG OPINIONS:")
        for o in eeat["opinions"]:
            lines.append(f"- {o.get('opinion','')}")
    return "\n".join(lines)


def build_prompt(article: dict, products: dict, eeat: dict, persona: dict) -> str:
    article_type = article["type"]
    h2_structure = article.get("h2_structure") or H2_STRUCTURES.get(article_type, "")
    word_count = TYPE_WORD_COUNTS.get(article_type, "1,800–2,200")

    products_brief = build_products_brief(article, products)
    eeat_brief = build_eeat_brief(eeat)
    all_slugs = sorted(products.keys())

    hub_url = article.get("hub_url", f"/{article.get('hub_slug','')}/")
    hub_label = article.get("hub_label", "")
    category_label = article.get("category_label", "")

    # For comparison articles, identify the two products
    comparison_note = ""
    if article_type == "Comparison" and len(article.get("products", [])) >= 2:
        p_keys = article["products"]
        p1 = products.get(p_keys[0], {})
        p2 = products.get(p_keys[1], {})
        comparison_note = f"\nThis is a head-to-head comparison: **{p1.get('name','Product A')}** vs **{p2.get('name','Product B')}**."

    # Sibling articles in same cluster that are already published
    siblings = article.get("_siblings", [])
    sibling_block = ""
    if siblings:
        sibling_lines = "\n".join(
            f'- [{s["keyword"].title()}](/{s["slug"]}/)'
            for s in siblings[:6]
        )
        sibling_block = f"""
INTERNAL LINKS — SIBLING ARTICLES:
These articles are already published on the site in the same topic area.
Link to 2-3 of them naturally where relevant in the body — not in a list, but as contextual anchor text mid-sentence.
{sibling_lines}
"""

    prompt = f"""Write a {article_type} article for One Happy Table.

TARGET KEYWORD: {article['keyword']}
ARTICLE TYPE: {article_type}
ANGLE / PERSONA HOOK: {article['angle']}
TARGET WORD COUNT: {word_count} words
CATEGORY: {category_label}
HUB: {hub_label} ({hub_url})
{comparison_note}

H2 STRUCTURE TO FOLLOW:
{h2_structure}

PRODUCTS TO COVER:
{products_brief}

{eeat_brief}

HUB LINK REQUIREMENT:
Include a contextual link to the hub page ({hub_url} — "{hub_label}") at least twice:
once naturally in the first half of the article (before or just after the first H2),
and once in the second half (before the FAQ or in a closing paragraph).
Use varied phrasing — don't repeat the same anchor text.
{sibling_block}
AFFILIATE LINKS:
When mentioning a product by name, link using its slug from products.yaml — NOT a raw Amazon URL.
Format: [Product Name](product:slug)
Example: [Costa Nova Nova White 5-piece Set](product:costa-nova-nova-white-5pc)

IMPORTANT SLUG RULES:
- Only use slugs from the list below. Do not invent or guess slugs.
- If the product you want to recommend is not in this list, omit the link or omit the product.
- Never write amazon.com, dp/, ASIN, or ?tag= anywhere in the article body.

AVAILABLE PRODUCT SLUGS:
{chr(10).join(f'  {s}' for s in all_slugs)}

FAQ SECTION:
End with an H2 "Frequently Asked Questions" section containing exactly 5 Q&A pairs.
Use H3 for each question. Questions should be the kind a real buyer would search.

Write the full article body now. Do not include frontmatter. Start with the intro paragraph."""

    return prompt


def generate_title_and_desc(article: dict, body: str, client: anthropic.Anthropic) -> tuple:
    """Draft a title (<65 chars) and meta description (150-160 chars) from the article body."""
    prompt = f"""Write a title and meta description for this article.

Keyword: {article['keyword']}
Type: {article['type']}
Article opening:
{body[:600]}

Rules:
- Title: under 65 characters, keyword near the front, specific and honest (no "ultimate", no "best ever")
- Meta description: 150–160 characters exactly, plain sentence, no em dashes, no exclamation marks

Return JSON only:
{{"title": "...", "description": "..."}}"""

    resp = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}],
    )
    text = resp.content[0].text.strip()
    start = text.find("{")
    end = text.rfind("}") + 1
    data = json.loads(text[start:end])
    return data.get("title", ""), data.get("description", "")


def generate_article(article: dict, products: dict, eeat: dict, persona: dict,
                     client: anthropic.Anthropic) -> tuple:
    """Returns (body_text, title, description)."""
    prompt = build_prompt(article, products, eeat, persona)

    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )
    body = resp.content[0].text.strip()
    body = _fix_punctuation(body)
    body = _americanize(body)
    title, description = generate_title_and_desc(article, body, client)
    return body, title, description


def _americanize(text: str) -> str:
    """Convert British spellings to American English."""
    import re
    replacements = [
        # -our → -or
        (r'\bcolours?\b', lambda m: 'colors' if m.group().endswith('s') else 'color'),
        (r'\bcolour(ed|ing|ful|less|s)?\b', lambda m: 'color' + (m.group(1) or '')),
        (r'\bflavours?\b', lambda m: 'flavors' if m.group().endswith('s') else 'flavor'),
        (r'\bhonours?\b', lambda m: 'honors' if m.group().endswith('s') else 'honor'),
        (r'\bhumours?\b', lambda m: 'humors' if m.group().endswith('s') else 'humor'),
        (r'\blabours?\b', lambda m: 'labors' if m.group().endswith('s') else 'labor'),
        (r'\bneighbou?rs?\b', lambda m: 'neighbors' if m.group().endswith('s') else 'neighbor'),
        (r'\bfavou?r(ite|s|ed|ing)?\b', lambda m: 'favor' + (m.group(1) or '')),
        # -ise → -ize
        (r'\brealise(d|s|r|rs|ing)?\b', lambda m: 'realize' + (m.group(1) or '')),
        (r'\brecognise(d|s|r|rs|ing)?\b', lambda m: 'recognize' + (m.group(1) or '')),
        (r'\borganise(d|s|r|rs|ing|ation|ations)?\b', lambda m: 'organize' + (m.group(1) or '')),
        (r'\bprioritise(d|s|ing)?\b', lambda m: 'prioritize' + (m.group(1) or '')),
        (r'\bminimise(d|s|ing)?\b', lambda m: 'minimize' + (m.group(1) or '')),
        (r'\bmaximise(d|s|ing)?\b', lambda m: 'maximize' + (m.group(1) or '')),
        (r'\bemphasise(d|s|ing)?\b', lambda m: 'emphasize' + (m.group(1) or '')),
        (r'\bspecialise(d|s|ing)?\b', lambda m: 'specialize' + (m.group(1) or '')),
        (r'\bcentralise(d|s|ing)?\b', lambda m: 'centralize' + (m.group(1) or '')),
        # -re → -er
        (r'\bcentre(d|s|ing)?\b', lambda m: 'center' + (m.group(1) or '')),
        (r'\bmetres?\b', lambda m: 'meters' if m.group().endswith('s') else 'meter'),
        (r'\bfibres?\b', lambda m: 'fibers' if m.group().endswith('s') else 'fiber'),
        (r'\btheatres?\b', lambda m: 'theaters' if m.group().endswith('s') else 'theater'),
        # -ise spellings (nouns)
        (r'\bfertiliser(s)?\b', lambda m: 'fertilizer' + (m.group(1) or '')),
        (r'\bfertilise(d|s|ing)?\b', lambda m: 'fertilize' + (m.group(1) or '')),
        # doubled consonants
        (r'\btravell(ing|ed|er|ers)\b', lambda m: 'travel' + m.group(1)),
        (r'\bcancell(ed|ing)\b', lambda m: 'cancel' + m.group(1)),
        (r'\blabelled?\b', 'labeled'),
        (r'\bchannelled?\b', 'channeled'),
        (r'\bcatalogued?\b', 'cataloged'),
        # misc
        (r'\baluminium\b', 'aluminum'),
        (r'\bgrey\b', 'gray'),
        (r'\bGrey\b', 'Gray'),
        (r'\bwhilst\b', 'while'),
        (r'\bamongst\b', 'among'),
        (r'\btowards\b', 'toward'),
        (r'\bafterwards\b', 'afterward'),
        (r'\bdefence\b', 'defense'),
        (r'\blicence\b', 'license'),
        (r'\bpractise\b', 'practice'),
        (r'\btyre(s)?\b', lambda m: 'tires' if m.group().endswith('s') else 'tire'),
        (r'\bkerb(s)?\b', lambda m: 'curbs' if m.group().endswith('s') else 'curb'),
    ]
    for pattern, repl in replacements:
        if callable(repl):
            text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
        else:
            text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
    return text


def _fix_punctuation(text: str) -> str:
    """Hard-fix punctuation and banned phrases the model generates despite instructions."""
    import re

    # Em dash variants → comma
    text = text.replace('\u2014', ',')
    text = text.replace('\u2013', ',')
    text = text.replace('---', ',')
    text = text.replace(' -- ', ', ')
    text = text.replace('--', ',')

    # Clean up double spaces or orphaned commas/parens
    text = re.sub(r'\(\s*\)', '', text)          # empty parens
    text = re.sub(r',\s*\)', ')', text)          # (which , qualifies)
    text = re.sub(r'\(\s*,', '(', text)
    text = re.sub(r',\s*,', ',', text)
    text = re.sub(r',\s*\.', '.', text)
    text = re.sub(r'[^\S\n]{2,}', ' ', text)    # double spaces (preserve newlines)

    return text


def build_review_txt(article: dict, body: str, title: str, description: str) -> str:
    """Clean .txt file for human review and editing. No YAML, no noise."""
    products_line = ", ".join(article.get("products", [])) or "none"
    return f"""TITLE: {title}
DESC: {description}

---
Article ID {article['id']} | {article['type']} | Cluster: {article['cluster']}
Hub: {article.get('hub_label','')} ({article.get('hub_url','')}) | KD: {article.get('kd',0)} | Vol: {article.get('volume',0)}
Products: {products_line}
---

{body}
"""


def build_frontmatter(article: dict, products: dict, title: str, description: str) -> str:
    """Build YAML frontmatter for the article .md file."""
    today = date.today().isoformat()
    article_type = article["type"].lower().replace(" ", "_")
    if article_type == "buyer_guide":
        layout_type = "buyer_guide"
    else:
        layout_type = article_type

    # Build products list
    prod_refs = []
    assigned_keys = article.get("products", [])
    if article_type == "comparison" and len(assigned_keys) >= 2:
        roles = ["primary", "alternative"]
    elif article_type == "roundup":
        roles = ["best_overall"] + ["also_consider"] * (len(assigned_keys) - 1)
    elif article_type == "review":
        roles = ["primary"]
    elif article_type == "buyer_guide":
        roles = ["best_overall"] + ["also_consider"] * (len(assigned_keys) - 1)
    else:
        roles = ["also_consider"] * len(assigned_keys)

    for i, key in enumerate(assigned_keys):
        role = roles[i] if i < len(roles) else "also_consider"
        p = products.get(key, {})
        def _cy(s): return s.replace('\u2014', ',').replace('\u2013', ',').replace('"', '\\"')
        pros = [_cy(x) for x in p.get("default_pros", [])[:2]]
        cons = [_cy(x) for x in p.get("default_cons", [])[:1]]
        ref = f'  - id: "{key}"\n    role: "{role}"'
        if pros:
            ref += f'\n    article_specific_pros:\n' + "\n".join(f'      - "{pr}"' for pr in pros)
        if cons:
            ref += f'\n    article_specific_cons:\n' + "\n".join(f'      - "{c}"' for c in cons)
        prod_refs.append(ref)

    products_yaml = "\n".join(prod_refs) if prod_refs else "  []"

    # Comparison-specific fields
    comparison_fields = ""
    if article_type == "comparison" and len(assigned_keys) >= 2:
        comparison_fields = f"""product_a: "{assigned_keys[0]}"
product_b: "{assigned_keys[1]}"
# winner: product_a  # SET THIS after review
# winner_reason: ""  # SET THIS after review
"""

    # Tags derived from cluster + type
    cluster = article.get("cluster", "")
    tags = [cluster, article["type"].lower()]

    def _clean_yaml(s: str) -> str:
        return s.replace('\u2014', ',').replace('\u2013', ',').replace('"', '\\"')

    safe_title = _clean_yaml(title) if title else article['keyword'].title()
    safe_desc = _clean_yaml(description) if description else ""
    hub = article.get("hub_slug", article.get("hub", ""))
    img_n = (article.get("id", 1) - 1) % 8 + 1
    hero_image = article.get('hero_image') or f"articles/{hub}-{img_n}.jpg"
    hero_alt = _clean_yaml(article.get('hero_image_alt', '') or safe_title)

    # Clean em dashes from product pros/cons
    for ref_block in prod_refs:
        pass  # already in string form; clean inline below

    fm = f"""---
title: "{safe_title}"
slug: "{article['slug']}"
type: "{layout_type}"
date: {today}
author: "wendy"
category: "home-entertaining"
hub: "{article.get('hub_slug', '')}"
hero_image: "{hero_image}"
hero_image_alt: "{hero_alt}"
description: "{safe_desc}"
target_keyword: "{article['keyword']}"
products:
{products_yaml}
tags: {json.dumps(tags)}
disclosure_required: true
noindex: false
{comparison_fields}---

"""
    return fm
