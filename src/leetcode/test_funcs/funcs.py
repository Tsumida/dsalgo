
DEFAULT_MSG = "Case {} failed -- output = {}\t ans = {}\nargs = {}"

def test_free_func(func, test_cases:list, failed_msg=DEFAULT_MSG):
    '''

    :param func:
        Function to be tested.
    :param test_cases:
        List of test cases. Case = ()
    :return:
        None
    '''
    def wrapper(*args, **kwargs):
        num = 0
        try:
            for i, case in test_cases:
                ans, inp = case
                output = func(*args, **kwargs)
                assert output == ans, failed_msg.format(i, output, ans, inp)
                num += 1
        except AssertionError:
            print("Test failed. {}/{} cases passed.".format(num, len(test_cases)))
            raise
        print("Test succeed. {}/{} cases passed.".format(num, test_cases))

    return wrapper

def test_method(method, test_cases:list, failed_msg=DEFAULT_MSG):
    '''

    :param func:
        Function to be tested.
    :param test_cases:
        List of test cases. Case = ()
    :return:
        None
    '''
    def wrapper(self, *args, **kwargs):
        num = 0
        try:
            for i, case in test_cases:
                ans, inp = case
                output = method(self, *args, **kwargs)
                assert output == ans, failed_msg.format(i, output, ans, inp)
                num += 1
        except AssertionError:
            print("Test failed. {}/{} cases passed.".format(num, len(test_cases)))
            raise
        print("Test succeed. {}/{} cases passed.".format(num, test_cases))

    return wrapper
