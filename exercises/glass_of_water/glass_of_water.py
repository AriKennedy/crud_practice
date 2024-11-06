class Glass:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def pour_in(self, amount)-> int:
        self.amount += amount
        if self.amount > self.capacity:
            self.amount = self.capacity

    def pour_out(self, amount)-> int:
        self.amount -= amount
        if self.amount < 0:
            self.amount = 0

glass = Glass(20)
glass.pour_in(21)

print(f"Capacity: {glass.capacity}\nAmount: {glass.amount}")