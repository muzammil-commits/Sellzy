# Sellzy — Multipurpose eCommerce Tailwind Website

A complete, modern, production-ready e-commerce web platform built on the **Tailwind Sellzy** architecture.

---

## 🌟 Key Features

### 1. Global Header
- **Top Announcement Bar**: Need Support hotline `(480) 555-0103`, multi-language switcher (English/Spanish/Arabic), multi-currency selector (USD/EUR/GBP), and quick links (Order Tracking, FAQs, Help).
- **Middle Header**:
  - Official **Sellzy** logo.
  - Interactive search input with floating label **"Search for the Items"**, recent search tags, and quick-filter category selectors.
  - User Account log in and live Shopping Cart counter.
- **Main Navigation Bar**:
  - Categorized dropdown menus: *Home* (Styles 1-5), *Shop* (Sidebars, Multi-col Grids, Filter Banners), *Vendors* (Grid, List, Dashboard), *Mega Menu*, *Pages* (About, Contact, FAQ, 404, Coming Soon), *Blog* (Grid, List, Details).
  - 24/7 Support hotline `(480) 555-0103`.
  - Mobile slide-in navigation drawer with smooth animations.

### 2. Global Footer
- **Theme**: Deep teal background (`bg-primary-darker`) with multi-column layout.
- **Sellzy Branding**: Official Sellzy footer logo and company description.
- **Navigation Columns**: Quick links for About, Categories, Customer Account, and Vendor Portal.
- **Contact & Payment**: Customer care email, phone hotline, and secure payment icons (VISA, Mastercard, AMEX, PayPal, Apple Pay).
- **Floating Scroll-To-Top**: Smooth scroll-to-top button.

### 3. Shopping Experience & Product Display
- **Product Cards**:
  - Clean card layout with high-resolution imagery and discount badges.
  - Direct Add-to-Cart actions, Wishlist toggles, Compare shortcuts, and Quick-View modal.
- **Product Details Pages** (`product-details.html` to `product-details-6.html`):
  - Vertical and horizontal thumbnail sliders with full gallery preview and zoom.
  - Badges: *Sales*, *New Arrival*.
  - Star ratings, customer review counts, discount tags.
  - Color variation swatches and Size selection pills (`S`, `M`, `L`, `XL`, `XXL`, `XXXL`) with Size Guide.
  - Quantity incrementer, *Buy Now* and *Add to Cart* buttons.
  - 4 Key Trust Badges: Free Shipping, 24x7 Support, 30 Days Return, Secure Payment.
  - In-depth specifications, customer reviews, and Related Products slick carousel.
- **Commerce Flows**:
  - Cart Single Vendor (`cart-single-vendor.html`) & Multi-Vendor (`cart-multi-vendor.html`).
  - Checkout (`checkout.html`) & Checkout V2 (`checkout-v2.html`).
  - Order Confirmation (`order-successful.html`).
  - Compare Products (`compare.html`) & Wishlist (`wishlist-style-v1.html`, `wishlist-style-v2.html`).

---

## 📁 Included Pages & Layouts (57 Complete Templates)

- **Homepage Layouts**: `index.html` (Home 1), `index-2.html`, `index-3.html`, `index-4.html`, `index-5.html`.
- **Shop & Catalog Layouts**:
  - `shop-left-sidebar-3col.html`, `shop-left-sidebar-4col.html`, `shop-left-sidebar-5col.html`
  - `banner-category-filter-3col.html` through `banner-category-filter-6col.html`
  - `banner-left-sidebar-3col.html` through `banner-left-sidebar-5col.html`
  - `banner-with-horizontal-filter-3col.html` through `banner-with-horizontal-filter-6col.html`
  - `full-banner-3col.html` through `full-banner-6col.html`
  - `top-banner-left-sidebar-3col.html` through `top-banner-left-sidebar-5col.html`
  - `banner-list-with-sidebar.html`, `banner-list-without-sidebar-2col.html`
- **Product Details Layouts**: `product-details.html`, `product-details-2.html` through `product-details-6.html`.
- **Cart & Checkout**: `cart-single-vendor.html`, `cart-multi-vendor.html`, `checkout.html`, `checkout-v2.html`, `order-successful.html`.
- **Vendor & Marketplace**: `vendors-grid.html`, `vendors-list.html`, `vendor-dashboard.html`, `vendor-account.html`, `vendor-left-sidebar-marketplace.html`, `vendor-left-top-marketplace.html`.
- **Blog**: `blog-grid.html`, `blog-list.html`, `blog-details.html`.
- **Utility Pages**: `about.html`, `contact.html`, `faq.html`, `compare.html`, `wishlist-style-v1.html`, `wishlist-style-v2.html`, `my-account.html`, `404.html`, `coming-soon.html`.

---

## 🚀 How to Run

Open `index.html` directly in any web browser, or serve locally with any static server:

```bash
# Using Python
python -m http.server 3000

# Using Node.js
npx serve .
```

Deployable to Vercel, Netlify, or GitHub Pages out of the box with `vercel.json` clean URL routing.
