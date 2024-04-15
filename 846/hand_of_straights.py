def isNStraightHand(hand: list[int], groupSize: int) -> bool:
        numbers = dict()

        for i in hand:
            numbers[i] = numbers[i] + 1 if numbers.get(i) != None else 1

        keys = sorted(numbers.keys())

        for k in keys:
              while numbers[k] > 0:
                for i in range(0, groupSize):
                        if k+i in numbers and numbers[k+i] > 0:
                            numbers[k+i] = numbers[k+i] - 1
                        else:
                             return False

        return sum(numbers.values()) == 0

print(isNStraightHand([1,2,3,4,5,6,7,8], 2))