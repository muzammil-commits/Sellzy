with open('assets/js/cart-engine.js', 'r', encoding='utf-8') as f:
    code = f.read()

handler = """
  // Global Add To Cart Delegator
  document.addEventListener('click', function(e) {
    const addBtn = e.target.closest('button, a, .btn-add-to-cart, [data-add-to-cart]');
    if (!addBtn) return;
    
    // Ignore internal cart table buttons
    if (addBtn.closest('#cart-items-tbody') || addBtn.closest('#modal-edit-product')) return;

    const btnText = (addBtn.innerText || '').trim();
    if (btnText.includes('Add to Cart') || btnText.includes('Add To Cart') || addBtn.hasAttribute('data-add-to-cart')) {
      e.preventDefault();

      const card = addBtn.closest('.product-card, .single-product-item, .product-details-content-wrapper, section, .grid > div') || document.body;
      let title = 'Morning Brew Instant Coffee';
      let price = 1499;
      let image = './assets/images/home-3/apple.png';
      let size = '250 ML';
      let color = 'Black';

      const titleEl = card.querySelector('.product-name, h3, h4, h2, .product-title');
      if (titleEl) title = titleEl.innerText.trim();

      const priceEl = card.querySelector('.product-price, .price, .text-primary, [class*="price"]');
      if (priceEl) {
        const numMatch = priceEl.innerText.replace(/[^0-9]/g, '');
        if (numMatch && parseInt(numMatch, 10) > 0) price = parseInt(numMatch, 10);
      }

      const imgEl = card.querySelector('img');
      if (imgEl && imgEl.getAttribute('src')) image = imgEl.getAttribute('src');

      window.SellzyCart.addItem({
        name: title,
        price: price,
        image: image,
        size: size,
        color: color,
        qty: 1
      });

      // Show toast
      const existing = document.querySelectorAll('.sellzy-toast');
      existing.forEach(t => t.remove());
      const toast = document.createElement('div');
      toast.className = 'sellzy-toast fixed bottom-6 right-6 px-5 py-3 rounded-xl shadow-2xl flex items-center gap-3 z-99 text-xs font-semibold animate-bounce bg-[#0d7d6f] text-white';
      toast.innerHTML = '<span class="bg-white/20 p-1 rounded-full">&#10003;</span> Added "' + title + '" (' + window.SellzyCart.formatINR(price) + ') to Cart!';
      document.body.appendChild(toast);
      setTimeout(() => toast.remove(), 2500);
    }
  });
"""

if 'Global Add To Cart Delegator' not in code:
    code = code.replace('})(window);', handler + '\n})(window);')
    with open('assets/js/cart-engine.js', 'w', encoding='utf-8') as f:
        f.write(code)
    print('Added Global Add To Cart handler to cart-engine.js')

