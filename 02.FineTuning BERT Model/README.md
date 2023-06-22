- BERT brings bidirectional attention to transformers. Prediciting sequences from left to right and masking the future tokens to train a model has serious limitations. 

- If the masked sequence contains the meaning we are looking for, the model will produce errors. BERT attends to all of the tokens of a sequence at the same time.

------

[In this notebook](02.FineTuning BERT Model/BERT_FineTuning.ipynb), We have went through all the fine-tuning process. First, we have loaded the dataset and loaded necessary pretrained modules of the model. Then, the model was trained, and its performance was measured.
