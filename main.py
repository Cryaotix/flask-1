from flask import Flask, jsonify
import os
import psutil

app = Flask(__name__)


@app.route('/')
def index():
    mac = get_mac_address()
    return jsonify({"Choo Choo": mac})


def get_mac_address():
    try:
        # Get a list of all network interfaces on the system
        interfaces = psutil.net_if_addrs()

        for interface_name, interface_addresses in interfaces.items():
            for address in interface_addresses:
                # Check if the address family is MAC address
                if address.family == psutil.AF_LINK:
                    return address.address
    except Exception as e:
        print("Error:", e)
    return None


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
