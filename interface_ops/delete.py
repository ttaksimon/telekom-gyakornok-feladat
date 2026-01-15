def delete_interface(m, interface_type, interface_number):
    """
    Delete a specified interface.
    
    :param m:                NETCONF manager object
    :param interface_type:   Type of the interface (e.g., GigabitEthernet)
    :param interface_number: Name/number of the interface (e.g., "1")
    :return:                 None
    """

    config_payload = f"""
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <{interface_type} operation="delete">
                    <name>{interface_number}</name>
                </{interface_type}>
            </interface>
        </native>
    </config>
    """

    try:
        response = m.edit_config(target='running', config=config_payload)
        print(f"Interface {interface_type} {interface_number} deleted successfully.")
    except Exception as e:
        print(f"An error occurred while deleting interface: {e}")