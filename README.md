# facenet-opencv
FaceNet face features using OpenCV 

# Credits

[facenet](https://github.com/davidsandberg/facenet) by [davidsandberg](https://github.com/davidsandberg/)

[facenet_opencv_dnn](https://github.com/TanFluent/facenet_opencv_dnn) by [TanFluent](https://github.com/TanFluent/)


# Why this exists
   1. The original project need tensorflow installed.
   2. The method/model need tensorflow 1.x, which is unavailable on python 3.8.
   3. A package with model in it, without depending tensorflow, is convenient.

# How is this done

## Download original models
[20180408-102900](https://drive.google.com/open?id=1R77HmFADxe87GmoLwzfgMu_HY0IhcyBz)

Or

[20180402-114759](https://drive.google.com/open?id=1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-)

## Install Tensorflow environment

python3.6 on linux

`pip3 install protobuf==3.19.4 grpcio==1.8.6 tensorflow==1.7`

## Run the scripts
with some model path fix

   1. `python3 convert_variable_to_constant.py`
   2. `python3 convert_tf_pb_to_cv_pb.py`

**Be noticed**: the package contains the result of model `20180408-102900`. 

# How to use

## Install

```bash
pip3 install opencv-python
pip3 install mtcnn_opencv
pip3 install facenet_opencv
```

## Code
```python
from facenet_cv2 import FaceNet
model = FaceNet()

vectors = model.face_features(open("x.jpg", "rb").read())

for v in vectors:
    print(v)
```
