# 🔍 Port Scanner

## 📝 Description
Port Scanner is a powerful network utility tool that helps you identify open and closed ports on your network devices. This tool provides real-time scanning capabilities for both websites and IP addresses, helping you assess network security vulnerabilities and potential breaches.

## ✨ Features
- 🌐 Website URL scanning
- 🔢 IP address scanning
- 📊 Well-known ports (0-1023) support
- 📈 Registered ports (1024-49150) support
- ⚡ Real-time results
- 🎨 Colored output for better visibility
- 📋 Service name identification
- ⏱️ Fast scanning with timeout control

## 🚀 Installation

### 📥 Prerequisites
- Python 3.x
- pip (Python package manager)

### ⚙️ Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/samrat-sarkar/Port_Scanner.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Port_Scanner
   ```

## 💻 Usage

### 🎮 Running the Application

#### Scan Ports using Website URL
```bash
python main.py url https://example.com/
```

#### Scan Ports using IP Address
```bash
python main.py ip 192.168.1.1
```

### 📋 Output Format
- 🟢 Green: Open ports with service names
- 🔴 Red: Closed ports
- ⚠️ Yellow: Error messages and instructions

## 🖼️ Screenshots
### Website URL Scan
![Port Scanner URL Scan](https://samrat-sarkar.github.io/Port_Scanner/screenshot1.PNG)

### IP Address Scan
![Port Scanner IP Scan](https://samrat-sarkar.github.io/Port_Scanner/screenshot2.PNG)

## 🛠️ Technical Details
- Uses `socket` for port scanning
- Implements `ipaddress` for IP validation
- Utilizes `urllib.parse` for URL parsing
- Reads port data from `ports.csv`
- Supports both IPv4 and IPv6 addresses

## ⚠️ Important Notes
- Always obtain proper authorization before scanning
- Some networks may block port scanning
- Scanning speed depends on network conditions
- Use responsibly and ethically

## 🤝 Contributing
We welcome contributions to improve Port Scanner! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👤 Author
- **Samrat Sarkar**
  - LinkedIn: [samratsarkar9999](https://www.linkedin.com/in/samratsarkar9999/)
  - Website: [samratsarkar.in](https://samratsarkar.in/)

## 📞 Support
If you encounter any issues or have questions, please:
1. Check the existing issues
2. Create a new issue with detailed information
3. Include system specifications and error messages

---

**Port Scanner - Network Security Assessment Tool** 🔒
