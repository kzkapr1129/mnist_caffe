import numpy as np
import sys
import os
import caffe

if len(sys.argv) != 4:
    print("Usage: " + sys.argv[0] + " deploy.prototxt deploy.caffemodel 28x28.png")
    sys.exit(1)

model_file = sys.argv[1]
weights_file = sys.argv[2]
image_file = sys.argv[3]

net = caffe.Classifier(model_file, weights_file, channel_swap=[0], image_dims=(28, 28))
input_image = caffe.io.load_image(image_file, color=False)
result = net.predict([input_image], False)
print("result = {}".format(result[0].argmax()))
