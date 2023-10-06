def linear_search_product(product_list, target_product):
    # Initialize an empty list to store indices
    indices = []
    
    # Iterate through the list and check if each product matches the target
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    
    return indices

# Example usage:
products = ["Apple", "Banana", "Orange", "Apple", "Mango", "Apple"]
target = "Apple"

result = linear_search_product(products, target)

if result:
    print(f"The product '{target}' was found at indices: {result}")
else:
    print(f"The product '{target}' was not found in the list.")