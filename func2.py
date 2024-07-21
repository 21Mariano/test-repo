def divide (nums):
  nums_list = nums.split(',')
  nums_list_int = [int(n) for n in nums_list]
  return nums_list_int[0] / nums_list_int[1]

nums = input("Dime dos numeros que quieras dividir (separados por comas:)")
print(divide(nums))
