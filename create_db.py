from gensim.models import Word2Vec
import nltk
import sqlite3

# Assuming data is a list of sentences
data = ["This is the first sentence",
        "We have another sentence here",
        "This is yet another sentence",
        "The final sentence is here"]

tokenized_data = [nltk.word_tokenize(sentence) for sentence in data]

# Create and train a Word2Vec model
model = Word2Vec(sentences=tokenized_data, vector_size=100, window=5, min_count=1, sg=1)

# Save the model
model.save("word2vec.model")

# Create a new database to store vectors
conn = sqlite3.connect('vector_db.sqlite3')
cursor = conn.cursor()

# Create a new table called Vectors in the database
cursor.execute('CREATE TABLE Vectors (word TEXT, vector BLOB)')

# Insert word vectors into the table
for word in model.wv.key_to_index:
    vector = model.wv[word]  # This retrieves the actual vector
    # Save the word vector pair to the DB
    cursor.execute("INSERT INTO Vectors (word, vector) VALUES (?, ?)", (word, vector))

# Save changes to DB and close connection
conn.commit()
conn.close()
