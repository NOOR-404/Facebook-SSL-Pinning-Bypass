<div align="center">
  <img src="https://github.com/user-attachments/assets/7fc5885c-dba1-44f7-9d18-bc7a0dc21a8a" />
  <br/>
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&pause=1000&color=00FFFF&center=true&vCenter=true&width=750&lines=NOOR-404+%7C+Facebook+SSL+Pinning+Bypass;Native+Library+Patch+%7C+ARM64+%26+x86_64;libcoldstart.so+%7C+SSL+Analysis+%26+Research" alt="NOOR-404 | Facebook SSL Pinning Bypass" />
  <br/>  



</div>  
---

## Facebook Android SSL Pinning — Native Library Research

Android native-library research project focused on understanding SSL/TLS certificate-pinning mechanisms, native library structures, and security-analysis workflows in Facebook's Android application.

> ⚠️ **Research Notice:** This project is intended for authorized security research, reverse engineering, debugging, and educational analysis. Only test applications and devices for which you have permission.

---

## 📱 Application Information

| Property | Details |
|----------|---------|
| **Application** | Facebook for Android |
| **Package Name** | `com.facebook.katana` |
| **Application Version** | `YOUR_VERSION_HERE` |
| **Platform** | Android |
| **Architecture** | ARM64 / ARM / x86 / x86_64 |
| **Root Access** | Required for protected application-directory access |
| **Primary Library** | `libcoldstart.so` |
| **Library Type** | Native ELF `.so` library |
| **Research Area** | SSL/TLS & Native Security Analysis |

---

## 📦 Package Information

### Application Package
```
com.facebook.katana
```

The package identifier used by the Facebook Android application.

### Native Library
```
libcoldstart.so
```

The primary native library examined in this research.

---

## 📍 Library Location

On installations where the library is stored in Facebook's compressed native-library directory:

```
/data/data/com.facebook.katana/lib-compressed/libcoldstart.so
```

### Full Path Breakdown
```
/data/
└── data/
    └── com.facebook.katana/
        └── lib-compressed/
            └── libcoldstart.so
```

> **Note:** The exact filesystem layout can vary between application versions, Android versions, installation methods, and device configurations.

---

## 🧩 Native Library Details

### libcoldstart.so

`libcoldstart.so` is a native shared library used by the Android application. Native `.so` libraries are ELF binaries containing compiled native code and related sections required by the application.

For security research, the library can be examined to understand:

- Native code structure
- ELF headers and sections
- Imported/exported symbols
- Native initialization routines
- String references
- TLS/SSL-related routines
- Certificate-validation logic
- Native control flow
- Architecture-specific instructions

---

## 🏗️ Supported Architectures

The project is intended to cover common Android architectures:

| Architecture | Status |
|-------------|--------|
| ARM64-v8a | ✅ Supported |
| armeabi-v7a / ARM | ✅ Supported |
| x86 | ✅ Supported |
| x86_64 | ✅ Supported |

> Architecture-specific analysis is important because the compiled instructions and binary layout can differ between builds.

---

## 🔬 SSL Pinning Research

SSL/TLS certificate pinning is a security mechanism that can restrict an application to accepting only expected certificates or public keys during TLS communication.

This project studies the native side of that mechanism, particularly where security-sensitive functionality may exist inside native libraries.

### Research Areas

```
Application
    │
    ▼
Java / Kotlin Layer
    │
    ▼
JNI / Native Interface
    │
    ▼
Native Libraries
    │
    ▼
TLS / Certificate Validation
    │
    ▼
Network Communication
```

The goal is to understand the relationship between the Android application layer and native security-sensitive components.

---

## 🧪 libcoldstart.so Analysis

The research workflow can include static examination of `libcoldstart.so` across all supported architectures.

### Typical Analysis Areas

**ELF Header**
- Architecture
- Entry Point
- Program Headers
- Section Headers

**Native Code**
- Functions
- Strings
- Cross References
- Control Flow

**Security Analysis**
- TLS-related routines
- Certificate handling
- Native validation logic
- JNI interactions

---

## 📂 Important Paths

| Component | Path |
|-----------|------|
| **Package** | `com.facebook.katana` |
| **Library** | `libcoldstart.so` |
| **Full Path** | `/data/data/com.facebook.katana/lib-compressed/libcoldstart.so` |

---

## 🛠️ Research Environment

| Component | Information |
|-----------|-------------|
| **OS** | Android |
| **Target Package** | `com.facebook.katana` |
| **Native Binary** | `libcoldstart.so` |
| **Binary Format** | ELF |
| **Architectures** | ARM / ARM64 / x86 / x86_64 |
| **Access Level** | Root / Authorized Debug Environment |
| **Purpose** | Security Research & Analysis |

---

## 📌 Version Information

Because native libraries can change between releases, always record the exact application version used during analysis.

```
Facebook Version : 578.0.0.40.75
Package          : com.facebook.katana
Library          : libcoldstart.so
```

> Keeping version information is important because a library structure or security implementation from one release may not match another release.

---

## 🌍 Project Information

| Detail | Value |
|--------|-------|
| **Location** | Bangladesh 🇧🇩 |
| **Project** | NOOR-404 |
| **Research** | Android Native Security |

---

## 📞 Contact & Links

```
👤 NOOR-404

Security Research • Android Native Analysis • Reverse Engineering

GitHub  : https://github.com/NOOR-404
Telegram: https://t.me/N_O_O_R_4_0_4
Email   : daniyaln.hossai@gmail.com
```

---

## ⚖️ Disclaimer

This repository is provided for educational and authorized security research purposes.

**Do not use this project to:**
- Intercept traffic without authorization
- Modify network communications on unauthorized devices
- Inspect applications, accounts, or networks without appropriate permission

The author is not responsible for misuse of the information or tools contained in this repository.

---

## 📜 License

MIT License — See LICENSE file for details.

---

<div align="center">

### 🔐 NOOR-404

*Android Security • Native Analysis • SSL/TLS Research*

**[GitHub](https://github.com/NOOR-404) • [Telegram](https://t.me/N_O_O_R_4_0_4) • [Email](mailto:daniyaln.hossai@gmail.com)**

</div>
