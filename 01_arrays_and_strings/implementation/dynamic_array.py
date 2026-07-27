"""
Dynamic Array - Build a resizable array from scratch
Operations: insert(index, value), append(value), delete(index),
            get(index), set(index, value), size(), reverse(), traverse()
"""


class DynamicArray:
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._array = [None] * self._capacity
        
    def _resize(self, new_capacity):
        new_array = [None] * new_capacity

        for i in range(self._size):
            new_array[i] = self._array[i]

        self._array = new_array
        self._capacity = new_capacity
        
    def insert(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        if self._size == self._capacity:
            self._resize(self._capacity + 1)
            
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]
        
        self._array[index] = value
        self._size += 1
        
    def append(self, value):
        if self._size == self._capacity:
           self._resize(self._capacity + 1)
            
        self._array[self._size] = value
        self._size += 1
        
    def delete(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        val = self._array[index]
        
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
            
        self._array[self._size - 1] = None
        self._size -= 1
        return val
        
    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        return self._array[index]
    
    def set(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        self._array[index] = value
        
    def size(self):
        return self._size
    
    def reverse(self):
        left = 0
        right = self._size - 1
        
        while (left < right):
            self._array[left], self._array[right] = self._array[right], self._array[left]
            
            left += 1
            right -= 1
        
    def traverse(self):
        for i in range(0, self._size):
            print(self._array[i])
        
    def __str__(self):
        return str([self._array[i] for i in range(self._size)])

if __name__ == "__main__":
    arr = DynamicArray()

    arr.append(10)
    arr.append(20)
    arr.append(30)

    arr.insert(1, 15)

    print(arr)      # [10, 15, 20, 30]

    arr.delete(2)

    print(arr)      # [10, 15, 30]

    arr.reverse()

    print(arr)      # [30, 15, 10]
