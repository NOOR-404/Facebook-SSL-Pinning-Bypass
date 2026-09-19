<div align="center">

![NOOR-404 Banner](https://github.com/user-attachments/assets/7fc5885c-dba1-44f7-9d18-bc7a0dc21a8a)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=24&pause=1000&color=00FFFF&center=true&vCenter=true&width=800&lines=NOOR-404+%7C+Facebook+SSL+Pinning+Research;Native+Library+Analysis+%7C+ARM64+%26+x86_64;libcoldstart.so+%7C+SSL+Analysis+%26+Research;Android+Security+%7C+Reverse+Engineering)](https://github.com/NOOR-404)

[![Architecture](https://img.shields.io/badge/Arch-ARM64%20%7C%20x86%20%7C%20x86__64-00FFFF?style=for-the-badge&logo=archlinux&logoColor=00FFFF)](https://github.com/NOOR-404)
[![Root Required](https://img.shields.io/badge/Root-Required-FF003C?style=for-the-badge&logo=android&logoColor=FFFFFF)](https://github.com/NOOR-404)
[![License](https://img.shields.io/badge/License-MIT-000000?style=for-the-badge&logoColor=00FFFF)](./LICENSE)
[![Android](https://img.shields.io/badge/Android-Native_Research-3DDC84?style=for-the-badge&logo=android&logoColor=white)](https://github.com/NOOR-404)

</div>

---

# 🔐 NOOR-404

**Facebook Android SSL Pinning — Native Library Research**

Android native-library research project focused on understanding SSL/TLS certificate-pinning mechanisms, native library structures, and security-analysis workflows in Facebook's Android application.

> ⚠️ **Research Notice:** This project is intended for authorized security research, reverse engineering, debugging, and educational analysis. Only test applications and devices for which you have permission.

---

## 📱 Application Information

| Property | Details |
|----------|---------|
| **Application** | Facebook for Android |
| **Package Name** | `com.facebook.katana` |
| **Application Version** | `578.0.0.40.75` |
| **Platform** | Android 6.0+ |
| **Architecture** | ARM64 / ARM / x86 / x86_64 |
| **Root Access** | Required for protected application-directory access |
| **Primary Library** | `libcoldstart.so` |
| **Library Type** | Native ELF `.so` shared library |
| **Research Area** | SSL/TLS & Native Security Analysis |
| **Binary Format** | ELF (Executable and Linkable Format) |

---

## 📦 Package Information

### Application Package
```
com.facebook.katana
```
The package identifier used by the Facebook Android application.

### Native Library Target
```
libcoldstart.so
```
The primary native library examined in this research project.

---

## 📍 Library Location

On installations where the library is stored in Facebook's compressed native-library directory:

```bash
/data/data/com.facebook.katana/lib-compressed/libcoldstart.so
```

### Full Path Breakdown
```
/data/
└── data/
    └── com.facebook.katana/
        ├── lib-compressed/
        │   └── libcoldstart.so
        ├── lib/
        │   └── [other native libraries]
        └── shared_prefs/
```

### Alternate Library Paths
```bash
# Direct lib directory (uncompressed)
/data/data/com.facebook.katana/lib/libcoldstart.so

# System partitions (if pre-installed)
/system/app/Facebook/lib/libcoldstart.so
/vendor/lib/libcoldstart.so
```

> **Note:** The exact filesystem layout can vary between application versions, Android versions, installation methods, and device configurations.

---

## 🧩 Native Library Details

### libcoldstart.so Overview

`libcoldstart.so` is a native shared library used by the Android application. Native `.so` libraries are ELF binaries containing compiled native code, symbol tables, and relocation sections required by the application runtime.

### Research-Relevant Analysis Points

For security research, the library can be examined to understand:

- **Structure:** Native code organization, segment layout, section headers
- **Symbols:** Imported and exported function symbols, external dependencies
- **Initialization:** Native library entry points (JNI_OnLoad, constructors)
- **Strings:** Embedded string references, debug symbols, resource identifiers
- **Security:** TLS/SSL routines, certificate validation logic, cryptographic operations
- **Control Flow:** Function calls, branching patterns, native call graphs
- **Architecture:** CPU-specific instruction sets, register usage, assembly patterns
- **JNI Interface:** Java-Native Interface method signatures and callbacks
- **Dependencies:** Linked shared libraries, external symbol resolution

---

## 🏗️ Supported Architectures

The project is intended to cover common Android architectures:

| Architecture | EABI | Status | Device Examples |
|-------------|------|--------|-----------------|
| **ARM64-v8a** | ARM64 | ✅ Actively Supported | Pixel 6+, Galaxy S20+, OnePlus 9+ |
| **armeabi-v7a** | ARMv7 | ✅ Supported | Older flagships, budget devices |
| **x86_64** | x86-64 | ✅ Supported | Android Studio Emulator, some tablets |
| **x86** | x86 | ✅ Supported | Legacy emulators, some devices |

> **Important:** Architecture-specific analysis is critical because the compiled instructions, binary layout, and security mechanisms can differ significantly between builds. ARM64 and x86_64 may have entirely different implementations of the same functionality.

---

## 🔬 SSL Pinning Research

### What is Certificate Pinning?

SSL/TLS certificate pinning is a security mechanism that restricts an application to accepting only specific certificates or public keys during TLS handshake. This prevents MITM (Man-in-the-Middle) attacks by validating that the server's certificate matches expected pins.

### Research Objectives

This project studies the native-side implementation of certificate pinning, particularly where security-sensitive functionality resides in native libraries rather than managed code.

### Research Flow Architecture

```
┌─────────────────────────────────────────────┐
│         Application Layer (Java/Kotlin)     │
│        ┌──────────────────────────────┐     │
│        │   Network Request / Activity │     │
│        └──────────────────┬───────────┘     │
└─────────────────────────────┼────────────────┘
                              │
                ┌─────────────▼────────────┐
                │   JNI / Native Interface │
                │   (Method Signatures)    │
                └─────────────┬────────────┘
                              │
              ┌───────────────▼──────────────┐
              │    Native Library Layer      │
              │   (libcoldstart.so, etc)     │
              └─────────────┬────────────────┘
                            │
            ┌───────────────▼────────────────┐
            │   TLS Handshake Initiation     │
            │   (Socket Creation, etc)       │
            └─────────────┬────────────────┘
                          │
        ┌─────────────────▼───────────────────┐
        │   Certificate Pinning Validation    │
        │   (Pin Comparison, Verification)    │
        └─────────────┬───────────────────────┘
                      │
            ┌─────────▼──────────┐
            │  Network IO / TLS  │
            │  Communication     │
            └─────────┬──────────┘
                      │
            ┌─────────▼──────────────┐
            │  Server Response       │
            │  (Encrypted / Secure)  │
            └────────────────────────┘
```

### Key Research Areas

1. **Pin Storage:** Where are certificate pins stored? How are they protected?
2. **Validation Logic:** How does the native library validate pins?
3. **Failure Handling:** What happens if a pin validation fails?
4. **JNI Interaction:** How does the native layer communicate with Java?
5. **Cryptographic Operations:** What algorithms and libraries are used?
6. **Bypass Potential:** What attack vectors exist at the native level?

---

## 🧪 libcoldstart.so Analysis Methodology

### Static Analysis Approach

The research workflow includes comprehensive static examination of `libcoldstart.so` across all supported architectures.

#### Step 1: Binary Acquisition
```bash
# Extract from running device
adb pull /data/data/com.facebook.katana/lib-compressed/libcoldstart.so

# Verify architecture
file libcoldstart.so
# Output: ELF 64-bit LSB shared object, ARM aarch64, version 1 (SYSV)
```

#### Step 2: ELF Header Analysis

**ELF Header Contents:**
- Magic bytes (0x7F ELF)
- Architecture (ARM64 / x86 / etc)
- Entry point address
- Program headers offset
- Section headers offset
- File format flags

#### Step 3: Symbols & Functions
```bash
# List exported symbols
readelf -s libcoldstart.so | grep FUNC

# Filter for TLS-related functions
nm -D libcoldstart.so | grep -i "ssl\|tls\|cert\|pin"
```

#### Step 4: Section Analysis

**Key Sections to Examine:**
- `.text` — Executable code
- `.rodata` — Read-only data (strings, constants)
- `.dynsym` — Dynamic symbol table
- `.dynstr` — Dynamic string table
- `.rel.dyn` / `.rela.dyn` — Relocation entries

#### Step 5: String Extraction
```bash
# Extract all strings
strings libcoldstart.so | grep -i "certificate\|pin\|ssl\|tls\|verify"
```

#### Step 6: Control Flow & Disassembly

**Tools for Deep Analysis:**
- **IDA Pro:** Industry-standard disassembler with decompilation
- **Ghidra:** Free, open-source reverse engineering suite
- **Radare2:** Command-line hex editor and disassembler
- **Binary Ninja:** Modern reverse engineering platform

#### Step 7: Cross-Reference Analysis

Understanding function calls and data references to map the certificate validation flow.

#### Step 8: Architecture-Specific Patterns

Each architecture (ARM64, x86_64, x86, ARM) has different calling conventions and instruction sets. Analysis must account for these differences.

### Typical Analysis Areas

**ELF Header**
- Architecture identification
- Endianness verification
- Entry point location
- Program header table
- Section header table

**Native Code Patterns**
- Function prologue/epilogue detection
- Loop structures
- Conditional branches
- JNI call sites
- Error handling paths

**Security Analysis**
- TLS/SSL-related function calls
- Certificate handling routines
- Public key extraction
- Validation logic
- Failure branches

**JNI Interactions**
- JNI method signatures
- Environment pointer usage
- Exception handling
- Data marshaling between Java and native

---

## 📂 Important Paths & Files

| Component | Path/Value |
|-----------|-----------|
| **Package** | `com.facebook.katana` |
| **Library** | `libcoldstart.so` |
| **Full Path** | `/data/data/com.facebook.katana/lib-compressed/libcoldstart.so` |
| **Alternate** | `/data/data/com.facebook.katana/lib/libcoldstart.so` |
| **App Data** | `/data/data/com.facebook.katana/` |
| **Cache** | `/data/data/com.facebook.katana/cache/` |
| **Shared Prefs** | `/data/data/com.facebook.katana/shared_prefs/` |

---

## 🛠️ Research Environment Setup

### Requirements

| Component | Specification |
|-----------|---------------|
| **OS** | Android 6.0 or higher |
| **Target Package** | `com.facebook.katana` |
| **Native Binary** | `libcoldstart.so` |
| **Binary Format** | ELF (Executable and Linkable Format) |
| **Architectures** | ARM / ARM64 / x86 / x86_64 |
| **Access Level** | Root / Authorized Debug Environment |
| **Tools** | ADB, Frida, IDA/Ghidra, readelf, strings |
| **Purpose** | Security Research & Authorized Analysis |

### Recommended Tools

- **Android Debug Bridge (ADB):** Device communication and file extraction
- **Frida:** Dynamic instrumentation and runtime analysis
- **IDA Pro / Ghidra:** Binary disassembly and decompilation
- **Radare2:** Lightweight analysis and scripting
- **Binary Ninja:** Modern UI-based reverse engineering
- **readelf / nm / strings:** Standard ELF analysis utilities
- **Android Studio:** Emulator and debugging environment

---

## 📌 Version Information

Version tracking is critical for accurate research:

```
Facebook Version : 578.0.0.40.75
Package Name     : com.facebook.katana
Target Library   : libcoldstart.so
Architecture     : ARM64 (primary analysis target)
Analysis Date    : [Your Date Here]
Researcher       : NOOR-404
```

### Why Version Matters

Native libraries change between releases:
- **Security patches** may alter validation logic
- **Performance optimizations** can change control flow
- **Refactoring** can reorganize functions
- **New features** may introduce new libraries or APIs
- **Dependency updates** can bring external library changes

A library structure or security implementation from one release **may not match another release**. Always document your version baseline.

---

## 🌍 Project Information

| Detail | Value |
|--------|-------|
| **Project Name** | NOOR-404 |
| **Location** | Bangladesh 🇧🇩 |
| **Research Focus** | Android Native Security |
| **Specialization** | SSL/TLS, Certificate Pinning, Reverse Engineering |
| **Status** | Active Research |

---

## 📞 Contact & Links

### Developer Information

**👤 NOOR-404**

Security Research • Android Native Analysis • Reverse Engineering

### Official Channels

| Platform | Link |
|----------|------|
| **GitHub** | [github.com/NOOR-404](https://github.com/NOOR-404) |
| **Telegram** | [@N_O_O_R_4_0_4](https://t.me/N_O_O_R_4_0_4) |
| **Email** | [daniyaln.hossai@gmail.com](mailto:daniyaln.hossai@gmail.com) |

### Quick Links

- [GitHub Profile](https://github.com/NOOR-404)
- [Telegram Channel](https://t.me/N_O_O_R_4_0_4)
- [Send Email](mailto:daniyaln.hossai@gmail.com?subject=NOOR-404%20Research)

---

## ⚖️ Legal Disclaimer

This repository is provided **for educational and authorized security research purposes only**.

### Permitted Use

✅ Security research on authorized systems  
✅ Educational analysis and learning  
✅ Authorized penetration testing  
✅ Debugging on your own devices  
✅ Academic research with proper documentation  

### Prohibited Use

❌ Unauthorized network traffic interception  
❌ Unauthorized device or account access  
❌ Malicious modification of applications  
❌ Unauthorized traffic inspection  
❌ Bypassing security for unauthorized purposes  
❌ Distributing bypasses or exploits  

### Responsibility

The author **is not responsible** for:
- Misuse of information or tools in this repository
- Unauthorized access to systems or networks
- Legal violations resulting from misuse
- Damage caused by improper implementation
- Data breaches or security incidents

**By using this repository, you agree to use it only for authorized, legal purposes.**

---

## 📜 License

MIT License — See [LICENSE](./LICENSE) file for details.

```
Copyright (c) 2024 NOOR-404

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🔗 Related Resources

### Research Materials
- [Android Security & Privacy Documentation](https://developer.android.com/security)
- [OWASP Mobile Security Testing Guide](https://mobile-security.gitbook.io/)
- [Android Native Development Kit (NDK)](https://developer.android.com/ndk)
- [ELF Binary Format Specification](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format)

### Tools & Frameworks
- [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb)
- [Frida Instrumentation Framework](https://frida.re/)
- [Ghidra Reverse Engineering Suite](https://ghidra-sre.org/)
- [Radare2 Analysis Framework](https://rada.re/)

### Community & Learning
- [Android Security & Privacy Year in Review](https://security.googleblog.com/)
- [XDA Forums - Android Development](https://forum.xda-developers.com/)
- [Reverse Engineering Stack Exchange](https://reverseengineering.stackexchange.com/)

---

<div align="center">

### 🔐 NOOR-404

*Android Security • Native Analysis • SSL/TLS Research*

**Forged in the Storm. Tempered in the Tower. Delivering Research.**

---

[![GitHub Follow](https://img.shields.io/github/followers/NOOR-404?style=social)](https://github.com/NOOR-404)
[![Email Contact](https://img.shields.io/badge/Email-daniyaln.hossai%40gmail.com-00FFFF?style=social&logo=gmail)](mailto:daniyaln.hossai@gmail.com)
[![Telegram Channel](https://img.shields.io/badge/Telegram-@N__O__O__R__4__0__4-00FFFF?style=social&logo=telegram)](https://t.me/N_O_O_R_4_0_4)

</div>
