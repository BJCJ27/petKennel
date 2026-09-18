"""Generate happy/sad SVG face images for each kennel pet.

Run from repo root:  python3 scripts/generate_pets.py
Outputs 2 files per pet into src/assets/pets/ (e.g. dog-happy.svg, dog-sad.svg).
The SVGs are self-contained (no external assets), so images always render.
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "src", "assets", "pets")
os.makedirs(OUT, exist_ok=True)

# Each pet: base fur color, inner-ear/cheek accent, and an ear drawing.
# Ears are drawn behind the head (cx=100, cy=110, r=70).
PETS = {
    "dog": {
        "fur": "#c8935f", "accent": "#a9713f", "nose": "#4a2f1a",
        "ears": '''
        <ellipse cx="45" cy="120" rx="24" ry="46" fill="{accent}" transform="rotate(-18 45 120)"/>
        <ellipse cx="155" cy="120" rx="24" ry="46" fill="{accent}" transform="rotate(18 155 120)"/>''',
        "extra": '''<ellipse cx="100" cy="150" rx="34" ry="26" fill="#f3e2cf"/>''',
    },
    "cat": {
        "fur": "#f0a94b", "accent": "#f7d19a", "nose": "#d76b6b",
        "ears": '''
        <polygon points="48,58 40,8 92,52" fill="{fur}"/>
        <polygon points="152,58 160,8 108,52" fill="{fur}"/>
        <polygon points="55,54 52,22 82,52" fill="{accent}"/>
        <polygon points="145,54 148,22 118,52" fill="{accent}"/>''',
        "extra": '''
        <line x1="20" y1="120" x2="70" y2="126" stroke="#7a5a2a" stroke-width="2"/>
        <line x1="20" y1="134" x2="70" y2="134" stroke="#7a5a2a" stroke-width="2"/>
        <line x1="180" y1="120" x2="130" y2="126" stroke="#7a5a2a" stroke-width="2"/>
        <line x1="180" y1="134" x2="130" y2="134" stroke="#7a5a2a" stroke-width="2"/>''',
    },
    "bunny": {
        "fur": "#d8d2ec", "accent": "#f4c6d8", "nose": "#e08aa6",
        "ears": '''
        <ellipse cx="74" cy="40" rx="16" ry="46" fill="{fur}" transform="rotate(-10 74 40)"/>
        <ellipse cx="126" cy="40" rx="16" ry="46" fill="{fur}" transform="rotate(10 126 40)"/>
        <ellipse cx="74" cy="42" rx="7" ry="32" fill="{accent}" transform="rotate(-10 74 42)"/>
        <ellipse cx="126" cy="42" rx="7" ry="32" fill="{accent}" transform="rotate(10 126 42)"/>''',
        "extra": "",
    },
    "fox": {
        "fur": "#e8743c", "accent": "#fbeee3", "nose": "#3a2a22",
        "ears": '''
        <polygon points="46,60 44,6 96,50" fill="{fur}"/>
        <polygon points="154,60 156,6 104,50" fill="{fur}"/>
        <polygon points="55,54 54,24 84,50" fill="#3a2a22"/>
        <polygon points="145,54 146,24 116,50" fill="#3a2a22"/>''',
        "extra": '''<path d="M100 96 Q64 150 100 176 Q136 150 100 96 Z" fill="{accent}"/>''',
    },
}

def svg(pet, mood):
    p = PETS[pet]
    ears = p["ears"].format(**p)
    extra = p["extra"].format(**p)
    if mood == "happy":
        eyes = '''
        <path d="M74 116 Q84 106 94 116" stroke="#2a2a2a" stroke-width="5" fill="none" stroke-linecap="round"/>
        <path d="M106 116 Q116 106 126 116" stroke="#2a2a2a" stroke-width="5" fill="none" stroke-linecap="round"/>'''
        mouth = '''<path d="M84 150 Q100 168 116 150" stroke="#2a2a2a" stroke-width="4" fill="none" stroke-linecap="round"/>
        <path d="M92 152 Q100 162 108 152 Z" fill="#e08aa6"/>'''
        cheeks = '''<circle cx="66" cy="140" r="8" fill="#f6a6b8" opacity="0.7"/>
        <circle cx="134" cy="140" r="8" fill="#f6a6b8" opacity="0.7"/>'''
        tear = ""
    else:  # sad
        eyes = '''
        <circle cx="84" cy="118" r="6" fill="#2a2a2a"/>
        <circle cx="116" cy="118" r="6" fill="#2a2a2a"/>
        <path d="M74 106 Q84 102 94 108" stroke="#2a2a2a" stroke-width="4" fill="none" stroke-linecap="round"/>
        <path d="M106 108 Q116 102 126 106" stroke="#2a2a2a" stroke-width="4" fill="none" stroke-linecap="round"/>'''
        mouth = '''<path d="M84 160 Q100 146 116 160" stroke="#2a2a2a" stroke-width="4" fill="none" stroke-linecap="round"/>'''
        cheeks = ""
        tear = '''<path d="M84 126 q-6 12 0 18 q6 -6 0 -18 Z" fill="#6fc3e8"/>'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200" role="img" aria-label="{pet} looking {mood}">
  <rect width="200" height="200" rx="24" fill="{'#fff6ea' if mood=='happy' else '#eef2f6'}"/>
  {ears}
  <circle cx="100" cy="112" r="70" fill="{p['fur']}"/>
  {extra}
  {eyes}
  {cheeks}
  <ellipse cx="100" cy="140" rx="9" ry="7" fill="{p['nose']}"/>
  {mouth}
  {tear}
</svg>
'''

for pet in PETS:
    for mood in ("happy", "sad"):
        path = os.path.join(OUT, f"{pet}-{mood}.svg")
        with open(path, "w") as f:
            f.write(svg(pet, mood))
        print("wrote", os.path.relpath(path))
print("done")
