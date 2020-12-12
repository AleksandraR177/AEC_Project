import os
import glob
import soundfile as sf
import numpy as np
from AECAlgorithm.classess import SoundBase


def load_sound_file():
    sound_list = []
    print("Please enter the path for the folder with waves: ")
    paths = input()
    for i, filename in enumerate(glob.glob(os.path.join(paths, '*.wav'))):
        wav_data, fs = sf.read(filename)
        sound_list.append(SoundBase(wav_data, fs, os.listdir(paths)[i][:-4]))

    return sound_list


def remove_dc_offset(sound_wave):
    sound_wave.samples = sound_wave.samples - np.mean(sound_wave.samples)

    return sound_wave


def normalise():
    #normalizacja do maxa!
    normalised = 0

    return normalised


def resampling():

    resampled = 0

    return resampled


def convolution():

    convolute = 0

    return convolute

