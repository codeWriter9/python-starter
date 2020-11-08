from algorithms.fibonacci import fibonacci
from hello.helloWorld import hello_world
from sample.simple import add_one

class Main:
    def __init__(self, name, age):
        pass;


    def run():
        print("\nMain\n")
        print("fibo 10:" + str(fibonacci(10)))
        print(hello_world())
        print(add_one(5))
        return 0


if __name__ == '__main__':
    Main.run()
