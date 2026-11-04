/**
 * Sellzy Dynamic Product Details Controller
 * Reads product ID or slug from URL query, updates gallery, variants, prices, inventory, and Add to Cart
 */
document.addEventListener('DOMContentLoaded', function() {
  const catalog = window.SellzyCatalog;
  const cartEngine = window.SellzyCart;
  if (!catalog) return;

  // 1. Get Product ID/slug from URL query parameters
  const urlParams = new URLSearchParams(window.location.search);
  const productId = urlParams.get('id') || urlParams.get('slug') || urlParams.get('product') || 'vitallife-omega-3';

  const product = catalog.getByIdOrSlug(productId);
  if (!product) return;

  // Active state
  let selectedSize = product.sizes && product.sizes.length ? product.sizes[0] : { name: 'Standard', priceMod: 0 };
  let selectedColor = product.colors && product.colors.length ? product.colors[0] : { name: 'Standard', hex: '#0d7d6f' };
  let currentQty = 1;
  let activeImageIndex = 0;

  // 2. Update Page Meta & Breadcrumbs
  document.title = `${product.name} | Sellzy eCommerce`;

  const bcCategory = document.getElementById('bc-product-category');
  const bcTitle = document.getElementById('bc-product-title');
  if (bcCategory) bcCategory.innerText = product.category;
  if (bcTitle) bcTitle.innerText = product.name;

  // 3. Dynamic Product Information
  const elTitle = document.getElementById('detail-product-title');
  if (elTitle) elTitle.innerText = product.name;

  const elBrand = document.getElementById('detail-product-brand');
  if (elBrand) elBrand.innerText = product.brand;

  const elSku = document.getElementById('detail-product-sku');
  if (elSku) elSku.innerText = product.sku;

  const elReviews = document.getElementById('detail-product-reviews');
  if (elReviews) elReviews.innerText = `(${product.reviews.toLocaleString()} reviews)`;

  const elRatingVal = document.getElementById('detail-product-rating-val');
  if (elRatingVal) elRatingVal.innerText = product.rating;

  const elStock = document.getElementById('detail-product-stock');
  if (elStock) elStock.innerText = `${product.stock} units in stock`;

  const elDescription = document.getElementById('detail-product-description');
  if (elDescription) elDescription.innerText = product.description;

  // 4. Price & Discount Function
  function updatePriceDisplay() {
    const unitPrice = product.price + (selectedSize.priceMod || 0);
    const origPrice = product.originalPrice + (selectedSize.priceMod || 0);
    const discount = catalog.calculateDiscount(unitPrice, origPrice);

    const elCurrentPrice = document.getElementById('detail-current-price');
    const elOldPrice = document.getElementById('detail-old-price');
    const elDiscountBadge = document.getElementById('detail-discount-badge');

    if (elCurrentPrice) elCurrentPrice.innerText = cartEngine ? cartEngine.formatINR(unitPrice) : `₹${unitPrice}`;
    if (elOldPrice) {
      if (origPrice > unitPrice) {
        elOldPrice.style.display = 'inline-block';
        elOldPrice.innerText = cartEngine ? cartEngine.formatINR(origPrice) : `₹${origPrice}`;
      } else {
        elOldPrice.style.display = 'none';
      }
    }
    if (elDiscountBadge) {
      if (discount > 0) {
        elDiscountBadge.style.display = 'inline-block';
        elDiscountBadge.innerText = `${discount}% OFF`;
      } else {
        elDiscountBadge.style.display = 'none';
      }
    }
  }

  updatePriceDisplay();

  // 5. Image Gallery Rendering
  const mainImage = document.getElementById('detail-main-image');
  const thumbsContainer = document.getElementById('detail-gallery-thumbnails');
  const galleryImages = product.images && product.images.length ? product.images : ['./assets/images/product-details/product-details-slider-1.png'];

  function setMainImage(index) {
    if (index < 0) index = galleryImages.length - 1;
    if (index >= galleryImages.length) index = 0;
    activeImageIndex = index;

    if (mainImage) {
      mainImage.src = galleryImages[activeImageIndex];
      mainImage.alt = product.name;
    }

    // Update active thumb border
    const thumbs = document.querySelectorAll('.gallery-thumb-btn');
    thumbs.forEach((t, i) => {
      if (i === activeImageIndex) {
        t.classList.add('border-[#0d7d6f]', 'ring-2', 'ring-[#0d7d6f]/30');
        t.classList.remove('border-gray-200');
      } else {
        t.classList.remove('border-[#0d7d6f]', 'ring-2', 'ring-[#0d7d6f]/30');
        t.classList.add('border-gray-200');
      }
    });
  }

  if (thumbsContainer) {
    thumbsContainer.innerHTML = '';
    galleryImages.forEach((imgUrl, idx) => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = `gallery-thumb-btn w-16 h-16 sm:w-20 sm:h-20 rounded-xl overflow-hidden border p-1 bg-white transition-all shrink-0 hover:border-[#0d7d6f] ${
        idx === 0 ? 'border-[#0d7d6f] ring-2 ring-[#0d7d6f]/30' : 'border-gray-200'
      }`;
      btn.innerHTML = `<img src="${imgUrl}" alt="${product.name} thumb ${idx+1}" class="w-full h-full object-contain" />`;
      btn.addEventListener('click', () => setMainImage(idx));
      thumbsContainer.appendChild(btn);
    });
  }

  setMainImage(0);

  // Gallery Prev / Next Buttons
  const btnPrev = document.getElementById('btn-gallery-prev');
  const btnNext = document.getElementById('btn-gallery-next');
  if (btnPrev) btnPrev.addEventListener('click', () => setMainImage(activeImageIndex - 1));
  if (btnNext) btnNext.addEventListener('click', () => setMainImage(activeImageIndex + 1));

  // 6. Variants: Color Swatches
  const colorContainer = document.getElementById('detail-color-swatches');
  const colorLabel = document.getElementById('detail-selected-color');
  if (colorContainer && product.colors) {
    colorContainer.innerHTML = '';
    product.colors.forEach((c, idx) => {
      const cBtn = document.createElement('button');
      cBtn.type = 'button';
      cBtn.className = `color-swatch-btn size-8 rounded-full border-2 transition-transform duration-200 hover:scale-110 flex items-center justify-center ${
        idx === 0 ? 'border-[#0d7d6f] ring-2 ring-[#0d7d6f]/40 scale-105' : 'border-gray-300'
      }`;
      cBtn.style.backgroundColor = c.hex;
      cBtn.title = c.name;
      cBtn.innerHTML = idx === 0 ? '<span class="text-white text-xs font-bold leading-none">&#10003;</span>' : '';

      cBtn.addEventListener('click', function() {
        selectedColor = c;
        if (colorLabel) colorLabel.innerText = c.name;
        document.querySelectorAll('.color-swatch-btn').forEach(b => {
          b.className = 'color-swatch-btn size-8 rounded-full border-2 border-gray-300 transition-transform duration-200 hover:scale-110 flex items-center justify-center';
          b.innerHTML = '';
        });
        this.className = 'color-swatch-btn size-8 rounded-full border-2 border-[#0d7d6f] ring-2 ring-[#0d7d6f]/40 scale-105 flex items-center justify-center';
        this.innerHTML = '<span class="text-white text-xs font-bold leading-none">&#10003;</span>';
      });

      colorContainer.appendChild(cBtn);
    });
    if (colorLabel && product.colors.length) colorLabel.innerText = product.colors[0].name;
  }

  // 7. Variants: Size Selector Pills
  const sizeContainer = document.getElementById('detail-size-pills');
  const sizeLabel = document.getElementById('detail-selected-size');
  if (sizeContainer && product.sizes) {
    sizeContainer.innerHTML = '';
    product.sizes.forEach((s, idx) => {
      const sBtn = document.createElement('button');
      sBtn.type = 'button';
      sBtn.className = `size-pill-btn px-4 py-2 rounded-xl text-xs font-semibold border transition-all ${
        idx === 0 ? 'bg-[#0d7d6f] text-white border-[#0d7d6f] shadow-sm' : 'bg-white text-gray-700 border-gray-300 hover:border-[#0d7d6f]'
      }`;
      sBtn.innerText = s.name;

      sBtn.addEventListener('click', function() {
        selectedSize = s;
        if (sizeLabel) sizeLabel.innerText = s.name;
        document.querySelectorAll('.size-pill-btn').forEach(b => {
          b.className = 'size-pill-btn px-4 py-2 rounded-xl text-xs font-semibold border bg-white text-gray-700 border-gray-300 hover:border-[#0d7d6f]';
        });
        this.className = 'size-pill-btn px-4 py-2 rounded-xl text-xs font-semibold border bg-[#0d7d6f] text-white border-[#0d7d6f] shadow-sm';
        updatePriceDisplay();
      });

      sizeContainer.appendChild(sBtn);
    });
    if (sizeLabel && product.sizes.length) sizeLabel.innerText = product.sizes[0].name;
  }

  // 8. Quantity Controls
  const inputQty = document.getElementById('detail-qty-input');
  const btnMinus = document.getElementById('detail-qty-minus');
  const btnPlus = document.getElementById('detail-qty-plus');

  if (btnMinus) {
    btnMinus.addEventListener('click', function() {
      if (currentQty > 1) {
        currentQty--;
        if (inputQty) inputQty.value = currentQty;
      }
    });
  }

  if (btnPlus) {
    btnPlus.addEventListener('click', function() {
      if (currentQty < product.stock) {
        currentQty++;
        if (inputQty) inputQty.value = currentQty;
      } else {
        showToast('Maximum available stock limit reached', 'error');
      }
    });
  }

  if (inputQty) {
    inputQty.addEventListener('change', function() {
      let val = parseInt(this.value, 10);
      if (isNaN(val) || val < 1) val = 1;
      if (val > product.stock) val = product.stock;
      currentQty = val;
      this.value = currentQty;
    });
  }

  // Toast Helper
  function showToast(message, type = 'success') {
    const existing = document.querySelectorAll('.sellzy-toast');
    existing.forEach(t => t.remove());

    const toast = document.createElement('div');
    toast.className = `sellzy-toast fixed bottom-6 right-6 px-5 py-3 rounded-xl shadow-2xl flex items-center gap-3 z-99 text-xs font-semibold animate-bounce ${
      type === 'error' ? 'bg-red-600 text-white' : 'bg-[#0d7d6f] text-white'
    }`;
    toast.innerHTML = `<span class="bg-white/20 p-1 rounded-full">&#10003;</span> <span>${message}</span>`;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 2800);
  }

  // 9. Add To Cart Button
  const btnAddToCart = document.getElementById('detail-add-to-cart-btn');
  if (btnAddToCart) {
    btnAddToCart.addEventListener('click', function(e) {
      e.preventDefault();
      const unitPrice = product.price + (selectedSize.priceMod || 0);
      const origPrice = product.originalPrice + (selectedSize.priceMod || 0);

      cartEngine.addItem({
        id: product.id,
        slug: product.slug,
        name: product.name,
        image: galleryImages[activeImageIndex] || galleryImages[0],
        price: unitPrice,
        originalPrice: origPrice,
        size: selectedSize.name,
        color: selectedColor.name,
        qty: currentQty,
        available: product.stock,
        rating: product.rating,
        reviews: product.reviews
      });

      showToast(`Added ${currentQty}x "${product.name}" (${selectedSize.name}, ${selectedColor.name}) to Cart!`);
    });
  }

  // 10. Buy Now Button (Instant Add & Navigate to Cart)
  const btnBuyNow = document.getElementById('detail-buy-now-btn');
  if (btnBuyNow) {
    btnBuyNow.addEventListener('click', function(e) {
      e.preventDefault();
      const unitPrice = product.price + (selectedSize.priceMod || 0);
      const origPrice = product.originalPrice + (selectedSize.priceMod || 0);

      cartEngine.addItem({
        id: product.id,
        slug: product.slug,
        name: product.name,
        image: galleryImages[activeImageIndex] || galleryImages[0],
        price: unitPrice,
        originalPrice: origPrice,
        size: selectedSize.name,
        color: selectedColor.name,
        qty: currentQty,
        available: product.stock,
        rating: product.rating,
        reviews: product.reviews
      });

      window.location.href = 'cart-single-vendor.html';
    });
  }

  // 11. Wishlist Button
  const btnWishlist = document.getElementById('detail-wishlist-btn');
  if (btnWishlist) {
    btnWishlist.addEventListener('click', function(e) {
      e.preventDefault();
      cartEngine.addToWishlist({
        id: product.id,
        name: product.name,
        image: galleryImages[0],
        price: product.price
      });
      showToast(`Saved "${product.name}" to your Wishlist!`);
      this.classList.add('text-red-500', 'bg-red-50');
    });
  }

  // 12. Specifications Table Rendering
  const specsTbody = document.getElementById('detail-specs-tbody');
  if (specsTbody && product.specifications) {
    specsTbody.innerHTML = '';
    Object.entries(product.specifications).forEach(([k, v]) => {
      const row = document.createElement('tr');
      row.className = 'border-b border-gray-100';
      row.innerHTML = `
        <td class="py-3 px-4 font-semibold text-gray-700 bg-gray-50/70 w-1/3 text-xs">${k}</td>
        <td class="py-3 px-4 text-gray-600 text-xs">${v}</td>
      `;
      specsTbody.appendChild(row);
    });
  }

  // 13. Related Products Grid Rendering
  const relatedGrid = document.getElementById('detail-related-products-grid');
  if (relatedGrid) {
    const relatedList = catalog.getRelated(product, 4);
    relatedGrid.innerHTML = '';
    relatedList.forEach(rel => {
      const discount = catalog.calculateDiscount(rel.price, rel.originalPrice);
      const card = document.createElement('div');
      card.className = 'bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-xs hover:shadow-lg transition-all duration-300 flex flex-col group';
      card.innerHTML = `
        <a href="product-details.html?id=${rel.slug}" class="relative overflow-hidden bg-gray-50 aspect-square block p-4">
          ${discount > 0 ? `<span class="absolute top-3 left-3 bg-[#f5a623] text-black font-bold text-[10px] px-2 py-0.5 rounded-full z-10">${discount}% OFF</span>` : ''}
          <img src="${rel.images[0]}" alt="${rel.name}" class="w-full h-full object-contain group-hover:scale-105 transition-transform duration-300" />
        </a>
        <div class="p-4 flex-1 flex flex-col justify-between">
          <div>
            <span class="text-[11px] text-gray-400 font-medium block mb-1">${rel.category}</span>
            <a href="product-details.html?id=${rel.slug}" class="font-bold text-gray-900 text-xs hover:text-[#0d7d6f] transition-colors line-clamp-2 leading-snug">
              ${rel.name}
            </a>
            <div class="flex items-center gap-1 text-amber-500 text-xs mt-1.5">
              <span>&#9733; ${rel.rating}</span>
              <span class="text-gray-400">(${rel.reviews.toLocaleString()})</span>
            </div>
          </div>
          <div class="mt-3 pt-3 border-t border-gray-100 flex items-center justify-between">
            <div>
              <span class="text-sm font-extrabold text-[#0d7d6f]">${cartEngine.formatINR(rel.price)}</span>
              ${rel.originalPrice > rel.price ? `<span class="text-xs text-gray-400 line-through ml-1">${cartEngine.formatINR(rel.originalPrice)}</span>` : ''}
            </div>
            <a href="product-details.html?id=${rel.slug}" class="bg-gray-100 hover:bg-[#0d7d6f] text-gray-700 hover:text-white p-2 rounded-lg transition-colors" title="View Product">
              <i class="hgi hgi-stroke hgi-arrow-right-01 text-sm"></i>
            </a>
          </div>
        </div>
      `;
      relatedGrid.appendChild(card);
    });
  }

});

