
def decorator(func):
    def decorated(input_text):
        print("함수 시작")
        func(input_text)
        print("함수 끝")
    return decorated


@decorator
def hello_world(input_text):
    print(input_text)


hello_world('hello World!')

print("\n\n")



def decorator1(func):
    def decorated1(a, h):
        if a > 0 and h > 0:
            func(a, h)
        else:
            ValueError('error')
    return decorated1

@decorator1
def sam(a, h):
    print(a * h / 2)

@decorator1
def sag(a, h):
    print(a * h)



sam(4, 5)
sag(4, 4)