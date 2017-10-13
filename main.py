# -*- coding: utf-8 -*-
#import math 
#import wave
#import numpy as np
#import struct
#from matplotlib import pylab as plt
import Player
import Sampler
import BaseWaveMaker
import EqualTemperament

if __name__ == "__main__" :
    et = EqualTemperament.EqualTemperament()
    wm = BaseWaveMaker.BaseWaveMaker()
    sampler = Sampler.Sampler()

    # 音声データ単体
    p = Player.Player()
    p.Open()
#    for key, f0 in et.Frequencies['C','D','E','F','G','A','B']:
    for key, f0 in et.Frequencies.items():
        if key not in ['C','D','E','F','G','A','B']: continue
        print(key, f0)
#        p.Play(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=0.5)))
        p.Play(sampler.Sampling(wm.Triangle(a=1, fs=8000, f0=f0, sec=0.5)))
#        p.Play(sampler.Sampling(wm.Square(a=1, fs=8000, f0=f0, sec=0.5)))
#        p.Play(sampler.Sampling(wm.Sawtooth(a=1, fs=8000, f0=f0, sec=0.5)))
    p.Close()
