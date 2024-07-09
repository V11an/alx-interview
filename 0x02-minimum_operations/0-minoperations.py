#!/usr/bin/python3
'''Minimum Operations python3 challenge question'''


def minOperations(n):
    """
    Calculates the fewest number of operations needed to achieve n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required, or 0 if impossible.
    """

    if n == 0:
        return 0

    # Base case for single character: 1 copy operation
    dp = [float('inf')] * (n + 1)  # Initialize DP table with infinity
    dp[1] = 1

    # Build the DP table iteratively
    for i in range(2, n + 1):
        # Minimum of copying the current string (i-1) or pasting from a previous copy
        dp[i] = min(dp[i - 1] + 2, dp[i // 2] + 1)  # +2 for copy & paste, +1 for paste only

    return dp[n] if dp[n] != float('inf') else 0  # Return min operations or 0 if impossible


# Example usage (can be removed for separate module)
if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
