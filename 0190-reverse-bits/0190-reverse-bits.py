class Solution:
    def reverseBits(self, n: int) -> int:
        # Format n as a 32-bit binary string (pads with leading zeros, no '0b')
        binary_string = bin(n)[2:].zfill(32)
        
        # Reverse the binary string
        reversed_binary_string = binary_string[::-1]

        # Convert the reversed binary string back to an integer
        number = int(reversed_binary_string, 2)

        return number