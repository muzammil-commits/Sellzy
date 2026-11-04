import os

DYNAMIC_PRODUCT_DETAILS_HTML = """
    <!-- ========== Breadcrumb Section Start ========== -->
    <div class="py-5 bg-gray-50 border-b border-gray-200">
      <div class="container mx-auto px-4">
        <div class="flex items-center gap-2 text-xs text-gray-500 flex-wrap">
          <a href="index.html" class="hover:text-[#0d7d6f] flex items-center gap-1 font-medium">
            <i class="hgi hgi-stroke hgi-home-01 text-sm"></i> Home
          </a>
          <span>/</span>
          <a href="shop-left-sidebar-4col.html" class="hover:text-[#0d7d6f] font-medium" id="bc-product-category">Healthcare & Wellness</a>
          <span>/</span>
          <span class="text-gray-900 font-semibold" id="bc-product-title">VitaLife Omega-3 Softgels</span>
        </div>
      </div>
    </div>
    <!-- ========== Breadcrumb Section End ========== -->

    <!-- ========== Product Details Section Start ========== -->
    <section class="py-10 bg-white">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start">
          
          <!-- Left Column: Premium Gallery (Desktop: Thumbnails + Main Image; Mobile: Responsive Stack) -->
          <div class="lg:col-span-7 col-span-12">
            <div class="flex flex-col-reverse md:flex-row gap-4 sm:gap-6 items-start">
              
              <!-- Vertical Thumbnails Column -->
              <div id="detail-gallery-thumbnails" class="flex md:flex-col gap-3 overflow-x-auto md:overflow-y-auto max-h-[550px] w-full md:w-24 shrink-0 pb-2 md:pb-0 scrollbar-thin">
                <!-- Dynamically populated by product-details.js -->
              </div>

              <!-- Main Product Image Frame with Controls -->
              <div class="relative w-full flex-1 rounded-3xl bg-gray-50 border border-gray-200 p-6 sm:p-10 flex items-center justify-center overflow-hidden aspect-square sm:aspect-4/3 md:aspect-square group">
                <img
                  id="detail-main-image"
                  src="./assets/images/product-details/product-details-slider-1.png"
                  alt="Product Image"
                  class="w-full h-full object-contain transition-transform duration-300 group-hover:scale-105"
                />

                <!-- Prev / Next Image Navigation Arrows -->
                <button
                  type="button"
                  id="btn-gallery-prev"
                  class="absolute left-3 top-1/2 -translate-y-1/2 size-10 rounded-full bg-white/90 hover:bg-white text-gray-800 shadow-md flex items-center justify-center transition-all hover:scale-110 z-10"
                  title="Previous Image"
                >
                  <i class="hgi hgi-stroke hgi-arrow-left-01 text-lg"></i>
                </button>
                <button
                  type="button"
                  id="btn-gallery-next"
                  class="absolute right-3 top-1/2 -translate-y-1/2 size-10 rounded-full bg-white/90 hover:bg-white text-gray-800 shadow-md flex items-center justify-center transition-all hover:scale-110 z-10"
                  title="Next Image"
                >
                  <i class="hgi hgi-stroke hgi-arrow-right-01 text-lg"></i>
                </button>
              </div>

            </div>
          </div>

          <!-- Right Column: Product Information, Variants & Purchase Actions -->
          <div class="lg:col-span-5 col-span-12">
            <div class="border border-gray-200 rounded-3xl p-6 sm:p-8 bg-white shadow-xs">
              
              <!-- Badges -->
              <div class="flex items-center gap-2 mb-3">
                <span class="bg-red-600 text-white font-bold text-[11px] px-2.5 py-0.5 rounded uppercase tracking-wider">SALES</span>
                <span class="bg-[#0d7d6f]/10 text-[#0d7d6f] font-bold text-[11px] px-2.5 py-0.5 rounded uppercase tracking-wider">NEW ARRIVAL</span>
                <span class="bg-emerald-100 text-emerald-800 font-semibold text-[11px] px-2 py-0.5 rounded" id="detail-product-stock">In Stock</span>
              </div>

              <!-- Product Title & Wishlist -->
              <div class="flex items-start justify-between gap-4 mb-3">
                <h1 id="detail-product-title" class="text-2xl sm:text-3xl font-extrabold text-gray-900 leading-tight">
                  VitaLife Omega-3 Softgels Heart Support Max Strength
                </h1>
                <button
                  type="button"
                  id="detail-wishlist-btn"
                  class="size-11 rounded-full bg-gray-100 hover:bg-red-50 text-gray-500 hover:text-red-500 border border-gray-200 flex items-center justify-center shrink-0 transition-all hover:scale-105"
                  title="Add to Wishlist"
                >
                  <i class="hgi hgi-stroke hgi-favourite text-xl"></i>
                </button>
              </div>

              <!-- Ratings -->
              <div class="flex items-center gap-2 mb-5 text-sm">
                <div class="flex items-center text-amber-500">
                  <span>&#9733;&#9733;&#9733;&#9733;&#9733;</span>
                </div>
                <span id="detail-product-reviews" class="text-xs text-gray-500 font-medium">(11.78k reviews)</span>
                <span class="text-gray-300">|</span>
                <span class="text-xs text-gray-400">SKU: <strong class="text-gray-700" id="detail-product-sku">SLZ-HLTH-001</strong></span>
              </div>

              <!-- Price Section (Selling price, Original price, mathematically accurate discount) -->
              <div class="flex items-baseline gap-3 mb-6 pb-6 border-b border-gray-100">
                <span id="detail-current-price" class="text-3xl font-extrabold text-[#0d7d6f]">₹2,999</span>
                <span id="detail-old-price" class="text-lg text-gray-400 line-through">₹3,499</span>
                <span id="detail-discount-badge" class="bg-[#f5a623] text-black font-extrabold text-xs px-2.5 py-1 rounded-full uppercase tracking-wider">14% OFF</span>
              </div>

              <!-- Color Variants -->
              <div class="mb-5">
                <div class="flex items-center justify-between mb-2">
                  <span class="text-xs font-bold text-gray-800 uppercase tracking-wide">
                    Color: <span id="detail-selected-color" class="font-normal text-gray-600">Emerald Green</span>
                  </span>
                </div>
                <div id="detail-color-swatches" class="flex items-center gap-3">
                  <!-- Populated dynamically -->
                </div>
              </div>

              <!-- Size / Volume Variants -->
              <div class="mb-6">
                <div class="flex items-center justify-between mb-2">
                  <span class="text-xs font-bold text-gray-800 uppercase tracking-wide">
                    Size: <span id="detail-selected-size" class="font-normal text-gray-600">S (60 Softgels)</span>
                  </span>
                  <a href="#specifications" class="text-[11px] text-[#0d7d6f] hover:underline font-medium">Specs & Guide</a>
                </div>
                <div id="detail-size-pills" class="flex flex-wrap items-center gap-2">
                  <!-- Populated dynamically -->
                </div>
              </div>

              <!-- Quantity Selector & Action Buttons -->
              <div class="space-y-4 mb-6">
                <div class="flex items-center gap-4">
                  <span class="text-xs font-bold text-gray-800 uppercase tracking-wide">Quantity:</span>
                  <div class="inline-flex items-center border border-gray-300 rounded-xl p-1 bg-white shadow-xs">
                    <button type="button" id="detail-qty-minus" class="size-8 rounded-lg inline-flex items-center justify-center hover:bg-gray-100 text-gray-700 font-bold transition-colors">
                      &minus;
                    </button>
                    <input type="number" id="detail-qty-input" value="1" min="1" max="50" class="w-12 text-center text-sm font-bold text-gray-900 border-none focus:outline-none" />
                    <button type="button" id="detail-qty-plus" class="size-8 rounded-lg inline-flex items-center justify-center hover:bg-gray-100 text-gray-700 font-bold transition-colors">
                      &#43;
                    </button>
                  </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                  <!-- Add to Cart -->
                  <button
                    type="button"
                    id="detail-add-to-cart-btn"
                    class="w-full bg-[#0d7d6f] hover:bg-[#09574d] text-white font-bold py-3.5 px-6 rounded-xl shadow-md hover:shadow-lg transition-all flex items-center justify-center gap-2 text-sm"
                  >
                    <i class="hgi hgi-stroke hgi-shopping-cart-01 text-lg"></i> Add to Cart
                  </button>

                  <!-- Buy Now -->
                  <button
                    type="button"
                    id="detail-buy-now-btn"
                    class="w-full bg-[#f5a623] hover:bg-amber-500 text-black font-extrabold py-3.5 px-6 rounded-xl shadow-md hover:shadow-lg transition-all flex items-center justify-center gap-2 text-sm"
                  >
                    <i class="hgi hgi-stroke hgi-flash text-lg"></i> Buy Now
                  </button>
                </div>
              </div>

              <!-- Product Highlights & Guarantees -->
              <div class="pt-5 border-t border-gray-100 space-y-2.5 text-xs text-gray-600">
                <div class="flex items-center gap-2.5">
                  <span class="text-[#0d7d6f] font-bold">&#10003;</span>
                  <span><strong>Free Express Shipping</strong> on orders above ₹999</span>
                </div>
                <div class="flex items-center gap-2.5">
                  <span class="text-[#0d7d6f] font-bold">&#10003;</span>
                  <span><strong>30-Day Easy Returns</strong> & Hassle-free Exchange</span>
                </div>
                <div class="flex items-center gap-2.5">
                  <span class="text-[#0d7d6f] font-bold">&#10003;</span>
                  <span><strong>100% Genuine Product</strong> direct from certified manufacturers</span>
                </div>
              </div>

            </div>
          </div>

        </div>

        <!-- Specifications & Description Section -->
        <div id="specifications" class="mt-14 pt-10 border-t border-gray-200">
          <div class="max-w-4xl">
            <h3 class="text-xl font-bold text-gray-900 mb-4">Product Description</h3>
            <p id="detail-product-description" class="text-sm text-gray-600 leading-relaxed mb-8">
              <!-- Dynamically populated -->
            </p>

            <h3 class="text-xl font-bold text-gray-900 mb-4">Product Specifications</h3>
            <div class="border border-gray-200 rounded-2xl overflow-hidden shadow-xs mb-12">
              <table class="w-full text-left border-collapse">
                <tbody id="detail-specs-tbody">
                  <!-- Dynamically populated -->
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- Related Products Section -->
        <div class="mt-12 pt-10 border-t border-gray-200">
          <div class="flex items-center justify-between mb-8">
            <div>
              <span class="text-xs font-bold uppercase tracking-wider text-[#0d7d6f]">Recommended</span>
              <h3 class="text-2xl font-bold text-gray-900 mt-1">Related Products You May Like</h3>
            </div>
            <a href="shop-left-sidebar-4col.html" class="text-xs font-semibold text-[#0d7d6f] hover:underline flex items-center gap-1">
              View All <i class="hgi hgi-stroke hgi-arrow-right-01"></i>
            </a>
          </div>

          <div id="detail-related-products-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <!-- Dynamically populated -->
          </div>
        </div>

      </div>
    </section>
    <!-- ========== Product Details Section End ========== -->
"""

