from tensorflow.python.client import device_lib
import tensorflow as tf


device_lib.list_local_devices()
print('###############################################')
tf.enable_eager_execution(tf.ConfigProto(log_device_placement=True))

print(tf.add([1.0, 2.0], [3.0, 4.0]))
