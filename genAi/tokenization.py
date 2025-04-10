import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")

# print("Vocab Size", encoder.n_vocab)


text ="The cat sat on the mat"
token = encoder.encode(text)

print("Tokenized Text", token)

tokens = [976, 9059, 10139, 402, 290, 2450]
encoded_text = encoder.decode(tokens)
print("Decoded Text", encoded_text)