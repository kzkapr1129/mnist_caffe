from mvnc import mvncapi as mvnc
import numpy as np
import cv2

mvnc.global_set_option(mvnc.GlobalOption.RW_LOG_LEVEL, 2)

devices = mvnc.enumerate_devices()
if len(devices) == 0:
	print('No devices found')
	quit()

device = mvnc.Device(devices[0])
device.open()

network_blob = 'graph'
with open(network_blob, mode='rb') as f:
	blob = f.read()

graph = mvnc.Graph('graph')
fifoIn, fifoOut = graph.allocate_with_fifos(device, blob)

img = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)
img = img.astype(np.float32)
img = img - 127.5
img = img * 0.00784313

graph.queue_inference_with_fifo_elem(fifoIn, fifoOut, img, 'user object')

output, userobj = fifoOut.read_elem()

result = output.argsort()[-1]

print('\n-------- predictions --------')
print('result = {}'.format(result))

fifoIn.destroy()
fifoOut.destroy()
graph.destroy()
device.close()
