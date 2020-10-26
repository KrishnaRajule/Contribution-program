import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class train:
    
    def __init__(self, m, nx, Tx, epochs):
        
        self.m = m
        self.nx = nx
        self.Ty = self.Tx = Tx
        self.epochs = epochs
        self.h_size = 64
        self.num_layers = 2
        self.dropout = 0.2
        self.batch_sz = 2
        self.num_batches = int(self.m/self.batch_sz)
        self.out_loss = 0
        
        self.h_0 = torch.zeros(self.num_layers*2, self.batch_sz, self.h_size).double()
        self.c_0 = torch.zeros(self.num_layers*2, self.batch_sz, self.h_size).double()
        
        print(self.h_0)
        print(self.c_0)

        self.optimizer = optim.Adam((self.h_0, self.c_0))
        
        self.rnn_lstm = nn.LSTM(input_size=self.nx, hidden_size=self.h_size, num_layers=self.num_layers, bias=False, batch_first=True, dropout=self.dropout, bidirectional=True)
        
        self.linear = nn.Linear(self.h_size*2, self.nx)
        
        self.softmax = nn.Softmax()
        
        self.loss = nn.CrossEntropyLoss()
        
        
    def flbo(self, x, y):
        
        for i in range(self.epochs):
            for j in range(self.num_batches):
                
                #try:
                self.x_batch = x[(j*self.batch_sz):((j+1)*self.batch_sz), :, :]
                self.y_batch = y[(j*self.batch_sz):((j+1)*self.batch_sz), :, :]
                print(self.x_batch)
                #except:
                    #x_batch = x[:, (j*self.batch_sz):, :]
                    #y_batch = y[:, (j*self.batch_sz):, :]
                    
                self.out, (self.h_0, self.c_0) = self.rnn_lstm(self.x_batch, (self.h_0, self.c_0))
                self.out_l = self.linear(self.out)
                self.y_pred = self.softmax(self.out_l)
                self.out_loss = self.loss(self.y_pred, self.y_batch)
                self.out_loss.backward()
                self.optimizer.step()
                
            print("Epoch:", (i+1), "\t Loss:", self.out_loss, "\t Parameters:", self.h_0, "\n")
                
                
                