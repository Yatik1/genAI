class tokenizer:
    def __init__(self,string):
        self.string = string

    def encoder(self):
        strs_token = [] 
        for char in self.string:
            strs_token.append(ord(char))
        return strs_token

    def decoder(self,strs_token):
        str=""
        for token in strs_token:
            str += chr(token)
        print(str)



str = input("Enter string : ")
tokener = tokenizer(str)

encoded_token = tokener.encoder()
print(encoded_token)

tokener.decoder(encoded_token)