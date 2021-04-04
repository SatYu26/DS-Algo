def maximumWealth(self, accounts):
    return max([sum(row) for row in accounts])