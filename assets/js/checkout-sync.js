/**
 * Sellzy Checkout Synchronizer
 * Connects checkout.html with SellzyCart state for 100% price and item consistency
 */
document.addEventListener('DOMContentLoaded', function() {
  const cartEngine = window.SellzyCart;
  if (!cartEngine) return;

  const totals = cartEngine.calculateTotals();
  const items = cartEngine.getItems();

  // Find order summary rows in checkout
  const summaryWrapper = document.querySelector('.checkout-order-summary, [class*="Order Summary"]');
  
  // Update elements by text matching or IDs
  const paragraphs = document.querySelectorAll('p, h5, h6, span');
  paragraphs.forEach(el => {
    const text = el.innerText || '';
    if (text.startsWith('Sub-Total') || text.startsWith('Subtotal')) {
      const span = el.querySelector('span');
      if (span) span.innerText = cartEngine.formatINR(totals.subtotal);
    } else if (text.startsWith('VAT') || text.startsWith('Tax')) {
      const span = el.querySelector('span');
      if (span) span.innerText = cartEngine.formatINR(totals.tax);
    } else if (text.startsWith('Discount')) {
      const span = el.querySelector('span');
      if (span) span.innerText = totals.couponDiscount > 0 ? '-' + cartEngine.formatINR(totals.couponDiscount) : '₹0';
    } else if (text.startsWith('Shipment') || text.startsWith('Shipping')) {
      const span = el.querySelector('span');
      if (span) {
        span.innerText = totals.shipping === 0 ? 'FREE' : cartEngine.formatINR(totals.shipping);
        if (totals.shipping === 0) span.className = 'text-green-600 font-bold';
      }
    } else if (text.startsWith('Total') && el.tagName === 'H6') {
      const span = el.querySelector('span');
      if (span) span.innerText = cartEngine.formatINR(totals.grandTotal);
    }
  });

  // Also update any dynamic product list in checkout
  const productListEl = document.getElementById('checkout-items-list');
  if (productListEl) {
    productListEl.innerHTML = '';
    items.forEach(item => {
      const itemEl = document.createElement('div');
      itemEl.className = 'flex items-center justify-between py-2 border-b border-gray-100 text-xs';
      itemEl.innerHTML = `
        <div class="flex items-center gap-2">
          <img src="${item.image}" alt="${item.name}" class="w-8 h-8 object-contain rounded" />
          <span>${item.name} (${item.qty}x)</span>
        </div>
        <span class="font-bold text-gray-900">${cartEngine.formatINR(item.price * item.qty)}</span>
      `;
      productListEl.appendChild(itemEl);
    });
  }
});
