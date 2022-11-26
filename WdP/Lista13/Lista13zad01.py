def format_bytes(bytes_):
    """Prints out the number of bytes formatted as a sum of GB, MB, kB and bytes"""
    if bytes_ // (1024 ** 3) > 1023:
        print("Too much bytes to process")
    else:
        giga = bytes_ // 1024**3
        mega = (bytes_ % 1024**3) // 1024**2
        kilo = ((bytes_ % 1024**3) % 1024**2) // 1024
        remainder = ((bytes_ % 1024**3) % 1024**2) % 1024
        print(f"{giga} GB + {mega} MB + {kilo} kB + {remainder} bajtów")


format_bytes(9876543210)
