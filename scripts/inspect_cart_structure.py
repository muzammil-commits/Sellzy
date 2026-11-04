with open('cart-single-vendor.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Remove All')
wrapper_start = text.rfind('<div class="container"', 0, pos)
if wrapper_start == -1:
    wrapper_start = text.rfind('<div class="container', 0, pos)

print("Wrapper start index:", wrapper_start)
# Find the end of this main container section
# It is before the footer
footer_pos = text.find('<!-- ========== Footer Section Start')
print("Footer start index:", footer_pos)

cart_block = text[wrapper_start:footer_pos]
print("Cart block length:", len(cart_block))

# Find order summary start inside cart_block
os_idx = cart_block.find('Order Summary')
print("Order summary offset in cart block:", os_idx)
print("Preview of start of cart block:")
print(cart_block[:600])
print("\nPreview around Order Summary:")
print(cart_block[os_idx-200:os_idx+800])
