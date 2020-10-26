# Next Word Predictor

## Code -- In progress

## Application
**Next Word Predictor** is a useful tool where it will assist us in writing emails, texts messages, also used in search engines, programming text editors, text documents such as MS Word and it is a Language Model which acts as the most common and important precursor to Voice Recognition. This application will be built using **RNN - LSTM** model and **PyTorch** library.

## Algorithms
**RNN - LSTM** is a deep learning **sequence model**. **Recurrent Neural Network(RNN)** is a basic sequence model and for this particular application we use the **many to many architecture**. **Gated Recurrent Unit(GRU)** and **Long Short Term Memorry(LSTM)** are the modified versions of the basic RNN.

> RNN Model
![RNN](Images/RNN.png)

> Many to One RNN Model
![Many to Many](Images/Many_to_Many.png)

**GRU** and **LSTM** is prefered over basic RNN, this is due to **long range connections**(when there is a long sequence of words to be predicted) and **vanishing gradient problem**(no dependncies of predicted words with the previous words in the sequence). These two reasons are taken care of in GRU and LSTM. In **GRU** we have **update and relevance gates** and **memory cell**, which helps in **memorizing** the previous words in the sequence and which helps in **predicting next words more accurately than RNN**. **LSTM** is more **general** and **powerful** than the GRU, it has **update, forget, output gates** and **memory cell**. This allows to separately keep track of **different effective words**(that might affect the next words) for **longer sequence/sentences** and also this makes the **predicted output more accurate than GRU**. 

> LSTM Cell
![LSTM Cell](Images/LSTM.png)

The main difference between GRU and LSTM during implementation is that **GRU** uses **less training parameters** and therefore use **less memory, execute faster and train faster** than LSTM, whereas LSTM is **more accurate on dataset using longer sequence**. In short, if sequence is large or accuracy is very critical, we can go for LSTM whereas for less memory consumption and faster operation we can go for GRU.


Alongside GRU or LSTM we can also use **Bidirectional RNN** model. This model would help us to **predict** and **re-predict** the words in a sequence after the full sequence is stored or made availabel to the model. This way the model can **correct itself** and **make more accurate predictions**. We also have **Deep RNNs** where **2 or more layers of RNN** are stacked upon each other. This can also be used with GRU, LSTM and Bidirectional RNN but it can make the model computationally more expensive and we use it only when the application needs it. 

## Links to dataset if any used
[Blogs](http://u.cs.biu.ac.il/~koppel/BlogCorpus.htm)

[WikiQA](http://research.microsoft.com/apps/mobile/download.aspx?p=4495da01-db8c-4041-a7f6-7984a4f6a905)

[SciFi Stories](https://www.kaggle.com/jannesklaas/scifi-stories-text-corpus#)

[More](https://lionbridge.ai/datasets/the-best-25-datasets-for-natural-language-processing/)

## How to run your model
