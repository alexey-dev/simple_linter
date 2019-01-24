import sys
import LintSystem
from input.InputSystem import ConsoleInputSystem
from os import walk

DEFAULT_FILE_EXTENSIONS_TO_LINT = ["cpp", "h", "hpp", "c"]

if __name__ == "__main__" :
    print("Start lint...")
    isystem = ConsoleInputSystem(DEFAULT_FILE_EXTENSIONS_TO_LINT)
    print("File extensions to accept: ", isystem.GetFileExtensions())
    isystem.ReadParameters()
    LintManager = LintSystem.LintSystem(isystem)
    if LintManager.IsEnableToStartLint() :
        LintManager.AnalyzeFilesForLintWarnings()