#  1. Get VQ tokens from reference audio
# python fish_speech/models/dac/inference.py \
#     -i "en-Alice_woman.wav" \
#     --checkpoint-path "checkpoints/openaudio-s1-mini/codec.pth"

# # 2. Generate semantic tokens from text:
# python fish_speech/models/text2semantic/inference.py \
#     --text "The text you want to convert" \
#     --prompt-text "Read as a narrator" \
#     --prompt-tokens "fake.npy" \
# --checkpoint-path "checkpoints/openaudio-s1-mini" \
# --compile

# 3. Generate vocals from semantic tokens:
python fish_speech/models/dac/inference.py \
    -i "temp/codes_0.npy" \
    --checkpoint-path "checkpoints/openaudio-s1-mini/codec.pth" \
    --output-path "test_output.wav"
rm temp/codes_0.npy
