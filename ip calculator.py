from datetime import datetime
import os

#Path the directory of file
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)
current_directory = os.getcwd()

''' USER INPUT, FILE HANDLING, DAN HISTORY '''
#Save calculation results to a text file
def save_calculation(ip_address, netmask, results):
    #timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open('ip_calc_history.txt', 'a') as f:
        f.write("\n" + "="*50 + "\n")
        #f.write(f"Time: {timestamp}\n")
        f.write(f"IP Address: {ip_address}\n")
        f.write(f"Netmask: {netmask}\n")
        f.write("Results:\n")
        for key, value in results.items():
            f.write(f"{key}: {value}\n")
        f.write("="*50 + "\n")

#Clear calculation results from a text file
def clear_history():
    f = open('ip_calc_history.txt', 'w')
    f.write('')

#Display calculation history
def view_history():
    try:
        with open('ip_calc_history.txt', 'r') as f:
            print("\n============= Calculation History =============")
            print(f.read())
    except FileNotFoundError:
        print("\nNo calculation history found.")

#Input The IP Address and Prefix 
def get_user_input():
    while True:
        print("\n============================================")
        print("1. Calculate new IP")
        print("2. View history")
        print("3. Clear history")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print("============================================")
            netmask = int(input("Input Netmask = "))
            ip_address = input("Input IP Address = ")
            if ip_address.count('.') != 3 or len(ip_address) > 15 or len(ip_address) < 7:
                continue
            else:
                return netmask, ip_address
        elif choice == '2':
            view_history()
        elif choice == '3':
            clear_history()
        elif choice == '4':
            exit()
        else:
            print("Invalid choice. Please try again.")


''' KALKULASI IP ADDRESS DAN SUBNETMASK '''
#Function for Sum IP Address for full IP and host IP
def sumIP(prefix):
    full_IP = 2**(32-prefix)
    host_IP = full_IP - 2
    return full_IP,host_IP

# Function for Calculate The Subnetmask (Class B and C) like 255.255.255.0 --> /24
def subnetting(full_IP,netmask):
    #Class C
    if netmask >= 24:
        subnetmask = 256 - full_IP
        return f'255.255.255.{subnetmask}'
    #Class B
    elif netmask < 24:
        subnetmask = 256 - (full_IP // 256)
        return f'255.255.{subnetmask}.0'

# Function for Calculate Network Address from The Particular Network
def network_broadcast_IP(x, jumlahIP):
    #Class C
    if jumlahIP <= 256:
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
    #Class B
    else:
        Networks = x.split('.')
        Network = int(Networks[2])
        if Network < (jumlahIP / 256):
            Networks.insert(2,0)
            Networks.insert(3,0)
            del Networks[4:]
            octetNet = ""
            for i in Networks:
                octetNet += (str(i) + '.')
            return octetNet[:-1]
        else:
            jumlahIP = jumlahIP // 256
            operation = (int(Networks[3]) // jumlahIP) * jumlahIP
            Networks.insert(2,operation)
            Networks.insert(3,0)
            del Networks[4:]
            octetNet = ""
            for i in Networks:
                octetNet += (str(i) + '.')
            return octetNet[:-1]

# Function for Calculate Broadcast Address from The Particular Network
def broadcastIP(x, jumlahIP):
    #Class C
    if jumlahIP <= 256:
        Network = x.split('.')
        Networks = int(Network[3])
        Broadcast = Networks + jumlahIP - 1
        Network.insert(3,Broadcast)
        Network.pop()
        octetBroad = ''
        for i in Network:
            octetBroad += (str(i) + '.')
        return octetBroad[:-1]
    #Class B
    else:
        Network = x.split('.')
        Networks = int(Network[2])
        Broadcast = Networks + (jumlahIP // 256) - 1
        Network.insert(2,Broadcast)
        Network.insert(3,255)
        del Network[4:]
        octetBroad = ''
        for i in Network:
            octetBroad += (str(i) + '.')
        return octetBroad[:-1]

def rangeIP(first, last, netmask):
    #Class C
    if netmask >= 24:
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
    #Class B
    else:
        firstRange = first.split('.')
        lastRange = last.split('.')

        firstIP = int(firstRange[2]) + 1
        lastIP = int(lastRange[2]) - 1

        # Insert the first IP for Range Host
        firstRange.insert(2,firstIP)
        firstRange.insert(3,254)
        del firstRange[4:]
        firstRangeHost = ''
        for i in firstRange:
            firstRangeHost += (str(i) + '.')

        # Insert the last IP for Range Host
        lastRange.insert(2,lastIP)
        lastRange.insert(3,254)
        del lastRange[4:]
        lastRangeHost = ''
        for i in lastRange:
            lastRangeHost += (str(i) + '.')

        return {
            'full_range': f"{first} - {last}",
            'host_range': f"{firstRangeHost[:-1]} - {lastRangeHost[:-1]}"
        }



''' RUN PROGRAM UTAMA '''
def main():
    while True:
        netmask, ip_address = get_user_input()
        # Calculate results
        full_IP, host_IP = sumIP(netmask)
        subnet = subnetting(full_IP,netmask)
        network = network_broadcast_IP(ip_address, full_IP)
        broadcast = broadcastIP(network, full_IP)
        range_ips = rangeIP(network, broadcast, netmask)
        
        # Prepare results dictionary
        results = {
            'Total IP': full_IP,
            'Total Host': host_IP,
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
