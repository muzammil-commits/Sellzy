import glob
import os

html_files = [f for f in glob.glob('*.html') if os.path.isfile(f)]

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content
    base = os.path.splitext(file_path)[0]

    # Include cart-engine.js on all pages before </body> if not present
    if 'cart-engine.js' not in content:
        content = content.replace('</body>', '    <script src="./assets/js/cart-engine.js"></script>\n  </body>')

    # If checkout, also include checkout-sync.js
    if 'checkout' in file_path and 'checkout-sync.js' not in content:
        content = content.replace('</body>', '    <script src="./assets/js/checkout-sync.js"></script>\n  </body>')

    if content != orig:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        # update extensionless clean file
        with open(base, 'w', encoding='utf-8') as f:
            f.write(content)

print("Injected cart engine across all pages and updated clean files!")
