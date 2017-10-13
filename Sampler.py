import struct
import pyaudio
#量子化する
class Sampler:
    def __init__(self):
        self.__audio_format = pyaudio.paInt16
        self.__audio_formats = [pyaudio.paFloat32, pyaudio.paInt32, pyaudio.paInt24, pyaudio.paInt16, pyaudio.paInt8, pyaudio.paUInt8, pyaudio.paCustomFormat]
        #https://docs.python.jp/3/library/struct.html
        self.__pack_formats = ['f', 'i', None, 'h', 'b', 'B', None]
        self.__formats = dict(zip(self.__audio_formats, self.__pack_formats))

    @property
    def Format(self): return self.__audio_format
    @Format.setter
    def Format(self, v):
        if v in [pyaudio.paInt32, pyaudio.paInt16, pyaudio.paInt8]: self.__audio_format = v
        else: raise Exception('pyaudio.paInt32, pyaudio.paInt16, pyaudio.paInt8以外には対応していません。')    

    def Sampling(self, wav):
        if self.__audio_format in [pyaudio.paInt32, pyaudio.paInt16, pyaudio.paInt8]:
            q = 2**(self.__get_bit(self.__audio_format)-1)-1 # 符号付きのため-1乗。0で1つ分減るため-1。
            swav = [int(x * q) for x in wav]            
            return struct.pack(self.__formats[self.__audio_format] * len(swav), *swav)
        else: raise Exception('pyaudio.paInt32, pyaudio.paInt16, pyaudio.paInt8以外には対応していません。')
    
    def __get_bit(self, pafmt):
        if pafmt == pyaudio.paFloat32: return 32
        elif pafmt == pyaudio.paInt32: return 32
        elif pafmt == pyaudio.paInt24: return 24
        elif pafmt == pyaudio.paInt16: return 16
        elif pafmt == pyaudio.paInt8: return 8
        elif pafmt == pyaudio.paUInt8: return 8
        else: raise Exception('__quantity pyaudio.paCustomFormatには対応していません。')

