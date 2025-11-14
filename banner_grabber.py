# banner_grabber.py
import socket
import sys

def banner_grabber(host, port):
    """Connects to a host:port and grabs the service banner."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        
        # Connect to the target
        s.connect((host, port))
        
        # Send a standard HTTP GET request if port is 80 or 443 
        # Otherwise, just listen for the response
        if port in [80, 443]:
            s.send(b'GET / HTTP/1.1\r\nHost: ' + host.encode() + b'\r\n\r\n')
            
        banner = s.recv(1024).decode(errors='ignore')
        
        print(f"\n[+] Banner received from {host}:{port}:")
        print("---------------------------------------")
        print(banner.strip())
        print("---------------------------------------")
        
        s.close()
        
    except ConnectionRefusedError:
        print(f"[-] Connection refused by {host} on port {port}.")
    except socket.timeout:
        print(f"[-] Connection timed out for {host}:{port}.")
    except Exception as e:
        print(f"[-] An error occurred: {e}")
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

if __name__ == "__main__":
    target_host = input("Enter the target IP or hostname: ")
    try:
        target_port = int(input("Enter the target port (e.g., 80, 21, 22): "))
    except ValueError:
        print("Invalid port number.")
        sys.exit(1)

    banner_grabber(target_host, target_port)
