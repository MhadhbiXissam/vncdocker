# vncdocker

# Install vnc  : 
```bash
sudo apt-get install novnc
```
## Run vnc : 
```bash
nohup sudo x11vnc -display :0 -forever -shared -rfbport 5901 &
/usr/share/novnc/utils/launch.sh --vnc localhost:5901
```
