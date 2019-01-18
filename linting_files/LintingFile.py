import os
from linting_actions.ILintActionVisitor import AbstractLintActionVisitor

class LintingFile :
    def __init__(self, _path) :
        self.mPath = _path
        self.mListLintWarningsFounded = []

    def IsInitedSuccessfully(self) :
        return self.IsFileExist()

    def HasLintingWarnings(self) :
        return (len(self.mListLintWarningsFounded) > 0)

    def GetLiningWarningsList(self) :
        return self.mListLintWarningsFounded

    def IsFileExist(self) :
        return os.path.isfile(self.mPath)

    def AcceptVisitor(self, _visitor) :
        if self.IsInitedSuccessfully() :
            File = open(self.mPath, "r")
            for Line in File :
                self.mListLintWarningsFounded = _visitor.VisitFileLine(Line, self.mListLintWarningsFounded)

    def AddNewLintingWarning(self, _warning) :
        self.mListLintWarningsFounded.append(_warning)