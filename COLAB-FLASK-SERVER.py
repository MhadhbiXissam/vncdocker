import requests , time , IPython , threading
from IPython.display import clear_output
import socket , os

def get_available_port():
    # Create a socket using the IPv4 address family and TCP protocol
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind to a port of value 0 which allows the OS to assign an available port
    sock.bind(('localhost', 0))

    # Retrieve the port number assigned by the OS
    port = sock.getsockname()[1]

    # Close the socket
    sock.close()

    return port

# Example usage
available_port = get_available_port()
os.environ["AVAILABLEPORT"] = str(available_port)

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']
clear_output()
public_ip = get_public_ip()
print(public_ip)

!npm install -g localtunnel
!nohup lt --port $AVAILABLEPORT > localtunnel.log 2>&1 &


time.sleep(5)
loacl_tunnel_url = None
with open('localtunnel.log') as log :
    loacl_tunnel_url = log.read().strip().split()[-1]



!pip install flask

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from your Colab server!"

def run_flask_app():
    app.run(host='0.0.0.0', port=available_port, debug=False)

# Create a daemonized thread to run the Flask app
flask_thread = threading.Thread(target=run_flask_app)
flask_thread.daemon = True
flask_thread.start()

from IPython.display import HTML

html_content = f"""

<div style="width: 100% , padding:12 ; display: flex;justify-content: center; ">
    <button id="copyButton" onclick="copyToClipboard()" style="width: 100%;margin: 12px ; padding: 12px">Copy Ip address</button>
    <script>
        function copyToClipboard() {{

            navigator.clipboard.writeText("{public_ip}") ; 
        }}
    </script>
</div>
"""

clear_output(wait= True)
display(HTML(html_content))
IPython.display.IFrame(loacl_tunnel_url,'100%','900')