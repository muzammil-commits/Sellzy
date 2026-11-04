import os

with open('about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

# Extract pre-main content: everything from <!DOCTYPE html> up to before breadcrumb or first main section
header_end_idx = about_html.find('</header>') + len('</header>')
head_and_header = about_html[:header_end_idx]

# Replace active menu states in header for Ebotas
head_and_header = head_and_header.replace('<title>Sellzy - Multipurpose eCommerce</title>', '<title>Ebotas Footwear & Leather Boots | Sellzy</title>')

# Extract footer and post-footer content: from footer start to end of file
footer_start_idx = about_html.find('<!-- ========== Footer Section Start')
footer_and_scripts = about_html[footer_start_idx:]

ebotas_main_content = """
    <!-- ========== Breadcrumb Section Start ========== -->
    <div class="py-6 bg-gray-50 border-b border-gray-100">
      <div class="container mx-auto px-4">
        <div class="flex items-center gap-2 text-xs text-gray-500">
          <a href="index.html" class="hover:text-[#087d71] flex items-center gap-1 font-medium">
            <i class="hgi hgi-stroke hgi-home-01 text-sm"></i> Home
          </a>
          <span>/</span>
          <a href="shop-left-sidebar-4col.html" class="hover:text-[#087d71] font-medium">Shop</a>
          <span>/</span>
          <span class="text-gray-900 font-semibold">Ebotas Footwear Brand Store</span>
        </div>
      </div>
    </div>
    <!-- ========== Breadcrumb Section End ========== -->

    <!-- ========== Hero Section Start ========== -->
    <section class="relative bg-gradient-to-r from-stone-900 via-[#1c2421] to-[#0a2e28] text-white py-16 lg:py-24 overflow-hidden">
      <div class="absolute inset-0 opacity-25 mix-blend-overlay">
        <img src="./assets/images/ebotas/ebotas-hero.jpg" alt="Ebotas Footwear" class="w-full h-full object-cover" />
      </div>
      <div class="container mx-auto px-4 relative z-10">
        <div class="max-w-2xl">
          <div class="inline-flex items-center gap-2 bg-[#f5a623]/20 border border-[#f5a623]/40 text-[#f5a623] text-xs font-bold px-3 py-1.5 rounded-full mb-4 uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-[#f5a623] animate-pulse"></span>
            Official Ebotas Store &bull; Demo Mode Active
          </div>
          <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold tracking-tight leading-tight mb-6">
            Engineered For The Journey.<br />
            <span class="text-[#f5a623]">Handcrafted From Pure Leather.</span>
          </h1>
          <p class="text-base md:text-lg text-gray-300 leading-relaxed mb-8">
            Explore authentic boots, chukkas, and outdoor footwear crafted with Goodyear welt construction, premium oiled leather, and shock-absorbing ergonomic insoles. Built to endure decades of exploration.
          </p>
          <div class="flex flex-wrap items-center gap-4">
            <a href="#ebotas-catalog" class="bg-[#f5a623] hover:bg-amber-500 text-black font-bold px-8 py-4 rounded-xl shadow-lg hover:shadow-xl transition-all duration-200 transform hover:-translate-y-0.5">
              Explore Collection
            </a>
            <a href="#craftsmanship" class="bg-white/10 hover:bg-white/20 text-white font-semibold px-6 py-4 rounded-xl border border-white/20 backdrop-blur-sm transition-all">
              Our Craftsmanship
            </a>
          </div>
        </div>
      </div>
    </section>
    <!-- ========== Hero Section End ========== -->

    <!-- ========== Demo Mode Banner Start ========== -->
    <section class="bg-amber-50 border-y border-amber-200 py-3.5">
      <div class="container mx-auto px-4 flex flex-wrap items-center justify-between gap-3 text-xs md:text-sm text-amber-900">
        <div class="flex items-center gap-2.5 font-medium">
          <span class="bg-[#f5a623] text-black text-xs font-bold px-2 py-0.5 rounded">DEMO MODE</span>
          <span>Instant Checkout Active &bull; No mandatory login, password, or OTP needed to browse and test the store.</span>
        </div>
        <div class="flex items-center gap-4 font-semibold text-xs text-amber-800">
          <span>&check; All Prices in Indian Rupees (₹)</span>
          <span>&check; Free Shipping Over ₹999</span>
        </div>
      </div>
    </section>
    <!-- ========== Demo Mode Banner End ========== -->

    <!-- ========== Value Highlights Start ========== -->
    <section class="py-10 bg-white border-b border-gray-100">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
          <div class="flex items-center gap-4 p-4 rounded-xl bg-gray-50 border border-gray-100">
            <div class="w-12 h-12 rounded-full bg-[#0d7d6f]/10 text-[#0d7d6f] flex items-center justify-center shrink-0">
              <i class="hgi hgi-stroke hgi-award-02 text-2xl"></i>
            </div>
            <div>
              <h4 class="font-bold text-sm text-gray-900">100% Full-Grain</h4>
              <p class="text-xs text-gray-500">Eco-certified organic leather</p>
            </div>
          </div>
          <div class="flex items-center gap-4 p-4 rounded-xl bg-gray-50 border border-gray-100">
            <div class="w-12 h-12 rounded-full bg-[#0d7d6f]/10 text-[#0d7d6f] flex items-center justify-center shrink-0">
              <i class="hgi hgi-stroke hgi-delivery-truck-01 text-2xl"></i>
            </div>
            <div>
              <h4 class="font-bold text-sm text-gray-900">Free Express Delivery</h4>
              <p class="text-xs text-gray-500">On all orders above ₹999</p>
            </div>
          </div>
          <div class="flex items-center gap-4 p-4 rounded-xl bg-gray-50 border border-gray-100">
            <div class="w-12 h-12 rounded-full bg-[#0d7d6f]/10 text-[#0d7d6f] flex items-center justify-center shrink-0">
              <i class="hgi hgi-stroke hgi-delivery-return-02 text-2xl"></i>
            </div>
            <div>
              <h4 class="font-bold text-sm text-gray-900">30-Day Easy Returns</h4>
              <p class="text-xs text-gray-500">Hassle-free size exchanges</p>
            </div>
          </div>
          <div class="flex items-center gap-4 p-4 rounded-xl bg-gray-50 border border-gray-100">
            <div class="w-12 h-12 rounded-full bg-[#0d7d6f]/10 text-[#0d7d6f] flex items-center justify-center shrink-0">
              <i class="hgi hgi-stroke hgi-customer-service-01 text-2xl"></i>
            </div>
            <div>
              <h4 class="font-bold text-sm text-gray-900">24/7 Dedicated Support</h4>
              <p class="text-xs text-gray-500">Direct phone & chat line</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- ========== Value Highlights End ========== -->

    <!-- ========== Ebotas Catalog Section Start ========== -->
    <section id="ebotas-catalog" class="py-14 bg-gray-50">
      <div class="container mx-auto px-4">
        <!-- Section Header -->
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 gap-4">
          <div>
            <span class="text-xs font-bold uppercase tracking-wider text-[#0d7d6f]">Handcrafted Footwear</span>
            <h2 class="text-2xl md:text-3xl font-extrabold text-gray-900 mt-1">Ebotas Boots & Footwear Collection</h2>
            <p class="text-sm text-gray-500 mt-1">Select from our signature heritage boots, chelsea slip-ons, and tactical outdoor gear.</p>
          </div>
          <!-- Filter Tabs -->
          <div class="flex flex-wrap items-center gap-2" id="ebotas-filter-tabs">
            <button class="filter-tab-btn active px-4 py-2 rounded-lg text-xs font-bold transition-all bg-[#0d7d6f] text-white shadow-sm" data-category="all">
              All Boots (12)
            </button>
            <button class="filter-tab-btn px-4 py-2 rounded-lg text-xs font-semibold bg-white text-gray-700 hover:bg-gray-100 border border-gray-200 transition-all" data-category="chelsea">
              Chelsea Slip-On
            </button>
            <button class="filter-tab-btn px-4 py-2 rounded-lg text-xs font-semibold bg-white text-gray-700 hover:bg-gray-100 border border-gray-200 transition-all" data-category="heritage">
              Heritage Moc-Toe
            </button>
            <button class="filter-tab-btn px-4 py-2 rounded-lg text-xs font-semibold bg-white text-gray-700 hover:bg-gray-100 border border-gray-200 transition-all" data-category="tactical">
              Work & Tactical
            </button>
            <button class="filter-tab-btn px-4 py-2 rounded-lg text-xs font-semibold bg-white text-gray-700 hover:bg-gray-100 border border-gray-200 transition-all" data-category="chukka">
              Desert Chukka
            </button>
          </div>
        </div>

        <!-- Product Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6" id="ebotas-product-grid">
          
          <!-- Card 1 -->
          <div class="ebotas-card bg-white rounded-2xl border border-gray-100 overflow-hidden shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col group" data-category="heritage">
            <div class="relative overflow-hidden bg-gray-100 aspect-square">
              <span class="absolute top-3 left-3 bg-[#f5a623] text-black font-bold text-[10px] px-2 py-0.5 rounded-full z-10 uppercase tracking-wide">Bestseller</span>
              <img src="./assets/images/ebotas/boot-1.jpg" alt="Ebotas Heritage 6-Inch Moc-Toe" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between text-xs text-gray-400 mb-1.5">
                  <span>Heritage Collection</span>
                  <div class="flex items-center gap-1 text-amber-500 font-semibold">
                    <span>&#9733; 4.9</span>
                    <span class="text-gray-400">(128)</span>
                  </div>
                </div>
                <h3 class="font-bold text-gray-900 text-sm hover:text-[#087d71] transition-colors leading-snug">
                  Ebotas Heritage 6-Inch Moc-Toe Boot
                </h3>
                <p class="text-xs text-gray-500 mt-1 line-clamp-2">Hand-stitched Goodyear welt with oil-tanned amber cowhide.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
                <div>
                  <span class="text-lg font-extrabold text-[#0d7d6f]">₹3,499</span>
                  <span class="text-xs text-gray-400 line-through ml-1.5">₹5,999</span>
                </div>
                <button onclick="addToEbotasCart('Ebotas Heritage 6-Inch Moc-Toe Boot', '₹3,499')" class="bg-[#0d7d6f] hover:bg-[#09574d] text-white text-xs font-bold px-3.5 py-2 rounded-lg shadow-sm hover:shadow transition-colors flex items-center gap-1.5">
                  <i class="hgi hgi-stroke hgi-shopping-cart-01 text-sm"></i> Add
                </button>
              </div>
            </div>
          </div>

          <!-- Card 2 -->
          <div class="ebotas-card bg-white rounded-2xl border border-gray-100 overflow-hidden shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col group" data-category="heritage">
            <div class="relative overflow-hidden bg-gray-100 aspect-square">
              <span class="absolute top-3 left-3 bg-[#0d7d6f] text-white font-bold text-[10px] px-2 py-0.5 rounded-full z-10 uppercase tracking-wide">40% OFF</span>
              <img src="./assets/images/ebotas/boot-2.jpg" alt="Ebotas Iron Ranger Full-Grain Boot" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between text-xs text-gray-400 mb-1.5">
                  <span>Iron Ranger Series</span>
                  <div class="flex items-center gap-1 text-amber-500 font-semibold">
                    <span>&#9733; 5.0</span>
                    <span class="text-gray-400">(94)</span>
                  </div>
                </div>
                <h3 class="font-bold text-gray-900 text-sm hover:text-[#087d71] transition-colors leading-snug">
                  Ebotas Iron Ranger Handcrafted Harness Boot
                </h3>
                <p class="text-xs text-gray-500 mt-1 line-clamp-2">Double-layer leather toe cap with rugged Vibram 430 mini-lug outsole.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
                <div>
                  <span class="text-lg font-extrabold text-[#0d7d6f]">₹4,499</span>
                  <span class="text-xs text-gray-400 line-through ml-1.5">₹7,999</span>
                </div>
                <button onclick="addToEbotasCart('Ebotas Iron Ranger Handcrafted Harness Boot', '₹4,499')" class="bg-[#0d7d6f] hover:bg-[#09574d] text-white text-xs font-bold px-3.5 py-2 rounded-lg shadow-sm hover:shadow transition-colors flex items-center gap-1.5">
                  <i class="hgi hgi-stroke hgi-shopping-cart-01 text-sm"></i> Add
                </button>
              </div>
            </div>
          </div>

          <!-- Card 3 -->
          <div class="ebotas-card bg-white rounded-2xl border border-gray-100 overflow-hidden shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col group" data-category="chelsea">
            <div class="relative overflow-hidden bg-gray-100 aspect-square">
              <span class="absolute top-3 left-3 bg-[#f5a623] text-black font-bold text-[10px] px-2 py-0.5 rounded-full z-10 uppercase tracking-wide">Popular</span>
              <img src="./assets/images/ebotas/boot-3.jpg" alt="Ebotas Chelsea Waterproof Oiled Boot" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between text-xs text-gray-400 mb-1.5">
                  <span>Chelsea Classics</span>
                  <div class="flex items-center gap-1 text-amber-500 font-semibold">
                    <span>&#9733; 4.8</span>
                    <span class="text-gray-400">(86)</span>
                  </div>
                </div>
                <h3 class="font-bold text-gray-900 text-sm hover:text-[#087d71] transition-colors leading-snug">
                  Ebotas Chelsea Waterproof Oiled Nubuck Boot
                </h3>
                <p class="text-xs text-gray-500 mt-1 line-clamp-2">Dual stretch gussets with hydrophobic silicone-treated oiled nubuck.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
                <div>
                  <span class="text-lg font-extrabold text-[#0d7d6f]">₹2,999</span>
                  <span class="text-xs text-gray-400 line-through ml-1.5">₹4,999</span>
                </div>
                <button onclick="addToEbotasCart('Ebotas Chelsea Waterproof Oiled Nubuck Boot', '₹2,999')" class="bg-[#0d7d6f] hover:bg-[#09574d] text-white text-xs font-bold px-3.5 py-2 rounded-lg shadow-sm hover:shadow transition-colors flex items-center gap-1.5">
                  <i class="hgi hgi-stroke hgi-shopping-cart-01 text-sm"></i> Add
                </button>
              </div>
            </div>
          </div>

          <!-- Card 4 -->
          <div class="ebotas-card bg-white rounded-2xl border border-gray-100 overflow-hidden shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col group" data-category="tactical">
            <div class="relative overflow-hidden bg-gray-100 aspect-square">
              <span class="absolute top-3 left-3 bg-red-600 text-white font-bold text-[10px] px-2 py-0.5 rounded-full z-10 uppercase tracking-wide">Heavy Duty</span>
              <img src="./assets/images/ebotas/boot-4.jpg" alt="Ebotas Tactical Lug Sole Boot" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between text-xs text-gray-400 mb-1.5">
                  <span>Work & Tactical</span>
                  <div class="flex items-center gap-1 text-amber-500 font-semibold">
                    <span>&#9733; 4.9</span>
                    <span class="text-gray-400">(110)</span>
                  </div>
                </div>
                <h3 class="font-bold text-gray-900 text-sm hover:text-[#087d71] transition-colors leading-snug">
                  Ebotas Stormproof Vibram-Sole Tactical Boot
                </h3>
                <p class="text-xs text-gray-500 mt-1 line-clamp-2">Reinforced steel shank with oil-resistant non-slip lug tread.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
                <div>
                  <span class="text-lg font-extrabold text-[#0d7d6f]">₹3,999</span>
                  <span class="text-xs text-gray-400 line-through ml-1.5">₹6,499</span>
                </div>
                <button onclick="addToEbotasCart('Ebotas Stormproof Vibram-Sole Tactical Boot', '₹3,999')" class="bg-[#0d7d6f] hover:bg-[#09574d] text-white text-xs font-bold px-3.5 py-2 rounded-lg shadow-sm hover:shadow transition-colors flex items-center gap-1.5">
                  <i class="hgi hgi-stroke hgi-shopping-cart-01 text-sm"></i> Add
                </button>
              </div>
            </div>
          </div>

          <!-- Card 5 -->
          <div class="ebotas-card bg-white rounded-2xl border border-gray-100 overflow-hidden shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col group" data-category="chukka">
            <div class="relative overflow-hidden bg-gray-100 aspect-square">
              <span class="absolute top-3 left-3 bg-[#0d7d6f] text-white font-bold text-[10px] px-2 py-0.5 rounded-full z-10 uppercase tracking-wide">35% OFF</span>
              <img src="./assets/images/ebotas/boot-5.jpg" alt="Ebotas Desert Chukka Boot" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between text-xs text-gray-400 mb-1.5">
                  <span>Desert Chukka</span>
                  <div class="flex items-center gap-1 text-amber-500 font-semibold">
                    <span>&#9733; 4.7</span>
                    <span class="text-gray-400">(62)</span>
                  </div>
                </div>
                <h3 class="font-bold text-gray-900 text-sm hover:text-[#087d71] transition-colors leading-snug">
                  Ebotas Desert Chukka Sand Suede Handcrafted
                </h3>
                <p class="text-xs text-gray-500 mt-1 line-clamp-2">Lightweight natural crepe rubber sole with premium calf suede upper.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
                <div>
                  <span class="text-lg font-extrabold text-[#0d7d6f]">₹2,499</span>
                  <span class="text-xs text-gray-400 line-through ml-1.5">₹3,999</span>
                </div>
                <button onclick="addToEbotasCart('Ebotas Desert Chukka Sand Suede Handcrafted', '₹2,499')" class="bg-[#0d7d6f] hover:bg-[#09574d] text-white text-xs font-bold px-3.5 py-2 rounded-lg shadow-sm hover:shadow transition-colors flex items-center gap-1.5">
                  <i class="hgi hgi-stroke hgi-shopping-cart-01 text-sm"></i> Add
                </button>
              </div>
            </div>
          </div>

          <!-- Card 6 -->
          <div class="ebotas-card bg-white rounded-2xl border border-gray-100 overflow-hidden shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col group" data-category="tactical">
            <div class="relative overflow-hidden bg-gray-100 aspect-square">
              <span class="absolute top-3 left-3 bg-[#f5a623] text-black font-bold text-[10px] px-2 py-0.5 rounded-full z-10 uppercase tracking-wide">Premium</span>
              <img src="./assets/images/ebotas/boot-6.jpg" alt="Ebotas Black Label Brogue Boot" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between text-xs text-gray-400 mb-1.5">
                  <span>Urban Combat</span>
                  <div class="flex items-center gap-1 text-amber-500 font-semibold">
                    <span>&#9733; 4.8</span>
                    <span class="text-gray-400">(77)</span>
                  </div>
                </div>
                <h3 class="font-bold text-gray-900 text-sm hover:text-[#087d71] transition-colors leading-snug">
                  Ebotas Black Label Brogue Combat Ankle Boot
                </h3>
                <p class="text-xs text-gray-500 mt-1 line-clamp-2">Perforated wingtip detailing on high-shine box calf leather.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
                <div>
                  <span class="text-lg font-extrabold text-[#0d7d6f]">₹3,799</span>
                  <span class="text-xs text-gray-400 line-through ml-1.5">₹5,499</span>
                </div>
                <button onclick="addToEbotasCart('Ebotas Black Label Brogue Combat Ankle Boot', '₹3,799')" class="bg-[#0d7d6f] hover:bg-[#09574d] text-white text-xs font-bold px-3.5 py-2 rounded-lg shadow-sm hover:shadow transition-colors flex items-center gap-1.5">
                  <i class="hgi hgi-stroke hgi-shopping-cart-01 text-sm"></i> Add
                </button>
              </div>
            </div>
          </div>

          <!-- Card 7 -->
          <div class="ebotas-card bg-white rounded-2xl border border-gray-100 overflow-hidden shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col group" data-category="heritage">
            <div class="relative overflow-hidden bg-gray-100 aspect-square">
              <span class="absolute top-3 left-3 bg-[#0d7d6f] text-white font-bold text-[10px] px-2 py-0.5 rounded-full z-10 uppercase tracking-wide">Trail Ready</span>
              <img src="./assets/images/ebotas/boot-7.jpg" alt="Ebotas Alpine Hiker Boot" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between text-xs text-gray-400 mb-1.5">
                  <span>Alpine Series</span>
                  <div class="flex items-center gap-1 text-amber-500 font-semibold">
                    <span>&#9733; 4.9</span>
                    <span class="text-gray-400">(95)</span>
                  </div>
                </div>
                <h3 class="font-bold text-gray-900 text-sm hover:text-[#087d71] transition-colors leading-snug">
                  Ebotas Alpine Hiker Weatherproof Mountain Boot
                </h3>
                <p class="text-xs text-gray-500 mt-1 line-clamp-2">Speed-hook lacing system with padded collar and waterproof membrane.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
                <div>
                  <span class="text-lg font-extrabold text-[#0d7d6f]">₹2,899</span>
                  <span class="text-xs text-gray-400 line-through ml-1.5">₹4,499</span>
                </div>
                <button onclick="addToEbotasCart('Ebotas Alpine Hiker Weatherproof Mountain Boot', '₹2,899')" class="bg-[#0d7d6f] hover:bg-[#09574d] text-white text-xs font-bold px-3.5 py-2 rounded-lg shadow-sm hover:shadow transition-colors flex items-center gap-1.5">
                  <i class="hgi hgi-stroke hgi-shopping-cart-01 text-sm"></i> Add
                </button>
              </div>
            </div>
          </div>

          <!-- Card 8 -->
          <div class="ebotas-card bg-white rounded-2xl border border-gray-100 overflow-hidden shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col group" data-category="chelsea">
            <div class="relative overflow-hidden bg-gray-100 aspect-square">
              <span class="absolute top-3 left-3 bg-[#f5a623] text-black font-bold text-[10px] px-2 py-0.5 rounded-full z-10 uppercase tracking-wide">Trending</span>
              <img src="./assets/images/ebotas/boot-8.jpg" alt="Ebotas Urban Commuter Boot" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between text-xs text-gray-400 mb-1.5">
                  <span>Urban Series</span>
                  <div class="flex items-center gap-1 text-amber-500 font-semibold">
                    <span>&#9733; 4.7</span>
                    <span class="text-gray-400">(53)</span>
                  </div>
                </div>
                <h3 class="font-bold text-gray-900 text-sm hover:text-[#087d71] transition-colors leading-snug">
                  Ebotas Urban Commuter Side-Zip Ankle Boot
                </h3>
                <p class="text-xs text-gray-500 mt-1 line-clamp-2">Quick side-zipper with burnished toe and shock-absorbing EVA midsole.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
                <div>
                  <span class="text-lg font-extrabold text-[#0d7d6f]">₹2,699</span>
                  <span class="text-xs text-gray-400 line-through ml-1.5">₹4,199</span>
                </div>
                <button onclick="addToEbotasCart('Ebotas Urban Commuter Side-Zip Ankle Boot', '₹2,699')" class="bg-[#0d7d6f] hover:bg-[#09574d] text-white text-xs font-bold px-3.5 py-2 rounded-lg shadow-sm hover:shadow transition-colors flex items-center gap-1.5">
                  <i class="hgi hgi-stroke hgi-shopping-cart-01 text-sm"></i> Add
                </button>
              </div>
            </div>
          </div>

          <!-- Card 9 -->
          <div class="ebotas-card bg-white rounded-2xl border border-gray-100 overflow-hidden shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col group" data-category="tactical">
            <div class="relative overflow-hidden bg-gray-100 aspect-square">
              <span class="absolute top-3 left-3 bg-[#0d7d6f] text-white font-bold text-[10px] px-2 py-0.5 rounded-full z-10 uppercase tracking-wide">Heavy Duty</span>
              <img src="./assets/images/ebotas/boot-1.jpg" alt="Ebotas Heavy-Duty Work Boot" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between text-xs text-gray-400 mb-1.5">
                  <span>Pro Workwear</span>
                  <div class="flex items-center gap-1 text-amber-500 font-semibold">
                    <span>&#9733; 5.0</span>
                    <span class="text-gray-400">(140)</span>
                  </div>
                </div>
                <h3 class="font-bold text-gray-900 text-sm hover:text-[#087d71] transition-colors leading-snug">
                  Ebotas Goodyear Welted Heavy-Duty Work Boot
                </h3>
                <p class="text-xs text-gray-500 mt-1 line-clamp-2">Full steel toe protection, anti-puncture composite plate, oil resistant.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
                <div>
                  <span class="text-lg font-extrabold text-[#0d7d6f]">₹4,199</span>
                  <span class="text-xs text-gray-400 line-through ml-1.5">₹6,999</span>
                </div>
                <button onclick="addToEbotasCart('Ebotas Goodyear Welted Heavy-Duty Work Boot', '₹4,199')" class="bg-[#0d7d6f] hover:bg-[#09574d] text-white text-xs font-bold px-3.5 py-2 rounded-lg shadow-sm hover:shadow transition-colors flex items-center gap-1.5">
                  <i class="hgi hgi-stroke hgi-shopping-cart-01 text-sm"></i> Add
                </button>
              </div>
            </div>
          </div>

          <!-- Card 10 -->
          <div class="ebotas-card bg-white rounded-2xl border border-gray-100 overflow-hidden shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col group" data-category="chukka">
            <div class="relative overflow-hidden bg-gray-100 aspect-square">
              <span class="absolute top-3 left-3 bg-[#f5a623] text-black font-bold text-[10px] px-2 py-0.5 rounded-full z-10 uppercase tracking-wide">Casual</span>
              <img src="./assets/images/ebotas/boot-5.jpg" alt="Ebotas Low-Top Suede Casual" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between text-xs text-gray-400 mb-1.5">
                  <span>Casual Suede</span>
                  <div class="flex items-center gap-1 text-amber-500 font-semibold">
                    <span>&#9733; 4.6</span>
                    <span class="text-gray-400">(48)</span>
                  </div>
                </div>
                <h3 class="font-bold text-gray-900 text-sm hover:text-[#087d71] transition-colors leading-snug">
                  Ebotas Low-Top Suede Casual Sneaker Boot
                </h3>
                <p class="text-xs text-gray-500 mt-1 line-clamp-2">Flexible cup-sole construction with breathable perforated leather lining.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
                <div>
                  <span class="text-lg font-extrabold text-[#0d7d6f]">₹1,999</span>
                  <span class="text-xs text-gray-400 line-through ml-1.5">₹3,299</span>
                </div>
                <button onclick="addToEbotasCart('Ebotas Low-Top Suede Casual Sneaker Boot', '₹1,999')" class="bg-[#0d7d6f] hover:bg-[#09574d] text-white text-xs font-bold px-3.5 py-2 rounded-lg shadow-sm hover:shadow transition-colors flex items-center gap-1.5">
                  <i class="hgi hgi-stroke hgi-shopping-cart-01 text-sm"></i> Add
                </button>
              </div>
            </div>
          </div>

          <!-- Card 11 -->
          <div class="ebotas-card bg-white rounded-2xl border border-gray-100 overflow-hidden shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col group" data-category="heritage">
            <div class="relative overflow-hidden bg-gray-100 aspect-square">
              <span class="absolute top-3 left-3 bg-[#0d7d6f] text-white font-bold text-[10px] px-2 py-0.5 rounded-full z-10 uppercase tracking-wide">Winter Special</span>
              <img src="./assets/images/ebotas/boot-2.jpg" alt="Ebotas Winter Thermal Boot" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between text-xs text-gray-400 mb-1.5">
                  <span>Winter Guard</span>
                  <div class="flex items-center gap-1 text-amber-500 font-semibold">
                    <span>&#9733; 4.9</span>
                    <span class="text-gray-400">(82)</span>
                  </div>
                </div>
                <h3 class="font-bold text-gray-900 text-sm hover:text-[#087d71] transition-colors leading-snug">
                  Ebotas Winter Thermal Shearling-Lined Boot
                </h3>
                <p class="text-xs text-gray-500 mt-1 line-clamp-2">100% Merino wool shearling interior rated down to -20&deg;C with ice-grip soles.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
                <div>
                  <span class="text-lg font-extrabold text-[#0d7d6f]">₹4,799</span>
                  <span class="text-xs text-gray-400 line-through ml-1.5">₹7,499</span>
                </div>
                <button onclick="addToEbotasCart('Ebotas Winter Thermal Shearling-Lined Boot', '₹4,799')" class="bg-[#0d7d6f] hover:bg-[#09574d] text-white text-xs font-bold px-3.5 py-2 rounded-lg shadow-sm hover:shadow transition-colors flex items-center gap-1.5">
                  <i class="hgi hgi-stroke hgi-shopping-cart-01 text-sm"></i> Add
                </button>
              </div>
            </div>
          </div>

          <!-- Card 12 -->
          <div class="ebotas-card bg-white rounded-2xl border border-gray-100 overflow-hidden shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col group" data-category="chelsea">
            <div class="relative overflow-hidden bg-gray-100 aspect-square">
              <span class="absolute top-3 left-3 bg-[#f5a623] text-black font-bold text-[10px] px-2 py-0.5 rounded-full z-10 uppercase tracking-wide">Signature</span>
              <img src="./assets/images/ebotas/boot-3.jpg" alt="Ebotas Signature Bison Leather Chelsea" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between text-xs text-gray-400 mb-1.5">
                  <span>Signature Bison</span>
                  <div class="flex items-center gap-1 text-amber-500 font-semibold">
                    <span>&#9733; 4.8</span>
                    <span class="text-gray-400">(69)</span>
                  </div>
                </div>
                <h3 class="font-bold text-gray-900 text-sm hover:text-[#087d71] transition-colors leading-snug">
                  Ebotas Signature Bison Leather Chelsea Boot
                </h3>
                <p class="text-xs text-gray-500 mt-1 line-clamp-2">Pebbled American bison leather with stacked leather heel and rubber strike pad.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
                <div>
                  <span class="text-lg font-extrabold text-[#0d7d6f]">₹3,999</span>
                  <span class="text-xs text-gray-400 line-through ml-1.5">₹6,299</span>
                </div>
                <button onclick="addToEbotasCart('Ebotas Signature Bison Leather Chelsea Boot', '₹3,999')" class="bg-[#0d7d6f] hover:bg-[#09574d] text-white text-xs font-bold px-3.5 py-2 rounded-lg shadow-sm hover:shadow transition-colors flex items-center gap-1.5">
                  <i class="hgi hgi-stroke hgi-shopping-cart-01 text-sm"></i> Add
                </button>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
    <!-- ========== Ebotas Catalog Section End ========== -->

    <!-- ========== Craftsmanship Section Start ========== -->
    <section id="craftsmanship" class="py-16 bg-white">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div class="relative rounded-3xl overflow-hidden shadow-2xl">
            <img src="./assets/images/ebotas/leather-craft.jpg" alt="Ebotas Workshop Craftsmanship" class="w-full h-[450px] object-cover" />
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-8">
              <div class="text-white">
                <span class="text-[#f5a623] text-xs font-bold uppercase tracking-wider">Master Artisans</span>
                <h3 class="text-2xl font-bold mt-1">Over 200 Handcrafted Steps In Every Pair</h3>
              </div>
            </div>
          </div>
          <div>
            <span class="text-xs font-bold uppercase tracking-wider text-[#0d7d6f]">Uncompromising Heritage</span>
            <h2 class="text-3xl font-extrabold text-gray-900 mt-2 mb-6">Built To Last Decades, Not Seasons.</h2>
            <p class="text-gray-600 leading-relaxed mb-6">
              Every pair of Ebotas boots is engineered from vegetable-tanned full-grain leather, assembled with genuine 360-degree Goodyear welt construction. This allows your boots to be completely resoled repeatedly across a lifetime of journeys.
            </p>
            <div class="space-y-4">
              <div class="flex items-start gap-4">
                <div class="w-8 h-8 rounded-full bg-[#0d7d6f]/10 text-[#0d7d6f] flex items-center justify-center shrink-0 mt-0.5">
                  <i class="hgi hgi-stroke hgi-checkmark-circle-01 text-lg"></i>
                </div>
                <div>
                  <h4 class="font-bold text-sm text-gray-900">Custom Cork Midsole Infill</h4>
                  <p class="text-xs text-gray-500">Molds to the exact shape of your foot with each step for bespoke orthotic comfort.</p>
                </div>
              </div>
              <div class="flex items-start gap-4">
                <div class="w-8 h-8 rounded-full bg-[#0d7d6f]/10 text-[#0d7d6f] flex items-center justify-center shrink-0 mt-0.5">
                  <i class="hgi hgi-stroke hgi-checkmark-circle-01 text-lg"></i>
                </div>
                <div>
                  <h4 class="font-bold text-sm text-gray-900">Hydrophobic Weatherproofing</h4>
                  <p class="text-xs text-gray-500">Infused oils naturally repel mud, rain, and snow while maintaining leather breathability.</p>
                </div>
              </div>
              <div class="flex items-start gap-4">
                <div class="w-8 h-8 rounded-full bg-[#0d7d6f]/10 text-[#0d7d6f] flex items-center justify-center shrink-0 mt-0.5">
                  <i class="hgi hgi-stroke hgi-checkmark-circle-01 text-lg"></i>
                </div>
                <div>
                  <h4 class="font-bold text-sm text-gray-900">Heavy-Gauge Brass Eyelets</h4>
                  <p class="text-xs text-gray-500">Corrosion-resistant metal hardware riveted directly into leather uppers.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- ========== Craftsmanship Section End ========== -->

    <!-- ========== Testimonials Section Start ========== -->
    <section class="py-14 bg-gray-50 border-t border-gray-100">
      <div class="container mx-auto px-4">
        <div class="text-center max-w-xl mx-auto mb-10">
          <span class="text-xs font-bold uppercase tracking-wider text-[#0d7d6f]">Customer Feedback</span>
          <h2 class="text-2xl md:text-3xl font-extrabold text-gray-900 mt-1">Trusted By Over 40,000 Riders & Walkers</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs">
            <div class="flex items-center gap-1 text-amber-500 text-sm mb-3">
              &#9733;&#9733;&#9733;&#9733;&#9733;
            </div>
            <p class="text-xs text-gray-600 leading-relaxed italic mb-4">
              "The Heritage 6-inch Moc-Toe boots exceeded all my expectations. The leather smells incredible, break-in took only 3 days, and the welt stitching is flawless. Truly world-class quality at an unbeatable INR price."
            </p>
            <div class="flex items-center gap-3">
              <div class="w-9 h-9 rounded-full bg-[#0d7d6f] text-white flex items-center justify-center font-bold text-xs">AK</div>
              <div>
                <h5 class="font-bold text-xs text-gray-900">Arjun Kapoor</h5>
                <span class="text-[11px] text-gray-400">Verified Buyer &bull; Mumbai</span>
              </div>
            </div>
          </div>

          <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs">
            <div class="flex items-center gap-1 text-amber-500 text-sm mb-3">
              &#9733;&#9733;&#9733;&#9733;&#9733;
            </div>
            <p class="text-xs text-gray-600 leading-relaxed italic mb-4">
              "I wear the Ebotas Chelsea Nubuck boots to the office and on weekend rides. The stretch elastic hasn't sagged even after 8 months. Best boots I've owned in India hands down."
            </p>
            <div class="flex items-center gap-3">
              <div class="w-9 h-9 rounded-full bg-[#f5a623] text-black flex items-center justify-center font-bold text-xs">RS</div>
              <div>
                <h5 class="font-bold text-xs text-gray-900">Rohit Sharma</h5>
                <span class="text-[11px] text-gray-400">Verified Buyer &bull; Bengaluru</span>
              </div>
            </div>
          </div>

          <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs">
            <div class="flex items-center gap-1 text-amber-500 text-sm mb-3">
              &#9733;&#9733;&#9733;&#9733;&#9733;
            </div>
            <p class="text-xs text-gray-600 leading-relaxed italic mb-4">
              "The Tactical Lug boots survived torrential rains and hiking trails in Himachal without a single leak. The cork footbed really takes the shape of your feet. 5 stars all the way!"
            </p>
            <div class="flex items-center gap-3">
              <div class="w-9 h-9 rounded-full bg-stone-800 text-white flex items-center justify-center font-bold text-xs">PM</div>
              <div>
                <h5 class="font-bold text-xs text-gray-900">Pranav Mehta</h5>
                <span class="text-[11px] text-gray-400">Verified Buyer &bull; New Delhi</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- ========== Testimonials Section End ========== -->

    <!-- ========== Ebotas Interactive Scripts ========== -->
    <script>
      // Filter tab switcher
      document.addEventListener('DOMContentLoaded', function() {
        const tabs = document.querySelectorAll('.filter-tab-btn');
        const cards = document.querySelectorAll('.ebotas-card');

        tabs.forEach(tab => {
          tab.addEventListener('click', function() {
            tabs.forEach(t => {
              t.classList.remove('bg-[#0d7d6f]', 'text-white', 'shadow-sm', 'active');
              t.classList.add('bg-white', 'text-gray-700');
            });
            this.classList.add('bg-[#0d7d6f]', 'text-white', 'shadow-sm', 'active');
            this.classList.remove('bg-white', 'text-gray-700');

            const category = this.getAttribute('data-category');
            cards.forEach(card => {
              if (category === 'all' || card.getAttribute('data-category') === category) {
                card.style.display = 'flex';
              } else {
                card.style.display = 'none';
              }
            });
          });
        });
      });

      // Cart function with live toast and badge update
      let ebotasCartCount = 0;
      function addToEbotasCart(title, price) {
        ebotasCartCount++;
        // Update header badges
        const countBadges = document.querySelectorAll('#header-cart-btn span, .cart-counter, .cart-count');
        countBadges.forEach(b => {
          if (b.innerText.includes('Items') || b.innerText.includes('item')) {
            b.innerText = ebotasCartCount + ' - Items';
          }
        });

        // Show toast
        const toast = document.createElement('div');
        toast.className = 'fixed bottom-6 right-6 bg-[#0d7d6f] text-white px-5 py-3.5 rounded-xl shadow-2xl flex items-center gap-3 z-50 text-xs font-semibold animate-bounce';
        toast.innerHTML = '<span class=\"bg-white/20 p-1 rounded-full\">&#10003;</span> Added ' + title + ' (' + price + ') to Cart! (Demo Mode)';
        document.body.appendChild(toast);
        setTimeout(() => {
          toast.remove();
        }, 3000);
      }
    </script>
"""

full_ebotas_html = head_and_header + ebotas_main_content + footer_and_scripts

with open('ebotas.html', 'w', encoding='utf-8') as f:
    f.write(full_ebotas_html)

with open('ebotas', 'w', encoding='utf-8') as f:
    f.write(full_ebotas_html)

print("ebotas.html and ebotas clean file created successfully!")

