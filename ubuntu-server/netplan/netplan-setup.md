# ⚙️ Netplan Setup

This folder contains Netplan configuration files used on my Ubuntu Server laptop.

The laptop runs Ubuntu Server and uses a **Broadcom BCM43142** wireless chipset, which is very difficult to get working on Linux. These configuration files allow network connectivity via USB tethering or Wi-Fi (once the Broadcom drivers are installed).

## Files

- `usb-tethering.yaml`: Configuration for connecting via USB tethering (e.g., using a mobile phone).
- `wifi-connection.yaml`: Configuration for connecting to a Wi-Fi network after installing Broadcom drivers.

## Usage

Copy the desired file to `/etc/netplan/`, then test and apply the configuration:

```bash
sudo cp <file>.yaml /etc/netplan/
sudo netplan try
sudo netplan apply
```
