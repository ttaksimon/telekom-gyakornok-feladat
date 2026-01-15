import os
from ncclient import manager
import xml.dom.minidom as xml


def print_menu():
    """
    Docstring for print_menu

    :return: None
    """

    print("\n" + "="*40)
    print("Cisco NetConf Manager - CLI Tool")
    print("\n" + "="*40)
    print("1. [READ] Get interface configuration")
    print("2. [READ] Get interface statistics")
    print("3. [UPDATE] Create a new Loopback interface")
    print("4. [UPDATE] Update interface description")
    print("5. [UPDATE] Set MTU on an interface")
    print("6. [UPDATE] Enable an interface")
    print("7. [UPDATE] Disable an interface")
    print("8. [DELETE] Delete an interface")
    print("0. Exit")
    print("-"*40)


def print_interface_types():
    """
    Print available interface types.

    :return: None
    """
    print("-"*40)
    print("1 - GigabitEthernet (default)")
    print("2 - Loopback")
    print("3 - TenGigabitEthernet")
    print("4 - MgmtEthernet")
    print("5 - Vlan")
    print("6 - Tunnel")
    print("0 - Vissza a főmenübe")
    print("-"*40)


def get_connection(host_ip, port, username, password):
    """
    Establish and return a NETCONF connection to the network device.

    :param host_ip:  IP address of the network device
    :param port:     NETCONF port number
    :param username: Username for authentication
    :param password: Password for authentication
    :return:         NETCONF manager object
    """ 

    return manager.connect(
        host=host_ip,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False, # Disable host key verification
        device_params={'name': 'iosxe'},
        allow_agent=False,
        look_for_keys=False
    )


def pretty_print_xml(xml_string):
    """
    Pretty print XML string for better readability.

    :param xml_string: XML string to be pretty printed
    :return:           None
    """
    try:
        parsed = xml.parseString(xml_string)
        print(parsed.toprettyxml())
    except Exception as e:
        print(f"Error pretty printing XML: {e}")
        print(xml_string)


def clear_screen():
    """
    Clear the console screen.

    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')