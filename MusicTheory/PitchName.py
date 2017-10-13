import math
#C,D,E,F,G,A,B
#ド,レ,ミ,ファ,ソ,ラ,シ
#ハ,ニ,ホ,ヘ,ト,イ,ロ
#♭,♯
#b,# (bはBの小文字だから避けたほうが賢明か)
#-,+
class Key:
    def __init__(self):
        self.__name = None
        self.__value = None
        self.__diff = None
        self.__NAMES = ('C','D','E','F','G','A','B')
        self.__NAME_VALUES = (0, 2, 4, 5, 7, 9, 11)
        self.__ACCIDENTALS = ('-', '+') #https://ja.wikipedia.org/wiki/%E5%A4%89%E5%8C%96%E8%A8%98%E5%8F%B7
        self.__FULL_NAMES = ('C','C+','D','D+','E','F','F+','G','G+','A','A+','B')
#        self.__FULL_DIFFS = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2] # 十二平均律
        self.__DIFFS = [-9,-7,-5,-4,-2,0,2] # 十二平均律
        self.__frequency = None

    #音のアルファベット表記名
    @property
    def Name(self): return self.__name
    #ド(C)音を基準とした相対位置
    @property
    def Value(self): return self.__value
    #十二平均律の基準音440Hz(ラ,A)との差分
    @property
    def Diff(self): return self.__diff
    #周波数（十二平均律から算出）
    @property
    def Frequency(self): return 440 * math.pow(2, self.Diff * (1/12.0))

    def Get(self, name):
        if not isinstance(name, str): raise Exception('引数nameはstr型にしてください。')
        if self.__validate_name(name):
            self.__name = name
            self.__value = self.__get_value(name)
            self.__diff = self.__get_diff(name)
            return self.__value
        return -1

    def __validate_name(self, name):
        if 1 == len(name): return name.upper() in self.__NAMES
        elif 2 == len(name):
            if name[0].upper() in self.__NAMES and name[1] in self.__ACCIDENTALS: return True
            else: return False
        else: raise Exception('引数nameは長さ1または2にしてください。')

    def __get_value(self, name):
        if 1 == len(name): return self.__FULL_NAMES.index(name[0].upper())
        elif 2 == len(name):
            v = self.__NAME_VALUES[self.__NAMES.index(name[0].upper())]
            if '+' == name[1]: v += 1
            elif '-' == name[1]: v -= 1
            if v < 0: v = len(self.__FULL_NAMES)-1
            elif len(self.__FULL_NAMES)-1 < v: v = 0
            return v
    
    def __get_diff(self, name):
        if 1 == len(name): return self.__DIFFS[self.__NAMES.index(name[0].upper())]
        elif 2 == len(name):
            v = self.__DIFFS[self.__NAMES.index(name[0].upper())]
            if '+' == name[1]: v += 1
            elif '-' == name[1]: v -= 1
            if v < self.__DIFFS[0]: v = self.__DIFFS[-1]
            elif self.__DIFFS[-1] < v: v = self.__DIFFS[0]
            return v

if __name__ == '__main__':
    # 12音は21*2=42通りの表現方法がある。
    k = Key()
    for n in ('C-','C','C+','D-','D','D+','E-','E','E+','F-','F','F+','G-','G','G+','A-','A','A+','B-','B','B+'):
        k.Get(n)
        print('{0:<2} {1:>2} {2:.1f}'.format(k.Name, k.Value, k.Frequency))
    for n in ('c-','c','c+','d-','d','d+','e-','e','e+','f-','f','f+','g-','g','g+','a-','a','a+','b-','b','b+'):
        k.Get(n)
        print('{0:<2} {1:>2} {2:.1f}'.format(k.Name, k.Value, k.Frequency))
        
