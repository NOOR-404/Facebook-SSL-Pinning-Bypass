<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00d1ff&height=200&section=header&text=NOOR-404&fontSize=70&animation=fadeIn" width="100%" />
  
  <br/>
  
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&pause=1000&color=00D1FF&center=true&vCenter=true&width=800&lines=>>+Facebook+SSL+Pinning+Research;>>+Native+Library+Analysis;>>+Android+Security+Research;>>+ARM64+%7C+x86_64+Architecture." alt="Typing SVG" />
  
  <p align="center">
    <img src="https://img.shields.io/badge/Status-Active_Research-00FF00?style=for-the-badge&logo=statuspage&logoColor=white" />
    <img src="https://img.shields.io/badge/Root-Required-FF003C?style=for-the-badge&logo=android&logoColor=white" />
    <img src="https://img.shields.io/badge/License-MIT-000000?style=for-the-badge&logoColor=00FFFF" />
  </p>

</div>

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## ⚡ PROJECT_OVERVIEW

**NOOR-404** is an advanced native-library research project focused on understanding SSL/TLS certificate-pinning mechanisms, native security implementations, and deep-level analysis workflows in Facebook's Android application.

🔬 **Research Focus:** Native security analysis, certificate validation, and TLS pinning mechanisms.

🎯 **Target Application:** Facebook for Android (com.facebook.katana)

⚙️ **Primary Library:** libcoldstart.so (ELF native binary)

🏗️ **Architectures:** ARM64 / ARM / x86 / x86_64

> ⚠️ **Research Notice:** This project is intended for authorized security research, reverse engineering, debugging, and educational analysis. Only test applications and devices for which you have permission.

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 📱 APPLICATION_INFO

| Property | Details |
|---|---|
| Application | Facebook for Android |
| Package Name | `com.facebook.katana` |
| Application Version | 578.0.0.40.75 |
| Platform | Android 6.0+ |
| Architecture Support | ARM64, ARM, x86, x86_64 |
| Root Access | Required |
| Primary Library | `libcoldstart.so` |
| Library Type | Native ELF ".so" binary |
| Binary Format | ELF (Executable and Linkable Format) |
| Research Area | SSL/TLS & Native Security |

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 📦 PACKAGE_INFORMATION

### Application Package
```
com.facebook.katana
```

### Native Library Target
```
libcoldstart.so
```

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 📍 LIBRARY_LOCATION

