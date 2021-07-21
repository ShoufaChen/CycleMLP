# CycleMLP for COCO Object Detection and Instance Segmentation

1. Install mmcv
```
# cuda10.1 pytorch1.7.1
pip install mmcv-full==1.3.5 -f https://download.openmmlab.com/mmcv/dist/cu101/torch1.7.1/index.html

or

git clone https://github.com/open-mmlab/mmcv.git
git checkout v1.3.5
MMCV_WITH_OPS=1 pip install -e .

# for pytorch>=1.9:
# https://github.com/open-mmlab/mmcv/pull/1138
```

2. Install mmdetection v2.11.0

```
pip install 'git+https://github.com/open-mmlab/mmdetection@2894516bacf9ff82c3bc6d6970019d0890a993aa'
```


Code and configs are coming soon.

