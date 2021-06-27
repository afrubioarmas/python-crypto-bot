class LowestHighestCalculator():

    @staticmethod
    def lowest(data, n):
        lowest = 9999999999999999999999

        for i in range(1, n + 1):
            if data.iloc[n] < lowest:
                lowest = data.iloc[i]
        return lowest

    @staticmethod
    def highest(data, n):
        highest = 0

        for i in range(1, n + 1):
            if data.iloc[i] > highest:
                highest = data.iloc[i]
        return highest
