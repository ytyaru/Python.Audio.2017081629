import math
#十二平均律
class EqualTemperament:
    def __init__(self):
        self.__names = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
        self.__diffs = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2]
        self.__frequencies = {}
        self.__CreateFrequencies()
    def __CreateFrequencies(self):
        for key, diff in zip(self.__names, self.__diffs):
            self.__frequencies[key] = 440 * math.pow(2, diff * (1/12.0))
    def CreateFrequency(self, key_name):
        if key_name in self.__frequencies: return self.__frequencies[key_name]
        else: raise Exception('そのキーは存在しません。')
    @property
    def Keys(self): return self.__names
    @property
    def Frequencies(self): return self.__frequencies
