import ass


def test_largest_number():
    num = ass.get_largest_number(1, 7)
    assert num == 7
    num = ass.get_largest_number(-1, -3)
    assert num == -1


def test_largest_of_three():
    assert 3 == ass.get_largest_of_three(1, 2, 3)
    assert 3 == ass.get_largest_of_three(1, 3, 2)
    assert 3 == ass.get_largest_of_three(2, 1, 3)
    assert 3 == ass.get_largest_of_three(2, 3, 1)
    assert 3 == ass.get_largest_of_three(3, 1, 2)
    assert 3 == ass.get_largest_of_three(3, 2, 1)

    
    
def test_sum_of_array_elements():
    assert 15 == ass.get_sum_of_array([1, 2, 3, 4, 5])
    assert -6 == ass.get_sum_of_array([-1, -2, -3])
    
    

def test_isprime():
    assert ass.isPrime(5)

    assert ass.isPrime(2)

    assert ass.isPrime(3)

    assert ass.isPrime(7)



def test_numbers_in_a_range():
    expectedArray = [3, 4, 5, 6, 7, 8, 9]
    assert expectedArray == ass.get_array_of_range_of_numbers(3, 9)
    expectedArray = [-3, -2, -1]
    assert expectedArray == ass.get_array_of_range_of_numbers(-3, -1)
    expectedArray = [-3, -2, -1, 0, 1]
    assert expectedArray == ass.get_array_of_range_of_numbers(-3, 1)


def test_sum():
    assert 12 == ass.get_sum(3, 9)
    assert 6 == ass.get_sum(-3, 9)
    assert -12 == ass.get_sum(-3, -9)
    


def test_reverse_digits():
    assert 12 == ass.reverse_digits(21)
    assert 4321 == ass.reverse_digits(1234)
   


def test_factorial():
    assert 6 == ass.get_factorial(3)
    assert 1 == ass.get_factorial(0)
    assert 1 == ass.get_factorial(1)  



def test_factorial_without_loop():
    assert 6 == ass.get_factorial_without_loop(3)
    assert 1 == ass.get_factorial_without_loop(0)
    assert 1 == ass.get_factorial_without_loop(1)


def test_find_number_of_occurences():
    assert 3 == ass.find_number_of_occurences([1, 1, 1], 1)
    assert 2 == ass.find_number_of_occurences([1, 2, 1], 1)
    assert 1 == ass.find_number_of_occurences([1, 2, 3], 1)
    assert 0 == ass.find_number_of_occurences([2, 3, 4], 1)

def test_find_first_occurrences():
    assert -1 == ass.find_first_occurrence([2, 2, 2, -1], 1)
    assert 0 == ass.find_first_occurrence([1, 1, 1, 1], 1)
    assert 2 == ass.find_first_occurrence([2, 2, 1, 1], 1)

def test_get_number_less_than_ten_in_words():
    assert "one" == ass.get_numbers_less_than_ten_in_words(1)
    assert "four" == ass.get_numbers_less_than_ten_in_words(4)
    assert "seven" == ass.get_numbers_less_than_ten_in_words(7)
    assert "three" == ass.get_numbers_less_than_ten_in_words(3)
    assert "two" == ass.get_numbers_less_than_ten_in_words(2)
    assert "eight" == ass.get_numbers_less_than_ten_in_words(8)
    assert "nine" == ass.get_numbers_less_than_ten_in_words(9)



def test_getNumberInWords():
    assert "thirty four" == ass.getNumberInWords(34)
    assert "two hundred and thirty four" == ass.getNumberInWords(234)
    assert "one thousand two hundred and thirty four" == ass.getNumberInWords(1234)
    assert "forty five thousand six hundred and fifty two" == ass.getNumberInWords( 45652)
    assert "two hundred and nine" == ass.getNumberInWords(209)
    assert "one thousand five" == ass.getNumberInWords(1005)
    assert "thirty five thousand seven hundred and four" == ass.getNumberInWords(35704)
    assert "five hundred and fifty thousand four hundred and ninety two" == ass.getNumberInWords(550492)


def test_prime_numbers_in_a_range():
    expectedArray = [2, 3, 5, 7]
    assert expectedArray == ass.prime_numbers_in_range(0, 9)
    expectedArray = [3, 5, 7]
    assert expectedArray == ass.prime_numbers_in_range(3, 9)