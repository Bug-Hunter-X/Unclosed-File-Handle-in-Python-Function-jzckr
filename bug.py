def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    # ... some code that might raise an exception ...
    # Missing f.close() call
    return