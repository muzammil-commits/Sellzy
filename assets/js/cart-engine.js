/**
 * Sellzy E-Commerce Centralized Cart & State Management Engine
 * Handles Cart, Wishlist, Product Variants, Calculations, Discounts, Shipping & Persistence
 */
(function(window) {
  'use strict';

  const STORAGE_KEY = 'sellzy_cart_items';
  const COUPON_KEY = 'sellzy_cart_coupon';
  const WISHLIST_KEY = 'sellzy_wishlist_items';
  const FREE_SHIPPING_THRESHOLD = 2999;
  const STANDARD_SHIPPING_FEE = 99;
  const TAX_RATE = 0.05; // 5% GST standard

  // Valid Coupons
  const VALID_COUPONS = {
    'SAVE10': { type: 'percent', value: 10, label: '10% OFF' },
    'SELLZY100': { type: 'flat', value: 100, label: '₹100 Flat OFF' },
    'WELCOME20': { type: 'percent', value: 20, label: '20% OFF' },
    'FREESHIP': { type: 'shipping', value: 0, label: 'Free Delivery' }
  };

  // Seed items matching image copy 12.png if cart is initially empty
  const DEFAULT_SEED_ITEMS = [
    {
      id: 'prod-coffee-1',
      name: 'Morning Brew Instant Coffee',
      image: './assets/images/home-3/apple.png',
      price: 1499,
      originalPrice: 1499,
      size: '250 ML',
      color: 'Black',
      qty: 1,
      available: 2,
      rating: 4.8,
      reviews: 118
    },
    {
      id: 'prod-coffee-2',
      name: 'Morning Brew Instant Coffee',
      image: './assets/images/home-3/corn-can.png',
      price: 1499,
      originalPrice: 1499,
      size: '250 ML',
      color: 'Black',
      qty: 1,
      available: 5,
      rating: 4.9,
      reviews: 118
    },
    {
      id: 'prod-coffee-3',
      name: 'Morning Brew Instant Coffee',
      image: './assets/images/home-1/hero-promo-1.png',
      price: 1499,
      originalPrice: 1499,
      size: '250 ML',
      color: 'Black',
      qty: 1,
      available: 4,
      rating: 5.0,
      reviews: 118
    }
  ];

  class CartEngine {
    constructor() {
      this.items = this.loadItems();
      this.coupon = this.loadCoupon();
      this.wishlist = this.loadWishlist();
      this.initHeaderSync();
    }

    loadItems() {
      try {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored !== null) {
          return JSON.parse(stored);
        }
        // First visit: seed default items matching screenshot
        this.saveItems(DEFAULT_SEED_ITEMS);
        return DEFAULT_SEED_ITEMS;
      } catch (e) {
        console.error('Error loading cart from storage', e);
        return DEFAULT_SEED_ITEMS;
      }
    }

    saveItems(items) {
      this.items = items;
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
      } catch (e) {
        console.error('Error saving cart to storage', e);
      }
      this.dispatchUpdate();
    }

    loadCoupon() {
      try {
        const stored = localStorage.getItem(COUPON_KEY);
        return stored ? JSON.parse(stored) : null;
      } catch (e) {
        return null;
      }
    }

    saveCoupon(coupon) {
      this.coupon = coupon;
      try {
        if (coupon) {
          localStorage.setItem(COUPON_KEY, JSON.stringify(coupon));
        } else {
          localStorage.removeItem(COUPON_KEY);
        }
      } catch (e) {}
      this.dispatchUpdate();
    }

    loadWishlist() {
      try {
        const stored = localStorage.getItem(WISHLIST_KEY);
        return stored ? JSON.parse(stored) : [];
      } catch (e) {
        return [];
      }
    }

    saveWishlist(list) {
      this.wishlist = list;
      try {
        localStorage.setItem(WISHLIST_KEY, JSON.stringify(list));
      } catch (e) {}
    }

    dispatchUpdate() {
      const totals = this.calculateTotals();
      const event = new CustomEvent('sellzy:cart-updated', {
        detail: {
          items: this.items,
          totals: totals,
          itemCount: this.getItemCount()
        }
      });
      window.dispatchEvent(event);
      this.updateHeaderBadges();
    }

    getItemCount() {
      return this.items.reduce((sum, item) => sum + (item.qty || 1), 0);
    }

    getItems() {
      return [...this.items];
    }

    addItem(product) {
      const items = [...this.items];
      // Check if product with identical variant (id + size + color) exists
      const existingIdx = items.findIndex(
        i => i.id === product.id && i.size === product.size && i.color === product.color
      );

      if (existingIdx > -1) {
        const maxStock = items[existingIdx].available || 10;
        const newQty = (items[existingIdx].qty || 1) + (product.qty || 1);
        items[existingIdx].qty = Math.min(newQty, maxStock);
      } else {
        items.push({
          id: product.id || 'prod-' + Date.now(),
          name: product.name || 'Sellzy Product',
          image: product.image || './assets/images/home-3/apple.png',
          price: Number(product.price) || 1499,
          originalPrice: Number(product.originalPrice) || Number(product.price) || 1499,
          size: product.size || 'Standard',
          color: product.color || 'Standard',
          qty: Number(product.qty) || 1,
          available: Number(product.available) || 10,
          rating: product.rating || 5.0,
          reviews: product.reviews || 100
        });
      }

      this.saveItems(items);
      return true;
    }

    updateQuantity(index, delta) {
      const items = [...this.items];
      if (index < 0 || index >= items.length) return false;

      const item = items[index];
      const maxStock = item.available || 10;
      const currentQty = item.qty || 1;
      const nextQty = currentQty + delta;

      if (nextQty <= 0) {
        return 'confirm_remove';
      }

      if (nextQty > maxStock) {
        return 'max_stock_reached';
      }

      items[index].qty = nextQty;
      this.saveItems(items);
      return true;
    }

    updateItemVariant(index, updates) {
      const items = [...this.items];
      if (index < 0 || index >= items.length) return false;

      items[index] = {
        ...items[index],
        ...updates
      };

      this.saveItems(items);
      return true;
    }

    removeItem(index) {
      const items = [...this.items];
      if (index < 0 || index >= items.length) return false;

      const removed = items.splice(index, 1)[0];
      this.saveItems(items);
      return removed;
    }

    clearCart() {
      this.saveCoupon(null);
      this.saveItems([]);
      return true;
    }

    applyCoupon(rawCode) {
      if (!rawCode) return { success: false, message: 'Please enter a coupon code' };
      const code = rawCode.trim().toUpperCase();

      if (!VALID_COUPONS[code]) {
        return { success: false, message: 'Invalid coupon code. Try SAVE10 or SELLZY100' };
      }

      const couponData = {
        code: code,
        ...VALID_COUPONS[code]
      };

      this.saveCoupon(couponData);
      return { success: true, message: `Coupon ${code} (${couponData.label}) applied successfully!`, coupon: couponData };
    }

    removeCoupon() {
      this.saveCoupon(null);
      return true;
    }

    addToWishlist(item) {
      const list = [...this.wishlist];
      const exists = list.some(i => i.id === item.id);
      if (!exists) {
        list.push({ ...item, addedAt: Date.now() });
        this.saveWishlist(list);
      }
      return true;
    }

    calculateTotals() {
      const subtotal = this.items.reduce((sum, item) => sum + (Number(item.price) * Number(item.qty || 1)), 0);
      
      // Coupon discount
      let couponDiscount = 0;
      if (this.coupon && subtotal > 0) {
        if (this.coupon.type === 'percent') {
          couponDiscount = Math.round(subtotal * (this.coupon.value / 100));
        } else if (this.coupon.type === 'flat') {
          couponDiscount = Math.min(this.coupon.value, subtotal);
        }
      }

      // Shipping calculation
      let shipping = 0;
      if (subtotal > 0) {
        if (this.coupon && this.coupon.type === 'shipping') {
          shipping = 0;
        } else if (subtotal >= FREE_SHIPPING_THRESHOLD) {
          shipping = 0;
        } else {
          shipping = STANDARD_SHIPPING_FEE;
        }
      }

      // Tax (5% GST)
      const taxableAmount = Math.max(0, subtotal - couponDiscount);
      const tax = taxableAmount > 0 ? Math.round(taxableAmount * TAX_RATE) : 0;

      // Grand Total
      const grandTotal = subtotal > 0 ? Math.max(0, taxableAmount + tax + shipping) : 0;

      // Free shipping remaining
      const shippingRemaining = Math.max(0, FREE_SHIPPING_THRESHOLD - subtotal);
      const shippingProgress = subtotal >= FREE_SHIPPING_THRESHOLD ? 100 : Math.min(100, Math.round((subtotal / FREE_SHIPPING_THRESHOLD) * 100));

      return {
        subtotal,
        couponDiscount,
        shipping,
        tax,
        grandTotal,
        shippingRemaining,
        shippingProgress,
        freeShippingThreshold: FREE_SHIPPING_THRESHOLD,
        coupon: this.coupon
      };
    }

    formatINR(num) {
      if (num === null || num === undefined || isNaN(num)) return '₹0';
      const val = Math.round(num);
      const s = val.toString();
      if (s.length > 3) {
        const last3 = s.substring(s.length - 3);
        const rest = s.substring(0, s.length - 3);
        const formattedRest = rest.replace(/\\B(?=(\\d{2})+(?!\\d))/g, ',');
        return '₹' + formattedRest + ',' + last3;
      }
      return '₹' + s;
    }

    updateHeaderBadges() {
      const count = this.getItemCount();
      const totals = this.calculateTotals();
      const countStr = count === 1 ? '1 item' : count + ' items';

      // Header desktop badges
      const cartBadges = document.querySelectorAll('#header-cart-btn span, .header-cart-count, .cart-counter, .cart-count');
      cartBadges.forEach(el => {
        if (el.innerText.includes('Items') || el.innerText.includes('item') || el.classList.contains('cart-count')) {
          el.innerText = count + ' - Items';
        }
      });

      // Update cart page title count if present
      const cartTitleCount = document.getElementById('cart-page-item-count');
      if (cartTitleCount) {
        cartTitleCount.innerText = `(${count} item${count === 1 ? '' : 's'})`;
      }
    }

    initHeaderSync() {
      // Sync on DOM ready and storage changes
      document.addEventListener('DOMContentLoaded', () => {
        this.updateHeaderBadges();
      });

      window.addEventListener('storage', (e) => {
        if (e.key === STORAGE_KEY || e.key === COUPON_KEY) {
          this.items = this.loadItems();
          this.coupon = this.loadCoupon();
          this.dispatchUpdate();
        }
      });
    }
  }

  // Expose global instance
  window.SellzyCart = new CartEngine();


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

})(window);
