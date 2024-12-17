
class QueueInterview:

    def __init__(self):
        self.queue_list=[]

    def queue_push(self, value): # first in, first out
        self.queue_list.append(value)

    def queue_pull(self):
        self.queue_list.pop(0)

    def queue_sort(self):
        self.queue_list.sort()

    
def findThreeLargestNumbers(array):
    largest_numbers = QueueInterview()
    largest_numbers.queue_push(array[0])
    largest_numbers.queue_push(array[1])
    largest_numbers.queue_push(array[2])
    largest_numbers.queue_sort()

    if len(array) == 3:
        return largest_numbers.queue_list
    
    for n in range(3,len(array)):
            
            if array[n] > largest_numbers.queue_list[0]:
                largest_numbers.queue_pull()
                largest_numbers.queue_push(array[n])
                largest_numbers.queue_sort()
                
    return largest_numbers.queue_list