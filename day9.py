import numpy as np

# print(np.random.rand(2, 2))

# print(np.random.randn(5))

# ran_num = np.random.randint(1, 10, 10)
# print(ran_num)

# ten_nums_arr = np.array([1, 2, 3, 4, 5])
# print(np.random.choice(ten_nums_arr, 3, replace=True))

# np.random.seed(5)
# print(np.random.randint(5))

# rng = np.random.default_rng(5)
# print(rng.integers(1, 10, 2))

# arr = np.random.seed(42)
# arr_ten_nums = np.random.randint(1, 100, 10)
# print(arr_ten_nums)

# now create a maks for this to get only sepcific conditioned data from this array.
# mask_one = (arr_ten_nums > 50) & (arr_ten_nums < 70)

# print(arr_ten_nums[mask_one])

# 🔟 Practice Questions

# Coin Toss (Basics)
# Simulate tossing a coin 20 times. Count how many times you get heads (1) and tails (0).

arr_of_zeros_one = np.random.randint(0, 2, 20)
num_of_zeros = np.sum(arr_of_zeros_one == 0)
print(
    f"Number of heads are {len(arr_of_zeros_one)-num_of_zeros} and number of one's are {num_of_zeros}"
)

# Two Coins Together
# Simulate tossing two coins 50 times. Find how many times both come out heads.

# Dice Roll (Basics)
# Simulate rolling a 6-sided dice 30 times. Print all results.

# Two Dice Sum
# Roll two dice 1000 times and calculate the average of their sums.

# Check for Doubles
# In 5000 rolls of two dice, calculate the probability of getting the same number on both dice.

# Custom Choice (Cards)
# Use np.random.choice to randomly pick 5 cards from a small deck: ["A", "K", "Q", "J", "10", "9"].

# Lottery Simulation
# Suppose a lottery gives numbers from 1 to 50. Use np.random.choice to pick 6 unique numbers.

# Class Attendance Simulation
# A class has 40 students. Each student has a 70% chance of attending on a given day. Simulate attendance for 10 days and count the average number of students present.

# Coin Toss Probability
# Toss a coin 10,000 times. Estimate the probability of getting heads. (Should be close to 0.5).

# Estimate Pi (Bonus Monte Carlo)
# Generate 100,000 random points inside a 1x1 square. Estimate π using the circle formula (like we did before).
