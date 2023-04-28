def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum+=1
    return sum

def test_count_int():
    assert count([1,2,3,4,2,4,2],2) == 3
    assert count ([1,2,3,5,2],4) == 0
    assert count([],2) == 0
    assert count ([1,2,3],4) == 0

def test_count_str():
    assert count(["apple", "pear", "peach", "peach"],"peach") == 2
    assert count([],"banana") == 0

def fact(x):
    if x ==0:
        return 1
    return x*fact(x-1)
def test_fact():
    assert fact(5) ==120
    assert fact(1) ==1
    assert fact(2) == 2

def vowels(word):
    number_of_vowels = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in the_vowels:
            number_of_vowels += 1
    return number_of_vowels
def test_vowels():
    assert vowels("apple") == 2
    assert vowels("YOUTUBE") == 4

def list_of_squares(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d
def test_list_of_squares():
    assert list_of_squares(1) == {1:1}
    assert list_of_squares(2) == {1:1, 2:4}
    assert list_of_squares(3) == {1:1, 2:4, 3:9}

def is_even(number):
    return number % 2 ==0
def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
def filter_even(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
def test_filter_even():
    assert filter_even([1,2,3,4,5]) == [2,4]
    assert filter_even ([2,4,6,8]) == [2,4,6,8]
    assert filter_even([-1,-2,-3, -4,-5]) ==[-2,-4]
    