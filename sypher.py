from values import char_list
class shift_sypher:
    def __init__(self, shift):
        self.shift = shift
        self.values = char_list


    def encode(self, text=""):
        if text == "":
            print('No text provided.')
            return None
        
        new_text = ""
        for char in text:
            if char in self.values:
                index = self.values.index(char)
                new_index = (index + self.shift) % len(self.values)
                new_text = new_text + self.values[new_index]
            else:
                new_text = new_text + char
        return new_text
    

    def decode(self, text=""):
        if text == "":
            print('No text provided.')
            return None
        
        new_text = ""
        for char in text:
            if char in self.values:
                index = self.values.index(char)
                new_index = (index - self.shift) % len(self.values)
                new_text = new_text + self.values[new_index]
            else:
                new_text = new_text + char
        return new_text



if __name__ == "__main__":

    with open('text.txt', 'r') as f:
        text_data = f.read()
    
    shift = 3
    sypher = shift_sypher(shift)
    # print('Encoded text:')
    # print(f'{sypher.encode(text_data)}', end='\n\n')
    # text_data = sypher.encode(text_data)
    print('Decoded text:')
    print(f'{sypher.decode(text_data)}')
