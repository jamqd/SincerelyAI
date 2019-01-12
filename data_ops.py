import tensorflow as tf
import tensorflow_hub as hub

# Import the Universal Sentence Encoder's TF Hub module
module_url = "https://tfhub.dev/google/universal-sentence-encoder/2"
embed = hub.Module(module_url)
print("downloaded USE TF hub module")

with tf.Session() as sess:
    sess.run([tf.global_variables_initializer(), tf.tables_initializer()])
    # create question embeddings
    question_embeddings = sess.run(embed(questions))
    print("created question embeddings")