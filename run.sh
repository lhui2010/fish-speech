#  1. Get VQ tokens from reference audio
# python fish_speech/models/dac/inference.py \
#     -i "en-Alice_woman.wav" \
#     --checkpoint-path "checkpoints/openaudio-s1-mini/codec.pth"

REPO_DIR=/home/liuhui/repos/fish-speech

source activate fish-speech

FILE=$1

TEXT=$(<$FILE)

# 2. Generate semantic tokens from text:
python $REPO_DIR/fish_speech/models/text2semantic/inference.py \
    --text "$TEXT" \
    --prompt-text "You are a helpful assistant" \
    --prompt-tokens $REPO_DIR/"fake.npy" \
--checkpoint-path $REPO_DIR/"checkpoints/openaudio-s1-mini" \
--compile

# 3. Generate vocals from semantic tokens:
python fish_speech/models/dac/inference.py \
    -i "temp/codes_0.npy" \
    --checkpoint-path "checkpoints/openaudio-s1-mini/codec.pth" \
    --output-path ${FILE%.md}.mp3
rm temp/codes_0.npy
