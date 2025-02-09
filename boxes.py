def min_count(product_count,box_size):
    min_box = 0
    while product_count > 0:
        product_count = product_count - box_size
        min_box +=1
    return min_box

