class Request:
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name

    def __str__(self):
        return "id: " + str(self.id) + "\n" + "name: " + self.name

class PrinterQueue:
    def __init__(self):
        self.requests = []

    def addRequest(self):
        #Take inputs from the user
        id_ = input("Input the id of your request: ")
        name_ = input("Input the name of your file: ")

        #Use them to create a requeest
        self.requests.append(Request(id_, name_))

    def isEmpty(self):
        if (self.requests.len == 0):
            return True

    def printWork(self):
        print("Printing Work")
        if (self.isEmpty == True):
            print("The queue is empty")
            return None

        print(self.requests[0])
        del self.requests[0]

    def getNumRequest(self):
        return len(self.requests)

    def showAll(self):
        for i in self.requests:
            print(i)

    def printAll(self):
        for i in range(len(self.requests)):
            self.printWork()

printer_queue = PrinterQueue()
for i in range(3):
    printer_queue.addRequest()

print(printer_queue.getNumRequest())
printer_queue.showAll()
printer_queue.printWork()
printer_queue.showAll()
printer_queue.printAll()
print(printer_queue.getNumRequest())
printer_queue.showAll()