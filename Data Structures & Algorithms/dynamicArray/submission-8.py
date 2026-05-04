class DynamicArray:
    
    
    def __init__(self, capacity: int):
        self.random_array = []
        if (capacity > 0) :
            i = 0
            while i< capacity  :
                self.random_array.append([])
                i = i + 1
        


    def get(self, i: int) -> int:
        return self.random_array[i]


    def set(self, i: int, n: int) -> None:
        self.random_array[i] = n


    def pushback(self, n: int) -> None:
        if (self.getSize() == self.getCapacity()):
            self.resize()
        size = self.getSize()
        self.random_array[size] = n


    def popback(self) -> int:
        to_return = self.random_array[self.getSize()-1]
        self.set(self.getSize()-1, [])
        return to_return
 

    def resize(self) -> None:
        curr_size = self.getSize()
        target_size = curr_size * 2
        i = 0
        while i < target_size:
            if i >= curr_size:
                self.random_array.append([])
            i= i + 1

    def getSize(self) -> int:
        size = 0
        for i in self.random_array:
            if (i != []):
                size = size+1

        return size

        
    
    def getCapacity(self) -> int:
        size = 0
        for i in self.random_array:
            size = size+1

        return size
