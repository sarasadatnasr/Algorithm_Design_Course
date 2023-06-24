# Define a function that checks if user has enough coins to buy potions.
def potion(q, n, prices):
    # Get user's coins
    coins = []
    for i in range(q):
        coins.append(int(input()))
    # Check if user has enough coins to buy each potion, and count the number of affordable potions.
    for i in range(q):
        sum = 0
        for j in range(n):
            if coins[i] >= prices[j]:
                sum = sum + 1
        print(sum)

# Get inputs from user and call the `potion` function with the user's inputs.
n = int(input())      # Number of potions
prices = list(map(int, input().split()))    # Prices of each potion
q = int(input())      # Number of coins
potion(q,n,prices)    # Call function to check affordable potions.