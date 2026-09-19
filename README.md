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

<p align="center">
  <img src="https://github.com/Platane/snk/raw/output/github-contribution-grid-snake.svg" />
</p>

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 📱 APPLICATION_INFO

| Property | Details |
|---|---|
| Application | Facebook for Android |
| Package Name | `com.facebook.katana` |
| Application Version | Dynamic (version-dependent) |
| Platform | Android |
| Architecture Support | ARM64, ARM, x86, x86_64 |
| Root Access | Required |
| Primary Library | `libcoldstart.so` |
| Library Type | Native ELF ".so" binary |
| Research Area | SSL/TLS & Native Security |

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
        └── lib-compressed/
            └── libcoldstart.so
```

⚠️ **Note:** Filesystem layout varies between versions, Android versions, and installation methods.

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 🧬 ARCHITECTURE_SUPPORT

| Architecture | Status | Notes |
|---|---|---|
| ARM64-v8a | ✅ Supported | Modern 64-bit ARM |
| armeabi-v7a / ARM | ✅ Supported | Legacy 32-bit ARM |
| x86 | ✅ Supported | 32-bit Intel |
| x86_64 | ✅ Supported | 64-bit Intel |

Architecture-specific analysis is critical because compiled instructions and binary layouts differ significantly between builds.

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 🔐 SSL_PINNING_RESEARCH

SSL/TLS certificate pinning is a security mechanism that restricts applications to accepting only expected certificates or public keys during TLS communication.

This research examines the **native-side implementation** of pinning, particularly security-sensitive functionality embedded in native libraries.

### Research Flow
```
Application Layer
    ↓
Java / Kotlin Interface
    ↓
JNI / Native Bridge
    ↓
Native Libraries
    ↓
TLS / Certificate Validation
    ↓
Network Communication
```

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 🧪 LIBCOLDSTART.SO_ANALYSIS

### Static Examination Areas

```
ELF Binary Structure
├── Architecture Detection
├── Entry Point Mapping
├── Program Headers
└── Section Headers

Native Code Analysis
├── Function Extraction
├── String References
├── Cross-Reference Mapping
└── Control Flow Analysis

Security Assessment
├── TLS-Related Routines
├── Certificate Handling
├── Native Validation Logic
└── JNI Interactions
```

### Analysis Methodology
- **Static Analysis:** IDA Pro, Ghidra, Radare2
- **Dynamic Analysis:** Frida instrumentation, native debugging
- **String Analysis:** Symbol extraction and cross-referencing
- **Control Flow:** Function call chains and dependency mapping

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## ⚙️ RESEARCH_ENVIRONMENT

| Component | Specification |
|---|---|
| Operating System | Android (rooted device/emulator) |
| Target Package | `com.facebook.katana` |
| Native Binary | `libcoldstart.so` |
| Binary Format | ELF 64-bit / 32-bit |
| Supported Architectures | ARM / ARM64 / x86 / x86_64 |
| Access Level | Root / Debug Environment |
| Analysis Tools | Ghidra, IDA, Frida, Radare2 |
| Purpose | Security Research & Analysis |

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 📌 VERSION_TRACKING

Native libraries change between releases. Always record exact application versions during analysis.

```
Facebook Version: 578.0.0.40.75
Package:          com.facebook.katana
Library:          libcoldstart.so
Architecture:     ARM64-v8a
Analysis Date:    [DATE_HERE]
```

Version tracking is critical because library structure and security implementations vary significantly between releases.

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 🌍 PROJECT_INFO

| Attribute | Value |
|---|---|
| Location | Bangladesh 🇧🇩 |
| Project Name | NOOR-404 |
| Research Focus | Android Native Security |
| Primary Domain | SSL/TLS Analysis |

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## 📡 CONTACT_&_SOCIAL

<p align="center">
  <a href="https://discord.gg/8k9R7Bv4">
    <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white"/>
  </a>
  <a href="https://t.me/N_O_O_R_4_0_4">
    <img src="https://img.shields.io/badge/Telegram-0088cc?style=for-the-badge&logo=telegram&logoColor=white"/>
  </a>
  <a href="https://github.com/NOOR-404">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
  <a href="mailto:daniyaln.hossai@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
</p>

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

## ⚖️ DISCLAIMER

This repository is provided for **authorized security research and educational purposes only**.

⚠️ **Legal Notice:**
- Do not use this project to intercept, modify, or inspect traffic on applications, accounts, devices, or networks without explicit authorization.
- Only conduct analysis on devices and applications for which you have legal permission.
- The author assumes no responsibility for misuse or unauthorized application of information contained herein.
- Compliance with applicable laws and regulations is your sole responsibility.

<img src="https://raw.githubusercontent.com/NOOR-404/NOOR-404/refs/heads/main/Assests/Rainbow.gif" width="100%">

<div align="center">
  <strong>🔐 NOOR-404 | Android Security Research | Native Analysis | SSL/TLS Investigation</strong>
  <br/>
  <em>Building security tools through deep technical research</em>
</div>
