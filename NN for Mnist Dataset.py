import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot = True)


no_batch=100
no_classes = 10

n_nodes1=500
n_nodes2=500
n_nodes3=500

def nn_design(data):

    hn1 = {'weights' : tf.Variable(tf.random.normal([784,n_nodes1])) , 'biases' : tf.Variable(tf.random.normal([n_nodes1])) }
    hn2 = {'weights' : tf.Variable(tf.random.normal([n_nodes1,n_nodes2])) , 'biases' : tf.Variable(tf.random.normal([n_nodes2])) }
    hn3 = {'weights' : tf.Variable(tf.random.normal([n_nodes2,n_nodes3])) , 'biases' : tf.Variable(tf.random.normal([n_nodes3])) }
    ot = {'weights' : tf.Variable(tf.random.normal([n_nodes3,no_classes])) , 'biases' : tf.Variable(tf.random.normal(no_classes)) }

    o1 = tf.add(tf.matmul(data,hn1['weights']) , hn1['biases'])
    o1=tf.nn.relu(o1)

    o2 = tf.add(tf.matmul(o1,hn2['weights']) , hn2['biases'])
    o2=tf.nn.relu(o2)
    
    o3 = tf.add(tf.matmul(o2,hn3['weights']) , hn3['biases'])
    o3=tf.nn.relu(o3)

    res = tf.matmul(o3,ot['weights']) + ot['biases'])

    return res

def train_nn(data):
    




    
    
    







    
    
