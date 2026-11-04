import glob
import os
import re

# 1. Update products-data.js to include global card click router
with open('assets/js/products-data.js', 'r', encoding='utf-8') as f:
    pdata_code = f.read()

click_enhancer = """
  // Auto-enrich product card clicks across the site
  document.addEventListener('click', function(e) {
    const link = e.target.closest('a[href*="product-details"]');
    if (!link) return;
    
    const href = link.getAttribute('href');
    // If link already has ?id=, let it proceed
    if (href.includes('?id=') || href.includes('?slug=')) return;

    // Find the enclosing product card
    const card = link.closest('.single-product-item, .product-card, .ebotas-card, [class*="product-item"]') || link.parentElement;
    if (!card) return;

    // Find product name in card
    const nameEl = card.querySelector('.product-name, h3, h4, h5, .product-title, h2');
    if (nameEl) {
      const titleText = nameEl.innerText.trim();
      const matched = window.SellzyCatalog.getByIdOrSlug(titleText);
      if (matched) {
        e.preventDefault();
        window.location.href = `product-details.html?id=${matched.slug}`;
      }
    }
  });
"""

if 'Auto-enrich product card clicks' not in pdata_code:
    pdata_code = pdata_code.replace('})(window);', click_enhancer + '\n})(window);')
    with open('assets/js/products-data.js', 'w', encoding='utf-8') as f:
        f.write(pdata_code)
    print("Added click enhancer to assets/js/products-data.js")

# 2. Ensure products-data.js is linked in all HTML files before cart-engine.js
for html_file in glob.glob('*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c
    base = os.path.splitext(html_file)[0]

    if 'products-data.js' not in c:
        if 'cart-engine.js' in c:
            c = c.replace('<script src="./assets/js/cart-engine.js"></script>', '<script src="./assets/js/products-data.js"></script>\n    <script src="./assets/js/cart-engine.js"></script>')
        else:
            c = c.replace('</body>', '    <script src="./assets/js/products-data.js"></script>\n  </body>')

    if c != orig:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(c)
        if os.path.exists(base):
            with open(base, 'w', encoding='utf-8') as f:
                f.write(c)

print("Linked products-data.js across all pages!")
