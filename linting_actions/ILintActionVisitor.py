from abc import ABC, abstractmethod

class AbstractLintActionVisitor(ABC) :
    def __init__(self) :
        pass

    @abstractmethod
    def VisitFileLine(self, _numberOfLine, _line, _listLintWarnings) :
        pass

    @abstractmethod
    def VisitFile(self, _listLintWarnings) :
        pass

    @abstractmethod
    def GenerateLineWarning(self, _numberOfLine) :
        pass