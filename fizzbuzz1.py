count = 1

for count in range(100):
            if count % 3  == 0 and count % 5 == 0:
                print('FizzBuzz')
                continue
            if count % 3 == 0:
                print('Fizz')
                continue
            if count % 5 == 0:
                print('Buzz')
                continue
            print(count)
