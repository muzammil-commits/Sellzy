/**
 * Sellzy Centralized Product Catalog & Database Engine
 * Defines authentic products, variants, images, prices, discounts, specifications and helper queries
 */
(function(window) {
  'use strict';

  const PRODUCTS_CATALOG = [
    {
      id: 'prod-omega3',
      slug: 'vitallife-omega-3',
      name: 'VitaLife Omega-3 Softgels Heart Support Max Strength',
      category: 'Healthcare & Wellness',
      brand: 'VitaLife Nutrition',
      sku: 'SLZ-HLTH-001',
      price: 2999,
      originalPrice: 3499,
      rating: 4.9,
      reviews: 11780,
      availability: 'In Stock',
      stock: 24,
      badge: 'Sales',
      subBadge: 'New Arrival',
      description: 'VitaLife Omega-3 Softgels deliver high-potency EPA and DHA fatty acids sourced from wild-caught cold-water fish. Molecularly distilled for maximum purity and zero fishy aftertaste, each enteric-coated softgel promotes cardiovascular health, cognitive function, and joint mobility.',
      specifications: {
        'Origin': 'Made in India (GMP & FSSAI Certified)',
        'Active Ingredients': '1200mg Fish Oil (600mg EPA, 400mg DHA)',
        'Packaging': 'Child-proof UV-protective bottle',
        'Net Quantity': '60 Softgels / Bottle',
        'Shelf Life': '24 Months from manufacturing date',
        'Dosage': 'Take 1 softgel daily with meals or as directed'
      },
      images: [
        './assets/images/product-details/product-details-slider-1.png',
        './assets/images/product-details/product-details-slider-2.png',
        './assets/images/product-details/product-details-slider-3.png',
        './assets/images/product-details/product-details-slider-4.png',
        './assets/images/product-details/product-details-slider-5.png',
        './assets/images/product-details/product-details-slider-6.png'
      ],
      sizes: [
        { name: 'S (60 Softgels)', priceMod: 0 },
        { name: 'M (120 Softgels)', priceMod: 999 },
        { name: 'L (240 Softgels)', priceMod: 1999 }
      ],
      colors: [
        { name: 'Emerald Green', hex: '#0d7d6f' },
        { name: 'Golden Amber', hex: '#f5a623' },
        { name: 'Coral Rose', hex: '#e05656' }
      ],
      relatedIds: ['prod-coffee-1', 'prod-pulse-oximeter', 'prod-ashwagandha', 'prod-ebotas-1']
    },
    {
      id: 'prod-coffee-1',
      slug: 'morning-brew-coffee',
      name: 'Morning Brew Instant Artisanal Coffee (Pouch)',
      category: 'Food & Gourmet Beverages',
      brand: 'Morning Brew Roasters',
      sku: 'SLZ-COFF-002',
      price: 1499,
      originalPrice: 1899,
      rating: 4.8,
      reviews: 840,
      availability: 'In Stock',
      stock: 15,
      badge: 'Popular',
      subBadge: '100% Arabica',
      description: 'Handpicked shade-grown Arabica beans from the misty hills of Coorg. Freeze-dried to lock in delicate chocolate and hazelnut notes. Dissolves instantly in hot milk or water for a rich, aromatic cafe-style brew right at home.',
      specifications: {
        'Origin': 'Coorg, Karnataka, India',
        'Bean Variety': '100% Premium Arabica Grade A',
        'Roast Level': 'Medium Dark Roast',
        'Net Weight': '250 ML / 200g Pouch',
        'Caffeine Content': 'Standard (Approx. 65mg / cup)',
        'Shelf Life': '18 Months'
      },
      images: [
        './assets/images/home-3/apple.png',
        './assets/images/home-3/corn-can.png',
        './assets/images/product-details/product-details-1.png',
        './assets/images/home-3/apple-juice.png'
      ],
      sizes: [
        { name: '100 ML (Travel Pack)', priceMod: -500 },
        { name: '250 ML (Standard)', priceMod: 0 },
        { name: '500 ML (Family Pack)', priceMod: 899 }
      ],
      colors: [
        { name: 'Black Roast', hex: '#1a1a1a' },
        { name: 'Espresso Brown', hex: '#4a2e18' },
        { name: 'Amber Gold', hex: '#b8860b' }
      ],
      relatedIds: ['prod-coffee-2', 'prod-omega3', 'prod-honey', 'prod-serum']
    },
    {
      id: 'prod-coffee-2',
      slug: 'morning-brew-coffee-can',
      name: 'Morning Brew Instant Coffee (Aroma-Lock Tin Can)',
      category: 'Food & Gourmet Beverages',
      brand: 'Morning Brew Roasters',
      sku: 'SLZ-COFF-003',
      price: 1499,
      originalPrice: 1999,
      rating: 4.9,
      reviews: 520,
      availability: 'In Stock',
      stock: 18,
      badge: 'Bestseller',
      subBadge: 'Aroma-Lock Tin',
      description: 'Preserved inside our signature hermetically sealed aroma-lock steel tin. Retains peak freshness and bold, smooth flavor profile for up to 2 years. Perfect gift for true coffee connoisseurs.',
      specifications: {
        'Origin': 'Chikmagalur, India',
        'Bean Variety': 'Estate Blend (80% Arabica, 20% Robusta)',
        'Packaging': 'Reusable Food-grade Steel Tin Can',
        'Net Weight': '250 ML / 200g',
        'Shelf Life': '24 Months'
      },
      images: [
        './assets/images/home-3/corn-can.png',
        './assets/images/home-3/corn-can-bg.png',
        './assets/images/home-3/apple.png'
      ],
      sizes: [
        { name: '250 ML (Standard)', priceMod: 0 },
        { name: '500 ML (Large Tin)', priceMod: 899 }
      ],
      colors: [
        { name: 'Gold Canister', hex: '#d4af37' },
        { name: 'Matte Black', hex: '#222222' }
      ],
      relatedIds: ['prod-coffee-1', 'prod-honey', 'prod-omega3']
    },
    {
      id: 'prod-pulse-oximeter',
      slug: 'smart-digital-pulse-oximeter',
      name: 'Smart Digital Fingertip Pulse Oximeter & Heart Monitor',
      category: 'Medical Diagnostics',
      brand: 'Sellzy MedTech',
      sku: 'SLZ-MED-004',
      price: 1499,
      originalPrice: 2499,
      rating: 5.0,
      reviews: 310,
      availability: 'In Stock',
      stock: 12,
      badge: 'Medical Grade',
      subBadge: 'FDA Approved',
      description: 'Clinical accuracy in under 5 seconds. Multi-directional OLED display shows SpO2 blood oxygen saturation, pulse rate bar graph, and plethysmogram waveform. Features automatic shut-off and low battery alert.',
      specifications: {
        'Display': 'Dual-color Four Directional OLED Display',
        'Accuracy': 'SpO2: ±2% (70%-100%), PR: ±2 bpm',
        'Power': '2x AAA Alkaline Batteries (Included)',
        'Dimensions': '58mm x 32mm x 34mm',
        'Weight': '50g (with batteries)',
        'Warranty': '2 Years Hassle-free Replacement Warranty'
      },
      images: [
        './assets/images/home-1/hero-promo-1.png',
        './assets/images/product-details/product-details-10.jpg',
        './assets/images/product-details/product-details-12.jpg'
      ],
      sizes: [
        { name: 'Standard Unit', priceMod: 0 },
        { name: 'Kit (With Case & Lanyard)', priceMod: 299 }
      ],
      colors: [
        { name: 'Medical White', hex: '#f8f9fa' },
        { name: 'Ocean Teal', hex: '#0d7d6f' },
        { name: 'Midnight Navy', hex: '#1b2a47' }
      ],
      relatedIds: ['prod-omega3', 'prod-ashwagandha', 'prod-earbuds']
    },
    {
      id: 'prod-ebotas-1',
      slug: 'ebotas-heritage-moc-toe',
      name: 'Ebotas Heritage 6-Inch Moc-Toe Full-Grain Leather Boot',
      category: 'Footwear & Boots',
      brand: 'Ebotas Official',
      sku: 'EB-HER-901',
      price: 3499,
      originalPrice: 5999,
      rating: 4.9,
      reviews: 128,
      availability: 'In Stock',
      stock: 20,
      badge: 'Bestseller',
      subBadge: 'Goodyear Welted',
      description: 'Masterfully built from vegetable-tanned oil-infused cowhide leather with authentic 360-degree Goodyear welt construction. Custom cork infill molds to your footbed over time, while the oil-resistant Traction Tred wedge sole absorbs shock all day long.',
      specifications: {
        'Leather': 'Oil-Tanned Full-Grain Cowhide (1.8mm - 2.0mm)',
        'Construction': 'Goodyear Welt 360° Recraftable',
        'Outsole': 'Cushioned Crepe Wedge Outsole',
        'Hardware': 'Solid Brass Eyelets with Speed Hooks',
        'Insole': 'Full Leather Footbed with Organic Cork Midsole',
        'Origin': 'Handcrafted by Artisans'
      },
      images: [
        './assets/images/ebotas/boot-1.jpg',
        './assets/images/ebotas/boot-2.jpg',
        './assets/images/ebotas/leather-craft.jpg',
        './assets/images/ebotas/boot-3.jpg'
      ],
      sizes: [
        { name: 'UK 7 (IND 7)', priceMod: 0 },
        { name: 'UK 8 (IND 8)', priceMod: 0 },
        { name: 'UK 9 (IND 9)', priceMod: 0 },
        { name: 'UK 10 (IND 10)', priceMod: 0 },
        { name: 'UK 11 (IND 11)', priceMod: 0 }
      ],
      colors: [
        { name: 'Amber Gold', hex: '#c68a4c' },
        { name: 'Dark Oak Brown', hex: '#4a2f1b' },
        { name: 'Onyx Black', hex: '#1a1a1a' }
      ],
      relatedIds: ['prod-ebotas-2', 'prod-ebotas-3', 'prod-ebotas-4']
    },
    {
      id: 'prod-ebotas-2',
      slug: 'ebotas-iron-ranger',
      name: 'Ebotas Iron Ranger Handcrafted Harness Leather Boot',
      category: 'Footwear & Boots',
      brand: 'Ebotas Official',
      sku: 'EB-IRN-902',
      price: 4499,
      originalPrice: 7999,
      rating: 5.0,
      reviews: 94,
      availability: 'In Stock',
      stock: 14,
      badge: '40% OFF',
      subBadge: 'Vibram Mini-Lug',
      description: 'Inspired by mesabi iron miners, the Iron Ranger features a distinctive double-layer leather cap toe and nickel-plated brass hardware. Fitted with a low-profile Vibram 430 mini-lug outsole for unstoppable grip across rugged terrains and wet city pavement.',
      specifications: {
        'Leather': 'Amber Harness Full-Grain Leather',
        'Toe Cap': 'Reinforced Double-Layer Leather',
        'Sole': 'Vibram® 430 Mini-Lug Nitrile Rubber',
        'Hardware': 'Dull Gilt Eyelets & Speed Hooks',
        'Shank': 'Tempered Steel Arch Support'
      },
      images: [
        './assets/images/ebotas/boot-2.jpg',
        './assets/images/ebotas/boot-1.jpg',
        './assets/images/ebotas/leather-craft.jpg'
      ],
      sizes: [
        { name: 'UK 7 (IND 7)', priceMod: 0 },
        { name: 'UK 8 (IND 8)', priceMod: 0 },
        { name: 'UK 9 (IND 9)', priceMod: 0 },
        { name: 'UK 10 (IND 10)', priceMod: 0 },
        { name: 'UK 11 (IND 11)', priceMod: 0 }
      ],
      colors: [
        { name: 'Dark Oak', hex: '#3b2219' },
        { name: 'Charcoal Black', hex: '#1f1f1f' }
      ],
      relatedIds: ['prod-ebotas-1', 'prod-ebotas-3', 'prod-ebotas-4']
    },
    {
      id: 'prod-ebotas-3',
      slug: 'ebotas-chelsea-nubuck',
      name: 'Ebotas Chelsea Waterproof Oiled Nubuck Ankle Boot',
      category: 'Footwear & Boots',
      brand: 'Ebotas Official',
      sku: 'EB-CHL-903',
      price: 2999,
      originalPrice: 4999,
      rating: 4.8,
      reviews: 86,
      availability: 'In Stock',
      stock: 22,
      badge: 'Popular',
      subBadge: 'Waterproof',
      description: 'Slip-on versatility meets all-weather grit. Premium silicone-treated oiled nubuck leather repels rain and splashes, while heavy-duty dual elastic side panels provide a snug, flexible fit with effortless entry.',
      specifications: {
        'Upper': 'Hydrophobic Oiled Nubuck Cowhide',
        'Elastic': 'High-tensile recovery side gore',
        'Lining': 'Breathable calfskin leather lining',
        'Sole': 'Durable lightweight commando rubber sole'
      },
      images: [
        './assets/images/ebotas/boot-3.jpg',
        './assets/images/ebotas/boot-8.jpg',
        './assets/images/ebotas/boot-1.jpg'
      ],
      sizes: [
        { name: 'UK 7 (IND 7)', priceMod: 0 },
        { name: 'UK 8 (IND 8)', priceMod: 0 },
        { name: 'UK 9 (IND 9)', priceMod: 0 },
        { name: 'UK 10 (IND 10)', priceMod: 0 }
      ],
      colors: [
        { name: 'Charcoal Black', hex: '#1a1a1a' },
        { name: 'Tobacco Brown', hex: '#593e2b' },
        { name: 'Desert Sand', hex: '#d2b48c' }
      ],
      relatedIds: ['prod-ebotas-1', 'prod-ebotas-2', 'prod-ebotas-4']
    },
    {
      id: 'prod-ebotas-4',
      slug: 'ebotas-tactical-lug',
      name: 'Ebotas Stormproof Vibram-Lug Tactical Outdoor Boot',
      category: 'Footwear & Boots',
      brand: 'Ebotas Official',
      sku: 'EB-TAC-904',
      price: 3999,
      originalPrice: 6499,
      rating: 4.9,
      reviews: 110,
      availability: 'In Stock',
      stock: 16,
      badge: 'Heavy Duty',
      subBadge: 'Vibram Sole',
      description: 'Engineered for tactical security, hiking trails, and heavy-duty worksites. Reinforced ankle collar, puncture-resistant composite plate, and deep multidirectional lugs offer maximum traction in wet mud and snow.',
      specifications: {
        'Upper': 'Ballistic Nylon & Waterproof Full-Grain Leather',
        'Outsole': 'Vibram Oil-Resistant Lug Tread',
        'Closure': 'Heavy-duty side YKK zipper & lace-up',
        'Weight': '620g per boot'
      },
      images: [
        './assets/images/ebotas/boot-4.jpg',
        './assets/images/ebotas/boot-7.jpg',
        './assets/images/ebotas/boot-1.jpg'
      ],
      sizes: [
        { name: 'UK 7 (IND 7)', priceMod: 0 },
        { name: 'UK 8 (IND 8)', priceMod: 0 },
        { name: 'UK 9 (IND 9)', priceMod: 0 },
        { name: 'UK 10 (IND 10)', priceMod: 0 }
      ],
      colors: [
        { name: 'Coyote Tan', hex: '#a88454' },
        { name: 'Tactical Black', hex: '#111111' }
      ],
      relatedIds: ['prod-ebotas-1', 'prod-ebotas-2', 'prod-ebotas-3']
    },
    {
      id: 'prod-honey',
      slug: 'pure-organic-forest-honey',
      name: 'Pure Organic Forest Multiflower Raw Honey (100% Unprocessed)',
      category: 'Organic Grocery',
      brand: 'Himalayan Nectar',
      sku: 'SLZ-ORG-005',
      price: 999,
      originalPrice: 1499,
      rating: 4.9,
      reviews: 430,
      availability: 'In Stock',
      stock: 30,
      badge: '100% Organic',
      subBadge: 'Raw & Unfiltered',
      description: 'Harvested from wild hives in deep Himalayan pine forests. Unpasteurized, unfiltered, and rich in natural pollen, bee propolis, and live enzymes. A natural immunity booster with an exquisite floral aroma.',
      specifications: {
        'Source': 'Himalayan Wild Forest Flora',
        'Processing': 'Cold-extracted & Raw (Never heated)',
        'Packaging': 'Food-grade Glass Hexagon Jar',
        'Net Weight': '500g',
        'Shelf Life': '36 Months (Natural honey never spoils)'
      },
      images: [
        './assets/images/home-3/greek-plain.png',
        './assets/images/home-3/apple-juice.png',
        './assets/images/home-3/apple.png'
      ],
      sizes: [
        { name: '250g Jar', priceMod: -400 },
        { name: '500g Jar', priceMod: 0 },
        { name: '1kg Value Pack', priceMod: 799 }
      ],
      colors: [
        { name: 'Golden Amber', hex: '#e5a823' }
      ],
      relatedIds: ['prod-coffee-1', 'prod-omega3', 'prod-serum']
    },
    {
      id: 'prod-serum',
      slug: 'glow-hydrating-face-serum',
      name: 'Glow Daily Hydrating Vitamin C & Hyaluronic Face Serum',
      category: 'Beauty & Skincare',
      brand: 'Glow Cosmetics',
      sku: 'SLZ-BEAU-006',
      price: 1299,
      originalPrice: 1899,
      rating: 4.8,
      reviews: 290,
      availability: 'In Stock',
      stock: 19,
      badge: 'Trending',
      subBadge: 'Dermatologist Tested',
      description: 'Formulated with 15% stabilized Vitamin C, multimolecular hyaluronic acid, and organic ferulic acid. Fades dark spots, evens skin tone, and deeply hydrates for an all-day glass-skin glow.',
      specifications: {
        'Key Actives': '15% L-Ascorbic Acid, 2% Hyaluronic Acid',
        'Skin Type': 'Suitable for All Skin Types (Non-comedogenic)',
        'Volume': '30 ML Dropper Bottle',
        'Free From': 'Parabens, Sulfates, Artificial Fragrance'
      },
      images: [
        './assets/images/home-2/apply-facewash.jpg',
        './assets/images/product-details/product-details-2.png',
        './assets/images/home-2/apply-makeup-1.jpg'
      ],
      sizes: [
        { name: '30 ML', priceMod: 0 },
        { name: '50 ML (Value Size)', priceMod: 699 }
      ],
      colors: [
        { name: 'Clear Radiance', hex: '#fef9e7' }
      ],
      relatedIds: ['prod-omega3', 'prod-coffee-1', 'prod-honey']
    },
    {
      id: 'prod-earbuds',
      slug: 'wireless-anc-earbuds',
      name: 'Sellzy UltraSound Pro Wireless ANC Earbuds (36H Battery)',
      category: 'Electronics & Audio',
      brand: 'Sellzy Sound',
      sku: 'SLZ-ELEC-007',
      price: 2499,
      originalPrice: 3999,
      rating: 4.7,
      reviews: 610,
      availability: 'In Stock',
      stock: 15,
      badge: 'Best Audio',
      subBadge: 'Active Noise Cancelling',
      description: 'Industry-leading 35dB Active Noise Cancellation with Transparency Mode. 11mm bio-cellulose dynamic drivers deliver punchy bass and crystal-clear vocals. Features IPX5 water resistance and wireless charging case.',
      specifications: {
        'Bluetooth': 'v5.3 Low Latency 40ms Gaming Mode',
        'Battery Life': '9 Hours per charge (36 Hours with case)',
        'Water Resistance': 'IPX5 Sweat & Splash Proof',
        'Microphone': '4-Mic ENC for crystal clear calls'
      },
      images: [
        './assets/images/home-5/earpods.png',
        './assets/images/home-5/headphone.png',
        './assets/images/product-details/electronics-2.png'
      ],
      sizes: [
        { name: 'Standard (With 3 Eartip Sizes)', priceMod: 0 }
      ],
      colors: [
        { name: 'Matte Black', hex: '#111111' },
        { name: 'Arctic White', hex: '#f5f5f5' },
        { name: 'Space Gray', hex: '#4a4a4a' }
      ],
      relatedIds: ['prod-pulse-oximeter', 'prod-omega3']
    },
    {
      id: 'prod-ashwagandha',
      slug: 'ayurvedic-ashwagandha-capsules',
      name: 'Ayurvedic Ashwagandha KSM-66 & Turmeric Stress Relief',
      category: 'Healthcare & Wellness',
      brand: 'AyurVeda Naturals',
      sku: 'SLZ-HLTH-008',
      price: 799,
      originalPrice: 1199,
      rating: 4.9,
      reviews: 1240,
      availability: 'In Stock',
      stock: 35,
      badge: 'Ayush Certified',
      subBadge: 'Pure Extract',
      description: 'Standardized KSM-66 full-spectrum Ashwagandha root extract combined with Curcumin and black pepper for 2000% higher absorption. Clinically proven to reduce cortisol, improve sleep quality, and boost mental clarity.',
      specifications: {
        'Formulation': '600mg KSM-66 Ashwagandha + 100mg Curcumin',
        'Net Quantity': '60 Vegetarian Capsules',
        'Certification': 'Ministry of AYUSH & GMP Certified',
        'Origin': 'Sourced from Rajasthan, India'
      },
      images: [
        './assets/images/product-details/product-details-3.jpg',
        './assets/images/product-details/product-details-4.jpg',
        './assets/images/product-details/product-details-1.png'
      ],
      sizes: [
        { name: '60 Capsules', priceMod: 0 },
        { name: '120 Capsules (Twin Pack)', priceMod: 599 }
      ],
      colors: [
        { name: 'Natural Gold', hex: '#d4af37' }
      ],
      relatedIds: ['prod-omega3', 'prod-pulse-oximeter', 'prod-coffee-1']
    }
  ];

  class ProductCatalog {
    constructor() {
      this.products = PRODUCTS_CATALOG;
    }

    getAll() {
      return [...this.products];
    }

    getByIdOrSlug(identifier) {
      if (!identifier) return this.products[0];
      const clean = identifier.toString().trim().toLowerCase();
      const found = this.products.find(p => 
        p.id.toLowerCase() === clean || 
        p.slug.toLowerCase() === clean ||
        p.name.toLowerCase().includes(clean)
      );
      return found || this.products[0];
    }

    getRelated(product, limit = 4) {
      if (!product || !product.relatedIds) return this.products.slice(1, limit + 1);
      const related = this.products.filter(p => product.relatedIds.includes(p.id) && p.id !== product.id);
      if (related.length < limit) {
        const others = this.products.filter(p => p.id !== product.id && !related.includes(p));
        return [...related, ...others].slice(0, limit);
      }
      return related.slice(0, limit);
    }

    calculateDiscount(price, originalPrice) {
      if (!originalPrice || originalPrice <= price) return 0;
      return Math.round(((originalPrice - price) / originalPrice) * 100);
    }
  }

  // Expose catalog to window
  window.SellzyCatalog = new ProductCatalog();


  // Auto-enrich product card clicks across the site
  document.addEventListener('click', function(e) {
    const link = e.target.closest('a[href*="product-details"]');
    if (!link) return;
    
    const href = link.getAttribute('href');
    // If link already has ?id=, let it proceed
    if (href.includes('?id=') || href.includes('?slug=')) return;

    // Find the enclosing product card
    const card = link.closest('.single-product-item, .product-card, .ebotas-card, [class*="product-item"]') || link.parentElement;
    if (!card) return;

    // Find product name in card
    const nameEl = card.querySelector('.product-name, h3, h4, h5, .product-title, h2');
    if (nameEl) {
      const titleText = nameEl.innerText.trim();
      const matched = window.SellzyCatalog.getByIdOrSlug(titleText);
      if (matched) {
        e.preventDefault();
        window.location.href = `product-details.html?id=${matched.slug}`;
      }
    }
  });

})(window);
