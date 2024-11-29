class Node:
    def __init__(self, value, operation_priority):
        self.value = value
        self.operation_priority = operation_priority  
        self.next_node = None


class MyStack:
    def __init__(self):
        self.top = None

    def push(self, value, operation_priority):
        new_node = Node(value, operation_priority)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        node_to_return = self.top
        self.top = self.top.next_node
        return node_to_return


class OperationPriority:
    POWER = 3
    DIVIDE = 2
    MULTIPLY = 2
    SUBTRACT = 1
    ADD = 1
    NONE = 0


def evaluate_rpn(expression):
    stack = MyStack()
    buffer = ""
    buffer_length = 0

    for char in expression:
        if char.isdigit() or char == '.': 
            buffer += char
            buffer_length += 1
        elif char == ' ':
            if buffer_length > 0:
                stack.push(buffer, OperationPriority.NONE)  
                buffer = ""
                buffer_length = 0
        elif char in "+-*/^":  
            first = stack.pop()  
            second= stack.pop() 

     
            if char == '+':
                precedence = OperationPriority.ADD
            elif char == '-':
                precedence = OperationPriority.SUBTRACT
            elif char == '*':
                precedence = OperationPriority.MULTIPLY
            elif char == '/':
                precedence = OperationPriority.DIVIDE
            elif char == '^':
                precedence = OperationPriority.POWER

            intermediate_result = ""
            if second and second.operation_priority != OperationPriority.NONE and second.operation_priority < precedence:
                intermediate_result += "(" + second.value + ")" 
                intermediate_result += char
            else:
                intermediate_result += second.value + char

            
            if first and first.operation_priority != OperationPriority.NONE and first.operation_priority < precedence:
                intermediate_result += "(" + first.value + ")" 
            else:
                intermediate_result += first.value

            stack.push(intermediate_result, precedence) 

    return stack.pop().value 


if __name__ == "__main__":
    rpn_input = input()  
    output_result = evaluate_rpn(rpn_input)
    print(eval(output_result)) 