class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        # Indices of possible future warmer days
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            current_temp = temperatures[i]
            print(i, current_temp, stack)
            # These days cannot answer the current day because
            # they are colder than or equal to the current temperature.
            while stack and temperatures[stack[-1]] <= current_temp:
                stack.pop()

            # The top is now the nearest warmer future day.
            if stack:
                result[i] = stack[-1] - i

            stack.append(i)

        return result