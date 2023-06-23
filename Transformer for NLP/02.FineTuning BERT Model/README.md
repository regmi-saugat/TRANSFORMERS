**Fine Tuning BERT Models**

- BERT brings bidirectional attention to transformers. Predicting sequences from left to right and masking the future tokens to train a model has serious limitations. 

- If the masked sequence contains the meaning we are looking for, the model will produce errors. BERT attends to all of the tokens of a sequence at the same time.

------

[In this notebook](https://github.com/regmi-saugat/TRANSFORMERS/blob/main/Transformer%20for%20NLP/02.FineTuning%20BERT%20Model/BERT_FineTuning.ipynb), We have gone through all the fine-tuning process. First, we loaded the dataset and loaded necessary pre-trained modules of the model. Then, the model was trained, and its performance was measured.
