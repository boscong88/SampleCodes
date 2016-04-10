import tensorflow as tf
import numpy as np

# create a 3x3x3 array
array = np.random.rand(3,3,3)
# placeholder
x = tf.placeholder("float", [3,3,3])
# the computation
y = x * 2

with tf.Session() as session:
	# feed the 3x3x3 array into the placeholder for computation 
    result = session.run(y, feed_dict={x: array})
    print(result)

print(result[0,0,0])