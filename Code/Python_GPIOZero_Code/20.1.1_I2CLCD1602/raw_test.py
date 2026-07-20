import smbus
import time

# Force connection to I2C bus 1 and address 0x22
bus = smbus.SMBus(1)
ADDR = 0x22


def send_byte(data, mode):
    """
    mode = 0 for commands (like clear screen)
    mode = 1 for data (like letters)
    """
    # Bitmask: Backlight ON (0x08)
    high_bits = (data & 0xF0) | mode | 0x08
    low_bits = ((data << 4) & 0xF0) | mode | 0x08

    # Send high nibble (Enable bit high, then low)
    bus.write_byte(ADDR, high_bits | 0x04)
    time.sleep(0.001)
    bus.write_byte(ADDR, high_bits & ~0x04)

    # Send low nibble (Enable bit high, then low)
    bus.write_byte(ADDR, low_bits | 0x04)
    time.sleep(0.001)
    bus.write_byte(ADDR, low_bits & ~0x04)


print("Forcing I2C connection and sending raw init data...")

try:
    # 1. Raw Initialization Sequence
    send_byte(0x33, 0)  # Force 8-bit mode
    send_byte(0x32, 0)  # Force 4-bit mode
    send_byte(0x28, 0)  # 2 lines, 5x7 matrix
    send_byte(0x0C, 0)  # Display ON, Cursor OFF
    send_byte(0x01, 0)  # Clear Display
    time.sleep(0.01)   # Wait for clear to finish

    # 2. Print "TEST"
    send_byte(ord('T'), 1)
    send_byte(ord('E'), 1)
    send_byte(ord('S'), 1)
    send_byte(ord('T'), 1)

    print("Data sent! Check the screen.")

except Exception as e:
    print(f"Communication failed: {e}")
