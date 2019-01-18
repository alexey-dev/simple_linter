from abc import ABC, abstractmethod

class AbstractLintWarning(ABC) :
    def __init__(self) :
        pass

    @abstractmethod
    def GetInfo(self) :
        pass