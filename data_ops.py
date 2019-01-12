import tensorflow as tf
import tensorflow_hub as hub
import pandas as pd

# read training data
train_df = pd.read_csv("data/train.csv")
print("read training data")

# get numpy array of questions
questions = train_df["question_text"].values
print("created questions dataframe")

# Import the Universal Sentence Encoder's TF Hub module
module_url = "https://tfhub.dev/google/universal-sentence-encoder/2"
embed = hub.Module(module_url)
print("downloaded USE TF hub module")


with tf.Session() as sess:
    sess.run([tf.global_variables_initializer(), tf.tables_initializer()])
    # create question embeddings
    question_embeddings = sess.run(embed(questions))
    print("created question embeddings")
    # save preprocessed data as a csv file
    embedding_df = pd.DataFrame(question_embeddings)
    embedding_df.to_csv("question_embeddings_full.csv", index=False)
    print("created data csv")