# vncdocker

# Install vnc  : 
```bash
sudo apt-get install novnc
```
## Run vnc server : 
```bash
x11vnc -quiet -cursor  -bg -localhost -nopw -forever -shared -rfbport 5901 --multiptr 
```
# run novnc web client  : 
```bash
/usr/share/novnc/utils/launch.sh --vnc localhost:5901
```
