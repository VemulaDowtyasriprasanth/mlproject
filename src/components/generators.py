def count_up_to(n):
    count=1
    while count<=n:
        yield count
        count+=1
counter=count_up_to(5)
for numbers in counter:
    print(numbers)