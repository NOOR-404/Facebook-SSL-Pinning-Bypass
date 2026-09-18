<div align="center"><img src="https://github.com/user-attachments/assets/7fc5885c-dba1-44f7-9d18-bc7a0dc21a8a" alt="NOOR-404" width="100%"><br><br>

🔐 NOOR-404

Facebook Android SSL Pinning — x86 Research

<p>
  <img src="https://img.shields.io/badge/Architecture-x86-00C853?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-Android-3DDC84?style=for-the-badge&logo=android&logoColor=white">
  <img src="https://img.shields.io/badge/Root-Required-E53935?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-1976D2?style=for-the-badge">
</p><p>
  <b>Native Library Analysis • Binary Patching • HTTPS Research</b>
</p></div>---

📌 About

NOOR-404 is an Android security-research project focused on studying SSL/TLS certificate validation, native libraries, and HTTPS traffic interception in a controlled testing environment.

This repository contains an x86 research build of:

libcoldstart.so

for the specified Facebook Android application version.

«⚠️ Use this project only on applications, devices, accounts, and network traffic that you own or are explicitly authorized to test.»

---

🎯 Target Information

Property| Value
Project| NOOR-404
GitHub| NOOR-404
Application| Facebook
Package| "com.facebook.katana"
Version| "555.0.0.49.59"
Architecture| "x86"
Library| "libcoldstart.so"
Environment| Rooted Android Emulator
Purpose| Security Research

---

📂 Repository Structure

NOOR-404/
│
├── x86/
│   └── libcoldstart.so
│
├── assets/
│   └── banner.jpg
│
└── README.md

---

📦 x86 Build

"libcoldstart.so"

Architecture:

x86

Library:

x86/libcoldstart.so

The repository intentionally contains x86 only.

Supported Architecture

✅ x86

❌ ARM64
❌ ARMv7
❌ x86_64

---

📱 Target Application

Package:
com.facebook.katana

Version:
555.0.0.49.59

Architecture:
x86

APK Type:
Standalone APK

DPI:
nodpi

«⚠️ The native library is version-specific. Do not assume that a library built for this release will work with another Facebook release.»

---

🧪 Research Setup

A typical controlled test environment:

┌──────────────────────────────┐
│          NOOR-404             │
│       Security Research      │
├──────────────────────────────┤
│                              │
│     Android x86 Emulator     │
│              │               │
│              ▼               │
│          Facebook            │
│              │               │
│              ▼               │
│      libcoldstart.so         │
│              │               │
│              ▼               │
│       HTTPS Inspection       │
│                              │
└──────────────────────────────┘

---

⚙️ Setup

1. Install the Matching APK

Install the Facebook version specified above in your controlled x86 Android environment.

Verify the package:

com.facebook.katana

---

2. Backup the Original Library

Before replacing anything, make a backup of the original native library.

Expected location:

/data/data/com.facebook.katana/lib-compressed/libcoldstart.so

Keep the original copy so that the application can be restored if necessary.

---

3. Replace the Library

Use the corresponding file:

x86/libcoldstart.so

and replace the original library inside the authorized test environment.

«Make sure the application is completely stopped before modifying its native library.»

---

4. Configure Your HTTPS Research Tool

For authorized testing, configure your preferred HTTPS inspection tool and install its CA certificate in accordance with the tool's documentation.

Examples:

Reqable
Burp Suite
HTTP Canary

---

5. Start Testing

Start the proxy/inspection tool and launch Facebook inside your controlled environment.

Perform test actions and inspect the resulting network traffic.

---

🔬 Research Topics

This project can be used to study:

- SSL/TLS certificate validation
- Certificate pinning concepts
- Android native libraries
- ELF binary structure
- ARM/x86 architecture differences
- Native code analysis
- Binary patching concepts
- HTTPS traffic inspection
- Android application security

---

🧱 Library Information

┌─────────────────────────────────┐
│          LIBRARY INFO           │
├─────────────────────────────────┤
│                                 │
│ Name      : libcoldstart.so     │
│ Arch      : x86                 │
│ Package   : com.facebook.katana │
│ Version   : 555.0.0.49.59       │
│                                 │
└─────────────────────────────────┘

---

⚠️ Important

Version Compatibility

The provided library corresponds to:

Facebook 555.0.0.49.59

Using an incompatible version may cause:

- Application crashes
- Library loading failures
- Unexpected behavior
- Failed initialization

Root Access

The described library replacement requires an appropriately controlled/rooted Android environment because application-private directories are normally protected.

Backup

Always preserve the original library before modification.

---

🛡️ Responsible Use

NOOR-404 is intended for legitimate security research and educational purposes.

Use it only when you have authorization to test the application or traffic involved.

Do not use this project for:

- Unauthorized traffic interception
- Credential theft
- Session/token collection
- Account compromise
- Privacy violations
- Unauthorized application modification

---

📜 Disclaimer

This repository is provided for educational and authorized security-research purposes only.

The author is not responsible for misuse of this material or for damage resulting from unauthorized modification, interception, or testing.

By using this project, you accept responsibility for complying with applicable laws, regulations, and service terms.

---

👤 Project

<div align="center">NOOR-404

Android Security Research

"Reverse Engineering • Native Analysis • Android Research"

<br><a href="https://github.com/NOOR-404">
  <img src="https://img.shields.io/badge/GitHub-NOOR--404-181717?style=for-the-badge&logo=github&logoColor=white">
</a><br><br>

NOOR-404
Security Research & Development

</div>---

<div align="center">⭐ If this research project is useful to you, consider starring the repository.

NOOR-404 © All rights reserved.

</div>
