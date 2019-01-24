import sys
from abc import ABC, abstractmethod

class AbstractInputSystem(ABC) :
    INPUT_KEY_PARAM_PATH="-p"

    def __init__(self, _defaultFileExtensions) :
        self.mFileExtensions = _defaultFileExtensions
        self.mFolderPath = ""

    @abstractmethod
    def ReadParameters(self) :
        pass

    @abstractmethod
    def GetFolderPath(self) :
        pass

    def GetFileExtensions(self) :
        return self.mFileExtensions

    def InitFolderPath(self, _path) :
        print("Initing folder path is %s"%(_path))
        self.mFolderPath = _path

    def ParseInputDataParams(self, _inputParams) :
        Len = len(_inputParams)
        i = 0;
        while i < Len :
            if _inputParams[i] == self.INPUT_KEY_PARAM_PATH and (i + 1) < Len :
                self.InitFolderPath(_inputParams[i+1])
                i += 2
                continue
            i += 1



class ConsoleInputSystem(AbstractInputSystem) :
    def __init__(self, _defaultFileExtensions) :
        super().__init__(_defaultFileExtensions)
        self.ParseInputDataParams(sys.argv)

    def ReadParameters(self) :
        pass

    def GetFolderPath(self) :
        return self.mFolderPath