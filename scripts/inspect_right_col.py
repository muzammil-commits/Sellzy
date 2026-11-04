with open('cart-single-vendor.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Order Summary')
right_col_start = text.rfind('<div class="xl:col-span-4', 0, pos)
print("Right col start:", right_col_start)
print(text[right_col_start:pos+1600].replace('\u20b9', 'INR'))
