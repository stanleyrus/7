
# # %
# product = 'Sony'
# price = 100
# # print('Product: %s, Price: %.2f' %
# #       (product, price))
# print('%.1f' % (.1 + .2))

# # print('Product of us: %(product)s, has price: %(price)04d it\'s a good price!' %
# #       {'product': "Sony", 'price': 100})
# print()


# format
product = 'Sony'
price = 100
# print(' Price: {1}, Product: {0}'.format(product, price))
# print('Product: {product}, Price: {price:.2f}'.format(
#     product=product, price=price))
# print('Product: {product}, Old price: {old_price}, Price: {price}, Discount: {discount:.2%}'.format(
#     product=product, old_price=100, price=85, discount=(1 - (85 / 90))))
# print('Product: {}, Price: {}'.format(product, price))
# print('Price: {1}, Product: {0}'.format(product, price))
# print('Product: {product}, Old price: {old_price}, Price: {price}, Discount: {discount:.2%}'.format(
#     product=product, old_price=100, price=85, discount=(1 - 85 / 100)))
print(f'Product: {product}, Price: {price:.2f}')
