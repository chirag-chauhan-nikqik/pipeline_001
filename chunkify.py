import os
import sqlite3
import pandas as pd
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from nltk.tokenize import word_tokenize, sent_tokenize


# Function to split a document into chunks
def split_into_chunks(text, num_chunks):
    sentences = sent_tokenize(text)
    return [sentences[i:i + num_chunks] for i in range(0, len(sentences), num_chunks)]


# Training a doc2vec model based on the chunks
def train_doc2vec_model(chunks):
    tagged_data = [TaggedDocument(words=word_tokenize(chunk.lower()), tags=[str(i)]) for i, chunk in enumerate(chunks)]
    model = Doc2Vec(vector_size=20, min_count=1, epochs=20)
    model.build_vocab(tagged_data)
    model.train(tagged_data, total_examples=model.corpus_count, epochs=model.epochs)
    return model


# Reading the markdown file and splitting it into chunks
with open('data/1.md', 'r') as file:
    content = file.read()
    chunks = split_into_chunks(content, 10)

doc2vec_model = train_doc2vec_model(chunks)

# Creating a new SQLite database and a table named 'chunks' for storing the chunk vectors
conn = sqlite3.connect('vector_db.sqlite3')
cursor = conn.cursor()

# Create a new table named 'chunks' in the database to store chunk vectors
cursor.execute('CREATE TABLE chunks (chunk_id INT, vector BLOB)')

# Adding the chunks and their respective vectors into the database
for i, chunk in enumerate(chunks):
    vector = doc2vec_model.infer_vector(word_tokenize(chunk.lower()))
    cursor.execute("INSERT INTO chunks (chunk_id, vector) VALUES (?, ?)", (i, vector))

# Remember to commit the changes and close the connection
conn.commit()
conn.close()
