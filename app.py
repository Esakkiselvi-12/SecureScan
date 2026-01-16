from flask import Flask, render_template, request
import socket

app = Flask(__name__)

# Common ports & services (demo purpose)
PORTS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL"
}

# ------------------ PORT SCAN FUNCTION ------------------
def scan_ports(target):
    open_ports = []

    for port, service in PORTS.items():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))

            if result == 0:
                open_ports.append(f"Port {port} ({service}) is OPEN")

            s.close()
        except:
            pass

    return open_ports


# ------------------ HOME PAGE ------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    target = None

    if request.method == "POST":
        target = request.form.get("target")

        try:
            ip = socket.gethostbyname(target)
            ports = scan_ports(ip)

            result = {
                "ip": ip,
                "ports": ports if ports else ["No common open ports found"]
            }

        except:
            result = {
                "ip": "Invalid Target",
                "ports": []
            }

    return render_template("index.html", result=result, target=target)


# ------------------ CONTACT PAGE ------------------
@app.route("/contact", methods=["GET", "POST"])
def contact():
    success = False

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Demo: print to terminal
        print("\n--- Contact Form Submitted ---")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)
        print("-----------------------------\n")

        success = True

    return render_template("contact.html", success=success)


# ------------------ APP RUN ------------------
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
