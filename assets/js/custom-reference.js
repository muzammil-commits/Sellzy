/**
 * Pretty Palette / Sellzy - Interactive Functions
 * - Live Cart Management (Add, Remove, Quantity, Update Total)
 * - Live Wishlist Toggle (Local Storage persistence)
 * - Search Filter functionality
 * - Toast Notifications
 * - Product Details Gallery Thumbnails & Variant Selectors
 */

(function ($) {
  'use strict';

  // Initialize Cart State from localStorage
  const CART_KEY = 'sellzy_cart';
  const WISHLIST_KEY = 'sellzy_wishlist';

  function getCart() {
    try {
      return JSON.parse(localStorage.getItem(CART_KEY)) || [];
    } catch (e) {
      return [];
    }
  }

  function saveCart(cart) {
    localStorage.setItem(CART_KEY, JSON.stringify(cart));
    updateCartUI();
  }

  function getWishlist() {
    try {
      return JSON.parse(localStorage.getItem(WISHLIST_KEY)) || [];
    } catch (e) {
      return [];
    }
  }

  function saveWishlist(wishlist) {
    localStorage.setItem(WISHLIST_KEY, JSON.stringify(wishlist));
    updateWishlistUI();
  }

  // Toast function
  window.showSellzyToast = function (message, type = 'success') {
    let $toast = $('#sellzy-toast');
    if (!$toast.length) {
      $toast = $('<div id="sellzy-toast" class="sellzy-toast"></div>').appendTo('body');
    }
    const icon = type === 'success' ? '<i class="hgi hgi-stroke hgi-tick-02 text-xl"></i>' : '<i class="hgi hgi-stroke hgi-information-circle text-xl"></i>';
    $toast.html(`${icon} <span>${message}</span>`).removeClass('sellzy-toast-success').addClass(type === 'success' ? 'sellzy-toast-success' : '');
    $toast.addClass('show');
    clearTimeout(window._toastTimeout);
    window._toastTimeout = setTimeout(() => {
      $toast.removeClass('show');
    }, 2800);
  };

  // Update Cart Counters across page
  function updateCartUI() {
    const cart = getCart();
    const count = cart.reduce((sum, item) => sum + (item.quantity || 1), 0);
    const subtotal = cart.reduce((sum, item) => sum + (parseFloat(item.price) * (item.quantity || 1)), 0);

    // Update Header Display: "0- Items" or "X Items"
    $('.cart-count-display').text(`${count}- Items`);
    $('.cart-count-badge').text(count);
    $('.cart-subtotal-display').text('$' + subtotal.toFixed(2));
  }

  // Update Wishlist buttons
  function updateWishlistUI() {
    const wishlist = getWishlist();
    $('.wishlist-count-badge').text(wishlist.length);
    $('.ref-wishlist-btn, [data-wishlist-id]').each(function () {
      const id = $(this).attr('data-id') || $(this).closest('[data-product-id]').attr('data-product-id');
      if (id && wishlist.includes(id)) {
        $(this).addClass('active');
      } else {
        $(this).removeClass('active');
      }
    });
  }

  $(document).ready(function () {
    updateCartUI();
    updateWishlistUI();

    // Add to Cart Click Handler
    $(document).on('click', '.ref-add-cart-btn, .btn-add-to-cart', function (e) {
      e.preventDefault();
      const $card = $(this).closest('.ref-product-card, [data-product-id]');
      const title = $card.find('.product-title, h3, h4').first().text().trim() || 'VitaLife Omega-3 Softgels';
      const priceText = $card.find('.product-price, .current-price').first().text().replace('$', '').trim() || '27.49';
      const price = parseFloat(priceText) || 27.49;
      const img = $card.find('img').first().attr('src') || './assets/images/vitamin-c.png';
      const id = $card.attr('data-product-id') || 'prod_' + Math.random().toString(36).substr(2, 9);

      const cart = getCart();
      const existing = cart.find(item => item.id === id);
      if (existing) {
        existing.quantity += 1;
      } else {
        cart.push({ id, title, price, img, quantity: 1 });
      }
      saveCart(cart);

      // Animate button
      const $btn = $(this);
      const originalHtml = $btn.html();
      $btn.html('<i class="hgi hgi-stroke hgi-tick-02"></i> Added!');
      setTimeout(() => $btn.html(originalHtml), 1500);

      window.showSellzyToast(`Added "${title.substring(0, 24)}..." to cart!`);
    });

    // Wishlist Toggle Handler
    $(document).on('click', '.ref-wishlist-btn, .btn-wishlist-toggle', function (e) {
      e.preventDefault();
      const $card = $(this).closest('.ref-product-card, [data-product-id]');
      const id = $(this).attr('data-id') || $card.attr('data-product-id') || 'prod_default';
      const title = $card.find('.product-title, h3, h4').first().text().trim() || 'Product';
      let wishlist = getWishlist();

      if (wishlist.includes(id)) {
        wishlist = wishlist.filter(item => item !== id);
        $(this).removeClass('active');
        window.showSellzyToast(`Removed from wishlist`, 'info');
      } else {
        wishlist.push(id);
        $(this).addClass('active');
        window.showSellzyToast(`Added "${title.substring(0, 20)}" to wishlist!`);
      }
      saveWishlist(wishlist);
    });

    // Live Product Search
    $('.header-search-input').on('keyup', function () {
      const q = $(this).val().toLowerCase().trim();
      if (!q) {
        $('.ref-product-card').show();
        return;
      }
      $('.ref-product-card').each(function () {
        const text = $(this).text().toLowerCase();
        if (text.includes(q)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });

    // Product Details Gallery Switcher
    $('.product-thumb-item').on('click', function () {
      $('.product-thumb-item').removeClass('border-primary ring-2 ring-primary/40');
      $(this).addClass('border-primary ring-2 ring-primary/40');
      const targetSrc = $(this).attr('data-target-src') || $(this).find('img').attr('src');
      $('#main-product-gallery-img').attr('src', targetSrc);
    });

    // Size Switcher
    $('.size-variant-btn').on('click', function () {
      $('.size-variant-btn').removeClass('bg-[#087d71] text-white border-[#087d71]').addClass('bg-white text-gray-700 border-gray-200');
      $(this).addClass('bg-[#087d71] text-white border-[#087d71]').removeClass('bg-white text-gray-700 border-gray-200');
      $('#selected-size-label').text($(this).text().trim());
    });

    // Color Switcher
    $('.color-variant-btn').on('click', function () {
      $('.color-variant-btn').removeClass('ring-2 ring-offset-2 ring-primary');
      $(this).addClass('ring-2 ring-offset-2 ring-primary');
      $('#selected-color-label').text($(this).attr('data-color-name') || 'Selected');
    });

    // Quantity Counter
    $('#qty-minus').on('click', function () {
      const $input = $('#product-qty-input');
      let val = parseInt($input.val()) || 1;
      if (val > 1) $input.val(val - 1);
    });

    $('#qty-plus').on('click', function () {
      const $input = $('#product-qty-input');
      let val = parseInt($input.val()) || 1;
      $input.val(val + 1);
    });

    // Product Details Add to Cart
    $('#btn-detail-add-cart').on('click', function () {
      const qty = parseInt($('#product-qty-input').val()) || 1;
      const title = $('#detail-product-title').text().trim() || 'VitaLife Omega-3 Softgels';
      const price = 62.97;
      const img = $('#main-product-gallery-img').attr('src') || './assets/images/product_detail_hero.png';
      const id = 'prod_detail_vitalife';

      const cart = getCart();
      const existing = cart.find(item => item.id === id);
      if (existing) {
        existing.quantity += qty;
      } else {
        cart.push({ id, title, price, img, quantity: qty });
      }
      saveCart(cart);
      window.showSellzyToast(`Added ${qty} item(s) to cart!`);
    });

    // Smooth scroll for top buttons
    $('.scroll-to-top').on('click', function () {
      $('html, body').animate({ scrollTop: 0 }, 500);
      return false;
    });
  });
})(jQuery);

