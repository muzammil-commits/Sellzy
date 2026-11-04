import os

CART_SECTION_HTML = """
    <!-- ========== Cart vendor Section Start ========== -->
    <div class="pb-[70px]">
      <div class="container mx-auto px-4">
        
        <!-- Cart Content Wrapper (Hidden when empty) -->
        <div id="cart-content-wrapper">
          <div class="grid grid-cols-12 mb-6">
            <div class="xl:col-span-8 col-span-12 flex items-center justify-between xl:px-2 px-0">
              <div class="flex items-center gap-x-2">
                <h3 class="text-2xl font-bold text-gray-900">Cart</h3>
                <span id="cart-page-item-count" class="text-sm font-semibold text-gray-500">(3 items)</span>
              </div>
              <div>
                <button
                  type="button"
                  id="btn-remove-all"
                  class="inline-flex gap-x-1.5 items-center justify-center font-semibold text-sm text-red-600 hover:text-red-700 transition-colors py-1.5 px-3 rounded-lg hover:bg-red-50"
                >
                  <i class="hgi hgi-stroke hgi-cancel-01 text-base font-bold"></i>
                  Remove All
                </button>
              </div>
            </div>
          </div>

          <div class="grid grid-cols-12 gap-x-6 gap-y-6">
            <!-- Left Side: Table of Products -->
            <div class="xl:col-span-8 col-span-12">
              <div class="border border-gray-200 rounded-2xl overflow-x-auto bg-white shadow-xs">
                <table class="w-full text-left border-collapse">
                  <thead class="bg-gray-50 border-b border-gray-200 text-xs font-semibold text-gray-600 uppercase tracking-wider">
                    <tr>
                      <th class="py-3.5 pl-4 pr-3">Product</th>
                      <th class="py-3.5 px-3">Price</th>
                      <th class="py-3.5 px-3">Quantity</th>
                      <th class="py-3.5 px-3">Total Price</th>
                      <th class="py-3.5 pr-4 pl-3 text-center">Action</th>
                    </tr>
                  </thead>
                  <tbody id="cart-items-tbody">
                    <!-- Populated dynamically by cart-ui.js -->
                  </tbody>
                </table>
              </div>

              <!-- Continue shopping / features info -->
              <div class="mt-6 flex flex-wrap items-center justify-between gap-4 p-4 rounded-xl bg-gray-50 border border-gray-200">
                <a href="shop-left-sidebar-4col.html" class="inline-flex items-center gap-2 text-sm font-semibold text-[#0d7d6f] hover:underline">
                  <i class="hgi hgi-stroke hgi-arrow-left-01 text-base"></i> Continue Shopping
                </a>
                <div class="flex items-center gap-4 text-xs text-gray-500">
                  <span>🔒 100% Secure Checkout</span>
                  <span>⚡ Instant Order Confirmation</span>
                </div>
              </div>
            </div>

            <!-- Right Side: Free Shipping Progress & Order Summary -->
            <div class="xl:col-span-4 col-span-12">
              <div class="flex flex-col gap-y-5 sticky top-24">
                
                <!-- Free Shipping Progress Card -->
                <div class="border border-gray-200 rounded-2xl p-4 bg-emerald-50/50 shadow-xs">
                  <div class="flex items-center gap-2.5 mb-2.5 text-xs text-emerald-900">
                    <div class="w-7 h-7 rounded-full bg-[#0d7d6f]/15 text-[#0d7d6f] flex items-center justify-center shrink-0">
                      <i class="hgi hgi-stroke hgi-delivery-truck-01 text-base"></i>
                    </div>
                    <div id="free-shipping-text" class="font-medium text-xs">
                      Spend <strong class="text-primary font-bold">₹2,999</strong> for <span class="font-bold text-primary">Free Shipping</span>
                    </div>
                  </div>
                  <!-- Progress Bar -->
                  <div class="w-full bg-gray-200 h-2 rounded-full overflow-hidden">
                    <div id="free-shipping-progress-bar" class="bg-[#0d7d6f] h-full rounded-full transition-all duration-500" style="width: 50%;"></div>
                  </div>
                </div>

                <!-- Order Summary Card -->
                <div class="border border-gray-200 rounded-2xl p-6 bg-white shadow-xs">
                  <h4 class="text-lg font-bold text-gray-900 mb-5">Order Summary</h4>
                  
                  <!-- Coupon input -->
                  <div class="mb-5">
                    <div class="relative flex items-center">
                      <input
                        type="text"
                        id="cart-coupon-input"
                        placeholder="Coupon Code (e.g. SAVE10)"
                        class="w-full pl-4 pr-24 py-2.5 rounded-full border border-gray-300 text-xs focus:outline-none focus:border-[#0d7d6f] focus:ring-1 focus:ring-[#0d7d6f] uppercase"
                      />
                      <button
                        type="button"
                        id="cart-coupon-apply-btn"
                        class="absolute right-1 top-1 bottom-1 px-4 rounded-full bg-[#0d7d6f] hover:bg-[#09574d] text-white text-xs font-semibold transition-colors"
                      >
                        Apply
                      </button>
                    </div>
                    <span id="cart-coupon-message" class="hidden"></span>
                  </div>

                  <!-- Calculations breakdown -->
                  <div class="space-y-3.5 pb-4 border-b border-gray-200 text-sm">
                    <div class="flex items-center justify-between text-gray-600">
                      <span>Sub-Total</span>
                      <span id="cart-subtotal" class="font-semibold text-gray-900">₹0</span>
                    </div>

                    <!-- Discount Row (Hidden if no discount) -->
                    <div id="cart-discount-row" class="hidden items-center justify-between text-emerald-600 font-medium">
                      <span id="cart-discount-label">Coupon Discount</span>
                      <span id="cart-discount" class="font-bold">-₹0</span>
                    </div>

                    <div class="flex items-center justify-between text-gray-600">
                      <span>Estimated Tax (5% GST)</span>
                      <span id="cart-tax" class="font-semibold text-gray-900">₹0</span>
                    </div>

                    <div class="flex items-center justify-between text-gray-600">
                      <span>Shipping</span>
                      <span id="cart-shipping" class="font-semibold text-gray-900">₹0</span>
                    </div>
                  </div>

                  <!-- Total -->
                  <div class="pt-4 flex items-center justify-between text-lg font-extrabold text-gray-900 mb-6">
                    <span>Total Amount</span>
                    <span id="cart-grand-total" class="text-xl text-[#0d7d6f]">₹0</span>
                  </div>

                  <!-- Terms Agreement -->
                  <div class="flex items-start gap-2 mb-6">
                    <input type="checkbox" id="terms-agree" checked class="mt-0.5 rounded border-gray-300 text-[#0d7d6f] focus:ring-[#0d7d6f]" />
                    <label for="terms-agree" class="text-xs text-gray-500 leading-snug">
                      I agree with the <a href="about.html" class="text-[#0d7d6f] hover:underline">Terms and Conditions</a> and privacy policy.
                    </label>
                  </div>

                  <!-- Checkout Button -->
                  <a
                    href="checkout.html"
                    class="w-full bg-[#0d7d6f] hover:bg-[#09574d] text-white font-bold py-3.5 px-6 rounded-xl shadow-md hover:shadow-lg transition-all text-center block text-sm"
                  >
                    Proceed to Checkout
                  </a>
                </div>

              </div>
            </div>
          </div>
        </div>

        <!-- Empty Cart Screen (Shown when cart has 0 items) -->
        <div id="cart-empty-screen" class="hidden py-16 text-center max-w-md mx-auto">
          <div class="w-24 h-24 mx-auto rounded-full bg-emerald-50 text-[#0d7d6f] flex items-center justify-center mb-6 shadow-sm">
            <i class="hgi hgi-stroke hgi-shopping-cart-01 text-5xl"></i>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-2">Your Shopping Cart is Empty</h3>
          <p class="text-sm text-gray-500 mb-8 leading-relaxed">
            Looks like you haven't added anything to your cart yet. Discover trending products, new footwear, and exclusive deals today!
          </p>
          <div class="flex flex-wrap items-center justify-center gap-4">
            <a href="shop-left-sidebar-4col.html" class="bg-[#0d7d6f] hover:bg-[#09574d] text-white font-bold px-7 py-3 rounded-xl shadow-sm hover:shadow transition-colors text-sm">
              Explore Products
            </a>
            <a href="ebotas.html" class="bg-[#f5a623] hover:bg-amber-500 text-black font-bold px-7 py-3 rounded-xl shadow-sm hover:shadow transition-colors text-sm">
              Ebotas Footwear
            </a>
          </div>
        </div>

      </div>
    </div>
    <!-- ========== Cart vendor Section End ========== -->

    <!-- ========== Remove All Confirmation Modal ========== -->
    <div id="modal-remove-all" class="fixed inset-0 bg-black/60 backdrop-blur-xs z-99 hidden items-center justify-center p-4">
      <div class="bg-white rounded-2xl max-w-sm w-full p-6 shadow-2xl animate-fade-in text-center">
        <div class="w-12 h-12 rounded-full bg-red-100 text-red-600 flex items-center justify-center mx-auto mb-4">
          <i class="hgi hgi-stroke hgi-delete-01 text-2xl"></i>
        </div>
        <h4 class="text-lg font-bold text-gray-900 mb-2">Remove All Items?</h4>
        <p class="text-xs text-gray-500 mb-6 leading-relaxed">
          Are you sure you want to remove all products from your cart? This action cannot be undone.
        </p>
        <div class="flex items-center gap-3">
          <button type="button" id="btn-cancel-remove-all" class="flex-1 py-2.5 px-4 rounded-xl border border-gray-300 text-xs font-semibold text-gray-700 hover:bg-gray-50 transition-colors">
            Cancel
          </button>
          <button type="button" id="btn-confirm-remove-all" class="flex-1 py-2.5 px-4 rounded-xl bg-red-600 hover:bg-red-700 text-white text-xs font-bold shadow-sm transition-colors">
            Remove All
          </button>
        </div>
      </div>
    </div>

    <!-- ========== Edit Product Variant Modal ========== -->
    <div id="modal-edit-product" class="fixed inset-0 bg-black/60 backdrop-blur-xs z-99 hidden items-center justify-center p-4">
      <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl animate-fade-in">
        <div class="flex items-center justify-between pb-3 border-b border-gray-100 mb-4">
          <h4 class="font-bold text-base text-gray-900">Edit Product Options</h4>
          <button type="button" id="btn-cancel-edit" class="text-gray-400 hover:text-gray-600 p-1 rounded-full hover:bg-gray-100">
            <i class="hgi hgi-stroke hgi-cancel-01 text-lg"></i>
          </button>
        </div>

        <form id="edit-product-form">
          <div class="flex items-center gap-4 mb-5 p-3 rounded-xl bg-gray-50 border border-gray-100">
            <img id="edit-modal-img" src="./assets/images/home-3/apple.png" alt="Product" class="w-14 h-14 object-contain rounded-lg shrink-0 bg-white p-1 border border-gray-200" />
            <div class="min-w-0 flex-1">
              <h5 id="edit-modal-title" class="font-semibold text-xs text-gray-900 truncate">Morning Brew Instant Coffee</h5>
              <span id="edit-modal-price" class="text-sm font-bold text-[#0d7d6f] mt-0.5 block">₹1,499</span>
            </div>
          </div>

          <!-- Size Variant -->
          <div class="mb-4">
            <label class="block text-xs font-semibold text-gray-700 mb-1.5">Select Size / Volume</label>
            <select id="edit-modal-size" class="w-full px-3 py-2 border border-gray-300 rounded-xl text-xs focus:outline-none focus:border-[#0d7d6f]">
              <option value="100 ML">100 ML (Travel Pack)</option>
              <option value="250 ML">250 ML (Standard)</option>
              <option value="500 ML">500 ML (Family Size)</option>
              <option value="Standard">Standard Size</option>
              <option value="Large">Large Pack</option>
            </select>
          </div>

          <!-- Color Variant -->
          <div class="mb-4">
            <label class="block text-xs font-semibold text-gray-700 mb-1.5">Select Color / Roast</label>
            <select id="edit-modal-color" class="w-full px-3 py-2 border border-gray-300 rounded-xl text-xs focus:outline-none focus:border-[#0d7d6f]">
              <option value="Black">Black Roast / Classic</option>
              <option value="Espresso Brown">Espresso Dark Roast</option>
              <option value="Amber Gold">Amber Gold / Medium Roast</option>
              <option value="Teal">Teal Green</option>
            </select>
          </div>

          <!-- Quantity -->
          <div class="mb-6">
            <label class="block text-xs font-semibold text-gray-700 mb-1.5">Quantity</label>
            <input type="number" id="edit-modal-qty" min="1" max="10" value="1" class="w-24 px-3 py-2 border border-gray-300 rounded-xl text-xs font-semibold text-center focus:outline-none focus:border-[#0d7d6f]" />
          </div>

          <div class="flex items-center gap-3">
            <button type="button" onclick="document.getElementById('modal-edit-product').classList.add('hidden'); document.getElementById('modal-edit-product').classList.remove('flex');" class="flex-1 py-2.5 px-4 rounded-xl border border-gray-300 text-xs font-semibold text-gray-700 hover:bg-gray-50 transition-colors">
              Cancel
            </button>
            <button type="submit" class="flex-1 py-2.5 px-4 rounded-xl bg-[#0d7d6f] hover:bg-[#09574d] text-white text-xs font-bold shadow-sm transition-colors">
              Save Changes
            </button>
          </div>
        </form>
      </div>
    </div>
"""

with open('cart-single-vendor.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate Cart vendor section
start_marker = '<!-- ========== Cart vendor Section Start ========== -->'
end_marker = '<!-- ========== Cart vendor Section End ========== -->'

if start_marker in html and end_marker in html:
    idx_start = html.find(start_marker)
    idx_end = html.find(end_marker) + len(end_marker)
    new_html = html[:idx_start] + CART_SECTION_HTML + html[idx_end:]
else:
    # Use container search
    wrapper_start = html.rfind('<div class="container"', 0, html.find('Remove All'))
    footer_pos = html.find('<!-- ========== Footer Section Start')
    new_html = html[:wrapper_start] + CART_SECTION_HTML + html[footer_pos:]

# Add script tags for cart-engine.js and cart-ui.js before </body>
script_tags = """
    <!-- ========== Sellzy Cart Engine & UI ========== -->
    <script src="./assets/js/cart-engine.js"></script>
    <script src="./assets/js/cart-ui.js"></script>
"""

if 'cart-engine.js' not in new_html:
    new_html = new_html.replace('</body>', script_tags + '\n  </body>')

with open('cart-single-vendor.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

with open('cart-single-vendor', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("cart-single-vendor.html and cart-single-vendor updated successfully!")

