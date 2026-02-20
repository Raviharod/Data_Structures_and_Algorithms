#buy and sell the stocks to get the maximum profit
#brute force approach
def max_profit_stocks(nums):
  n = len(nums)
  max_prof = 0
  for i in range(0,n):
    for j in range(i+1, n):
      if nums[j] > nums[i]:
        p = nums[j] - nums[i]
        max_prof = max(max_prof, p)
  return max_prof

nums = [7,2,1,5,6,4,8]
print(max_profit_stocks(nums))

#optimal solution
def max_profit(prices):
  n = len(prices)
  max_prof = 0
  min_price = float("infinity")
  for i in range(0,n):
    min_price = min(nums[i], min_price)
    max_prof = max(max_prof, nums[i] - min_price)
  return max_prof

prices = [7,2,1,5,6,4,8]
print(max_profit(prices))
