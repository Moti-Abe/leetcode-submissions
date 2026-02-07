class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output = 0
        for operation in operations:
            if operation == "X++" or operation == "++X":
                output += 1
            elif operation == "X--" or operation == "--X":
                output -= 1
        
        return output
            

        