# Input The IP Address and Prefix 
print("Anggota Kelompok : Jamil, Sabda, Radit")
print("============================================")
inputSubnet = int(input("Input Netmask = "))    # Input The IP Address
inputIP = input("Input IP Address = ")          # Input The Prefix
print("============================================")

#Function for Sum IP Address
def sumIP(x):
    jumlahIP = 2**(32-x)
    return jumlahIP


# Function for Calculate The Subnetmask like 255.255.255.0 --> /24
def subnetting(x):
    subnetmask = 256 - x
    print(f'Subnetmask      = 255.255.255.{subnetmask}')


# Function for Calculate Network and Broadcast Address from The Particular Network
def network_broadcast_IP(x):
    Networks = x.split('.')
    Network = int(Networks[3])
    if Network < jumlahIP:
        Networks.insert(3,0)
        Networks.pop()
        Network = int(Networks[3])
        Network = int(Networks[3])
        octetNet = ""
        for i in Networks:
            octetNet += (str(i) + '.')
        print(f"Network IP      = {octetNet[:-1]}")
    else:
        operation = (int(Networks[3]) // jumlahIP) * jumlahIP
        Networks.insert(3,operation)
        Networks.pop()
        Network = int(Networks[3])
        Network = int(Networks[3])
        octetNet = ""
        for i in Networks:
            octetNet += (str(i) + '.')
        print(f"Network IP      = {octetNet[:-1]}")

    Broadcast = Network + jumlahIP - 1
    Networks.insert(3,Broadcast)
    Networks.pop()
    octetBroad = ''
    for i in Networks:
        octetBroad += (str(i) + '.')
    print(f"Broadcast IP    = {octetBroad[:-1]}")

    host_bottom = Networks
    host_top = host_bottom
    bottomIP = Network + 1
    topIP = Broadcast - 1

    host_bottom.insert(3,bottomIP)
    host_bottom.pop()
    octetHostBottom = ''
    for i in host_bottom:
        octetHostBottom += (str(i) + '.')
    

    host_top.insert(3,topIP)
    host_top.pop()
    octetHostTop = ''
    for i in host_top:
        octetHostTop += (str(i) + '.')
    
    print(f"Range Host      = {octetHostBottom[:-1]} - {octetHostTop[:-1]}")
    print(f"Range IP        = {octetNet[:-1]} - {octetBroad[:-1]}")



# Start The Calculate 
jumlahIP = sumIP(inputSubnet)


# The Main Function That Print The Result of Calculate
def main():
    print("\n============================================")
    print(f"Total IP        = {jumlahIP}")
    subnet = subnetting(jumlahIP)
    network_broadcast_IP(inputIP)
    print("============================================")

# Run Result Function
main()