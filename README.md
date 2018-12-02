# mnist_caffe
## 学習方法
$HOME/caffe/build/tools/caffe train --solver=solver.prototxt
→ xxxx.caffemodelが出力される

## 一般画像の識別方法
python predict.py deploy.prototxt xxxx.caffemodel
→ deploy.prototxtはtrain.prototxtから作成したもの
→ xxxx.caffemodelは学習後に出力されるもの
