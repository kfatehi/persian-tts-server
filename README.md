# persian-tts-server

Every so often I check this scene, here we go...

this is an abandoned-looking project https://github.com/shenasa-ai/persian-tts

but this looks lively https://github.com/karim23657/Persian-tts-coqui

Indeed Karim's project sounds quite good having tested his pre-trained model `persian-tts-female-vits` I've elected to wrap it in a server.

This server can then be used from platforms like read-aloud (albeit I am hacking my riva_tts_proxy project to utilize it, speaking of, I need to push this branch, it's just now become a misnomer project given this is obviously not Riva.)

Anyway the files in this repo allowed me to setup and use this project.

# Getting the model

```
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/Kamtera/persian-tts-female-vits
cd persian-tts-female-vits
git lfs pull
```

After that you can just run ./server.sh