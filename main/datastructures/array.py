# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:

    # My solution to https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1
    # Note: len(A) is guaranteed to be equal to len(B)
    def check(self, A, B, N):
        frequencies = dict()
        for element in A:
            if element not in frequencies:
                frequencies[element] = 1
            else:
                frequencies[element] += 1
        for element in B:
            if element not in frequencies:
                return False
            else:
                frequencies[element] -= 1
        for element in frequencies:
            if frequencies[element] != 0:
                return False
        return True

    # My solution for https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1/
    # Function to find contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr, N):
        if arr and N == len(arr):
            maximum_sum = arr[0]
            current_maximum_sum = arr[0]
            for index in range(1, N):
                current_maximum_sum = max(arr[index], current_maximum_sum + arr[index])
                maximum_sum = max(current_maximum_sum, maximum_sum)
            return maximum_sum

    # My solution to https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):

        for array_index in range(0, N, K):

            subgroup_first_index = array_index
            subgroup_last_index = min(N, array_index + K) - 1

            while subgroup_first_index < subgroup_last_index:
                temp = arr[subgroup_first_index]
                arr[subgroup_first_index] = arr[subgroup_last_index]
                arr[subgroup_last_index] = temp
                subgroup_first_index += 1
                subgroup_last_index -= 1

        return arr