```
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

> **Note:** Filesystem layout varies between application versions, Android versions, installation methods, and device configurations.

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 🧩 NATIVE_LIBRARY_DETAILS

### libcoldstart.so Overview

`libcoldstart.so` is a native shared library used by the Android application. Native `.so` libraries are ELF binaries containing compiled native code, symbol tables, and relocation sections required by the application runtime.

### Research Analysis Points

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

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 🏗️ ARCHITECTURE_SUPPORT

| Architecture | EABI | Status | Device Examples |
|---|---|---|---|
| **ARM64-v8a** | ARM64 | ✅ Supported | Pixel 6+, Galaxy S20+, OnePlus 9+ |
| **armeabi-v7a** | ARMv7 | ✅ Supported | Older flagships, budget devices |
| **x86_64** | x86-64 | ✅ Supported | Android Studio Emulator, tablets |
| **x86** | x86 | ✅ Supported | Legacy emulators, some devices |

> **Important:** Architecture-specific analysis is critical because compiled instructions, binary layout, and security mechanisms differ significantly between builds.

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 🔐 SSL_PINNING_RESEARCH

### What is Certificate Pinning?

SSL/TLS certificate pinning is a security mechanism that restricts applications to accepting only specific certificates or public keys during TLS handshake. This prevents MITM attacks by validating that the server's certificate matches expected pins.

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

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 🧪 LIBCOLDSTART.SO_ANALYSIS

### Static Analysis Approach

The research workflow includes comprehensive static examination of `libcoldstart.so` across all supported architectures.

#### Binary Acquisition
```bash
adb pull /data/data/com.facebook.katana/lib-compressed/libcoldstart.so
file libcoldstart.so
# Output: ELF 64-bit LSB shared object, ARM aarch64, version 1 (SYSV)
```

#### ELF Header Analysis
- Magic bytes (0x7F ELF)
- Architecture (ARM64 / x86 / etc)
- Entry point address
- Program headers offset
- Section headers offset

#### Symbols & Functions
```bash
readelf -s libcoldstart.so | grep FUNC
nm -D libcoldstart.so | grep -i "ssl\|tls\|cert\|pin"
```

#### Section Analysis
- `.text` — Executable code
- `.rodata` — Read-only data (strings, constants)
- `.dynsym` — Dynamic symbol table
- `.dynstr` — Dynamic string table
- `.rel.dyn` / `.rela.dyn` — Relocation entries

#### String Extraction
```bash
strings libcoldstart.so | grep -i "certificate\|pin\|ssl\|tls\|verify"
```

#### Analysis Tools
- **IDA Pro:** Industry-standard disassembler with decompilation
- **Ghidra:** Free, open-source reverse engineering suite
- **Radare2:** Command-line hex editor and disassembler
- **Binary Ninja:** Modern reverse engineering platform

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 📂 IMPORTANT_PATHS

| Component | Path |
|---|---|
| **Package** | `com.facebook.katana` |
| **Library** | `libcoldstart.so` |
| **Full Path** | `/data/data/com.facebook.katana/lib-compressed/libcoldstart.so` |
| **Alternate** | `/data/data/com.facebook.katana/lib/libcoldstart.so` |
| **App Data** | `/data/data/com.facebook.katana/` |
| **Cache** | `/data/data/com.facebook.katana/cache/` |
| **Shared Prefs** | `/data/data/com.facebook.katana/shared_prefs/` |

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 🛠️ RESEARCH_ENVIRONMENT

| Component | Specification |
|---|---|
| **OS** | Android 6.0 or higher |
| **Target Package** | `com.facebook.katana` |
| **Native Binary** | `libcoldstart.so` |
| **Binary Format** | ELF (Executable and Linkable Format) |
| **Architectures** | ARM / ARM64 / x86 / x86_64 |
| **Access Level** | Root / Authorized Debug Environment |
| **Tools** | ADB, Frida, IDA/Ghidra, readelf, strings |
| **Purpose** | Security Research & Authorized Analysis |

### Recommended Tools
- Android Debug Bridge (ADB)
- Frida (Dynamic instrumentation)
- IDA Pro / Ghidra (Binary analysis)
- Radare2 (Lightweight analysis)
- Binary Ninja (Modern reverse engineering)
- readelf / nm / strings (ELF utilities)
- Android Studio (Emulator and debugging)

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 📌 VERSION_TRACKING

Version tracking is critical for accurate research:

```
Facebook Version : 578.0.0.40.75
Package Name     : com.facebook.katana
Target Library   : libcoldstart.so
Architecture     : ARM64
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

Always document your version baseline.

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 🌍 PROJECT_INFO

| Attribute | Value |
|---|---|
| **Location** | Bangladesh 🇧🇩 |
| **Project Name** | NOOR-404 |
| **Research Focus** | Android Native Security |
| **Specialization** | SSL/TLS, Certificate Pinning, Reverse Engineering |
| **Status** | Active Research |

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 📡 CONTACT_&_SOCIAL

<p align="center">
  <a href="https://github.com/NOOR-404">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
  <a href="https://t.me/N_O_O_R_4_0_4">
    <img src="https://img.shields.io/badge/Telegram-0088cc?style=for-the-badge&logo=telegram&logoColor=white"/>
  </a>
  <a href="mailto:daniyaln.hossai@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
</p>

| Platform | Link |
|---|---|
| **GitHub** | [github.com/NOOR-404](https://github.com/NOOR-404) |
| **Telegram** | [@N_O_O_R_4_0_4](https://t.me/N_O_O_R_4_0_4) |
| **Email** | [daniyaln.hossai@gmail.com](mailto:daniyaln.hossai@gmail.com) |

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## ⚖️ DISCLAIMER

This repository is provided for **authorized security research and educational purposes only**.

⚠️ **Legal Notice:**
- Do not use this project to intercept, modify, or inspect traffic on applications, accounts, devices, or networks without explicit authorization.
- Only conduct analysis on devices and applications for which you have legal permission.
- The author assumes no responsibility for misuse or unauthorized application of information contained herein.
- Compliance with applicable laws and regulations is your sole responsibility.

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 📜 LICENSE

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

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

<div align="center">
  <strong>🔐 NOOR-404 | Android Security Research | Native Analysis | SSL/TLS Investigation</strong>
  <br/>
  <em>Building security tools through deep technical research</em>
</div>
