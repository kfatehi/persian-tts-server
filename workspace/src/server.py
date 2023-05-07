from flask import Flask, request, Response
from TTS.utils.synthesizer import Synthesizer
import wave
import numpy as np
import io

app = Flask(__name__)

model_path = "/kaggle/working/best_model_30824.pth"
config_path = "/kaggle/working/config.json"

synthesizer = Synthesizer(model_path, config_path, use_cuda=True)

@app.route('/synthesize', methods=['POST'])
def synthesize():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return Response("Invalid payload. Missing 'text' key.", status=400)

    wav_list = synthesizer.tts(text)
    sample_rate = 24000  # Set the sample rate to match your TTS model

    # Convert the list to a NumPy array and normalize
    wav_array = np.array(wav_list, dtype=np.float32)
    wav_norm = wav_array * (32767 / max(0.01, np.max(np.abs(wav_array))))
    wav_int16 = wav_norm.astype(np.int16)

    # Create an in-memory buffer to store the WAV data
    with io.BytesIO() as buf:
        # Write WAV data to the buffer
        with wave.open(buf, 'wb') as wav_file:
            wav_file.setnchannels(1)  # Assuming mono audio
            wav_file.setsampwidth(2)  # 2 bytes per sample for int16 data
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(wav_int16)

        buf.seek(0)
        wav_data = buf.read()

    return Response(wav_data, content_type='application/octet-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
