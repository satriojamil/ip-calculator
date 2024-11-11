from datetime import datetime

def save_calculation(ip_address, netmask, results):
    """Save calculation results to a text file"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open('ip_calc_history.txt', 'a') as f:
        f.write("\n" + "="*50 + "\n")
        f.write(f"Time: {timestamp}\n")
        f.write(f"IP Address: {ip_address}\n")
        f.write(f"Netmask: {netmask}\n")
        f.write("Results:\n")
        for key, value in results.items():
            f.write(f"{key}: {value}\n")
        f.write("="*50 + "\n")

def view_history():
    """Display calculation history"""
    try:
        with open('ip_calc_history.txt', 'r') as f:
            print("\n============= Calculation History =============")
            print(f.read())
    except FileNotFoundError:
        print("\nNo calculation history found.")

# Input The IP Address and Prefix 
def get_user_input():
    while True:
        print("\n============================================")
        print("1. Calculate new IP")
        print("2. View history")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            print("============================================")
            netmask = int(input("Input Netmask = "))
            ip_address = input("Input IP Address = ")
            return netmask, ip_address
        elif choice == '2':
            view_history()
        elif choice == '3':
            exit()
        else:
            print("Invalid choice. Please try again.")

#Function for Sum IP Address
def sumIP(x):
    jumlahIP = 2**(32-x)
    return jumlahIP

# Function for Calculate The Subnetmask like 255.255.255.0 --> /24
def subnetting(x):
    subnetmask = 256 - x
    return f'255.255.255.{subnetmask}'

# Function for Calculate Network Address from The Particular Network
def network_broadcast_IP(x, jumlahIP):
    Networks = x.split('.')
    Network = int(Networks[3])
    if Network < jumlahIP:
        Networks.insert(3,0)
        Networks.pop()
        octetNet = ""
        for i in Networks:
            octetNet += (str(i) + '.')
        return octetNet[:-1]
    else:
        operation = (int(Networks[3]) // jumlahIP) * jumlahIP
        Networks.insert(3,operation)
        Networks.pop()
        octetNet = ""
        for i in Networks:
            octetNet += (str(i) + '.')
        return octetNet[:-1]

# Function for Calculate Broadcast Address from The Particular Network
def broadcastIP(x, jumlahIP):
    Network = x.split('.')
    Networks = int(Network[3])
    Broadcast = Networks + jumlahIP - 1
    Network.insert(3,Broadcast)
    Network.pop()
    octetBroad = ''
    for i in Network:
        octetBroad += (str(i) + '.')
    return octetBroad[:-1]

def rangeIP(first, last):
    firstRange = first.split('.')
    lastRange = last.split('.')

    firstIP = int(firstRange[3]) + 1
    lastIP = int(lastRange[3]) - 1

    # Insert the first IP for Range Host
    firstRange.insert(3,firstIP)
    firstRange.pop()
    firstRangeHost = ''
    for i in firstRange:
        firstRangeHost += (str(i) + '.')

    # Insert the last IP for Range Host
    lastRange.insert(3,lastIP)
    lastRange.pop()
    lastRangeHost = ''
    for i in lastRange:
        lastRangeHost += (str(i) + '.')

    return {
        'full_range': f"{first} - {last}",
        'host_range': f"{firstRangeHost[:-1]} - {lastRangeHost[:-1]}"
    }

def main():
    while True:
        netmask, ip_address = get_user_input()
        
        # Calculate results
        jumlahIP = sumIP(netmask)
        subnet = subnetting(jumlahIP)
        network = network_broadcast_IP(ip_address, jumlahIP)
        broadcast = broadcastIP(network, jumlahIP)
        range_ips = rangeIP(network, broadcast)
        
        # Prepare results dictionary
        results = {
            'Total IP': jumlahIP,
            'Subnetmask': subnet,
            'Network Address': network,
            'Broadcast Address': broadcast,
            'Range IP': range_ips['full_range'],
            'Range Host': range_ips['host_range']
        }
        
        # Display results
        print("\n============================================")
        for key, value in results.items():
            print(f"{key}: {value}")
        print("============================================")
        
        # Save calculation to history
        save_calculation(ip_address, netmask, results)

if __name__ == "__main__":
    main()
