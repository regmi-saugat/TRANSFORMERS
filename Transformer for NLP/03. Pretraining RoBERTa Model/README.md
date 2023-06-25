In this notebook, I have trained **KantaiBERT** as a RoBERTa Transformer with DistilBERT architecture. The dataset was compiled with three books by Immanuel Kant downloaded from the [Gutenberg Project](https://www.gutenberg.org/)

The KantaiBERT project was used to train a tokenizer on the kant.txt dataset. The trained merges.txt and vocab.json files were saved. A tokenizer was recreated with our pretrained files. 

KantaiBERT built the customized dataset and defined a data collator to process the training batches for backpropagation. The trainer was initialized, and we explored the parameters of the RoBERTa model in detail. The model was trained and saved. Finally, the saved model was loaded for a downstream language modeling task. The goal was to fill the mask using Immanuel Kant’s logic

