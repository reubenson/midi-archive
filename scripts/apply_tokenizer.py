# This function to be moved into the repo to run locally and upload to S3 ...
# The tokenizer config and vocab should be handled there as well?
# Tokenize a whole dataset and save it at Json files

from miditok import Structured, TokenizerConfig, MIDITokenizer
from pathlib import Path
import os

TOKENIZER_PARAMS = {
    "pitch_range": (21, 109),
    "beat_res": {(0, 4): 8, (4, 12): 4},
    "num_velocities": 4,
    # "special_tokens": ["PAD", "BOS", "EOS", "MASK"],
    "use_chords": True,
    "use_rests": True,
    "use_tempos": True,
    "use_time_signatures": False,
    # "use_programs": False,
    "num_tempos": 4,  # nb of tempo bins
    "tempo_range": (40, 250),  # (min, max),
    "one_token_stream": True,
    "one_token_stream_for_programs": True,
    "use_programs": True
  }
config = TokenizerConfig(**TOKENIZER_PARAMS)
tokenizer = Structured(config)

assets_path = '../src/assets'
target_dir = '../tokens_noBPE'
midi_directories = [d for d in os.listdir(assets_path) if os.path.isdir(os.path.join(assets_path, d))]

print(f'midi_directories: {midi_directories}')
for d in midi_directories:
    print(f'd: {d}')
    midi_paths = list(Path(os.path.join(assets_path, d)).glob('**/*.mid'))
    if len(midi_paths):
        tokenizer.tokenize_midi_dataset(midi_paths, Path(os.path.join('tokens_noBPE', d)))

# TO DO: explore data augmentation
# data_augmentation_offsets = [2, 1, 1]  # data augmentation on 2 pitch octaves, 1 velocity and 1 duration values

# Saving our tokenizer, to retrieve it back later with the load_params method
token_zip_path = Path("../tokens_noBPE/tokenizer.json")
print(f'token_zip_path: {token_zip_path}')
tokenizer.save_params(token_zip_path)