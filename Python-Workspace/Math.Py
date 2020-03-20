class Math:
    def add(*args):
        sum=0
        for num in args:
            sum += sum
        return sum

print(Math.add(5,6,7))
print(Math.add(5,6))