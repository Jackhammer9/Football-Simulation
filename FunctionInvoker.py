import time

class FunctionInvoker:

    def __init__(self , function , Delay):
        self.function = function
        self.delay = Delay
        self.StartTime = time.time()
        self.ExecuteOnce = True
        self.ExecutionStatus = 0

    def Invoke(self):
        self.Current = time.time() - self.StartTime
        if self.Current >= self.delay and self.ExecuteOnce:
            self.function()
            self.ExecuteOnce = False
            self.ExecutionStatus = 1

    def GetStatus(self):
        return self.ExecutionStatus