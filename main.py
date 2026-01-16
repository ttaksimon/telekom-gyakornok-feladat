import sys
import utils
import config.interfaces as iface_types
import interface_ops.read as interface_read
import interface_ops.create as interface_create
import interface_ops.delete as interface_delete
from getpass import getpass # getpass can be used for hidden input


def main():
    print("--- SIGN IN ---")
    host_ip = input("Enter the device IP address: ")
    username = input("Username: ")
    password = input("Password: ")
    port = 830  # Default NETCONF port

    while True:
        try:
            # Establish a NETCONF session
            with utils.get_connection(
                host_ip,
                port,
                username,
                password
            ) as m:
                print("\nNETCONF session established successfully.")

                utils.print_menu()
                choice = input("Select an option: ")

                # Exit the program
                if choice == '0':
                    print("Exiting the program.")
                    break
                
                # Get interface configuration
                elif choice == '1':
                    utils.print_interface_types()
                    if_type = input("Select interface type: ")
                    if_name = input("Enter interface name/number (e.g., 1): ")
                    interface_read.get_interface_config(
                        m, 
                        interface_type=iface_types.interfaces.get(if_type, "GigabitEthernet"), 
                        interface_number=if_name
                    )

                # Get interface statistics
                elif choice == '2':
                    utils.print_interface_types()
                    if_type = input("Select interface type: ")
                    if_name = input("Enter interface name/number (e.g., 1): ")
                    if_type_str = iface_types.interfaces.get(if_type, "GigabitEthernet")
                    interface_read.get_interface_stats(
                        m, 
                        interface_number=f"{if_type_str}{if_name}"
                    )

                # Create new Loopback interface
                elif choice == '3':
                    loopback_id = input("Enter Loopback ID (e.g., 101): ")
                    ip_address = input("Enter IP address (e.g., 192.168.1.1): ")
                    subnet_mask = input("Enter Subnet Mask (e.g., 255.255.255.0): ")
                    interface_create.create_loopback_interface(
                        m,
                        loopback_id,
                        ip_address,
                        subnet_mask
                    )

                # Update interface description
                elif choice == '4':
                    utils.print_interface_types()
                    if_type = input("Select interface type: ")
                    if_name = input("Enter interface name/number (e.g., 1): ")
                    new_desc = input("Enter new description: ")
                    interface_create.update_interface_description(
                        m,
                        interface_type=iface_types.interfaces.get(if_type, "GigabitEthernet"),
                        interface_number=if_name,
                        new_desc=new_desc
                    )

                # Set MTU on an interface
                elif choice == '5':
                    utils.print_interface_types()
                    if_type = input("Select interface type: ")
                    if_name = input("Enter interface name/number (e.g., 1): ")
                    mtu_value = int(input("Enter MTU value (e.g., 1500): "))
                    interface_create.set_interface_mtu(
                        m,
                        interface_type=iface_types.interfaces.get(if_type, "GigabitEthernet"),
                        interface_number=if_name,
                        mtu_size=mtu_value
                    )

                # Enable an interface
                elif choice == '6':
                    utils.print_interface_types()
                    if_type = input("Select interface type: ")
                    if_name = input("Enter interface name/number (e.g., 1): ")
                    interface_create.enable_interface(
                        m,
                        interface_type=iface_types.interfaces.get(if_type, "GigabitEthernet"),
                        interface_number=if_name
                    )

                # Disable an interface
                elif choice == '7':
                    utils.print_interface_types()
                    if_type = input("Select interface type: ")
                    if_name = input("Enter interface name/number (e.g., 1): ")
                    interface_create.disable_interface(
                        m,
                        interface_type=iface_types.interfaces.get(if_type, "GigabitEthernet"),
                        interface_number=if_name
                    )

                # Delete an interface
                elif choice == '8':
                    utils.print_interface_types()
                    if_type = input("Select interface type: ")
                    if_name = input("Enter interface name/number (e.g., 1): ")
                    interface_delete.delete_interface(
                        m,
                        interface_type=iface_types.interfaces.get(if_type, "GigabitEthernet"),
                        interface_number=if_name
                    )

                else:
                    print("Invalid choice. Please select a valid option.")

            input("\nPress Enter to continue...")
            utils.clear_screen()
                    
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    

if __name__ == "__main__":
    if "ncclient" not in sys.modules:
        try:
            import ncclient
        except ImportError:
            print("Error: ncclient library is not installed.")
            print("Please install it using: pip install ncclient.")
            sys.exit(1)

    main()
