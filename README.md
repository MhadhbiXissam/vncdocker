# if you want when ever open terminal , the terminal use docker as shared volume with local machine  : 
# add to ~/.bashrc 
```bash
docker run -w /home --rm --name $(basename $(pwd))  -it  -v $(pwd):/home  ubuntu:20.04  bash

```
