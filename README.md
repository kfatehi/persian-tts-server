# persian-tts-server

Every so often I look for Persian TTS software.

This year was a huge success.

First I found https://github.com/shenasa-ai/persian-tts but I did not see any pretrained models.

Then I (re-found) https://github.com/karim23657/Persian-tts-coqui which has pretrained models!

Indeed Karim's models sound quite good! Specifically I enjoy using `persian-tts-female-vits` and this repo contains the scripts to use it.

This server is designed to be used by https://github.com/kfatehi/riva_tts_proxy/tree/sapi5_and_coqui which is designed to be used from the [Read Aloud browser extension](https://github.com/ken107/read-aloud) thus providing a high-quality, offline, easy-to-use Persian TTS solution!

## Prequisites

* Docker
* Nvidia GPU

Coqui TTS does not require using the GPU but I have made the assumption that we'll be using Nvidia GPUs through Docker.

## Get the model


```
mkdir -p trained
pushd trained
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/Kamtera/persian-tts-female-vits
pushd persian-tts-female-vits
git lfs pull
popd
popd
```

## Build and run the server

```
docker build -t persian-tts .
docker run --rm --gpus all -v $PWD/pretrained_models/persian-tts-female-vits:/kaggle/working -p 5000:5000 -it persian-tts
```