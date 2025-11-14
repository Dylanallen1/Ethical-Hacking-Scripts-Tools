import socket
import sys

def scan_port(host, port):
    """Attempts to connect to a specific port on a given host."""
    try:
        # Create a socket object (AF_INET for IPv4, SOCK_STREAM for TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Set a timeout of 1 second

        # Attempt to connect to the target port
        result = s.connect_ex((host, port)) 
        
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is closed or filtered")
        
        s.close()
    
    except socket.error as e:
        print(f"Error connecting: {e}")
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

if __name__ == "__main__":
    target_host = input("Enter the target IP or hostname (e.g., 127.0.0.1): ")
    target_port = int(input("Enter the port number to scan (e.g., 80): "))

    print(f"\n--- Scanning {target_host} ---")
    scan_port(target_host, target_port)
