class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        arr_index = 0
        for i, operation in enumerate(operations):
            print(arr, i)
            if operation == '+':
                arr.append(int(arr[arr_index-1])+int(arr[arr_index-2]))
                arr_index += 1
            elif (operation == 'D'):
                arr.append(int(arr[arr_index-1]) * 2)
                arr_index += 1
            elif (operation == 'C'):
                arr.pop(arr_index-1)
                arr_index = arr_index - 1
            else:
                arr.append(operation)
                arr_index += 1

        queue = []
        queue.append(operations[0])
        print(arr)
        summ = 0
        for a in arr:
            summ += int(a)
        return summ



        