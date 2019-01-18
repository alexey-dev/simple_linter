from linting_files.LintingFileManager import LintingFileManager
from linting_actions.ILintWarning import AbstractLintWarning
from linting_actions.ILintActionVisitor import AbstractLintActionVisitor
from linting_actions.LintActionExtraSpaces import LintActionExtraSpaces

class LintSystem :
    def __init__(self, _inputSystem) :
        self.mInput = _inputSystem
        self.mFileManager = LintingFileManager(self.mInput.GetFileExtensions(), self.mInput.GetFolderPath())
        self.mFileManager.ReadFiles()
        self.mListLintActionsToVisit = [LintActionExtraSpaces()]

    def AnalyzeFilesForLintWarnings(self) :
        if self.mFileManager.IsSuccessfullyInited() :
            self.mFileManager.AcceptListOfLintActions(self.mListLintActionsToVisit)
            self.mFileManager.PrintLintWarningsInfo()
        
    def FixLintWarnings(self) :
        pass

    def IsEnableToStartLint(self) :
        return self.mFileManager.IsSuccessfullyInited()