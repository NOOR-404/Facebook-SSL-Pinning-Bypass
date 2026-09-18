<div align="center"><img src="https://github.com/user-attachments/assets/7fc5885c-dba1-44f7-9d18-bc7a0dc21a8a" alt="NOOR-404 Facebook SSL Pinning Research" width="100%"/><br/>🛡️ NOOR-404

Facebook Android SSL Pinning Research

"Native Library Analysis" • "x86" • "Android Security Research"

<br/>"Architecture" (https://img.shields.io/badge/Architecture-x86-00C853?style=flat-square&logo=android&logoColor=white)
"Platform" (https://img.shields.io/badge/Platform-Android-3DDC84?style=flat-square&logo=android&logoColor=white)
"Root" (https://img.shields.io/badge/Root-Required-E53935?style=flat-square)
"License" (https://img.shields.io/badge/License-MIT-1976D2?style=flat-square)

</div>---

🔎 Project Overview

NOOR-404 is an Android security-research project focused on studying SSL/TLS certificate validation and native-library behavior inside the Facebook Android application.

The project provides a research-oriented patched "libcoldstart.so" for the specified application version and x86 architecture, allowing authorized researchers to study HTTPS traffic interception in a controlled environment.

«Research Project: Use only with applications, devices, accounts, and traffic that you own or have explicit permission to test.»

---

📋 Target Information

Property| Details
Project| NOOR-404
Target App| Facebook
Package| "com.facebook.katana"
Test Version| "555.0.0.49.59"
Architecture| "x86"
Library| "libcoldstart.so"
Technique| Native binary patching
Environment| Rooted Android / Android Emulator

«⚠️ The patched library is intended for the exact application version and architecture listed above.»

---

📁 Repository Layout

NOOR-404/
│
├── assets/
│   └── banner.jpg
│
├── x86/
│   └── libcoldstart.so
│
└── README.md

---

📥 x86 Resources

Native Library

Architecture: "x86"

x86/libcoldstart.so

Download the corresponding "libcoldstart.so" from the repository's x86 directory.

Facebook APK

Use the corresponding Facebook release:

Package: com.facebook.katana
Version: 555.0.0.49.59
Architecture: x86
DPI: nodpi
APK: standalone APK

---

🧪 Research Environment

Recommended setup:

Android Emulator
       │
       ├── Root Access
       │
       ├── Facebook
       │
       ├── Patched libcoldstart.so
       │
       └── HTTPS Proxy
              │
              └── Traffic Analysis

Suitable research environments include rooted Android emulators where the researcher controls the application installation and network configuration.

---

⚙️ Installation

01 — Prepare the Environment

Install the matching Facebook APK and make sure the emulator/device is running the x86 architecture.

Confirm the package:

com.facebook.katana

---

02 — Backup the Original Library

Before making any modification, create a backup of the original native library.

Typical location:

/data/data/com.facebook.katana/lib-compressed/libcoldstart.so

Keep the original file somewhere safe so the application can be restored later.

---

03 — Replace the Research Library

Replace the original:

libcoldstart.so

with the corresponding research build from:

x86/libcoldstart.so

The replacement should only be performed on an installation that you are authorized to modify.

---

04 — Configure HTTPS Inspection

For an authorized test environment, configure your preferred HTTPS inspection tool and install its CA certificate according to the tool's official documentation.

Possible research tools include:

Reqable
Burp Suite
HTTP Canary

---

05 — Start Traffic Analysis

Start the HTTPS inspection session and launch the test application.

Perform normal test actions inside the authorized environment and inspect the resulting network requests.

---

🧩 Why "libcoldstart.so"?

Facebook uses native Android components as part of its application runtime.

Studying native libraries such as:

libcoldstart.so

can help security researchers understand:

- Native certificate-validation flows
- Android TLS implementation
- Binary patching concepts
- Runtime behavior of native libraries
- HTTPS interception techniques
- Application security controls

This repository is intended as a learning and research reference.

---

🖥️ x86 Emulator Focus

This repository intentionally contains x86 only.

┌──────────────────────────────┐
│          NOOR-404             │
├──────────────────────────────┤
│                              │
│  Architecture : x86          │
│  Platform     : Android      │
│  Target       : Facebook     │
│  Library      : libcoldstart │
│                              │
└──────────────────────────────┘

ARM64, ARMv7, and x86_64 builds are intentionally not included in this version.

---

⚠️ Important Notes

Version Matching

The library is tied to a specific Facebook release.

Facebook: 555.0.0.49.59
Architecture: x86

Using a library from a different application version or architecture may cause the application to malfunction or fail to load.

Root Requirement

Access to the application's private native-library directory generally requires an appropriately controlled/rooted test environment.

Backup

Always keep the original library before performing any modification.

---

🔐 Responsible Security Research

NOOR-404 is intended for:

- Android security research
- Reverse-engineering education
- Native-library analysis
- Controlled HTTPS testing
- Application security testing
- Learning about certificate pinning

Do not use this project to intercept traffic, credentials, sessions, or data belonging to other users or services without authorization.

---

📜 Disclaimer

This repository is provided for educational and authorized security-research purposes only.

The author does not encourage unauthorized interception, credential collection, account compromise, or modification of applications that you do not own or have permission to test.

You are solely responsible for complying with applicable laws, terms of service, and authorization requirements when using this material.

---

🧰 Custom Research Work

Need a custom Android security-research project?

• Android native-library analysis
• Application security research
• Authorized SSL/TLS testing
• Reverse-engineering assistance
• Python automation projects
• Android research tooling

Contact:

NOOR-404

---

📡 Contact

<div align="center">NOOR-404

"Security Research • Reverse Engineering • Android"

<br/>"Facebook" (https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)
"WhatsApp" (https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)
"Telegram" (https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)

<br/><br/>

NOOR-404
Android Security Research

</div>
