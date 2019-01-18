from linting_actions.ILintActionVisitor import AbstractLintActionVisitor
from linting_actions.ILintWarning import AbstractLintWarning

class LintWarningExtraSpaces(AbstractLintWarning) :
    def __init__(self) :
        pass

    def GetInfo(self) :
        pass

class LintActionExtraSpaces(AbstractLintActionVisitor) :
    def __init__(self) :
        pass

    def VisitFileLine(self, _line, _listLintWarnings) :
        print(_line," is linting ")

    def VisitFile(self, _listLintWarnings):
        pass

    def GenerateWarning(self):
        pass