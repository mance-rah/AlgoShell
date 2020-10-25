def array_of_array_products(arr):
  if len(arr) <= 1:
    return []
  
  rightProducts, leftProducts = calc_right_products(arr), calc_left_products(arr)
  
  return [left* right for left, right in zip(leftProducts, rightProducts)]
  
def calc_left_products(arr):
  product = 1
  productArr = [1] * len(arr)
  
  for i in range(len(arr)):

    productArr[i] = product
    product *= arr[i]
    
  return productArr

def calc_right_products(arr):
  product = 1
  productArr = [1] * len(arr)
  
  for i in reversed(range(len(arr))):
    productArr[i] = product
    product *= arr[i]
    
  return productArr