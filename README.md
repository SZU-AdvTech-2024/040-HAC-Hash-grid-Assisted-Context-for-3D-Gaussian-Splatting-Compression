# HAC
参考论文
```bibtex
@inproceedings{hac2024,
  title={HAC: Hash-grid Assisted Context for 3D Gaussian Splatting Compression},
  author={Chen, Yihang and Wu, Qianyi and Lin, Weiyao and Harandi, Mehrtash and Cai, Jianfei},
  booktitle={European Conference on Computer Vision},
  year={2024}
}
```

## 搭建环境
1. Unzip files
```
cd submodules
unzip diff-gaussian-rasterization.zip
unzip gridencoder.zip
unzip simple-knn.zip
unzip arithmetic.zip
cd ..
```
1. Install environment
```
conda env create --file environment.yml
conda activate HAC_env
```

## 构造数据集

输入数据集文件结构应该如下：

```
data/
├── dataset_name
│   ├── scene1/
│   │   ├── images
│   │   │   ├── IMG_0.jpg
│   │   │   ├── IMG_1.jpg
│   │   │   ├── ...
│   │   ├── sparse/
│   │       └──0/
│   ├── scene2/
│   │   ├── images
│   │   │   ├── IMG_0.jpg
│   │   │   ├── IMG_1.jpg
│   │   │   ├── ...
│   │   ├── sparse/
│   │       └──0/
...
```
## Training
 ```
 python train.py -s /data --eval --lod 0 --voxel_size 0.001 --update_init_factor 16 --iterations 30_000 -m outputs --lmbda {lmbda}
 ```
