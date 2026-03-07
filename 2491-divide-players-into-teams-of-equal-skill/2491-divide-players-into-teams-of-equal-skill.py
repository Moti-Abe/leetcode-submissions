class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left= 0
        right = len(skill) -1
        total_skill = skill[0] + skill[len(skill) -1]
        chem_sum = 0
        while left < right:
            chem_sum += (skill[left] * skill[right])
            skill_sum = skill[left] + skill[right]
            left += 1
            right -= 1
            if skill_sum != total_skill:
                return -1

        return chem_sum