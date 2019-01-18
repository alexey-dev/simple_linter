import sys
import LintSystem
from input.InputSystem import ConsoleInputSystem
from os import walk

DEFAULT_FILE_EXTENSIONS_TO_LINT = ["cpp", "h", "txt"]

if __name__ == "__main__" :
    print("Start lint...")
    isystem = ConsoleInputSystem(DEFAULT_FILE_EXTENSIONS_TO_LINT)
    isystem.GetFolderPath()
    print(isystem.GetFileExtensions())
    isystem.ReadParameters()
    LintManager = LintSystem.LintSystem(isystem)
    if LintManager.IsEnableToStartLint() :
        LintManager.AnalyzeFilesForLintWarnings()
    
    #f = []
    #print("\nParse path")
    #path = r"D:\test\python\vs\linter\PythonTestLinter\TestDataFolder"
    #for (dirpath, dirnames, filenames) in walk(path):
    #    print(dirpath)
    #    print(dirnames)
    #    print(filenames)
    #    if (len(filenames) > 0) :
    #        print("Checked files:")
    #        print([file for file in filenames if any(str("." + ext) in file for ext in DEFAULT_FILE_EXTENSIONS_TO_LINT)])
