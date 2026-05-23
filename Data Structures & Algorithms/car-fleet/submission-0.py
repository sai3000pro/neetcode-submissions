class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        cars = sorted(zip(position,speed), reverse = True)
        maxTime = 0.0
        for car in cars:
            time = (target - car[0])/car[1]
            if maxTime < time:
                maxTime = time
                fleets += 1
        return fleets