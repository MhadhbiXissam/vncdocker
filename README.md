# vncdocker

# Install vnc  : 
```bash
sudo apt-get install novnc
```
## Run vnc server : 
```bash
x11vnc -quiet -cursor  -bg -localhost -nopw -forever -shared -rfbport 5900 --multiptr 
```
# run novnc web client  : 
```bash
/usr/share/novnc/utils/launch.sh --vnc localhost:5900
```
" to avoid lang and keyboard settings  : 
```bash
FROM ubuntu:latest

RUN apt-get update && apt-get install -y tzdata && \
    echo "tzdata tzdata/Areas select Europe" | debconf-set-selections && \
    echo "tzdata tzdata/Zones/Europe select Berlin" | debconf-set-selections && \
    dpkg-reconfigure -f noninteractive tzdata
RUN apt-get update &&  apt-get install -y \
    keyboard-configuration && \
    echo "keyboard-configuration keyboard-configuration/layoutcode string us" | debconf-set-selections && \
    echo "keyboard-configuration keyboard-configuration/xkb-keymap select us" | debconf-set-selections && \
    dpkg-reconfigure -f noninteractive keyboard-configuration

```
