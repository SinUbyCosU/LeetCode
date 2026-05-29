def max_profit(prices):
    left=0
    right=1
    max_profit=0
    while right<len(prices):
        if left<right and prices[left]<prices[right]:
            profit=prices[right]-prices[left]
            max_profit=max(max_profit, profit)
        else:
            left=right
            right+=1
    return max_profit