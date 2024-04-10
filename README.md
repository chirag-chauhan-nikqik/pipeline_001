# Vector-based Text Search Engine & QA System

Hello, folks! I've worked on this enjoyable project that delves into the world of Natural Language Processing (NLP) by creating an amalgamation of Information Retrieval (IR) and Question-Answering (QA) systems. It's designed to sift through textual data within a database, fetch relevant chunks in response to a natural language query, and summons the best possible answer! 🚀️

## A Snippet of Its Wonders

Let's get down to the mechanics of the IR and QA system combo:

1. **Text Storehouse & Transformation:**
   - We start by splitting the story into digestible pieces called chunks, which could be sentences or paragraphs.
   - Each chunk is then translated into a language that machines love - vectors, using the celebrated language model, BERT.
   - These vectors, landscape of BERT embeddings, capture the semantic likeness between different pieces of text.
   - We tuck away the chunks and their corresponding vectors safely into an SQLite database.

2. **Question Time and Spotlights on Answers:**
   - Have a question? Toss it in!
   - Our system translates the question to its vector form, akin to the story chunks.
   - It's then off to the database to bring back the chunk with the most likeness to the question, thanks to cosine similarity.
   - A transformer model, trained on the prestigious SQuAD dataset, takes the selected chunk and the question, and secures an answer!

## Here's How to Set It Up!

### The Prerequisites!

Python is essential, along with a few Python libraries:

  - numpy
  - sqlite3
  - transformers

But, pip is here to simplify things:

## Cracking the Story Code

Our first mission is to sort our text data into the database:

- First off, we slice up the text field into manageable chunks.
- BERT comes into play to give each chunk a vector representation.
- And, into the SQLite database it goes! Each chunk, its vector, and a unique identifier all stored together.

You can check out the `store_chunks.py` (be sure to replace with your file name) for a scripted version of these steps.

## Unleash the Questions

With the database ready to roll, you can start the question spree:

- Pop your question into the system, and it's automatically transformed to vector form, mirroring the story chunks.
- The system checks the database for the vector-chunk closest to your question.
- Featuring the selected chunk and your question, the transformer model delivers you an answer. Voila!

Take a look at `retrieve_answer.py` (switch it out for your file name) to grasp the magic behind the scenes.

## Tools of the Trade

- Python - Our loyal friend!
- numpy - Our go-to for array and matrix operations.
- sqlite3 - All praises for sqlite3, our SQL operations whizz!
- transformers - Powerhouse library for all kinds of NLP tasks.

## Got Suggestions? Bring Them On!

Feel free to contribute, add features, crack bugs, and make this project even more awesome!

## Version 1.0.0

First, but certainly not the last!

## Brought to You By

Chirag Chauhan

## License

Under the open-sky license of MIT! Check the `LICENSE.md` for more details.

## Shoutout!

To the awesome brains behind the BERT and Transformer models, kudos! Your revolutionary work has been the key gear in making this project come to life.
