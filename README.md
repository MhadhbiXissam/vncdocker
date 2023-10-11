# if you want when ever open terminal , the terminal use docker as shared volume with local machine  : 
# add to ~/.bashrc 
```bash
docker run -w /home --rm  -it  -v $(pwd):/home  <img>  bash


```

