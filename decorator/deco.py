def multiply_by(num):
    def _multiply(method):
        def _multiply_method(a, b):
            return method(a, b) * num
        return _multiply_method
    return _multiply
    
def square_by(num):
    def _square(method):
        def _square_method(a, b):
            return method(a, b) * num
        return _square_method
    return _square

@square_by(3)
@multiply_by(3)
def add(a, b):
    return a + b


print(add(1, 5))