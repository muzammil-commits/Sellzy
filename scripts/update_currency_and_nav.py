import glob
import re
import os

# Complete price map
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
    # Fallback formula
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

html_files = [f for f in glob.glob('*.html') if os.path.isfile(f)]
updated_count = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # 1. Update 999 RS to ₹999 in top announcement
    content = content.replace('>999 RS<', '>₹999<')
    content = content.replace('999 RS', '₹999')

    # 2. Convert all $ prices
    content = re.sub(r'\$([0-9,]+(?:\.[0-9]+)?)', convert_usd_to_inr_match, content)

    # 3. Add Ebotas link to desktop navigation if not already present
    if 'ebotas.html' not in content:
        # Insert after Shop dropdown or About Us
        target = '<!-- Shop -->'
        if target in content:
            # Look for closing </div> of Shop dropdown
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

        # Insert into mobile menu
        mobile_target = '<li>\n                <a class=\'active\' href=\'about.html\'>About Us</a>\n              </li>'
        mobile_target2 = "<li><a href='about.html'>About Us</a></li>"
        if 'About Us</a>' in content and 'Ebotas Brand Store' not in content:
            # find shop in mobile menu
            mobile_shop = "<li>\n                <a href=\"#\">Shop</a>"
            if mobile_shop in content:
                content = content.replace(mobile_shop, EBOTAS_MOBILE_NAV + '\n' + mobile_shop)

    # 4. Clean stray comment marks
    content = content.replace('<!-- ========== HEADER Section End ========== --> -->', '<!-- ========== HEADER Section End ========== -->')
    content = content.replace('<!-- ========== Footer Section End ========== --> -->', '<!-- ========== Footer Section End ========== -->')
    content = content.replace('--> -->', '-->')

    if content != orig:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1

print(f"Successfully updated {updated_count} HTML files!")
