class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        max_value_index = 0
        fixed_value_index = len(arr)

        output = []
        count = 0
        while fixed_value_index > 1:
            max_value = max(arr[:fixed_value_index])
            max_value_index = arr.index(max_value)
            max_value_index += 1
            output.append(max_value_index)
            arr[:max_value_index] = arr[:max_value_index][::-1]
            output.append(fixed_value_index)
            arr[:fixed_value_index] = arr[:fixed_value_index][::-1]
            fixed_value_index -= 1
            count += 2
        
        return output

        
        