<div align="center"><img src="https://github.com/user-attachments/assets/7fc5885c-dba1-44f7-9d18-bc7a0dc21a8a" width="100%" alt="NOOR-404">🔐 FACEBOOK SSL PINNING BYPASS

"NOOR-404"

📚 Educational Purpose Only

""Architecture" (https://img.shields.io/badge/Architecture-x86__64%20%7C%20x86%20%7C%20ARM64-blue?style=for-the-badge)" (#-supported-architectures)
""Platform" (https://img.shields.io/badge/Platform-Android-green?style=for-the-badge)" (#-platform)
""Purpose" (https://img.shields.io/badge/Purpose-Education-orange?style=for-the-badge)" (#-disclaimer)

</div>---

📖 About

NOOR-404 Facebook SSL Pinning Bypass is an Android security-research project focused on understanding SSL/TLS certificate validation, certificate pinning, native libraries, and Android network-security mechanisms.

The project is intended for:

- 📚 Educational research
- 🔬 Android security analysis
- 🧪 Authorized testing
- 🛠️ Debugging test builds
- 🔐 TLS/SSL security research
- 📱 Controlled laboratory environments

«Educational Purpose Only.»

---

🧩 Supported Architectures

Architecture| Support
🖥️ x86_64| ✅ Supported
🖥️ x86| ✅ Supported
📱 ARM64| ✅ Supported

NOOR-404
   │
   ├── x86_64
   ├── x86
   └── ARM64

---

📱 Platform

Android

The project is designed around Android security research and multi-architecture testing environments.

---

🔐 SSL Pinning

SSL certificate pinning is a security mechanism that allows an application to restrict which certificates or public keys it trusts when establishing a TLS connection.

Researching pinning can help developers and security researchers understand:

- Certificate validation
- TLS communication
- Trust stores
- Public-key pinning
- Android Network Security Configuration
- Native security implementations
- Runtime instrumentation
- Application hardening

---

📂 Native Library Research

For an authorized test build, a native library may reside inside the application's private native-library directory.

Example structure:

/data/data/<your.test.package>/lib-compressed/libcoldstart.so

Example library

libcoldstart.so

Example directory

/data/data/<your.test.package>/lib-compressed/

«The exact location can differ depending on the Android version, application build, packaging method, and runtime environment.»

---

🔧 ADB Deployment — Authorized Test Builds

For an application that you own or have explicit permission to modify, the general ADB file-deployment pattern is:

adb push [Patched-libcoldstart.so-Path] /data/data/<your.test.package>/lib-compressed/libcoldstart.so

Where:

[Patched-libcoldstart.so-Path]
        │
        ▼
Your authorized test library
        │
        ▼
/data/data/<your.test.package>/
        │
        └── lib-compressed/
              └── libcoldstart.so

⚠️ Note

Private application directories are protected by Android's permission and sandboxing model. ADB access to these locations may require an appropriate authorized test environment, such as a debuggable development build or emulator.

---

🧪 Recommended Research Environment

For legitimate security research, use:

Android Emulator
      │
      ├── x86_64
      ├── x86
      └── ARM64
            │
            ▼
      Test Application
            │
            ▼
      TLS / SSL Analysis

Recommended targets include:

- Your own Android application
- A dedicated security-testing APK
- A deliberately vulnerable lab application
- Development/debug builds
- Applications for which you have written authorization

---

🔬 Research Areas

Android Security

Study application sandboxing, permissions, package structure, and native libraries.

TLS / SSL

Understand HTTPS connections, certificates, certificate chains, and trust validation.

Certificate Pinning

Study how applications restrict trusted certificates or public keys.

Native Libraries

Analyze how native ".so" libraries are packaged and loaded by Android applications.

Multi-Architecture Support

Test application behavior across:

x86_64
x86
ARM64

---

🛡️ Defensive Security

The same research can be used to improve application security.

Developers can investigate:

- TLS configuration
- Certificate validation
- Certificate pinning
- Root/instrumentation detection
- Native-code protections
- Network Security Configuration
- Secure key management
- Runtime tampering detection

---

📁 Example Project Structure

NOOR-404/
│
├── README.md
│
├── research/
│   ├── android/
│   ├── tls/
│   └── ssl-pinning/
│
├── architectures/
│   ├── x86/
│   ├── x86_64/
│   └── arm64/
│
└── docs/
    └── security-research.md

---

⚙️ Architecture Matrix

Component| x86| x86_64| ARM64
Android testing| ✅| ✅| ✅
Native ".so" research| ✅| ✅| ✅
TLS/SSL research| ✅| ✅| ✅
Emulator testing| ✅| ✅| —
Physical-device testing| —| —| ✅

---

🎯 Educational Objectives

The project aims to help researchers understand:

1. How TLS connections are established.
2. How Android validates certificates.
3. How certificate pinning works.
4. How native ".so" libraries are loaded.
5. How Android application sandboxing works.
6. How different CPU architectures affect native code.
7. How developers can harden applications against tampering.

---

⚠️ Responsible Use

Use this project only in environments where you have authorization.

✅ Allowed Research Targets

✔ Your own application
✔ Your own test build
✔ Authorized penetration-testing target
✔ Security laboratory
✔ Android emulator
✔ Deliberately vulnerable application

❌ Do Not Use For

✘ Unauthorized account access
✘ Credential theft
✘ Intercepting private communications
✘ Circumventing security without authorization
✘ Modifying third-party applications without permission

---

📜 Disclaimer

NOOR-404 — Educational Purpose Only

This project is intended solely for education, security research, debugging, and authorized testing.

The author does not encourage unauthorized access, interception of communications, account compromise, credential theft, privacy violations, or circumvention of security controls on systems without permission.

Users are responsible for complying with applicable laws, platform policies, and the authorization provided by the system owner.

---

<div align="center">🔐 NOOR-404

Android Security Research

"x86_64" • "x86" • "ARM64"

SSL/TLS • Certificate Pinning • Native Libraries

📚 EDUCATIONAL PURPOSE ONLY

---

Made for Learning • Research • Authorized Testing

</div>
