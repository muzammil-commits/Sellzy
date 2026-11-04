import os
import shutil
import re

SRC_DIR = 'Tailwind Sellzy/sellzy-preview.netlify.app'
DEST_DIR = '.'

# Price converter map
PRICE_MAP = {
    '$0.00': '₹0',
    '$0.33': '₹29',
    '$1.15': '₹99',
    '$4.00': '₹299',
    '$19': '₹999',
    '$20': '₹999',
    '$20.00': '₹999',
    '$24.00': '₹1,199',
    '$27.46': '₹1,499',
    '$27.49': '₹1,499',
    '$27.99': '₹1,499',
    '$28.56': '₹1,499',
    '$29.56': '₹1,499',
    '$29.95': '₹1,499',
    '$29.99': '₹1,499',
    '$39.99': '₹1,999',
    '$40': '₹1,999',
    '$40.00': '₹1,999',
    '$60.00': '₹2,999',
    '$62.97': '₹2,999',
    '$89': '₹4,499',
    '$120': '₹5,999',
    '$120.00': '₹5,999',
    '$127.49': '₹6,499',
    '$150': '₹7,499',
    '$250': '₹12,499',
}

def convert_usd_to_inr_match(match):
    full = match.group(0)
    if full in PRICE_MAP:
        return PRICE_MAP[full]
    try:
        val = float(match.group(1).replace(',', ''))
        inr_val = round(val * 50)
        if inr_val < 500:
            inr = 499
        elif inr_val < 1000:
            inr = 999
        elif inr_val < 2000:
            inr = 1499 if inr_val < 1500 else 1999
        elif inr_val < 3000:
            inr = 2499 if inr_val < 2500 else 2999
        elif inr_val < 5000:
            inr = 3999 if inr_val < 4000 else 4999
        else:
            inr = round(inr_val / 500) * 500 - 1
        s = str(inr)
        if len(s) > 3:
            last3 = s[-3:]
            rest = s[:-3]
            rest = re.sub(r'(\d)(?=(\d\d)+$)', r'\1,', rest)
            return f"₹{rest},{last3}"
        return f"₹{s}"
    except:
        return full

EBOTAS_DESKTOP_NAV = '''            <!-- Ebotas Experience -->
            <a href="ebotas.html" class="text-gray-800 hover:text-[#087d71] font-semibold text-sm transition-colors py-2 flex items-center gap-1.5 group">
              <span class="text-[#0d7d6f] font-bold group-hover:underline">Ebotas</span>
              <span class="bg-[#f5a623] text-black text-[10px] font-bold px-1.5 py-0.5 rounded-full uppercase shadow-xs">NEW</span>
            </a>'''

EBOTAS_MOBILE_NAV = '''              <li>
                <a href='ebotas.html' class="flex items-center justify-between text-[#0d7d6f] font-bold">
                  <span>Ebotas Brand Store</span>
                  <span class="bg-[#f5a623] text-black text-[10px] font-bold px-2 py-0.5 rounded-full">NEW</span>
                </a>
              </li>'''

template_files = [f for f in os.listdir(SRC_DIR) if not os.path.isdir(os.path.join(SRC_DIR, f))]
print(f"Found {len(template_files)} files in {SRC_DIR}")

for fname in template_files:
    src_path = os.path.join(SRC_DIR, fname)
    with open(src_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Convert prices to INR
    content = re.sub(r'\$([0-9,]+(?:\.[0-9]+)?)', convert_usd_to_inr_match, content)

    # 2. Update Free Shipping threshold to ₹999
    content = content.replace('>999 RS<', '>₹999<')
    content = content.replace('999 RS', '₹999')
    content = content.replace('orders over $100', 'orders over ₹999')
    content = content.replace('orders above $100', 'orders above ₹999')

    # 3. Add Ebotas to Desktop nav
    if 'ebotas.html' not in content:
        # Check standard Sellzy nav patterns
        shop_match = re.search(r'(<li[^>]*>\s*<a[^>]*href=[\'"][^\'"]*shop[^\'"]*[\'"][^>]*>.*?</li>)', content, re.DOTALL | re.IGNORECASE)
        if '<!-- Shop -->' in content:
            target = '<!-- Shop -->'
            shop_pos = content.find(target)
            end_div_pos = content.find('</div>\n\n            <!-- Sellers -->', shop_pos)
            if end_div_pos != -1:
                insert_pos = end_div_pos + len('</div>\n\n')
                content = content[:insert_pos] + EBOTAS_DESKTOP_NAV + '\n\n' + content[insert_pos:]
            else:
                end_div_pos2 = content.find('</div>\n            <!-- Sellers -->', shop_pos)
                if end_div_pos2 != -1:
                    insert_pos = end_div_pos2 + len('</div>\n')
                    content = content[:insert_pos] + EBOTAS_DESKTOP_NAV + '\n' + content[insert_pos:]
        elif shop_match:
            insert_pos = shop_match.end()
            ebotas_li = '''
              <li class="relative group">
                <a href="ebotas.html" class="text-sm font-semibold leading-[22px] py-4 text-[#0d7d6f] flex items-center gap-1.5">
                  <span>Ebotas</span>
                  <span class="bg-[#f5a623] text-black text-[10px] font-bold px-1.5 py-0.5 rounded-full">NEW</span>
                </a>
              </li>'''
            content = content[:insert_pos] + ebotas_li + content[insert_pos:]

        # Add to Mobile Menu
        if 'About Us</a>' in content and 'Ebotas Brand Store' not in content:
            mobile_shop = '<li>\n                <a href="#">Shop</a>'
            if mobile_shop in content:
                content = content.replace(mobile_shop, EBOTAS_MOBILE_NAV + '\n' + mobile_shop)

    # 4. Save both as clean filename and as .html filename
    if fname.endswith('.html'):
        base_name = fname[:-5]
        html_name = fname
    else:
        base_name = fname
        html_name = f"{fname}.html"

    # Write clean file
    with open(os.path.join(DEST_DIR, base_name), 'w', encoding='utf-8') as f:
        f.write(content)

    # Write .html file
    with open(os.path.join(DEST_DIR, html_name), 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully processed and restored all {len(template_files)} files as both clean and .html!")

