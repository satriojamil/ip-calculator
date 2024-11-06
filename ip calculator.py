# Input The IP Address and Prefix 
print("============================================")
inputSubnet = int(input("Input Netmask = "))    # Input The IP Address
inputIP = input("Input IP Address = ")          # Input The Prefix
print("============================================")

#Function for Sum IP Address
def sumIP(x):
    jumlahIP = 2**(32-x)
    return jumlahIP

# Function for Calculate The Subnetmask Class 'C' like 255.255.255.0 --> /24
def subnetmaskC(x):
    subnetmask = 256 - x
    return f'Subnetmask      = 255.255.255.{subnetmask}'

# Function for Calculate The Subnetmask Class 'B' like 255.255.0.0 --> /16
def subnetmaskB(x):
    prefix = inputSubnet + 8
    subnetmask = 256 - (sumIP(prefix))
    return f'Subnetmask      = 255.255.{subnetmask}.0'


# Function for Calculate Network Address from The Particular Network
def networkIP(x):
    Networks = x.split('.')
    Network = int(Networks[3])
    sumip = sumIP(inputSubnet)
    if Network < sumip:
        Networks.insert(3,0)
        Networks.pop()
        octetNet = ""
        for i in Networks:
            octetNet += (str(i) + '.')
        return octetNet[:-1]
    else:
        operation = (int(Networks[3]) // sumip) * sumip
        Networks.insert(3,operation)
        Networks.pop()
        octetNet = ""
        for i in Networks:
            octetNet += (str(i) + '.')
        return octetNet[:-1]
network = networkIP(inputIP)


# Function for Calculate Broadcast Address from The Particular Network
def broadcastIP(x):
    Network = x.split('.')
    Networks = int(Network[3])
    sumip = sumIP(inputSubnet)
    Broadcast = Networks + sumip - 1
    Network.insert(3,Broadcast)
    Network.pop()
    octetBroad = ''
    for i in Network:
        octetBroad += (str(i) + '.')
    return octetBroad[:-1]
broadcast = broadcastIP(network)

def rangeIP(first,last):
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

    return f"Range IP = {first} - {last}\nRange Host = {firstRangeHost[:-1]} - {lastRangeHost[:-1]}"
RangeIP = rangeIP(network,broadcast)

# Start The Calculate 
if inputSubnet >= 24:
    jumlahIP = sumIP(inputSubnet)
    subnet = subnetmaskC(jumlahIP)
else:
    subnet = subnetmaskB(inputSubnet)


# The Main Function That Print The Result of Calculate
def main():
    print("\n============================================")
    print(f"Total IP        = {jumlahIP}")
    print(subnet)
    print(network)
    print(broadcast)
    print(RangeIP)
    print("============================================")

# Run Result Function
main()
