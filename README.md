# vncdocker
# run all from single command  : 
```bash
sudo apt-get update && apt-get install -y x11vnc xvfb novnc && port_to_check=6080; pid=$(lsof -t -i:$port_to_check); if [ -n "$pid" ]; then echo "Process using port $port_to_check found with PID: $pid"; kill $pid; echo "Process with PID $pid terminated."; else echo "No process found using port $port_to_check."; fi && x11vnc_output=$(x11vnc -quiet -cursor -bg -localhost -nopw -forever -shared --multiptr) && port=$(echo "$x11vnc_output" | grep -oP 'PORT=\K\d+') && echo "PORT value: $port" && /usr/share/novnc/utils/launch.sh --vnc localhost:$port

```

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
# on none display machines  : 
```bash
Xvfb :1 -screen 0 1024x768x16 & fluxbox & x11vnc -display :1  -quiet -cursor  -bg -localhost -nopw -forever -shared --multiptr -create
```
# kill any process that uses port 6080 : 
```bash
port_to_check=6080; pid=$(lsof -t -i:$port_to_check); if [ -n "$pid" ]; then echo "Process using port $port_to_check found with PID: $pid"; kill $pid; echo "Process with PID $pid terminated."; else echo "No process found using port $port_to_check."; fi
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
