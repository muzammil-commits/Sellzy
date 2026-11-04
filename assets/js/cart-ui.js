/**
 * Sellzy Cart UI Controller
 * Manages DOM updates, user actions, Modals, Quantity adjustments, Delete, Remove All, and Checkout Sync
 */
document.addEventListener('DOMContentLoaded', function() {
  const cartEngine = window.SellzyCart;
  if (!cartEngine) return;

  const tbody = document.getElementById('cart-items-tbody');
  const emptyScreen = document.getElementById('cart-empty-screen');
  const contentWrapper = document.getElementById('cart-content-wrapper');
  const cartCountEl = document.getElementById('cart-page-item-count');

  // Summary elements
  const elSubtotal = document.getElementById('cart-subtotal');
  const elTax = document.getElementById('cart-tax');
  const elShipping = document.getElementById('cart-shipping');
  const elDiscountRow = document.getElementById('cart-discount-row');
  const elDiscount = document.getElementById('cart-discount');
  const elDiscountLabel = document.getElementById('cart-discount-label');
  const elGrandTotal = document.getElementById('cart-grand-total');

  // Free shipping elements
  const elShippingText = document.getElementById('free-shipping-text');
  const elShippingProgressBar = document.getElementById('free-shipping-progress-bar');

  // Coupon elements
  const couponInput = document.getElementById('cart-coupon-input');
  const couponApplyBtn = document.getElementById('cart-coupon-apply-btn');
  const couponMessage = document.getElementById('cart-coupon-message');

  // Modals
  const removeAllModal = document.getElementById('modal-remove-all');
  const removeAllConfirmBtn = document.getElementById('btn-confirm-remove-all');
  const removeAllCancelBtn = document.getElementById('btn-cancel-remove-all');
  const btnRemoveAll = document.getElementById('btn-remove-all');

  const editModal = document.getElementById('modal-edit-product');
  const editModalForm = document.getElementById('edit-product-form');
  const editModalCancelBtn = document.getElementById('btn-cancel-edit');
  let currentEditingIndex = -1;

  // Render Full Cart
  function renderCart() {
    const items = cartEngine.getItems();
    const totals = cartEngine.calculateTotals();

    // 1. Update Cart Count Header
    if (cartCountEl) {
      cartCountEl.innerText = `(${totals.subtotal > 0 ? items.length : 0} item${items.length === 1 ? '' : 's'})`;
    }

    // 2. Empty Cart Check
    if (!items || items.length === 0) {
      if (contentWrapper) contentWrapper.style.display = 'none';
      if (emptyScreen) emptyScreen.style.display = 'block';
      updateOrderSummary(totals);
      return;
    }

    if (contentWrapper) contentWrapper.style.display = 'block';
    if (emptyScreen) emptyScreen.style.display = 'none';

    // 3. Render Table Rows
    if (tbody) {
      tbody.innerHTML = '';
      items.forEach((item, index) => {
        const itemTotal = Number(item.price) * (item.qty || 1);
        const tr = document.createElement('tr');
        tr.className = 'border-b border-gray-200 hover:bg-gray-50/50 transition-colors';
        tr.innerHTML = `
          <td class="product py-4 pl-4 pr-3">
            <div class="flex items-center gap-4">
              <div class="w-16 h-16 sm:w-20 sm:h-20 rounded-xl overflow-hidden bg-gray-100 shrink-0 border border-gray-200">
                <img src="${item.image}" alt="${item.name}" class="w-full h-full object-contain p-1.5" onerror="this.src='./assets/images/home-3/apple.png'" />
              </div>
              <div class="flex-1 min-w-0">
                <a href="product-details.html?id=${item.slug || item.id}" class="product-name text-light-primary-text font-semibold text-sm hover:text-primary transition-colors block truncate">
                  ${item.name}
                </a>
                <p class="text-xs text-gray-500 mt-0.5 flex items-center gap-2">
                  <span>Color: <strong class="text-gray-800">${item.color}</strong>, Size: <strong class="text-gray-800">${item.size}</strong></span>
                  <button type="button" class="btn-edit-item text-primary hover:text-primary-dark p-1 rounded hover:bg-primary/10 transition-colors" data-index="${index}" title="Edit Size/Color">
                    <i class="hgi hgi-stroke hgi-edit-02 text-sm leading-none"></i>
                  </button>
                </p>
                <p class="text-xs text-gray-400 mt-0.5">
                  Available: <span class="font-medium text-gray-600">${item.available || 5}</span>
                </p>
                <div class="flex items-center gap-1 text-amber-500 text-xs mt-1">
                  <span>&#9733;&#9733;&#9733;&#9733;&#9733;</span>
                  <span class="text-gray-400">(${item.reviews || 118})</span>
                </div>
              </div>
            </div>
          </td>
          <td class="product-price py-4 px-3 text-sm font-semibold text-gray-900 whitespace-nowrap">
            ${cartEngine.formatINR(item.price)}
            ${item.originalPrice && item.originalPrice > item.price ? `<span class="text-xs text-gray-400 line-through block font-normal">${cartEngine.formatINR(item.originalPrice)}</span>` : ''}
          </td>
          <td class="product-quantity py-4 px-3 whitespace-nowrap">
            <div class="inline-flex items-center border border-gray-300 rounded-full p-1 bg-white shadow-xs">
              <button type="button" class="btn-qty-minus size-7 rounded-full inline-flex items-center justify-center hover:bg-gray-100 text-gray-700 font-bold transition-colors" data-index="${index}">
                &minus;
              </button>
              <span class="w-8 text-center text-sm font-semibold text-gray-900 select-none">${item.qty}</span>
              <button type="button" class="btn-qty-plus size-7 rounded-full inline-flex items-center justify-center hover:bg-gray-100 text-gray-700 font-bold transition-colors" data-index="${index}">
                &#43;
              </button>
            </div>
          </td>
          <td class="product-total-price py-4 px-3 text-sm font-bold text-gray-900 whitespace-nowrap">
            ${cartEngine.formatINR(itemTotal)}
          </td>
          <td class="product-actions py-4 pr-4 pl-3 text-center whitespace-nowrap">
            <div class="flex items-center justify-center gap-3">
              <button type="button" class="btn-wishlist-item text-gray-400 hover:text-red-500 p-1.5 rounded-full hover:bg-red-50 transition-colors" data-index="${index}" title="Save to Wishlist">
                <i class="hgi hgi-stroke hgi-favourite text-lg leading-none"></i>
              </button>
              <button type="button" class="btn-delete-item text-gray-400 hover:text-red-600 p-1.5 rounded-full hover:bg-red-50 transition-colors" data-index="${index}" title="Delete Item">
                <i class="hgi hgi-stroke hgi-delete-01 text-lg leading-none"></i>
              </button>
            </div>
          </td>
        `;
        tbody.appendChild(tr);
      });
    }

    // 4. Update Summary
    updateOrderSummary(totals);
  }

  // Update Summary DOM
  function updateOrderSummary(totals) {
    if (elSubtotal) elSubtotal.innerText = cartEngine.formatINR(totals.subtotal);
    if (elTax) elTax.innerText = cartEngine.formatINR(totals.tax);
    
    // Shipping
    if (elShipping) {
      if (totals.subtotal === 0) {
        elShipping.innerText = '₹0';
      } else if (totals.shipping === 0) {
        elShipping.innerHTML = '<span class="text-green-600 font-bold">FREE</span>';
      } else {
        elShipping.innerText = cartEngine.formatINR(totals.shipping);
      }
    }

    // Free Shipping Progress
    if (elShippingText) {
      if (totals.subtotal >= totals.freeShippingThreshold) {
        elShippingText.innerHTML = '<span class="text-green-600 font-bold">🎉 Congratulations! You unlocked Free Shipping.</span>';
      } else if (totals.subtotal > 0) {
        elShippingText.innerHTML = `Spend <strong class="text-primary font-bold">${cartEngine.formatINR(totals.shippingRemaining)}</strong> more for <span class="font-bold text-primary">Free Shipping</span>`;
      } else {
        elShippingText.innerHTML = `Spend <strong class="text-primary font-bold">₹2,999</strong> for <span class="font-bold text-primary">Free Shipping</span>`;
      }
    }

    if (elShippingProgressBar) {
      elShippingProgressBar.style.width = totals.shippingProgress + '%';
    }

    // Coupon discount
    if (elDiscountRow && elDiscount) {
      if (totals.couponDiscount > 0) {
        elDiscountRow.style.display = 'flex';
        elDiscount.innerText = '-' + cartEngine.formatINR(totals.couponDiscount);
        if (elDiscountLabel && totals.coupon) {
          elDiscountLabel.innerHTML = `Coupon (${totals.coupon.code}) <button type="button" id="btn-remove-coupon" class="text-xs text-red-500 hover:underline ml-1">Remove</button>`;
          const btnRemoveCoupon = document.getElementById('btn-remove-coupon');
          if (btnRemoveCoupon) {
            btnRemoveCoupon.onclick = function() {
              cartEngine.removeCoupon();
              showToast('Coupon removed');
            };
          }
        }
      } else {
        elDiscountRow.style.display = 'none';
      }
    }

    // Grand total
    if (elGrandTotal) {
      elGrandTotal.innerText = cartEngine.formatINR(totals.grandTotal);
    }
  }

  // Toast notification helper
  function showToast(message, type = 'success') {
    const existing = document.querySelectorAll('.sellzy-toast');
    existing.forEach(t => t.remove());

    const toast = document.createElement('div');
    toast.className = `sellzy-toast fixed bottom-6 right-6 px-5 py-3 rounded-xl shadow-2xl flex items-center gap-3 z-99 text-xs font-semibold animate-bounce ${
      type === 'error' ? 'bg-red-600 text-white' : 'bg-[#0d7d6f] text-white'
    }`;
    toast.innerHTML = `<span class="bg-white/20 p-1 rounded-full">&#10003;</span> <span>${message}</span>`;
    document.body.appendChild(toast);
    setTimeout(() => {
      toast.remove();
    }, 2800);
  }

  // Delegate Events on Table Body
  if (tbody) {
    tbody.addEventListener('click', function(e) {
      const btnPlus = e.target.closest('.btn-qty-plus');
      const btnMinus = e.target.closest('.btn-qty-minus');
      const btnDelete = e.target.closest('.btn-delete-item');
      const btnEdit = e.target.closest('.btn-edit-item');
      const btnWishlist = e.target.closest('.btn-wishlist-item');

      if (btnPlus) {
        const index = parseInt(btnPlus.getAttribute('data-index'), 10);
        const res = cartEngine.updateQuantity(index, 1);
        if (res === 'max_stock_reached') {
          showToast('Maximum available stock reached for this item', 'error');
        }
      } else if (btnMinus) {
        const index = parseInt(btnMinus.getAttribute('data-index'), 10);
        const res = cartEngine.updateQuantity(index, -1);
        if (res === 'confirm_remove') {
          if (confirm('Do you want to remove this product from your cart?')) {
            cartEngine.removeItem(index);
            showToast('Item removed from cart');
          }
        }
      } else if (btnDelete) {
        const index = parseInt(btnDelete.getAttribute('data-index'), 10);
        const item = cartEngine.getItems()[index];
        if (confirm(`Remove "${item.name}" from your cart?`)) {
          cartEngine.removeItem(index);
          showToast(`Removed "${item.name}" from cart`);
        }
      } else if (btnEdit) {
        const index = parseInt(btnEdit.getAttribute('data-index'), 10);
        openEditModal(index);
      } else if (btnWishlist) {
        const index = parseInt(btnWishlist.getAttribute('data-index'), 10);
        const item = cartEngine.getItems()[index];
        cartEngine.addToWishlist(item);
        showToast(`Saved "${item.name}" to your Wishlist!`);
      }
    });
  }

  // Edit Modal Handler
  function openEditModal(index) {
    const items = cartEngine.getItems();
    if (index < 0 || index >= items.length) return;
    currentEditingIndex = index;
    const item = items[index];

    // Populate modal fields
    const modalImg = document.getElementById('edit-modal-img');
    const modalTitle = document.getElementById('edit-modal-title');
    const modalPrice = document.getElementById('edit-modal-price');
    const selectSize = document.getElementById('edit-modal-size');
    const selectColor = document.getElementById('edit-modal-color');
    const inputQty = document.getElementById('edit-modal-qty');

    if (modalImg) modalImg.src = item.image;
    if (modalTitle) modalTitle.innerText = item.name;
    if (modalPrice) modalPrice.innerText = cartEngine.formatINR(item.price);
    if (selectSize) selectSize.value = item.size || '250 ML';
    if (selectColor) selectColor.value = item.color || 'Black';
    if (inputQty) inputQty.value = item.qty || 1;

    if (editModal) {
      editModal.classList.remove('hidden');
      editModal.classList.add('flex');
    }
  }

  function closeEditModal() {
    if (editModal) {
      editModal.classList.add('hidden');
      editModal.classList.remove('flex');
    }
    currentEditingIndex = -1;
  }

  if (editModalCancelBtn) {
    editModalCancelBtn.addEventListener('click', closeEditModal);
  }

  if (editModalForm) {
    editModalForm.addEventListener('submit', function(e) {
      e.preventDefault();
      if (currentEditingIndex === -1) return;

      const newSize = document.getElementById('edit-modal-size').value;
      const newColor = document.getElementById('edit-modal-color').value;
      const newQty = parseInt(document.getElementById('edit-modal-qty').value, 10) || 1;

      cartEngine.updateItemVariant(currentEditingIndex, {
        size: newSize,
        color: newColor,
        qty: Math.max(1, newQty)
      });

      closeEditModal();
      showToast('Product options updated successfully!');
    });
  }

  // Remove All Modal Handlers
  if (btnRemoveAll) {
    btnRemoveAll.addEventListener('click', function() {
      if (cartEngine.getItems().length === 0) return;
      if (removeAllModal) {
        removeAllModal.classList.remove('hidden');
        removeAllModal.classList.add('flex');
      }
    });
  }

  if (removeAllCancelBtn) {
    removeAllCancelBtn.addEventListener('click', function() {
      if (removeAllModal) {
        removeAllModal.classList.add('hidden');
        removeAllModal.classList.remove('flex');
      }
    });
  }

  if (removeAllConfirmBtn) {
    removeAllConfirmBtn.addEventListener('click', function() {
      cartEngine.clearCart();
      if (removeAllModal) {
        removeAllModal.classList.add('hidden');
        removeAllModal.classList.remove('flex');
      }
      showToast('All items removed from cart');
    });
  }

  // Coupon Apply
  if (couponApplyBtn && couponInput) {
    couponApplyBtn.addEventListener('click', function() {
      const code = couponInput.value.trim();
      const res = cartEngine.applyCoupon(code);
      if (res.success) {
        showToast(res.message);
        couponInput.value = '';
        if (couponMessage) {
          couponMessage.className = 'text-xs text-green-600 font-semibold mt-1 block';
          couponMessage.innerText = res.message;
        }
      } else {
        showToast(res.message, 'error');
        if (couponMessage) {
          couponMessage.className = 'text-xs text-red-600 font-semibold mt-1 block';
          couponMessage.innerText = res.message;
        }
      }
    });
  }

  // Listen to engine updates
  window.addEventListener('sellzy:cart-updated', function() {
    renderCart();
  });

  // Initial render
  renderCart();
});

