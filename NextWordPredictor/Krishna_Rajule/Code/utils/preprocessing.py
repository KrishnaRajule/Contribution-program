import numpy as np

class dataset:
    
    def __init__(self, file):
        self.file = file
        self.wds = list()
    
    
    # Read the text file and preprocessing the data to form dataset
    def readfile(self):
        # Open and read the text file
        f_list = open(self.file).readlines()
        # Strip all the newline (\n) character
        self.f_lines = [s.rstrip("\n") for s in f_list]
        
        lines = list()
        # Split the lines into list of words
        for i in self.f_lines:
            lines.append(i.split(" "))
        
        # Separate all the words and append them into a list
        for i in lines:
            for j in i:
                self.wds.append(j)
        
        # Remove all the special characters from each word and store all the unique words
        valid = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        p_valid = [".", ",", "!", "?", ":", ";"]
        self.words_dict = list()
        self.seq = list()
        
        for i in p_valid:
            self.words_dict.append(i)
        for word in self.wds:
            s = ""
            p_s = ""
            for char in word:
                if char in valid:
                    s += char
                if char in p_valid:
                    p_s = char
            self.seq.append(s)
            if s not in self.words_dict:
                self.words_dict.append(s)
            if p_s != "":
                self.seq.append(p_s)
                
        self.words_dict.append(" ")
        self.words_dict.sort()
    
    
    # Build dataset
    def build(self):
        self.X = list()
        self.Y = list()
        #self.Tx = Tx
        self.seq_len = len(self.seq)
        prev_p = -1
        len_exp = list()
        
        for i, wrd in enumerate(self.seq):
            if wrd == "." or wrd == "?" or wrd == "!":
                self.X.append(self.seq[prev_p+1:i+1])
                self.Y.append(self.seq[prev_p+2:i+2])
                prev_p = i
        
        # To find length of each example/sentence and find the maximum to then assign it to Tx
        for i in self.X:
            len_exp.append(len(i))
        self.Tx = max(len_exp)
        
        # To pad each example with " " and length less than Tx
        for i, exp in enumerate(self.X):
            n_pad = self.Tx - len(exp)
            if n_pad != 0:
                for j in range(n_pad):
                    self.X[i].append(" ")
                    self.Y[i].append(" ")
            if i == (len(self.X)-1):
                self.Y[i].append(" ")
                
            #else:
            #    self.Y[i].append(" ")
        
        #for i in self.X:
        #    if len(i) == 106:
        #        print("_")
        #    else:
        #        print("1")
        #for i in self.Y:
        #    if len(i) == 106:
        #        print("_")
        #    else:
        #        print("1")
                
        # Using sequence length we create training examples
        #for i in range(0, self.m):
        #    i_x = i*self.Tx
        #    i_y = (i+1)*self.Tx
        #    self.X.append(self.seq[i_x:i_y])
        #    self.Y.append(self.seq[(i_x+1):(i_y+1)])
            
        # Adding remaning words as the last example in the dataset and padding the empty elements in the last example    
        #self.X.append(self.seq[(self.m*self.Tx):])
        #self.Y.append(self.seq[((self.m*self.Tx)+1):])
        #pad_len = self.Tx-len(self.X[self.m])
        #for i in range(pad_len):
        #    self.X[self.m].append(" ")
        #    self.Y[self.m].append(" ")
        #self.Y[self.m].append(" ")
    
    
    # One hot vector or Vectorization
    def one_hot_vector(self):
        self.m = len(self.X)
        self.nx = len(self.words_dict)
        self.x = np.zeros((self.m, self.Tx, self.nx))
        self.y = np.zeros((self.m, self.Tx, self.nx))
        self.idx_word = dict((i,w) for i,w in enumerate(self.words_dict))
        self.word_idx = dict((w,i) for i,w in enumerate(self.words_dict))
        
        # Creating one hot vectors
        for i, exp in enumerate(self.X):
            for t, wrd in enumerate(exp):
                self.x[i, t, self.word_idx[wrd]] = 1
                self.y[i, t, self.word_idx[self.Y[i][t]]] = 1
        
        return self.x, self.y
        
        
        
        
        