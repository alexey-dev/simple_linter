import os
from os import walk
from linting_files.LintingFile import LintingFile

class LintingFileManager :
    def __init__(self, _lFileExtensions, _folderPath):
        self.mFileExtensions = _lFileExtensions
        self.mFolderPath = _folderPath
        self.mIsFileAlreadyRead = False
        self.mListFilesToLint = []

    def IsFilesAlreadyRead(self) :
        return self.mIsFileAlreadyRead

    def IsSuccessfullyInited(self) :
        return self.IsFilesAlreadyRead()

    def AddNewFilesToLint(self, _listPaths) :
        for CurPath in _listPaths :
            self.mListFilesToLint.append(LintingFile(CurPath))

    def AcceptListOfLintActions(self, _listActions) :
        for i,f in enumerate(self.mListFilesToLint) :
            for CurAction in _listActions :
                self.mListFilesToLint[i].AcceptVisitor(CurAction)

    def PrintLintWarningsInfo(self) :
        for i,f in enumerate(self.mListFilesToLint) :
            CurWarningsList = self.mListFilesToLint[i].GetLiningWarningsList()
            if len(CurWarningsList) > 0 :
                self.mListFilesToLint[i].PrintFileWarningsTitle()
                for CurLintWarning in self.mListFilesToLint[i].GetLiningWarningsList() :
                    CurLintWarning.GetInfo()

    def ReadFiles(self) :
        if not self.IsFilesAlreadyRead() :
            if self.CheckInputData() :
                TempListApprovedFiles = []
                for (dirpath, dirnames, filenames) in walk(self.mFolderPath):
                    print("DirPath is %s \n Dirnames:"%(dirpath))
                    print(dirnames)
                    print("Filenames:")
                    print(filenames)
                    if (len(filenames) > 0) :
                        TempListApprovedFiles = TempListApprovedFiles + [dirpath + "/" + file for file in filenames if any(str("." + ext) in file for ext in self.mFileExtensions)]
                        print("Approved files generated:",TempListApprovedFiles)
                self.mIsFileAlreadyRead = True
                print(TempListApprovedFiles)
                self.AddNewFilesToLint(TempListApprovedFiles)
                print("Files to lint:",self.mListFilesToLint)

    def CheckInputData(self) :
        if len(self.mFileExtensions) < 0 :
            print("Bad input data, no file extensions given!")
            return False
        elif (not self.mFolderPath) or (not os.path.isfile(self.mFolderPath) and not os.path.isdir(self.mFolderPath)) :
            print("Bad files path, bad filepath or directory path given!%s"%(self.mFolderPath))
            return False
        return True