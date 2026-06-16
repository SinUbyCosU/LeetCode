def rodcutting(prices,n):
    dp=[0]*(n+1)
    for i in range(1,n+1):
        max_profit=0
        for j in range(1,i+1):
            profit=prices[j-1]+dp[i-j]
            if profit>max_profit:
                max_profit=profit
        dp[i]=max_profit
    return dp[n]

