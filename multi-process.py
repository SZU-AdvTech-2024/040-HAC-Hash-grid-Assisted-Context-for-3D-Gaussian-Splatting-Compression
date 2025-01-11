import os
# scenes = ['bicycle', 'garden', 'stump', 'room', 'counter', 'kitchen', 'bonsai', 'flowers', 'treehill']
scenes = ['flowers']
for lmbda in [0.004]:  # Optionally, you can try: 0.003, 0.002, 0.001, 0.0005
    for cuda, scene in enumerate(scenes):
        one_cmd = f'CUDA_VISIBLE_DEVICES={0} python train.py -s /data/share/NVS-Datasets/MipNeRF360/{scene} --eval --lod 0 --voxel_size 0.001 --update_init_factor 16 --iterations 30_000 -m outputs/mipnerf360/{scene}/{lmbda} --lmbda {lmbda}'
        os.system(one_cmd)