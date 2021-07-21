# CycleMLP for Semantic Segmentation


## Installation

1. Install mmcv v1.3.5
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

2. Install mmsegmentation v0.13.0

```
pip install 'git+https://github.com/open-mmlab/mmsegmentation@f884489120c3b1af6506651e82458dd8a2bd10ec'
```

Code and configs are coming soon.