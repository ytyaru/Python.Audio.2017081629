import math 
import numpy as np
#http://aidiary.hatenablog.com/entry/20110607/1307449007
#https://gist.github.com/taogawa/4586999
class BaseWaveMaker:
    """
    サイン波を生成する。
    a:   振幅
    fs:  サンプリング周波数
    f0:  周波数
    sec: 秒
    """
    def Sin(self, a=1, fs=8000, f0=440, sec=5):
        fs = self.__sampling_theorem(fs, f0)
        wave = []
        for n in np.arange(fs * sec):
            s = a * np.sin(2.0 * np.pi * f0 * n / fs) # サンプリング(標本化)する
            wave.append(s)
        return wave

    # 三角波
    def Triangle(self, a=1, fs=8000, f0=440, sec=5):
        fs = self.__sampling_theorem(fs, f0)
        wave = []
        for n in np.arange(sec * fs):  # nはサンプルインデックス
            s = 0.0
            for k in range(0, 10):  # サンプルごとに10個のサイン波を重ね合わせ
#                s += (-1)**k * (a / (2*k+1)**2) * np.sin((2*k+1) * 2 * np.pi * f0 * n / fs)
                s += (-1)**k * (a / (2*k+1)**2) * np.sin((2*k+1) * 2 * np.pi * f0 * n / fs)
            # 振幅を-1～1の範囲内に
            if s > 1.0:  s = 1.0
            if s < -1.0: s = -1.0
            wave.append(s)
        return wave
    
    # 矩形波
    def Square(self, a=1, fs=8000, f0=440, sec=5):
        fs = self.__sampling_theorem(fs, f0)
        wave = []    
        for n in np.arange(sec * fs):  # nはサンプルインデックス
            s = 0.0
            for k in range(1, 10):
                s += (a / (2*k-1)) * np.sin((2*k-1) * 2 * np.pi * f0 * n / fs)
            if s > 1.0:  s = 1.0
            if s < -1.0: s = -1.0
            wave.append(s)
        return wave
    
    # ノコギリ波
    def Sawtooth(self, a=1, fs=8000, f0=440, sec=5):
        fs = self.__sampling_theorem(fs, f0)
        wave = []    
        for n in np.arange(sec * fs):  # nはサンプルインデックス
            s = 0.0
            for k in range(1, 30):
                s += (a / k) * np.sin(2 * np.pi * k * f0 * n / fs)
            if s > 1.0:  s = 1.0
            if s < -1.0: s = -1.0
            wave.append(s)
        return wave
            
    # サンプリング定理
    def __sampling_theorem(self, fs, f0):
        if fs < 2*f0:
            print('サンプリング定理によると	、サンプリング周波数は周波数の2倍以上でないと元の信号を再現できない。fs={}をfs={}に強制変換する。'.format(fs, 2*f0))
            fs = 2*f0
        return fs
