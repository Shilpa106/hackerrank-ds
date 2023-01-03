def multiply_by(num):
    def _multiply(method):
        def _multiply_method(a, b):
            print("hi multiply")
            print(method(a,b)*num)
            return method(a, b) * num
        return _multiply_method
    return _multiply
def divide_by(num):
    def _divide(method):
        def _divide_method(a, b):
            print("hiii divide")
            return method(a, b) / num
        return _divide_method
    return _divide

@divide_by(3)
@multiply_by(3)
def add(a, b):
    return a + b

print(add(1, 5))