with open('product-details.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate section start and end
start_marker = '<!-- ========== Breadcrumb Section Start ========== -->'
end_marker = '<!-- ========== Product Details Section End ========== -->'

if start_marker in html and end_marker in html:
    idx_start = html.find(start_marker)
    idx_end = html.find(end_marker) + len(end_marker)
    new_html = html[:idx_start] + DYNAMIC_PRODUCT_DETAILS_HTML + html[idx_end:]
else:
    # Find breadcrumb or section
    sec_start = html.find('<section')
    sec_end = html.find('<!-- ========== Footer Section Start')
    new_html = html[:sec_start] + DYNAMIC_PRODUCT_DETAILS_HTML + html[sec_end:]

# Ensure products-data.js, cart-engine.js and product-details.js are linked
scripts = """
    <!-- ========== Sellzy Dynamic Product & Cart System ========== -->
    <script src="./assets/js/products-data.js"></script>
    <script src="./assets/js/cart-engine.js"></script>
    <script src="./assets/js/product-details.js"></script>
"""

# Replace any existing script tags or append before </body>
if 'product-details.js' not in new_html:
    new_html = new_html.replace('</body>', scripts + '\n  </body>')
elif 'products-data.js' not in new_html:
    new_html = new_html.replace('<script src="./assets/js/cart-engine.js"></script>', '<script src="./assets/js/products-data.js"></script>\n    <script src="./assets/js/cart-engine.js"></script>')

with open('product-details.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

with open('product-details', 'w', encoding='utf-8') as f:
    f.write(new_html)

# Also update other product-details versions (product-details-2 to 6)
for v in [2, 3, 4, 5, 6]:
    v_html = f'product-details-{v}.html'
    v_clean = f'product-details-{v}'
    if os.path.exists(v_html):
        with open(v_html, 'w', encoding='utf-8') as f:
            f.write(new_html)
    if os.path.exists(v_clean):
        with open(v_clean, 'w', encoding='utf-8') as f:
            f.write(new_html)

print("Dynamic Product Details page updated across all versions!")
