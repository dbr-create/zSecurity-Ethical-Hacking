#!/usr/bin/ env python

import subprocess #module used to call commands
import optparse #module allows accepting command line arguments
import re #allows for use of regular expressions

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface of which you intend to change the mac address")
    parser.add_option("-n", "--new_mac", dest="new_mac", help="new MAC address which you intend the interface to have")
    # 'dest' indicates the name of the var that the command arg is stored inm
    # 'help' gives a relevant help message for the given command arg when "--help" is used
    (options,arguments) = parser.parse_args()

    #error handling
    if not options.interface:
        parser.error("[-] Please specify an interface")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC address")
    return options

def change_mac(interface, new_mac):
    print("Changing " + interface + " to " + new_mac)

    #subprocess executes the commands
    #each word in the list is a single word in the command (prevents command injection)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_interface_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    result_mac = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if result_mac:
        return result_mac.group(0)
    else:
        print("[-] Could not read MAC address")

options = get_arguments()

curr_mac = get_interface_mac(options.interface)
print("Current MAC: " + str(curr_mac))

change_mac(options.interface,options.new_mac)

current_mac = get_interface_mac(options.interface)

if options.new_mac == current_mac:
    print("[+] MAC address was successfully changed to " + options.new_mac)
else:
    print("[-] MAC address change failure")





