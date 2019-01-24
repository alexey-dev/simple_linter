import os
import codecs
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

    def PrintFileWarningsTitle(self) :
        print(self.mPath, " contains next warnings:")

    def AcceptVisitor(self, _visitor) :
        print("Reading file(%s)..."%(self.mPath))
        if self.IsInitedSuccessfully() :
            try:
                File = codecs.open(self.mPath, "r", errors='strict')
                for line in File:
                    break
                self.AcceptVisitorForReadLinesFromOpenedFile(File, _visitor)
            except UnicodeDecodeError:
                print("!!!!invalid utf-8!!!!")
                File = codecs.open(self.mPath, "r", encoding='utf-8', errors='ignore')
                self.AcceptVisitorForReadLinesFromOpenedFile(File, _visitor)
            #File = codecs.open(self.mPath, "r", encoding="utf_8_sig", errors='ignore')
            #File = codecs.open(self.mPath, "r", errors='ignore')
            #File = open(self.mPath, "r")
            
    def AcceptVisitorForReadLinesFromOpenedFile(self, _file, _visitor) :
        NumberOfLine = 0
        for Line in _file :
            NumberOfLine = NumberOfLine + 1
            self.mListLintWarningsFounded = _visitor.VisitFileLine(NumberOfLine, Line, self.mListLintWarningsFounded)

    def AddNewLintingWarning(self, _warning) :
        self.mListLintWarningsFounded.append(_warning)