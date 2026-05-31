class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people_sorted = sorted(people)
        first_person = 0
        last_person = len(people) - 1
        print(last_person)
        groups = 0

        while (first_person <= last_person):
            remaining_cap = limit - people_sorted[last_person]
            last_person = last_person - 1
            groups += 1
            if (first_person <= last_person and people_sorted[first_person] <= remaining_cap):
                first_person += 1
                

        print(people_sorted)
        return groups


        