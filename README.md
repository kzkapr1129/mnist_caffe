# mnist_caffe
## 学習方法
$HOME/caffe/build/tools/caffe train --solver=solver.prototxt  
→ xxxx.caffemodelが出力される

## 一般画像で認識を行う方法
python predict.py deploy.prototxt xxxx.caffemodel 28x28.png  
→ deploy.prototxt: train.prototxtから作成したもの  
→ xxxx.caffemodel: 学習後に出力されるもの  
→ 28x28.png: 28x28の白黒画像を入力する

## movidiusを使用して一般画像の認識を行う方法
$ mvNCCompile deploy.prototxt -w deploy.caffemodel  
→ graphなどのファイルが出力される  
$ python3 predict_movidius.py  
→ test.pngを入力として識別  
