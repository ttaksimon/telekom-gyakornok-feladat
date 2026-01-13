from ncclient import manager
import sys


def netconf_client():
    host_ip = input("Enter the device IP address: ")
    username = input("Username: ")
    password = input("Password: ")

    port = 830 # Default NETCONF port

    try:
        # Establish a NETCONF session
        with manager.connect(
            host=host_ip,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False, # Disable host key verification
            device_params={'name': 'iosxe'},
            allow_agent=False,
            look_for_keys=False,
            timeout=60
        ) as m:
            print("NETCONF session established successfully.")
            print("Downloading running configuration...")

            response = m.get_config(source='running')

            print("\n--- Answer from the device ---")
            print(response.data_xml)
    except Exception as e:
        print(f"An error occurred: {e}")
    

if __name__ == "__main__":
    if "ncclient" not in sys.modules:
        try:
            import ncclient
        except ImportError:
            print("Error: ncclient library is not installed.")
            print("Please install it using: pip install ncclient.")
            sys.exit(1)

    netconf_client()
