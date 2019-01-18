from abc import ABC, abstractmethod

class AbstractLintActionVisitor(ABC) :
    def __init__(self) :
        pass

    @abstractmethod
    def VisitFileLine(self, _line, _listLintWarnings) :
        pass

    @abstractmethod
    def VisitFile(self, _listLintWarnings):
        pass

    @abstractmethod
    def GenerateWarning(self):
        pass