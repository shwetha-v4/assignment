def get_largest_of_three(first, second, third):
    if first >= second:
        if first >= third:
            return first
        else:
            return third
    else:
        if second >= third:
            return second
        else:
            return third
largest = get_largest_of_three(22, 55,88)
print(largest)



def get_largest_number(first, second):
    if first >=second:
        return first
    else:
        return second
largest = get_largest_number(55,66)
print(largest)



def get_sum_of_array(array):
    total = 0
    for element in array:
        total += element
    return total
my_array = [2, 5, 7, 9]
sum_of_array = get_sum_of_array(my_array)
print(sum_of_array)


def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  
    return True 
print(isPrime(4)) 
   

def get_array_of_range_of_numbers(first, second):
    return list(range(first, second + 1))
result = get_array_of_range_of_numbers(3, 9)
print(result)



def get_sum(first, second):
    total = first + second  
    print("sum:", total)    
    return total
print(get_sum(3, 9))



def reverse_digits(num):
    reversed_dig = 0
    while num > 0:
        digit = num % 10
        reversed_dig = reversed_dig * 10 + digit
        num //= 10
    return reversed_dig
number = 12345
reversed_digit = reverse_digits(number)
print(reversed_digit)



def get_factorial(n):
    if n < 0:
        print("its not a factorial number ")
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial
print(get_factorial(4))



def get_factorial_without_loop(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * get_factorial_without_loop(n - 1)
print(get_factorial_without_loop(6))


def find_number_of_occurences(array, number):
    count = 0
    for element in array:
        if element == number:
            count += 1
    return count
array = [1, 2, 4, 2, 4, 2, 5]
num = 1
print(find_number_of_occurences(array, num))



def find_first_occurrence(array, number):
    for index, value in enumerate(array):
        if value == number:
            return index  
    return -1  
array = [4, 2, 3, 2, 5, 2]
number_to_find = 5
result = find_first_occurrence(array, number_to_find)
print(result)


def get_numbers_less_than_ten_in_words(number):
    number_words = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    if 0 <= number < 10:
        return number_words[number]
    else:
        return "Number is not less than ten"
print(get_numbers_less_than_ten_in_words(6)) 



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_numbers_in_range(lowerLimit, upperLimit):
    primes = []
    for num in range(lowerLimit, upperLimit + 1):
        if is_prime(num):
            primes.append(num)
    return primes
print(prime_numbers_in_range(10, 50))


def getNumberInWords(num):
    if num == 0:
        return "zero"
    
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]
    
    def three_digit_to_words(n):
        if n < 20:
            return units[n]
        elif n < 100:
            return tens[n // 10] + ("" if n % 10 == 0 else " " + units[n % 10])
        else:
            return units[n // 100] + " hundred" + ("" if n % 100 == 0 else " and " + three_digit_to_words(n % 100))
    
    words = []
    chunk_count = 0
    while num > 0:
        chunk = num % 1000
        if chunk > 0:
            if chunk_count > 0 and num // 1000 > 0:
                words.append("and "+three_digit_to_words(chunk) + (" " + thousands[chunk_count] if thousands[chunk_count] else ""))
            else:
                words.append(three_digit_to_words(chunk) + (" " + thousands[chunk_count] if thousands[chunk_count] else ""))
        num //= 1000
        chunk_count += 1

    return ' '.join(reversed(words)).strip()
print(getNumberInWords(1005))