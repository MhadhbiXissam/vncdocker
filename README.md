# vncdocker

# Install vnc  : 
```bash
sudo apt-get update && apt-get install -y x11vnc xvfb novnc
```
# Run x11vnc and novnc from single command  : 
```bash
x11vnc_output=$(x11vnc -quiet -cursor -bg -localhost -nopw -forever -shared --multiptr) && port=$(echo "$x11vnc_output" | grep -oP 'PORT=\K\d+') && echo "PORT value: $port" && /usr/share/novnc/utils/launch.sh --vnc localhost:$port
```


# run boths eperatly : 

## Run vnc server : 
```bash
x11vnc -quiet -cursor  -bg -localhost -nopw -forever -shared -rfbport 5900 --multiptr 
```
## run novnc web client  : 
```bash
/usr/share/novnc/utils/launch.sh --vnc localhost:5900
```


# to avoid lang and keyboard settings  : 
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
