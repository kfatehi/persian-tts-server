#!/bin/bash
docker build -t persian-tts .
model=persian-tts-female-vits
docker run --rm --gpus all \
    -v $PWD/workspace/cache:/home/user/.cache \
    -v $PWD/workspace/src:/home/user/app \
    -v $PWD/trained/$model:/kaggle/working \
    -p 5001:5000 \
    -it persian-tts