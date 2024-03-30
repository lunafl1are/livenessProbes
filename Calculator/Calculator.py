class OperationHandler:
    def set_next(self, next_handler):
        pass

    def handle_request(self, request):
        pass

class AdditionHandler(OperationHandler):
    def set_next(self, next_handler):
        self.next_handler = next_handler

    def handle_request(self, request):
        if request.operation == 'add':
            result = request.operand1 + request.operand2
            print(f"{request.operand1} + {request.operand2} = {result}")
        elif self.next_handler:
            self.next_handler.handle_request(request)

class SubtractionHandler(OperationHandler):
    def set_next(self, next_handler):
        self.next_handler = next_handler

    def handle_request(self, request):
        if request.operation == 'subtract':
            result = request.operand1 - request.operand2
            print(f"{request.operand1} - {request.operand2} = {result}")
        elif self.next_handler:
            self.next_handler.handle_request(request)

class MultiplicationHandler(OperationHandler):
    def set_next(self, next_handler):
        self.next_handler = next_handler

    def handle_request(self, request):
        if request.operation == 'multiply':
            result = request.operand1 * request.operand2
            print(f"{request.operand1} * {request.operand2} = {result}")
        elif self.next_handler:
            self.next_handler.handle_request(request)

class DivisionHandler(OperationHandler):
    def set_next(self, next_handler):
        self.next_handler = next_handler

    def handle_request(self, request):
        if request.operation == 'divide':
            if request.operand2 != 0:
                result = request.operand1 / request.operand2
                print(f"{request.operand1} : {request.operand2} = {result}")
            else:
                print("Nuh uh")
        elif self.next_handler:
            self.next_handler.handle_request(request)

class OperationRequest:
    def __init__(self, operand1, operand2, operation):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operation = operation

if __name__ == "__main__":
    add_handler = AdditionHandler()
    subtract_handler = SubtractionHandler()
    multiply_handler = MultiplicationHandler()
    divide_handler = DivisionHandler()

    add_handler.set_next(subtract_handler)
    subtract_handler.set_next(multiply_handler)
    multiply_handler.set_next(divide_handler)

    operand1 = float(input("First operand: "))
    operation = input("Operation (add, subtract, multiply, divide): ")
    operand2 = float(input("Second operand: "))

    user_request = OperationRequest(operand1, operand2, operation)

    add_handler.handle_request(user_request)
