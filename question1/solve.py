import sys

def find_summands(sum, nums):
    """
    Finds the two entries in a list that sum to the given sum and returns them in a list
    :param sum: the sum number to check against
    :param nums: the list of numbers
    """
    result = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == sum:
                    result.append(nums[i])
                    result.append(nums[j])
                    return result

# I could probably deal with command args better but this is lazy just to get the question
file_path = sys.argv[1]
SUM = int(sys.argv[2])
nums = []
with open(file_path) as file:
    content = file.readlines()
    nums = [int(x) for x in content]

summands = find_summands(SUM, nums)
print("The Answer is: {0}".format(summands[0] * summands[1]))
