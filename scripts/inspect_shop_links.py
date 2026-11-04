with open('shop-left-sidebar-4col.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<a[^>]*href=[\'"][^\'"]*product-details[^\'"]*[\'"][^>]*>([\s\S]*?)</a>', text)
print(f"Product details links in shop: {len(matches)}")
for m in matches[:10]:
    clean = re.sub(r'<[^>]+>', '', m).strip()
    if clean:
        print(" -", clean[:60])
