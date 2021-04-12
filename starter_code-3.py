#!/usr/bin/python3
import socket
import base64
import binascii

port = 55349
ip = "challenge.acictf.com"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((ip, port))

f = sock.makefile()
    
for line in f:
    print(line)
    if line.startswith("-"):
        format = next(f).rstrip()
        print(format)
        src = format[:3]
        ans = format[7:]
        print("src line: " + src)
        print("ans line: " + ans)
        source_data = next(f)
        print("Source: " + source_data)
        border = next(f)
        
        # identify source type and convert to decimal
        
        if src == "hex":
            # from hex to dec
            decoded = int(source_data, 16)

        elif src == "dec":
            # remain as dec
            decoded = int(source_data)

        elif src == "oct":
            # from oct to dec
            decoded = int(source_data, 8)

        elif src == "bin":
            # from bin to dec
            decoded = int(source_data, 2)

        elif src == "b64":
            decoded_hex = base64.b64decode(source_data).hex()
            decoded = int(decoded_hex, 16)

        elif src == "raw":
            decoded = binascii.hexlify(bytes(source_data, "ascii"))
            decoded = decoded.decode("ascii")
            print(decoded)
            decoded = decoded[:-2]
            # decoded = "0x" + decoded
            decoded = int(decoded, 16)

        else:
            print("No src detected")

        print("Decoded: " + str(decoded))

        # Looks to encode the dec data
        if ans == "hex":
            # from dec to hex
            encoded = hex(int(decoded))[2:]

        elif ans == "dec":
            # remain as dec
            encoded = decoded             

        elif ans == "oct":
            # from dec to oct
            encoded = oct(int(decoded))[2:]

        elif ans == "bin":
            # from dec to bin
            encoded = bin(int(decoded))[2:]

        elif ans == "raw":
            # is this useful
            encoded = hex(int(decoded))[2:]
            encoded = bytes.fromhex(encoded)
            encoded = encoded.decode("ascii")
            
        
        elif ans == "b64":
            encoded = hex(int(decoded))[2:]
            encoded = bytes.fromhex(encoded)
            encoded = base64.b64encode(encoded)
            encoded = encoded.decode("ascii")

        else:
            encoded = "No ans"
            print("No ans detected")
        
        # Convert output to string
        encoded = str(encoded)

        print("Sending to Server - encoded: " + encoded)
        
        sock.send((encoded + "\n").encode())
          
    # raw = the unencoded ASCII string (contains only printable characters that are not whitespace)
    # b64 = standard base64 encoding (see 'base64' unix command)
    # hex = hex (base 16) encoding (case insensitive)
    # dec = decimal (base 10) encoding
    # oct = octal (base 8) encoding
    # bin = binary (base 2) encoding (should consist of ASCII '0' and '1')
    