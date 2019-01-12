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


for n in range(0,130):
    with tf.Session() as sess:
        sess.run([tf.global_variables_initializer(), tf.tables_initializer()])
        # create question embeddings
        question_embeddings = sess.run(embed(questions[n*10000:n*10000+10000]))
        print("created question embeddings" + str(n))
        # save preprocessed data as a csv file
        embedding_df = pd.DataFrame(question_embeddings)
        embedding_df.to_csv("question_embeddings" + str(n) + ".csv", index=False)
        print("created data csv" + str(n))