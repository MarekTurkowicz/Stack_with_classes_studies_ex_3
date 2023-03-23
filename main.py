class Stack:
    def __init__(self, size_of_stack=0):
        self.size_of_stack = size_of_stack
        self.quantity_of_elements = 0
        self.stack_table = []

    def full(self):
        return self.quantity_of_elements == size_of_stack

    def empty(self):
        return self.quantity_of_elements == 0

    def push(self, value):
        if not self.full():
            self.stack_table.append(value)
            self.quantity_of_elements += 1
        else:
            print("No space to add")

    def pop(self):
        if not self.empty():
            self.stack_table.pop()
            self.quantity_of_elements -= 1

    def top(self):
        if not self.empty():
            return int((self.stack_table[self.quantity_of_elements - 1]))
        else:
            return None

    def print_whole_list(self):
        if not self.empty():
            for element in self.stack_table:
                if element:
                    print(element)
                else:
                    print("0 elements")


def change_location(obj1, obj2):
    while not obj1.empty():
        obj2.push(obj1.top())
        obj1.pop()


def change_location_plus_print(obj1, obj2):
    while not obj1.empty():
        obj2.push(obj1.top())
        print(obj1.top())
        obj1.pop()


size_of_stack = 10
stack1 = Stack(size_of_stack)
stack2 = Stack(size_of_stack)
print("Po")
while (not stack1.full()):
    user_value = input("Podaj element " + str(stack1.quantity_of_elements + 1) + ": ")
    if user_value.isnumeric():
        stack1.push(user_value)

change_location(stack1, stack2)
print("Stack after copying: \n")
change_location_plus_print(stack2, stack1)
#TEST
# print("STOS 1 po wypisaniu : \n")
# stack1.print_whole_list()
