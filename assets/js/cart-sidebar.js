/**
 * Sellzy Dynamic Cart Sidebar & Drawer Controller
 * Synchronizes the slide-out cart drawer with SellzyCart state in real time
 */
(function() {
  'use strict';

  function initCartSidebar() {
    const cartEngine = window.SellzyCart;
    if (!cartEngine) return;

    const sidebar = document.querySelector('.cart-sidebar');
    if (!sidebar) return;

    const cartContent = sidebar.querySelector('.cart-products-content');
    const countEl = sidebar.querySelector('.cart-products-header p');

    // Render Cart Products inside Sidebar Drawer
    function renderSidebarCart() {
      const items = cartEngine.getItems();
      const totals = cartEngine.calculateTotals();
      const totalCount = cartEngine.getItemCount();

      // 1. Update Drawer Header Count
      if (countEl) {
        countEl.innerText = `${totalCount} Item${totalCount === 1 ? '' : 's'} in Cart`;
      }

      // 2. Update Subtotal in Footer
      const subtotalBox = sidebar.querySelector('.cart-subtotal');
      if (subtotalBox) {
        const headings = subtotalBox.querySelectorAll('h5, p, span');
        if (headings.length >= 2) {
          headings[headings.length - 1].innerText = cartEngine.formatINR(totals.subtotal);
        } else if (headings.length === 1) {
          headings[0].innerText = cartEngine.formatINR(totals.subtotal);
        }
      }

      // Also target any subtotal elements with text matching Subtotal
      const subtotalSpans = sidebar.querySelectorAll('span, p, h5');
      subtotalSpans.forEach(el => {
        const text = (el.innerText || '').trim();
        if (text.startsWith('Subtotal') || text.startsWith('Sub-Total')) {
          const valEl = el.querySelector('span');
          if (valEl) {
            valEl.innerText = cartEngine.formatINR(totals.subtotal);
          }
        }
      });

      // 3. Render Cart Items inside .cart-products-content
      if (!cartContent) return;

      if (!items || items.length === 0) {
        cartContent.innerHTML = `
          <div class="py-16 text-center text-gray-500 flex flex-col items-center justify-center h-full">
            <div class="w-16 h-16 rounded-full bg-gray-100 text-gray-400 flex items-center justify-center mb-3">
              <i class="hgi hgi-stroke hgi-shopping-cart-01 text-3xl"></i>
            </div>
            <p class="font-bold text-base text-gray-800">Your Cart is Currently Empty</p>
            <p class="text-xs text-gray-400 mt-1 max-w-[220px]">Add products from the catalog or similar products to see them here.</p>
          </div>
        `;
        return;
      }

      cartContent.innerHTML = '';
      items.forEach((item, index) => {
        const card = document.createElement('div');
        card.className = 'cart-product-item flex flex-col sm:flex-row items-center sm:gap-x-4 gap-y-2 sm:gap-y-0 p-4 border border-gray-300 rounded-2xl bg-white transition-all hover:border-[#0d7d6f]/40';
        card.innerHTML = `
          <a class="cart-product-item-image sm:w-[102px] sm:h-[102px] rounded-xl bg-[#F4F3F5] overflow-hidden relative shrink-0 block" href="product-details.html?id=${item.slug || item.id}">
            <img
              src="${item.image}"
              alt="${item.name}"
              class="w-full h-full object-cover rounded-xl"
              onerror="this.src='./assets/images/home-3/apple.png'"
            />
          </a>
          <div class="cart-product-item-content flex flex-col gap-y-2 flex-1 w-full min-w-0">
            <div class="flex items-center justify-between gap-x-2">
              <h6 class="text-base font-semibold truncate">
                <a href="product-details.html?id=${item.slug || item.id}" class="hover:text-primary transition-colors text-gray-900">${item.name}</a>
              </h6>
              <div class="cart-edit-remove flex items-center gap-x-3 shrink-0">
                <a href="product-details.html?id=${item.slug || item.id}" class="btn-drawer-edit inline-flex" title="Edit product">
                  <i class="hgi hgi-stroke hgi-edit-02 text-xl text-light-primary-text hover:text-primary transition-colors"></i>
                </a>
                <button type="button" class="btn-drawer-delete inline-flex cursor-pointer" data-index="${index}" title="Remove item">
                  <i class="hgi hgi-stroke hgi-delete-01 text-xl text-light-primary-text hover:text-red-500 transition-colors"></i>
                </button>
              </div>
            </div>
            <p class="text-sm leading-[22px] text-gray-500">Color: ${item.color || 'Standard'}, Size: ${item.size || 'Standard'}</p>
            <div class="flex items-center justify-between">
              <div class="price-section flex items-center gap-x-3">
                <span class="current-price text-base font-semibold text-light-primary-text">${cartEngine.formatINR(item.price)}</span>
                ${item.originalPrice && item.originalPrice > item.price ? `
                <span class="old-price text-base text-light-disabled-text line-through">${cartEngine.formatINR(item.originalPrice)}</span>` : ''}
              </div>
              <div class="border border-gray-300 inline-flex items-center justify-center rounded-[80px] max-w-[108px] py-1.5 px-3 bg-white">
                <button type="button" class="btn-drawer-minus inline-flex items-center justify-center hover:text-primary cursor-pointer" data-index="${index}" title="Decrease quantity">
                  <i class="hgi hgi-stroke hgi-remove-circle text-2xl leading-6"></i>
                </button>
                <input type="text" readonly="" value="${item.qty}" class="border-0 w-8 grow text-center focus:outline-none font-semibold text-sm select-none" />
                <button type="button" class="btn-drawer-plus inline-flex items-center justify-center hover:text-primary cursor-pointer" data-index="${index}" title="Increase quantity">
                  <i class="hgi hgi-stroke hgi-add-circle text-2xl leading-6"></i>
                </button>
              </div>
            </div>
          </div>
        `;
        cartContent.appendChild(card);
      });
    }

    // Attach Event Listeners to Sidebar Cart Controls
    if (cartContent) {
      cartContent.addEventListener('click', function(e) {
        const btnPlus = e.target.closest('.btn-drawer-plus');
        const btnMinus = e.target.closest('.btn-drawer-minus');
        const btnDelete = e.target.closest('.btn-drawer-delete');

        if (btnPlus) {
          const index = parseInt(btnPlus.getAttribute('data-index'), 10);
          cartEngine.updateQuantity(index, 1);
        } else if (btnMinus) {
          const index = parseInt(btnMinus.getAttribute('data-index'), 10);
          const res = cartEngine.updateQuantity(index, -1);
          if (res === 'confirm_remove') {
            cartEngine.removeItem(index);
          }
        } else if (btnDelete) {
          const index = parseInt(btnDelete.getAttribute('data-index'), 10);
          cartEngine.removeItem(index);
        }
      });
    }

    // Connect Similar Products "Add" buttons inside the left pane of drawer
    const similarProducts = sidebar.querySelector('.similar-products-content');
    if (similarProducts) {
      similarProducts.addEventListener('click', function(e) {
        const addBtn = e.target.closest('.btn, button, a');
        if (!addBtn) return;
        
        const btnText = (addBtn.innerText || '').trim();
        const hasCartIcon = Boolean(addBtn.querySelector('[class*="shopping-cart"]'));
        if (btnText.includes('Add') || hasCartIcon) {
          e.preventDefault();
          e.stopPropagation();
          const itemCard = addBtn.closest('.similar-product-item') || addBtn.closest('div');
          if (itemCard) {
            let title = 'Fresh Bask Basket Fruits';
            let price = 1499;
            let originalPrice = 1999;
            let image = './assets/images/home-3/apple.png';

            const titleEl = itemCard.querySelector('h6, h5, h4, .product-name, a');
            if (titleEl) title = titleEl.innerText.trim();

            const priceEl = itemCard.querySelector('.current-price, .price, span');
            if (priceEl) {
              const numMatch = priceEl.innerText.replace(/[^0-9]/g, '');
              if (numMatch && parseInt(numMatch, 10) > 0) price = parseInt(numMatch, 10);
            }

            const oldPriceEl = itemCard.querySelector('.old-price, .line-through');
            if (oldPriceEl) {
              const numMatch = oldPriceEl.innerText.replace(/[^0-9]/g, '');
              if (numMatch && parseInt(numMatch, 10) > 0) originalPrice = parseInt(numMatch, 10);
            }

            const imgEl = itemCard.querySelector('img');
            if (imgEl && imgEl.src) image = imgEl.src;

            // Lookup product in catalog if available
            const catalog = window.SellzyCatalog;
            const matched = catalog ? catalog.getByIdOrSlug(title) : null;

            cartEngine.addItem({
              id: matched ? matched.id : 'prod-' + Date.now(),
              slug: matched ? matched.slug : 'product',
              name: matched ? matched.name : title,
              image: matched ? matched.images[0] : image,
              price: matched ? matched.price : price,
              originalPrice: matched ? matched.originalPrice : originalPrice,
              size: '250 ML',
              color: 'Standard',
              qty: 1
            });
          }
        }
      });
    }

    // Open Cart Sidebar helper
    window.openCartSidebar = function() {
      const activeSidebar = document.querySelector('.cart-sidebar');
      if (!activeSidebar) return;
      activeSidebar.setAttribute('data-state', 'open');
      const overlay = document.querySelector('.modal-overlay');
      if (overlay) {
        if (window.jQuery) {
          window.jQuery(overlay).fadeIn();
        } else {
          overlay.style.display = 'block';
        }
        overlay.setAttribute('data-overlay-for', '.cart-sidebar');
      }
      document.body.classList.add('overflow-hidden', 'scrollbar-offset');
    };

    // Close button
    const closeBtn = sidebar.querySelector('[data-close-sidebar], .close-sidebar-btn, #cart-sidebar-close, button:has(.hgi-cancel-01), button:has(.hgi-stroke)');
    const allCloseBtns = sidebar.querySelectorAll('button');
    allCloseBtns.forEach(btn => {
      if (btn.querySelector('.hgi-cancel-01') || btn.innerText.includes('✕') || btn.id === 'cart-sidebar-close') {
        btn.addEventListener('click', function() {
          sidebar.setAttribute('data-state', 'close');
          const overlay = document.querySelector('.modal-overlay');
          if (overlay) {
            if (window.jQuery) window.jQuery(overlay).fadeOut();
            else overlay.style.display = 'none';
          }
          document.body.classList.remove('overflow-hidden', 'scrollbar-offset');
        });
      }
    });

    // Listen to cart updates
    window.addEventListener('sellzy:cart-updated', function() {
      renderSidebarCart();
    });

    // Initial render
    renderSidebarCart();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCartSidebar);
  } else {
    initCartSidebar();
  }

})();
