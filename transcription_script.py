import os
import whisper

# Here you can specify the model size and the file name of the audio file.
params = {'model_size': 'medium', 'input_file': 'test_audio.mp3'}


def transcription(model_size, input_file):
    """

    :param input_file:
    :param model:
    :param data_path:
    :return:
    """
    # Audio file path
    input_path = os.path.join('audio', input_file)
    # Load model
    model = whisper.load_model(model_size)
    # Initiate transcription
    res = model.transcribe(input_path)
    # Split transcription str at punctuation
    text_lst = res['text'].split('.')
    # Rename the input filename for the output filename
    input_file = input_file.split('.')[0] + '.txt'
    # Write transcription to .txt file
    with open(os.path.join('text_output', input_file), 'w', encoding='utf8') as f:
        for line in text_lst:
            f.write(line.strip() + '\n')

    return print('The transcribed file "{}" was placed in the text_output folder.'.format(input_file))


# Execution
transcription(**params)
