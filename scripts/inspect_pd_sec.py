with open('product-details.html', 'r', encoding='utf-8') as f:
    text = f.read()

sec_start = 260998
sec_end = 282124
print("Section start preview:")
print(text[sec_start:sec_start+800].replace('\u20b9', 'INR'))
print("\nSection end preview:")
print(text[sec_end-800:sec_end+200].replace('\u20b9', 'INR'))
