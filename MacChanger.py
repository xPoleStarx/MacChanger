import subprocess
import optparse
import re

def get_user_input():
    parseobject = optparse.OptionParser()
    parseobject.add_option("-i","--interface",dest="interface",help="For change MAC which one of the interface do you prefer")
    parseobject.add_option("-m","--mac",dest="mac_address",help="You need to enter the new MAC address")
    return parseobject.parse_args()

def check_macaddress(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None

def changeMacaddress(user_interface,user_macaddress):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_macaddress])
    subprocess.call(["ifconfig",user_interface,"up"])
    subprocess.call(["ifconfig",user_interface])

print("MacChanger is started!\n")
print("*******************************************************************")
(user_input,arguments) = get_user_input()
changeMacaddress(user_input.interface,user_input.mac_address)
final_mac = check_macaddress(user_input.interface)
print("*******************************************************************")

if final_mac == user_input.mac_address:
    print("MAC address was changed succesfully!")
else:
    print("MAC address wasn't changed, something got wrong")