# mnist_caffe
## 学習方法
$HOME/caffe/build/tools/caffe train --solver=solver.prototxt  
→ xxxx.caffemodelが出力される

## 一般画像の識別方法
python predict.py deploy.prototxt xxxx.caffemodel 28x28.png  
→ deploy.prototxt: train.prototxtから作成したもの  
→ xxxx.caffemodel: 学習後に出力されるもの  
→ 28x28.png: 28x28の白黒画像を入力する
