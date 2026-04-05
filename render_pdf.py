#!/usr/bin/env python3
"""Render the Technical Note markdown to a styled academic PDF."""

import re
import markdown
from weasyprint import HTML

INPUT = "EXPERIMENTAL_CORROBORATION_NOTE.md"
OUTPUT = "EXPERIMENTAL_CORROBORATION_NOTE.pdf"

with open(INPUT, "r") as f:
    md_text = f.read()

# Convert LaTeX math to Unicode/HTML before markdown processing.
# Display equation: the winding number integral
md_text = md_text.replace(
    r"$$l = \frac{1}{2\pi} \oint \nabla\phi \cdot d\mathbf{l}$$",
    '<p style="text-align:center; font-style:italic; font-size:12pt; '
    'margin:0.8em 0;">'
    '<i>l</i> = (1/2\u03c0) \u222e \u2207\u03c6 \u00b7 d<b>l</b>'
    '</p>'
)

# Inline math: $l$ -> italic l, $c$ -> italic c, etc.
# Match $...$ but not $$...$$
md_text = re.sub(
    r'(?<!\$)\$([^$]+)\$(?!\$)',
    r'<i>\1</i>',
    md_text,
)

# Clean up superscripts in density projections: 10^{15} etc.
md_text = md_text.replace("$", "")  # remove any stray dollar signs

html_body = markdown.markdown(
    md_text,
    extensions=["tables", "smarty", "md_in_html"],
)

html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
@page {{
    size: A4;
    margin: 2.5cm 2.5cm 3cm 2.5cm;
    @bottom-center {{
        content: counter(page);
        font-family: "Times New Roman", "DejaVu Serif", Georgia, serif;
        font-size: 10pt;
        color: #555;
    }}
}}

body {{
    font-family: "Times New Roman", "DejaVu Serif", Georgia, serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #1a1a1a;
    max-width: 100%;
}}

h1 {{
    font-size: 16pt;
    font-weight: bold;
    text-align: center;
    margin-top: 0.5cm;
    margin-bottom: 0.3cm;
    line-height: 1.3;
}}

h1:first-of-type {{
    font-size: 15pt;
    margin-bottom: 0.1cm;
}}

h2 {{
    font-size: 13pt;
    font-weight: bold;
    margin-top: 1.2em;
    margin-bottom: 0.5em;
    border-bottom: 0.5pt solid #ccc;
    padding-bottom: 0.2em;
}}

h3 {{
    font-size: 11.5pt;
    font-weight: bold;
    margin-top: 1em;
    margin-bottom: 0.4em;
}}

p {{
    text-align: justify;
    margin-bottom: 0.6em;
    orphans: 3;
    widows: 3;
}}

blockquote {{
    margin: 0.8em 1.5cm;
    padding-left: 0.5cm;
    border-left: 2pt solid #999;
    font-style: italic;
    color: #333;
}}

table {{
    border-collapse: collapse;
    width: 100%;
    margin: 0.8em 0;
    font-size: 10pt;
}}

th, td {{
    border: 0.5pt solid #999;
    padding: 4pt 8pt;
    text-align: left;
}}

th {{
    background-color: #f0f0f0;
    font-weight: bold;
}}

tr:nth-child(even) {{
    background-color: #fafafa;
}}

a {{
    color: #1a5276;
    text-decoration: none;
}}

hr {{
    border: none;
    border-top: 0.5pt solid #ccc;
    margin: 1.2em 0;
}}

code {{
    font-family: "DejaVu Sans Mono", "Courier New", monospace;
    font-size: 9.5pt;
    background: #f5f5f5;
    padding: 1pt 3pt;
    border-radius: 2pt;
}}

em {{
    font-style: italic;
}}

strong {{
    font-weight: bold;
}}

/* Title block styling */
body > h1:first-child {{
    font-size: 15pt;
    text-transform: uppercase;
    letter-spacing: 0.3pt;
}}

body > h1:first-child + h2 {{
    font-size: 11pt;
    font-weight: normal;
    font-style: italic;
    text-align: center;
    border-bottom: none;
    margin-bottom: 1cm;
}}

/* Abstract heading */
h1:nth-of-type(2) {{
    font-size: 13pt;
    text-align: left;
}}

/* Keep references and metadata compact */
h1:last-of-type {{
    font-size: 13pt;
    text-align: left;
}}

/* Equation-like content */
p > code {{
    font-size: 10pt;
}}

/* Lists */
ul, ol {{
    margin-bottom: 0.6em;
    padding-left: 1.2cm;
}}

li {{
    margin-bottom: 0.3em;
}}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

HTML(string=html_doc).write_pdf(OUTPUT)
print(f"Written: {OUTPUT}")
