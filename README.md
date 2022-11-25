# OAI_Whisper
whisper: https://openai.com/blog/whisper/
whisper_git: https://github.com/openai/whisper


## Installation
The instructions for installing whisper itself and further information can be found [here](https://github.com/openai/whisper).

Since the installation involves some peculiarities, the following step-by-step instructions explain how to install Whisper and its dependencies on Windows.

#### 1) Installing Python 
Whisper is currently supported for Python versions 3.7 - 3.10
- Various Python versions can be downloaded [here](Various Python versions can be downloaded here). Currently version [3.10](https://www.python.org/downloads/release/python-3100/) is recommended
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

## Usage
To test whisper, a 30 second excerpt is stored as an mp3 file in the audio folder.


## Results
tiny model

Beim Nachrichten Dienst Twitter dachte sich wohl so mancher bei dem Pipzwohl. Seitdem will ja der Elon Musk den Laden übernommen hat, und gleich einmal Massenentlassungen vornahm. Der letzte macht das Licht aus, mochte einem auch angesichts dieser Radikalkur einfallen. Beim Musk eine konstantische Strategie zu erkennen ist schwer. Klar ist wohl nur, er will den Dienst kommerzieller machen. Vergaulte aber durch seine Aktionen schon Werbekunden und er will weniger inhaltlich eingreifen.

base model

Beim Nachrichtendienst Twitter dachte sich wohl so mancher bei dem Piepswohl. Seitdem Milliardär Elon Musk den Laden übernommen hat und gleich einmal Massenentlassungen vornahm. Der letzte macht das Licht aus. Mache einem auch angesichts dieser Radikalkur einfallen. Bei Musk eine konstante Strategie zu erkennen, ist schwer. Klar ist wohl nur, er will den Dienst kommerzieller machen. Vergauerte aber durch seine Aktionen schon Werbekunden und er will weniger inhaltlich eingreifen.


medium model

Beim Nachrichtendienst Twitter dachte sich wohl so mancher bei dem Pieps wohl. Seitdem Milliardär Elon Musk den Laden übernommen hat, und gleich einmal Massenentlassungen vornahm. Der Letzte macht das Licht aus, mochte einem auch angesichts dieser Radikal-Cure einfallen. Bei Musk eine konstante Strategie zu erkennen, ist schwer. Klar ist wohl nur, er will den Dienst kommerzieller machen. Vergaulte aber durch seine Aktionen schon Werbekunden. Und er will weniger inhaltlich eingreifen.


