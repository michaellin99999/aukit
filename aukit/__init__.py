#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: KDD
# @time: 2018-11-10
"""
## aukit
audio toolkit: 语音和频谱处理的工具箱。

### 安装

```
pip install aukit
```

- 注意
    * 如果安装过程中依赖报错，则单独另外安装依赖后，再安装aukit。
    * 容易安装报错的依赖包：tensorflow,pyaudio,sounddevice。
    * TensorFlow<=1.13.1
    * pyaudio暂不支持python37以上版本直接pip安装，需要下载whl文件安装，下载路径：https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
"""

__version__ = '1.3.1'

from .audio_io import load_wav, save_wav, anything2bytesio, anything2wav
from .audio_editor import strip_audio, remove_silence_audio, split_audio
from .audio_tuner import tune_pitch, tune_speed
from .audio_player import play_audio, play_sound
from .audio_noise_remover import remove_noise
from .audio_normalizer import preprocess_wav
from .audio_spectrogram import linear_spectrogram, mel_spectrogram
from .audio_griffinlim import linear_spectrogram as linear_spectrogram_gf, mel_spectrogram as mel_spectrogram_gf
from .audio_griffinlim import inv_linear_spectrogram, inv_linear_spectrogram_tf, inv_mel_spectrogram
from .audio_changer import change_male, change_pitch, change_attention, change_stretch, change_vague, change_pitchspeed
from .audio_changer import change_reback, change_sample, change_speed

from .audio_io import __doc__ as io_doc
from .audio_editor import __doc__ as editor_doc
from .audio_tuner import __doc__ as tuner_doc
from .audio_player import __doc__ as player_doc
from .audio_noise_remover import __doc__ as noise_remover_doc
from .audio_normalizer import __doc__ as normalizer_doc
from .audio_spectrogram import __doc__ as spectrogram_doc
from .audio_griffinlim import __doc__ as griffinlim_doc
from .audio_changer import __doc__ as changer_doc
from .audio_cli import __doc__ as cli_doc

version_doc = """
### 版本
v{}
""".format(__version__)

if __name__ == "__main__":
    print(__file__)
