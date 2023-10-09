# install udocker 
```bash
pip install udocker
udocker --allow-root install
udocker --allow-root --help
```

# pull image  : 
```bash
udocker  --allow-root pull nvidia/cuda:11.8.0-runtime-ubuntu18.04
```
# create container  : 
```bash
!udocker  --allow-root create --name=ubuntu nvidia/cuda:11.8.0-runtime-ubuntu18.04
```bash
