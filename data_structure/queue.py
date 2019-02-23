class Queue:
    def __init__(self):
        self.Queue_item = []
        
    #Enqueue 기능 구현
    def Enqueue(self, x):
        self.Queue_item.append(x)
    
    #Dequeue 기능 구현
    def Dequeue(self):
        item_length = len(self.Queue_item)
        if item_length < 1:
            print("Queue is empty!")
        result = self.Queue_item[0]
        del self.Queue_item[0]
        return result
    
    #isEmpty 기능 구현
    def isEmpty(self):
        return not self.Queue_item
    

        