for i in range(1,16):
    if i % 3 == 0 or i % 5 == 0:
        print('fizz' * (1 if i % 3 == 0 else 0) + 'buzz' * (1 if i % 5 == 0 else 0)
    else:
        print(i)
