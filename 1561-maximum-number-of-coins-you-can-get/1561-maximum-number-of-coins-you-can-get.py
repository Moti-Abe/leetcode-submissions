class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        count_piles_you_chose = 0
        output = 0
        piles.sort(reverse=True)
        for i in range (len(piles)):
            if i%2 != 0:
                count_piles_you_chose += 1
                output += piles[i]
            if count_piles_you_chose == int(len(piles)/3):
                break

        return output
    


        