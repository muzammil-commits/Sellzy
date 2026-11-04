import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

links = re.findall(r'<a[^>]*href=[\'"][^\'"]*product-details[^\'"]*[\'"][^>]*>([\s\S]*?)</a>', text)
print(f"Total product-details links in index.html: {len(links)}")
for l in links[:12]:
    clean = re.sub(r'<[^>]+>', '', l).strip()
    if clean:
        print(" - Text:", clean[:60])

