<div align="center"><img src="assets/banner.png" alt="NOOR-404" width="100%"><br>🔐 NOOR-404

FACEBOOK SSL PINNING RESEARCH

Educational Purpose Only

<br>""Platform" (https://img.shields.io/badge/Platform-Android-3DDC84?style=for-the-badge%26logo=android%26logoColor=white)" (#platform)
""x86" (https://img.shields.io/badge/Arch-x86-0078D4?style=for-the-badge)" (#supported-architectures)
""x86_64" (https://img.shields.io/badge/Arch-x86__64-0078D4?style=for-the-badge)" (#supported-architectures)
""ARM64" (https://img.shields.io/badge/Arch-ARM64-0078D4?style=for-the-badge)" (#supported-architectures)
""Education" (https://img.shields.io/badge/Purpose-Education-FF9800?style=for-the-badge)" (#disclaimer)

</div>---

📖 About

NOOR-404 is an Android security-research project focused on learning how applications implement TLS/SSL certificate validation, certificate pinning, native libraries, and network-security mechanisms.

The project is intended for:

- 📚 Educational research
- 🔬 Android security analysis
- 🧪 Authorized testing
- 🛠️ Debugging test builds
- 🔐 TLS/SSL research
- 📱 Controlled laboratory environments

«Educational Purpose Only.»

---

🧩 Supported Architectures

Architecture| Status
🖥️ x86_64| ✅ Supported
🖥️ x86| ✅ Supported
📱 ARM64| ✅ Supported

                    ┌─────────────────┐
                    │     NOOR-404    │
                    │ Security Research │
                    └────────┬────────┘
                             │
             ┌───────────────┼───────────────┐
             │               │               │
             ▼               ▼               ▼
        ┌─────────┐     ┌─────────┐     ┌─────────┐
        │   x86   │     │ x86_64  │     │  ARM64  │
        └─────────┘     └─────────┘     └─────────┘
             │               │               │
             └───────────────┼───────────────┘
                             ▼
                    Android Test Environment

---

📱 Platform

Android

The project is designed for studying Android application security across multiple CPU architectures.

---

🔐 SSL / TLS Research

SSL/TLS provides encrypted communication between an application and a server.

Certificate pinning adds another layer of trust validation by restricting which certificates or public keys an application accepts.

This project can be used to study:

- 🔒 TLS connections
- 📜 Certificates
- 🔗 Certificate chains
- 📌 Certificate pinning
- 🛡️ Trust validation
- ⚙️ Network Security Configuration
- 🧩 Native ".so" libraries
- 🔎 Runtime security mechanisms

---

📂 Native Library

For an authorized test application/build, a native library may be located inside the application's private native-library directory.

Example:

/data/data/<your.test.package>/lib-compressed/libcoldstart.so

Library

libcoldstart.so

Directory

/data/data/<your.test.package>/lib-compressed/

«The exact path may vary depending on the Android version, application build, packaging configuration, and runtime environment.»

---

🔧 ADB — Authorized Test Environment

For an application that you own or are explicitly authorized to test, the general ADB deployment format is:

adb push [Patched-libcoldstart.so-Path] /data/data/<your.test.package>/lib-compressed/libcoldstart.so

Path Structure

[Patched-libcoldstart.so-Path]
             │
             ▼
      libcoldstart.so
             │
             ▼
/data/data/<your.test.package>/
             │
             └── lib-compressed/
                     │
                     └── libcoldstart.so

«Android's application sandbox and file permissions may prevent direct access to private application directories. Use an appropriate debug/emulator/test environment.»

---

🧪 Research Environment

Recommended environment:

Android
   │
   ├── x86
   │
   ├── x86_64
   │
   └── ARM64
          │
          ▼
   Authorized Test Build
          │
          ▼
   TLS / SSL Research

Suitable targets include:

- ✔ Your own application
- ✔ Your own debug build
- ✔ Authorized security-testing target
- ✔ Dedicated laboratory APK
- ✔ Deliberately vulnerable test application
- ✔ Android emulator

---

🔬 Research Areas

Android Security

Study:

- Application sandboxing
- Permissions
- APK structure
- Native libraries
- Runtime behavior

TLS / SSL

Study:

- HTTPS
- TLS handshakes
- Certificates
- Trust stores
- Certificate validation

Certificate Pinning

Study how applications restrict trusted certificates or public keys and how developers can test their own implementations.

Native Libraries

Study:

.so
│
├── ELF structure
├── Architecture
├── Native code
└── Runtime loading

---

🛡️ Defensive Security

The same research can be used to improve Android application security.

Recommended areas of study:

- Strong TLS configuration
- Proper certificate validation
- Certificate pinning
- Secure key management
- Network Security Configuration
- Runtime tampering detection
- Root/instrumentation detection
- Native-code hardening

---

📁 Repository Structure

NOOR-404/
│
├── README.md
│
├── assets/
│   └── banner.png
│
├── architectures/
│   ├── x86/
│   ├── x86_64/
│   └── arm64/
│
├── research/
│   ├── android/
│   ├── tls/
│   └── ssl-pinning/
│
└── docs/
    └── security-research.md

---

⚙️ Architecture Matrix

Component| x86| x86_64| ARM64
Android Testing| ✅| ✅| ✅
Native ".so" Research| ✅| ✅| ✅
TLS / SSL Research| ✅| ✅| ✅
Emulator Testing| ✅| ✅| —
Physical Device Testing| —| —| ✅

---

🎯 Educational Objectives

The project aims to help researchers understand:

01 ── TLS / SSL
02 ── Certificate Validation
03 ── Certificate Pinning
04 ── Android Network Security
05 ── Native .so Libraries
06 ── Android Application Sandboxing
07 ── Multi-Architecture Analysis
08 ── Application Hardening

---

📚 Learning Flow

        Android Application
                │
                ▼
          HTTPS / TLS
                │
                ▼
      Certificate Validation
                │
                ▼
       Certificate Pinning
                │
                ▼
        Native Components
                │
                ▼
       Security Analysis
                │
                ▼
       Defensive Hardening

---

⚠️ Responsible Use

This project should only be used where you have permission.

✅ Authorized

✔ Own applications
✔ Own development builds
✔ Authorized penetration tests
✔ Security laboratories
✔ Test APKs
✔ Android emulators

❌ Unauthorized

✘ Account compromise
✘ Credential theft
✘ Private communication interception
✘ Unauthorized application modification
✘ Unauthorized security bypass
✘ Privacy violations

---

📜 Disclaimer

<div align="center">⚠️ EDUCATIONAL PURPOSE ONLY ⚠️

</div>NOOR-404 is intended for education, security research, debugging, and authorized testing.

The project does not encourage unauthorized access, interception of communications, account compromise, credential theft, privacy violations, or circumvention of security controls without permission.

Users are responsible for complying with applicable laws, platform policies, and the authorization provided by the system owner.

---

<div align="center">🔐 NOOR-404

Android Security Research

x86 • x86_64 • ARM64

SSL/TLS • Certificate Pinning • Native Libraries

<br>"EDUCATIONAL PURPOSE ONLY"

<br>---

Made for Learning • Research • Authorized Testing

</div>
