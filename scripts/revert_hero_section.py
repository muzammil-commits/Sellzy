import re
import os

# 1. Clean assets/css/style.css
for css_path in ['assets/css/style.css', 'Tailwind Sellzy/sellzy-preview.netlify.app/assets/css/style.css']:
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()
        marker = '/* ========================================================\n   Mobile Hero Section Fix'
        if marker in css:
            pos = css.find(marker)
            cleaned_css = css[:pos].rstrip() + '\n'
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_css)
            print(f"Reverted hero styles in {css_path}")

# 2. Clean assets/js/main.js
js_path = 'assets/js/main.js'
if os.path.exists(js_path):
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()
    marker = '/* Mobile Preloader & Hero Safety */'
    if marker in js:
        # Remove the block
        end_pos = js.find('}, 1000);', js.find(marker))
        if end_pos != -1:
            end_pos += len('}, 1000);')
            # find start of marker
            start_pos = js.rfind('\n', 0, js.find(marker))
            cleaned_js = js[:start_pos] + js[end_pos:]
            with open(js_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_js)
            print("Reverted safety code in assets/js/main.js")

# 3. Restore exact Hero sections in index pages from original template
PAGES = [
    ('index.html', 'index', 'Tailwind Sellzy/sellzy-preview.netlify.app/index.html'),
    ('index-2.html', 'index-2', 'Tailwind Sellzy/sellzy-preview.netlify.app/index-2'),
    ('index-3.html', 'index-3', 'Tailwind Sellzy/sellzy-preview.netlify.app/index-3'),
    ('index-4.html', 'index-4', 'Tailwind Sellzy/sellzy-preview.netlify.app/index-4'),
    ('index-5.html', 'index-5', 'Tailwind Sellzy/sellzy-preview.netlify.app/index-5'),
]

hero_start_tag = '<!-- ========== Hero Section Start ========== -->'
hero_end_tag = '<!-- ========== Hero Section End ========== -->'

for html_file, clean_file, orig_file in PAGES:
    if not os.path.exists(orig_file):
        print(f"Warning: {orig_file} not found")
        continue

    with open(orig_file, 'r', encoding='utf-8', errors='ignore') as f:
        orig_text = f.read()

    # Extract original hero section
    orig_start = orig_text.find(hero_start_tag)
    orig_end = orig_text.find(hero_end_tag)
    if orig_start == -1 or orig_end == -1:
        print(f"Could not find hero markers in {orig_file}")
        continue
    orig_hero = orig_text[orig_start:orig_end + len(hero_end_tag)]

    # Replace hero section in target files
    for target in [html_file, clean_file]:
        if os.path.exists(target):
            with open(target, 'r', encoding='utf-8') as f:
                target_text = f.read()
            t_start = target_text.find(hero_start_tag)
            t_end = target_text.find(hero_end_tag)
            if t_start != -1 and t_end != -1:
                new_target_text = target_text[:t_start] + orig_hero + target_text[t_end + len(hero_end_tag):]
                with open(target, 'w', encoding='utf-8') as f:
                    f.write(new_target_text)
                print(f"Restored original hero section in {target}")

print("Hero section restoration complete!")

