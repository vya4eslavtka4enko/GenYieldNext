def countdown(num):
    print("start")
    while num > 0:
        yield num
        num -= 1
    return num

cd = countdown(4)
value = next(cd)

print(value)
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))