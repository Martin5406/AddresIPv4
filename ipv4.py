class AddressIPv4:
    def __init__(self, address: str):
        self.set(address)
    
    def isValid(self) -> bool:
        octets = self.address.split('.')
        if len(octets) != 4:
            return False
        for octet in octets:
            if not octet.isdigit() or not (0 <= int(octet) <= 255):
                return False
        return True
    
    def set(self, address: str):
        self.address = address
        if not self.isValid():
            raise ValueError(f"Neplatná IPv4 adresa: {address}")
        return self
    
    def getAsString(self) -> str:
        return self.address
    
    def getAsInt(self) -> int:
        octets = map(int, self.address.split('.'))
        return (next(octets) << 24) + (next(octets) << 16) + (next(octets) << 8) + next(octets)
    
    def getAsBinaryString(self) -> str:
        return '.'.join(f"{int(octet):08b}" for octet in self.address.split('.'))
    
    def getOctet(self, number: int) -> int:
        if number < 1 or number > 4:
            raise ValueError("Číslo oktetu musí být mezi 1 a 4")
        return int(self.address.split('.')[number - 1])
    
    def getClass(self) -> str:
        first_octet = int(self.address.split('.')[0])
        if 1 <= first_octet <= 126:
            return 'A'
        elif 128 <= first_octet <= 191:
            return 'B'
        elif 192 <= first_octet <= 223:
            return 'C'
        elif 224 <= first_octet <= 239:
            return 'D'
        elif 240 <= first_octet <= 255:
            return 'E'
        else:
            return 'Neznámá'
    
    def isPrivate(self) -> bool:
        octets = list(map(int, self.address.split('.')))
        if (octets[0] == 10 or
            (octets[0] == 172 and 16 <= octets[1] <= 31) or
            (octets[0] == 192 and octets[1] == 168)):
            return True
        return False


ip = AddressIPv4("192.168.0.1")

print("Textová reprezentace:", ip.getAsString())
print("Je platná:", ip.isValid())
print("Číselná reprezentace:", ip.getAsInt())
print("Binární reprezentace:", ip.getAsBinaryString())
print("První oktet:", ip.getOctet(1))
print("Třída IP adresy:", ip.getClass())
print("Je privátní:", ip.isPrivate())

try:
    invalid_ip = AddressIPv4("256.256.256.256")
except ValueError as e:
    print(e)
