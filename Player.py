import pyaudio
class Player:
    def __init__(self):
        self.__pyaudio = pyaudio.PyAudio()
        self.__stream = None
    def __del__(self): self.Close()
    def Open(self, format=pyaudio.paInt16, channels=1, rate=8000):
        if not self.__stream:
            self.__stream = self.__pyaudio.open(format=format,
                    channels=channels,
                    rate=int(rate),
                    output=True)
    def Close(self):
        self.__stream.stop_stream()
        self.__stream.close()
        self.__pyaudio.terminate()
    # 16bitで量子化したPCM(WAV)データに対応
    # paFloat32, paInt32, paInt24, paInt16, paInt8, paUInt8, paCustomFormat
    def Play(self, data, format=pyaudio.paInt16, channels=1, rate=8000):
#        self.__chunk_write(data)
        chunk = 1024
        sp = 0  # 再生位置ポインタ
        buffer = data[sp:sp+chunk]
        while sp <= len(data):
#        while buffer != '':
#        while buffer != b'':
            self.__stream.write(buffer)
            sp = sp + chunk
            buffer = data[sp:sp+chunk]
#            print('sp:', sp)
