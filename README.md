# OAI_Whisper
Whisper is an automatic speech recognition (ASR) system trained on 680,000 hours of multilingual and multitask supervised data collected from the web.

whisper: https://openai.com/blog/whisper/

whisper_git: https://github.com/openai/whisper


## Installation
The instructions for installing whisper itself and further information can be found [here](https://github.com/openai/whisper).

Since the installation involves some peculiarities, the following step-by-step instructions explain how to install Whisper and its dependencies on Windows.

#### 1) Installing Python 
Whisper is currently supported for Python versions 3.7 - 3.10
- Various Python versions can be downloaded Various Python versions can be downloaded here [here](https://www.python.org/downloads/). Currently version [3.10](https://www.python.org/downloads/release/python-3100/) is recommended
- A detailed tutorial on how to install Python can be found [here](https://medium.com/co-learning-lounge/how-to-download-install-python-on-windows-2021-44a707994013).

#### 2) Installing whisper
- The following command will pull and install the latest commit from this repository, along with its Python dependencies

```pip install git+https://github.com/openai/whisper.git```

- To update the package to the latest version of this repository, please run:

```pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git```

#### 3) Installing ffmpeg
The ffmpeg is a  cross-platform & open-source software utility to record, convert and stream video/audio files.
- Download the latest version of ffmpeg
- Unzip this file by using any file archiver such as Winrar or 7z.
- Rename the extracted folder to ffmpeg and move it into the root of C: drive.
- Now, run cmd as an administrator and set the environment path variable for ffmpeg by running the following command:

``setx /m PATH "C:\ffmpeg\bin;%PATH%"``

- Restart your computer and verify the installation by running:

``ffmpeg -version``

- Then run the following command in your python terminal

`` pip install ffmpeg-python``

#### 4) Installing rust
You may need rust installed as well, in case tokenizers does not provide a pre-built wheel for your platform.

``pip install setuptools-rust``

---

## Usage
There are two ways to use transcription.
1) [transcription_script.py](https://github.com/LeonMunz/OAI_Whisper/blob/main/transcription_script.py)
2) [transcription_notebook.py](https://github.com/LeonMunz/OAI_Whisper/blob/main/transcription_notebook.ipynb)

### Transcription_script
The transcription script offers an easy way to use Whisper, especially if Jupyter notebooks is not installed.

First, the audio file to be transcribed must be stored in the project folder in the audi folder.

At the very top of the file transcription_script.py is the dictionary "params". Here, the model size of Whisper and 
the name of the audio file can be specified. 

``params = {'model_size': 'tiny',
          'input_file': 'test_audio.wav'}``

---

## Results
**Tiny model**

Beim Nachrichten Dienst Twitter dachte sich wohl so mancher bei dem Pipzwohl. Seitdem will ja der Elon Musk den Laden übernommen hat, und gleich einmal Massenentlassungen vornahm. Der letzte macht das Licht aus, mochte einem auch angesichts dieser Radikalkur einfallen. Beim Musk eine konstantische Strategie zu erkennen ist schwer. Klar ist wohl nur, er will den Dienst kommerzieller machen. Vergaulte aber durch seine Aktionen schon Werbekunden und er will weniger inhaltlich eingreifen.

**Base model**

Beim Nachrichtendienst Twitter dachte sich wohl so mancher bei dem Piepswohl. Seitdem Milliardär Elon Musk den Laden übernommen hat und gleich einmal Massenentlassungen vornahm. Der letzte macht das Licht aus. Mache einem auch angesichts dieser Radikalkur einfallen. Bei Musk eine konstante Strategie zu erkennen, ist schwer. Klar ist wohl nur, er will den Dienst kommerzieller machen. Vergauerte aber durch seine Aktionen schon Werbekunden und er will weniger inhaltlich eingreifen.


**Medium model**

Beim Nachrichtendienst Twitter dachte sich wohl so mancher bei dem Pieps wohl. Seitdem Milliardär Elon Musk den Laden übernommen hat, und gleich einmal Massenentlassungen vornahm. Der Letzte macht das Licht aus, mochte einem auch angesichts dieser Radikal-Cure einfallen. Bei Musk eine konstante Strategie zu erkennen, ist schwer. Klar ist wohl nur, er will den Dienst kommerzieller machen. Vergaulte aber durch seine Aktionen schon Werbekunden. Und er will weniger inhaltlich eingreifen.


