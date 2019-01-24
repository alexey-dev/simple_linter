from linting_actions.ILintActionVisitor import AbstractLintActionVisitor
from linting_actions.ILintWarning import AbstractLintWarning
import re

class LintWarningExtraSpaces(AbstractLintWarning) :
    def __init__(self, _numberOfLine) :
        self.mNumberOfLine = _numberOfLine

    def GetInfo(self) :
        print(" ->", self.mNumberOfLine, "line contains extra spaces at the end")

class LintActionExtraSpaces(AbstractLintActionVisitor) :
    REG_EXTRA_SPACES_PATTERN = r"([ ]+)$"

    def __init__(self) :
        pass

    def VisitFileLine(self, _numberOfLine, _line, _listLintWarnings) :
        if re.search(self.REG_EXTRA_SPACES_PATTERN, _line) :
            self.mHasExtraSpcacesAtTheEnd = True
            _listLintWarnings.append(self.GenerateLineWarning(_numberOfLine))

        return _listLintWarnings

    def VisitFile(self, _listLintWarnings):
        pass

    def GenerateLineWarning(self, _numberOfLine) :
        return LintWarningExtraSpaces(_numberOfLine)