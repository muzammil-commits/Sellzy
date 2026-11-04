with open('ebotas.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace boot titles/links with links to product-details.html?id=...
replacements = [
    ('Ebotas Heritage 6-Inch Moc-Toe Boot', 'ebotas-heritage-moc-toe'),
    ('Ebotas Iron Ranger Handcrafted Harness Boot', 'ebotas-iron-ranger'),
    ('Ebotas Chelsea Waterproof Oiled Nubuck Boot', 'ebotas-chelsea-nubuck'),
    ('Ebotas Stormproof Vibram-Sole Tactical Boot', 'ebotas-tactical-lug'),
    ('Ebotas Desert Chukka Sand Suede Handcrafted', 'ebotas-heritage-moc-toe'),
    ('Ebotas Black Label Brogue Combat Ankle Boot', 'ebotas-tactical-lug'),
    ('Ebotas Alpine Hiker Weatherproof Mountain Boot', 'ebotas-tactical-lug'),
    ('Ebotas Urban Commuter Side-Zip Ankle Boot', 'ebotas-chelsea-nubuck'),
    ('Ebotas Goodyear Welted Heavy-Duty Work Boot', 'ebotas-iron-ranger'),
    ('Ebotas Low-Top Suede Casual Sneaker Boot', 'ebotas-chelsea-nubuck'),
    ('Ebotas Winter Thermal Shearling-Lined Boot', 'ebotas-iron-ranger'),
    ('Ebotas Signature Bison Leather Chelsea Boot', 'ebotas-chelsea-nubuck'),
]

for title, slug in replacements:
    target = f'<h3 class="font-bold text-gray-900 text-sm hover:text-[#087d71] transition-colors leading-snug">\n                  {title}\n                </h3>'
    replacement = f'<h3 class="font-bold text-gray-900 text-sm hover:text-[#087d71] transition-colors leading-snug">\n                  <a href="product-details.html?id={slug}" class="hover:text-[#0d7d6f] transition-colors">{title}</a>\n                </h3>'
    if target in text:
        text = text.replace(target, replacement)

with open('ebotas.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('ebotas', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated ebotas product card links to dynamic product details!")

