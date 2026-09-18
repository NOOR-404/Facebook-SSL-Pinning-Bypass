<div align="center"><img src="https://github.com/user-attachments/assets/7fc5885c-dba1-44f7-9d18-bc7a0dc21a8a" alt="NOOR-404" width="100%"><br>🔐 FACEBOOK SSL PINNING BYPASS

Android SSL/TLS Security Research

<p>
  <img src="https://img.shields.io/badge/Android-Security-3DDC84?style=for-the-badge&logo=android&logoColor=white">
  <img src="https://img.shields.io/badge/ARM64-Supported-00C853?style=for-the-badge">
  <img src="https://img.shields.io/badge/x86-Supported-00C853?style=for-the-badge">
  <img src="https://img.shields.io/badge/x86__64-Supported-00C853?style=for-the-badge">
</p><p>
  <b>SSL/TLS Research • Native Analysis • Android Reverse Engineering</b>
</p><p>
  <img src="https://img.shields.io/badge/Purpose-Education-1976D2?style=flat-square">
  <img src="https://img.shields.io/badge/Platform-Android-3DDC84?style=flat-square&logo=android&logoColor=white">
</p></div>---

📌 About

FACEBOOK SSL PINNING BYPASS is an Android security-research project created by NOOR-404 for educational purposes.

The project focuses on studying:

- 🔐 SSL/TLS certificate validation
- 🧩 SSL certificate pinning concepts
- 📱 Android application security
- 🔬 Native ".so" library analysis
- 🛠️ Reverse-engineering techniques
- 🖥️ Emulator and device testing
- ⚡ Multi-architecture native libraries

«🎓 Education Purpose: This project is intended for learning, research, and authorized security testing in controlled environments.»

---

🎯 Target Information

Property| Details
Project| FACEBOOK SSL PINNING BYPASS
Application| Facebook for Android
Package| "com.facebook.katana"
Native Library| "libcoldstart.so"
ARM64| ✅ Supported
x86| ✅ Supported
x86_64| ✅ Supported
Platform| Android
Purpose| 🎓 Education / Security Research

---

🧬 Architecture Support

This repository contains architecture-specific native libraries.

Architecture| Support| Environment
ARM64-v8a| ✅| Physical Android Devices
x86| ✅| Android Emulators
x86_64| ✅| Android Emulators

Supported Structure

FACEBOOK-SSL-PINNING-BYPASS/
│
├── ARM64/
│   └── libcoldstart.so
│
├── x86/
│   └── libcoldstart.so
│
├── x86_64/
│   └── libcoldstart.so
│
├── assets/
│   └── banner.jpg
│
├── LICENSE
└── README.md

---

📂 Native Library

The primary native library used for research is:

libcoldstart.so

Typical application-private location:

/data/data/com.facebook.katana/lib-compressed/libcoldstart.so

Architecture Mapping

ARM64-v8a
    ↓
ARM64/libcoldstart.so

x86
    ↓
x86/libcoldstart.so

x86_64
    ↓
x86_64/libcoldstart.so

«⚠️ Important: Always use a library matching the target application's ABI and compatible application build. Mixing incompatible binaries may cause loading failures or application crashes.»

---

🧪 Educational Research Environment

A controlled research environment may include:

Android Emulator / Test Device
            │
            ▼
     Facebook Test APK
            │
            ▼
    Native Library Analysis
            │
            ▼
      SSL/TLS Validation
            │
            ▼
   Authorized Traffic Study

Common research tools include:

- ADB
- Ghidra
- IDA
- MT Manager
- Reqable
- Burp Suite
- HTTP Canary

---

🔬 Research Topics

Android Security

- Android application architecture
- Native ELF libraries
- Application-private directories
- ABI and architecture differences
- Native code loading

SSL/TLS

- Certificate validation
- Certificate pinning
- Trust chains
- HTTPS inspection
- TLS debugging

Reverse Engineering

- ".so" library analysis
- ELF structures
- Native functions
- Static analysis
- Dynamic analysis
- Architecture-specific binaries

---

🖥️ ABI Compatibility

Supported ABIs:

┌─────────────────────────────┐
│       ARCHITECTURES         │
├─────────────────────────────┤
│  ✅ ARM64-v8a               │
│  ✅ x86                     │
│  ✅ x86_64                  │
└─────────────────────────────┘

Use the corresponding directory for the target environment:

ARM64 → ARM64/libcoldstart.so
x86   → x86/libcoldstart.so
x86_64 → x86_64/libcoldstart.so

---

⚠️ Compatibility

Native Android libraries are highly dependent on:

- Application version
- Application build
- ABI
- Native dependencies
- Runtime environment

Therefore:

Application Version
        +
Matching ABI
        +
Matching Native Build
        ↓
Compatible Research Environment

Do not assume that a library from one application release will work correctly with another release.

---

🎓 Education Purpose

This repository is published for educational and security-research purposes.

It can be used to study:

- How Android applications implement TLS security
- How certificate validation works
- How native libraries participate in application security
- How ABI differences affect native Android applications
- How security researchers analyze native binaries

«📚 The goal is to improve understanding of Android application security and reverse engineering.»

---

🛡️ Responsible Use

Use this project only in environments where you have appropriate authorization.

Do not use it for:

- Unauthorized traffic interception
- Credential collection
- Session theft
- Account compromise
- Privacy violations
- Circumventing security controls on systems you do not own or have permission to test

Always follow applicable laws, regulations, and service terms.

---

⚠️ Disclaimer

NOOR-404 provides this project strictly for education, research, and authorized security testing.

The author does not encourage unauthorized modification, interception, or analysis of third-party applications or user traffic.

You are solely responsible for how you use the materials contained in this repository.

---

👤 NOOR-404

<div align="center"><img src="https://img.shields.io/badge/NOOR--404-Security%20Research-181717?style=for-the-badge&logo=github&logoColor=white"><br><br>

🔐 FACEBOOK SSL PINNING BYPASS

Education • Android Security • Reverse Engineering

<br><img src="https://img.shields.io/badge/ARM64-✓-00C853?style=flat-square">
<img src="https://img.shields.io/badge/x86-✓-00C853?style=flat-square">
<img src="https://img.shields.io/badge/x86__64-✓-00C853?style=flat-square"><br><br>

🎓 Education Purpose Only

<br>© NOOR-404

</div>---
