
class Reverse:
    def __init__(self, data) -> None:
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

def main():
    rev = Reverse("Seattle")
    for i in rev:
        print(i, end = '')

if __name__ == '__main__':
    main()


      