def create_loopback_interface(m, loopback_id, ip_address, subnet_mask):
    """
    Create a Loopback interface with specified IP address and subnet mask.
    
    :param m:           NETCONF manager object
    :param loopback_id: ID of the Loopback interface (e.g., "101")
    :param ip_address:  IP address to assign to the Loopback interface
    :param subnet_mask: Subnet mask for the IP address
    :return:            None
    """

    config_payload = f"""
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <Loopback>
                    <name>{loopback_id}</name>
                    <description>Managed by Python NETCONF</description>
                    <ip>
                        <address>
                            <primary>
                                <address>{ip_address}</address>
                                <mask>{subnet_mask}</mask>
                            </primary>
                        </address>
                    </ip>
                </Loopback>
            </interface>
        </native>
    </config>
    """

    try:
        response = m.edit_config(target='running', config=config_payload)
        print(f"Loopback interface {loopback_id} created successfully.")
    except Exception as e:
        print(f"An error occurred while creating loopback interface: {e}")


def update_interface_description(m, interface_number, new_desc, interface_type="GigabitEthernet"):
    """
    Update the description of a specified interface.

    :param m:                NETCONF manager object
    :param interface_number: Name/number of the interface (e.g., "1")
    :param interface_type:   Type of the interface (e.g., GigabitEthernet)
    :param new_desc:         New description for the interface
    :return:                 None
    """

    config_payload = f"""
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <{interface_type}>
                    <name>{interface_number}</name>
                    <description>{new_desc}</description>
                </{interface_type}>
            </interface>
        </native>
    </config>
    """

    try:
        response = m.edit_config(target='running', config=config_payload)
        print("Interface description updated successfully.")
    except Exception as e:
        print(f"An error occurred while updating interface description: {e}")


def set_interface_mtu(m, interface_type, interface_number, mtu_size):
    """
    Set the MTU size for a specified interface.

    :param m:                NETCONF manager object
    :param interface_type:   Type of the interface (e.g., GigabitEthernet)
    :param interface_number: Name/number of the interface (e.g., "1")
    :param mtu_size:        MTU size to set
    :return:                 None
    """

    config_payload = f"""
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <{interface_type}>
                <name>{interface_number}</name>
                <mtu>{mtu_size}</mtu>
            </{interface_type}>
        </interface>
    </native>
    """

    try:
        response = m.edit_config(target='running', config=config_payload)
        print(f"MTU size for interface {interface_type} {interface_number} set to {mtu_size}.")
    except Exception as e:
        print(f"An error occurred while setting MTU size: {e}")


def enable_interface(m, interface_number, interface_type="GigabitEthernet"):
    """
    Enable a specified interface.

    :param m:                NETCONF manager object
    :param interface_number: Name/number of the interface (e.g., "1")
    :param interface_type:   Type of the interface (e.g., GigabitEthernet)
    :return:                 None
    """

    config_payload = f"""
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <{interface_type}>
                    <name>{interface_number}</name>
                    <shutdown operation="delete" />
                </{interface_type}>
            </interface>
        </native>
    </config>
    """

    try:
        response = m.edit_config(target='running', config=config_payload)
        print(f"Interface {interface_type} {interface_number} enabled successfully.")
    except Exception as e:
        print(f"An error occurred while enabling interface: {e}")


def disable_interface(m, interface_number, interface_type="GigabitEthernet"):
    """
    Disable a specified interface.

    :param m:                NETCONF manager object
    :param interface_number: Name/number of the interface (e.g., "1")
    :param interface_type:   Type of the interface (e.g., GigabitEthernet)
    :return:                 None
    """

    config_payload = f"""
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <{interface_type}>
                    <name>{interface_number}</name>
                    <shutdown />
                </{interface_type}>
            </interface>
        </native>
    </config>
    """

    try:
        response = m.edit_config(target='running', config=config_payload)
        print(f"Interface {interface_type} {interface_number} disabled successfully.")
    except Exception as e:
        print(f"An error occurred while disabling interface: {e}")