# TrainTheEngine's Speech To Text

This program is intended to transcribe English audio files into two text files, one containing the basic transcript and the other a timestamped sentence log. It is written in Python and HTML, and utilises the Openai/Whisper directory (https://github.com/openai/whisper) for transcription and the Flask directory (https://github.com/pallets/flask) for web display. It is written for Windows.


## Installation

Download the relevant files from the GitHub page (https://github.com/TrainTheEngine/Speech-To-Text) and then open a shell such as Windows Command Prompt/Powershell and install the following directories (you will need python installed):

If you do not have PIP:
```bash
py -m ensurepip --upgrade
```

Scoop:
```bash
iwr -useb get.scoop.sh | iex
```
Whisper:
```bash
pip install -U openai-whisper
```
FFMPEG:
```bash
scoop install ffmpeg
```
Flask:
```bash
pip install flask
```

## Usage
Run the python file speechtotext.py and it will direct you to a website. Visit this website and enter in the relevant information (for reference, file format should be as follows: C:/Users/User/Documents/Folder/file.<name extension>). You may have to wait a while, depending on the length of the audio file and the speed of your processor. The program will notify you when it is done and you will be able to access your transcriptions in the files you specified.

## Reading the Timestamped Transcript
You may find second, timestamped transcript to be hard to understand, however most of it can be ignored if you only want the timestamps. Here is an example of such a transcript, and how to decode it:
```bash
[{'id': 0, 'seek': 0, 'start': 0.0, 'end': 4.48, 'text': ' The stale smell of old beer lingers.', 'tokens': [50364, 440, 342, 1220, 4316, 295, 1331, 8795, 22949, 433, 13, 50588], 'temperature': 0.0, 'avg_logprob': -0.25378386654070956, 'compression_ratio': 1.4210526315789473, 'no_speech_prob': 0.022392638027668}, {'id': 1, 'seek': 0, 'start': 4.48, 'end': 7.0200000000000005, 'text': ' It takes heat to bring out the odor.', 'tokens': [50588, 467, 2516, 3738, 281, 1565, 484, 264, 41176, 13, 50715], 'temperature': 0.0, 'avg_logprob': -0.25378386654070956, 'compression_ratio': 1.4210526315789473, 'no_speech_prob': 0.022392638027668}, {'id': 2, 'seek': 0, 'start': 7.0200000000000005, 'end': 9.94, 'text': ' A cold dip restores health and zest.', 'tokens': [50715, 316, 3554, 10460, 1472, 2706, 1585, 293, 37889, 13, 50861], 'temperature': 0.0, 'avg_logprob': -0.25378386654070956, 'compression_ratio': 1.4210526315789473, 'no_speech_prob': 0.022392638027668}, {'id': 3, 'seek': 0, 'start': 9.94, 'end': 12.620000000000001, 'text': ' A salt pickle tastes fine with ham.', 'tokens': [50861, 316, 5139, 31433, 8666, 2489, 365, 7852, 13, 50995], 'temperature': 0.0, 'avg_logprob': -0.25378386654070956, 'compression_ratio': 1.4210526315789473, 'no_speech_prob': 0.022392638027668}, {'id': 4, 'seek': 0, 'start': 12.620000000000001, 'end': 15.08, 'text': ' Tacos al pastor are my favorite.', 'tokens': [50995, 38848, 329, 419, 21193, 366, 452, 2954, 13, 51118], 'temperature': 0.0, 'avg_logprob': -0.25378386654070956, 'compression_ratio': 1.4210526315789473, 'no_speech_prob': 0.022392638027668}, {'id': 5, 'seek': 0, 'start': 15.08, 'end': 17.6, 'text': ' A zestful food is the hot cross bun.', 'tokens': [51118, 316, 37889, 906, 1755, 307, 264, 2368, 3278, 6702, 13, 51244], 'temperature': 0.0, 'avg_logprob': -0.25378386654070956, 'compression_ratio': 1.4210526315789473, 'no_speech_prob': 0.022392638027668}]
```
Pay attention only to the "start" and "end" values and the number they are associated with (which is measured in seconds). These will tell you the start and end intervals of the phrases or sentences that have been said within the audio file.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[Apache](https://choosealicense.com/licenses/apache-2.0/)
