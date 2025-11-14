# mac_changer.py
import subprocess
import optparse
import re

def get_arguments():
    """Handles command-line arguments for the script."""
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address to set")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for info.")
    if not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for info.")
    return options

def change_mac(interface, new_mac):
    """Changes the MAC address of the specified network interface."""
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    
    # Use subprocess to execute system commands
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    
    print(f"[+] MAC address changed successfully.")

def get_current_mac(interface):
    """Retrieves the current MAC address of the specified interface."""
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode()
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")
        return None

if __name__ == "__main__":
    options = get_arguments()
    
    current_mac = get_current_mac(options.interface)
    if current_mac:
        print(f"[*] Current MAC: {current_mac}")
        
    change_mac(options.interface, options.new_mac)
    
    final_mac = get_current_mac(options.interface)
    if final_mac == options.new_mac:
        print(f"[+] New MAC address is {final_mac}")
    else:
        print("[-] MAC address change failed.")
