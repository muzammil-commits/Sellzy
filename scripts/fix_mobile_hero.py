import re
import os
import glob

# 1. Update assets/css/style.css with mobile hero styles
CSS_PATH = 'assets/css/style.css'
MOBILE_HERO_CSS = """
/* ========================================================
   Mobile Hero Section Fix - Ensure 100% Visibility on Mobile
   ======================================================== */
.single-hero-slider-item,
[class*="single-hero-slider-item"],
[class*="hero-slider-item"] {
  display: flex !important;
  align-items: center !important;
  min-height: 480px !important;
  background-size: cover !important;
  background-position: center !important;
  background-repeat: no-repeat !important;
  width: 100% !important;
  position: relative !important;
}

@media (max-width: 767px) {
  .sellzy-slider,
  .home-one-hero-slider,
  .home-two-hero-slider,
  .home-three-hero-slider,
  .home-four-hero-slider,
  .home-five-hero-slider {
    display: block !important;
    min-height: 440px !important;
    background-color: #0b685c !important;
  }

  .single-hero-slider-item,
  [class*="single-hero-slider-item"],
  [class*="hero-slider-item"] {
    display: flex !important;
    min-height: 440px !important;
    padding: 2.25rem 1.25rem !important;
    background-size: cover !important;
    background-position: center !important;
  }

  .single-hero-slider-item::before,
  [class*="single-hero-slider-item"]::before {
    content: "" !important;
    position: absolute !important;
    inset: 0 !important;
    background: linear-gradient(135deg, rgba(13, 125, 111, 0.88) 0%, rgba(11, 74, 66, 0.75) 100%) !important;
    border-radius: 1.5rem !important;
    z-index: 1 !important;
  }

  .single-hero-slider-content {
    position: relative !important;
    z-index: 2 !important;
    width: 100% !important;
    max-width: 100% !important;
  }

  .single-hero-slider-content h2 {
    font-size: 1.65rem !important;
    line-height: 2.15rem !important;
    color: #ffffff !important;
    margin-top: 0.5rem !important;
    margin-bottom: 0.75rem !important;
  }

  .single-hero-slider-content p {
    font-size: 0.875rem !important;
    line-height: 1.35rem !important;
    color: rgba(255, 255, 255, 0.95) !important;
    margin-bottom: 1.25rem !important;
  }

  .single-hero-slider-content .btn {
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.5rem !important;
    position: relative !important;
    z-index: 3 !important;
  }
}
"""

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'Mobile Hero Section Fix' not in css_content:
    css_content += "\n" + MOBILE_HERO_CSS
    with open(CSS_PATH, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Added Mobile Hero CSS to assets/css/style.css")

# Also update Tailwind Sellzy preview style.css if exists
preview_css = 'Tailwind Sellzy/sellzy-preview.netlify.app/assets/css/style.css'
if os.path.exists(preview_css):
    with open(preview_css, 'r', encoding='utf-8') as f:
        pcss = f.read()
    if 'Mobile Hero Section Fix' not in pcss:
        pcss += "\n" + MOBILE_HERO_CSS
        with open(preview_css, 'w', encoding='utf-8') as f:
            f.write(pcss)
        print("Updated preview style.css")

# 2. Update index HTML files to remove md: from bg-[url(...)] and add explicit inline styles
home_pages = [
    'index.html', 'index',
    'index-2.html', 'index-2',
    'index-3.html', 'index-3',
    'index-4.html', 'index-4',
    'index-5.html', 'index-5'
]

for page in home_pages:
    if not os.path.exists(page):
        continue
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # Replace md:bg-[url(../images/...)] with bg-[url('./assets/images/...')] and add inline style
    def replace_hero_div(match):
        full_tag = match.group(0)
        # extract image path from md:bg-[url(...)]
        img_match = re.search(r'md:bg-\[url\((\.\.\/images\/[^)]+)\)\]', full_tag)
        if img_match:
            rel_img = img_match.group(1).replace('../', './assets/')
            # remove md: restriction
            updated_tag = full_tag.replace(img_match.group(0), f"bg-[url('{rel_img}')]")
            # add inline background-image and min-height if not already in style
            if 'style=' in updated_tag:
                updated_tag = re.sub(r'style=[\'"]([^\'"]*)[\'"]', rf'style="\1; background-image: url(\'{rel_img}\'); min-height: 480px; display: flex;"', updated_tag)
            else:
                updated_tag = updated_tag[:-1] + f' style="background-image: url(\'{rel_img}\'); min-height: 480px; display: flex;">'
            return updated_tag
        return full_tag

    # Match hero slider item divs
    content = re.sub(r'<div[^>]*single-hero-slider-item[^>]*>', replace_hero_div, content)
    content = re.sub(r'<div[^>]*hero-slider-item[^>]*>', replace_hero_div, content)

    if content != orig:
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated hero slides in {page}")

# 3. Update assets/js/main.js to ensure slick refresh and preloader timeout
MAIN_JS = 'assets/js/main.js'
with open(MAIN_JS, 'r', encoding='utf-8') as f:
    js_content = f.read()

if '/* Mobile Preloader & Hero Safety */' not in js_content:
    safety_js = """
  /* Mobile Preloader & Hero Safety */
  setTimeout(function() {
    $(".preloader").addClass("loaded");
    if ($.fn && $.fn.slick) {
      $(".sellzy-slider, .home-one-hero-slider").slick("setPosition");
    }
  }, 1000);
"""
    # Insert right before the last closing }); or at the bottom
    insert_pos = js_content.rfind('});')
    if insert_pos != -1:
        js_content = js_content[:insert_pos] + safety_js + js_content[insert_pos:]
    else:
        js_content += safety_js

    with open(MAIN_JS, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("Added Mobile Preloader & Hero safety to assets/js/main.js")

print("Mobile hero fix complete!")
