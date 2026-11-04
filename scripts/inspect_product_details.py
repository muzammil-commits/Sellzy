with open('product-details.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('VitaLife Omega-3')
# Look at 3000 chars before pos
chunk = text[pos-3000:pos]
print("Last 1500 chars before VitaLife:")
print(chunk[-1500:].replace('\u20b9', 'INR'))
