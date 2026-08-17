#!/usr/bin/ env python

import subprocess #module used to call commands
import optparse #module allows accepting command line arguments

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
    print("changing " + interface + " to " + new_mac)

    #subprocess executes the commands
    #each word in the list is a single word in the command (prevents command injection)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface,options.new_mac)

subprocess.call(["ifconfig"])





