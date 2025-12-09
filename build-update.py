import sys
import re

css_file = sys.argv[1]

update_file = False

with open(css_file, "r", encoding="utf-8") as css:
    css_content = css.readlines()

for line_index, line in enumerate(css_content):
    if "https://cdn.jsdelivr.net/gh/Mozza7/CX-BDC" in line:
        version = sys.argv[2]
        new_line = re.sub(r"(https://cdn\.jsdelivr\.net/gh/Mozza7/CX-BDC)@[^/]+", f"\\1@{version}", line)
        
        if new_line != line:
            css_content[line_index] = new_line
            update_file = True

if update_file:
    with open(css_file, "w", encoding="utf-8") as f:
        f.writelines(css_content)
