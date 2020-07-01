import unittest

def test_list_sum_product():
    assert sum_product([1,2,3,4]) == 34, "should be 34"

if __name__ == "__main__":
    test_list_sum_product()
    print("all tests passed")