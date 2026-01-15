import utils


def get_interface_config(m, interface_number, interface_type="GigabitEthernet"):
    """
    Retrieve and print the configuration of a specified interface type and name.

    :param m:              NETCONF manager object
    :param interface_number: Name/number of the interface (e.g., "1", "101")
    :param interface_type: Type of the interface (e.g., GigabitEthernet, Loopback)
    :return:               None
    """

    # Build the filter for the interface configuration
    if interface_number:
        filter_xml = f"""
        <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <interface>
                    <{interface_type}>
                        <name>{interface_number}</name>
                    </{interface_type}>
                </interface>
            </native>
        </filter>
        """
    else:
        filter_xml = """
        <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <interface>
                    <{interface_type} />
                </interface>
            </native>
        </filter>
        """

    try:
        response = m.get_config(source='running', filter=filter_xml)

        # Handle empty data response
        if "<data />" in response.data_xml or "<data xmlns" in response.data_xml and \
            "/>" in response.data_xml.split(">")[-1]:
            pass

        utils.pretty_print_xml(response.data_xml)
    except Exception as e:
        print(f"An error occurred while fetching interface configuration: {e}")


def get_interface_stats(m, interface_number):
    """
    Retrieve and print the statistics of a specified interface.

    :param m:                NETCONF manager object
    :param interface_number: Name/number of the interface (e.g., "1")
    :return:                 None
    """
    
    filter_xml = f"""
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces-state xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <interface>
                <name>{interface_number}</name>
            </interface>
        </interfaces-state>
    </filter>
    """

    try:
        response = m.get(filter=filter_xml)
        utils.pretty_print_xml(response.data_xml)
    except Exception as e:
        print(f"An error occurred while fetching interface statistics: {e}")