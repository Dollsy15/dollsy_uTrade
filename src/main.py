class Engine:

    def __init__(self):
        self.data = []

    def process_input(self):
        value = input("Enter value: ")
        self.data.append(value)

    def display(self):
        for item in self.data:
            print(item)

    def run(self):
        self.process_input()
        self.display()


def main():
    engine = Engine()
    engine.run()


if __name__ == "__main__":
    main()