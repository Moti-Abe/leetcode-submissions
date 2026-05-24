class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def dfs(expr):

            results = []

            for i, ch in enumerate(expr):

                if ch in "+-*":

                    left = dfs(expr[:i])
                    right = dfs(expr[i + 1:])

                    for l in left:
                        for r in right:

                            if ch == "+":
                                results.append(l + r)

                            elif ch == "-":
                                results.append(l - r)

                            else:
                                results.append(l * r)

            # Base case:
            # expression contains only a number
            if not results:
                results.append(int(expr))

            return results

        return dfs(expression)