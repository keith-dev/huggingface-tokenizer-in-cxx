import transformers
import builtins
from os import path


def load_gpt2_tokenizer() -> transformers.GPT2Tokenizer:
    builtins.open, tmp_open = open, builtins.open
    gpt2_dir = "/Users/y/w/gpt2cpp/assets"
    tokenizer = transformers.GPT2Tokenizer(
        vocab_file=path.join(gpt2_dir, "vocab.json"),
        merges_file=path.join(gpt2_dir, "merges.txt"),
    )
    builtins.open = tmp_open
    return tokenizer


# t = load_gpt2_tokenizer()
# with open("/tmp/sample.txt") as f:
#     for line in f:
#         lst = t._tokenize(line[:-1]) # Remove the trailing '\n'.
#         print(*lst, sep=', ') # Do no quote strings.

t = transformers.GPT2Tokenizer.from_pretrained('gpt2')
txt = 'this is <|endoftext|> else <|endoftext|>'
print(t.tokenize(txt))
txt = '<|endoftext|> else <|endoftext|>'
print(t.tokenize(txt))
txt = 'this is <|endoftext|> else'
print(t.tokenize(txt))
txt = 'this is else'
print(t.tokenize(txt))
