import sqlite3
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, BertModel, BertTokenizer


class QA:
    def __init__(self):
        # Model & tokenizer for embeddings - BERT Base uncased
        self.model_emb = BertModel.from_pretrained('bert-base-uncased')
        self.tokenizer_emb = BertTokenizer.from_pretrained('bert-base-uncased')

        # Model & tokenizer for Question-Answering - BERT fine-tuned on SQuAD
        self.model_qa = AutoModelForQuestionAnswering.from_pretrained(
            "bert-large-uncased-whole-word-masking-finetuned-squad")
        self.tokenizer_qa = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

    def get_vector(self, text):
        inputs = self.tokenizer_emb.encode_plus(text, return_tensors='pt', truncation=True, padding='max_length',
                                                max_length=128)
        outputs = self.model_emb(**inputs)
        return outputs[1].detach().numpy()[0]  # use the BERT [CLS] token embedding as sentence vector

    def get_answer(self, question, context):
        inputs = self.tokenizer_qa.encode_plus(question, context, return_tensors='pt')
        answer = self.model_qa(**inputs)
        answer_start = torch.argmax(answer.start_logits)
        answer_end = torch.argmax(answer.end_logits)
        return self.tokenizer_qa.convert_tokens_to_string(
            self.tokenizer_qa.convert_ids_to_tokens(inputs.input_ids[0][answer_start:answer_end + 1]))


qa = QA()

# Connect to the database and fetch all vectors
conn = sqlite3.connect('vector_db.sqlite3')
cursor = conn.cursor()
cursor.execute("SELECT chunk_id, vector FROM chunks")
rows = cursor.fetchall()

# Convert query to vector using BERT
query = "What happened at the end of the story?"
query_vector = qa.get_vector(query)

max_sim_id = None  # Initialize id of the most similar chunk to None
max_sim = -1  # Initialize maximum similarity to 1
for row in rows:
    chunk_id, chunk_vector = row[0], np.array(row[1])  # Retrieve chunk_id and vector
    sim = np.dot(chunk_vector, query_vector)  # Calculate dot product as similarity
    if sim > max_sim:  # If this vector is more similar than the current maximum
        max_sim = sim  # Update the maximum similarity
        max_sim_id = chunk_id  # Update the id of the most similar chunk

# Fetch the chunk text from the database
cursor.execute("SELECT chunk_text FROM chunks WHERE chunk_id=?", (max_sim_id,))
row = cursor.fetchone()
context = row[0]

# Get the answer from QA model
answer = qa.get_answer(query, context)
print("Answer:", answer)
