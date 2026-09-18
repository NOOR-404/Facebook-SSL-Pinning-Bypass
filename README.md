<div align="center">

<img src="https://github.com/user-attachments/assets/7fc5885c-dba1-44f7-9d18-bc7a0dc21a8a" alt="NOOR-404 Animated Header" width="100%">

<br><br>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=25&pause=900&color=00FF88&center=true&vCenter=true&width=850&lines=NOOR-404;Android+Security+Research;SSL%2FTLS+%7C+Native+Analysis;ARM64+%7C+x86+%7C+x86_64;Reverse+Engineering+Research" alt="NOOR-404 Typing Animation">

<br><br>

<img src="https://img.shields.io/badge/⚡_STATUS-ONLINE-00C853?style=for-the-badge&labelColor=101010">
<img src="https://img.shields.io/badge/ANDROID-SECURITY-3DDC84?style=for-the-badge&logo=android&logoColor=white">
<img src="https://img.shields.io/badge/ARM64-SUPPORTED-00C853?style=for-the-badge">
<img src="https://img.shields.io/badge/x86-SUPPORTED-00C853?style=for-the-badge">
<img src="https://img.shields.io/badge/x86__64-SUPPORTED-00C853?style=for-the-badge">

<br><br>

<img src="https://img.shields.io/github/stars/NOOR-404?style=for-the-badge&logo=github&label=STARS&color=00C853">
<img src="https://img.shields.io/github/forks/NOOR-404?style=for-the-badge&logo=github&label=FORKS&color=1976D2">
<img src="https://img.shields.io/github/last-commit/NOOR-404?style=for-the-badge&label=LAST%20UPDATE&color=FF9800">

<br><br>

<b>🔬 Native Analysis • 🔐 SSL/TLS Research • 📱 Android Security</b>

<br><br>

<img src="https://capsule-render.vercel.app/api?type=rect&height=3&color=00FF88&section=header" width="90%">

</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">
</p>

---

## 📌 About

**NOOR-404** is an Android security-research project focused on understanding SSL/TLS certificate validation, native Android libraries, and application security mechanisms.

The project is designed for controlled research environments where the researcher has authorization to inspect and modify the target application.

### ✨ Highlights

- 🔬 Native library research
- 🔐 SSL/TLS security analysis
- 🧩 Binary patching research
- 📱 Android application analysis
- 🖥️ Emulator & physical-device testing
- ⚡ Multi-architecture support
- 🛠️ Reverse-engineering research

---

## 🎯 Target Information

| Property | Details |
|:--|:--|
| **Project** | NOOR-404 |
| **Application** | Facebook |
| **Package** | `com.facebook.katana` |
| **Test Version** | `555.0.0.49.59` |
| **Native Library** | `libcoldstart.so` |
| **ARM64** | ✅ Supported |
| **x86** | ✅ Supported |
| **x86_64** | ✅ Supported |
| **Environment** | Android / Emulator |
| **Purpose** | Security Research |

> ⚠️ Native libraries are version-dependent. A library built for one application release should not be assumed to work with another release.

---

## 📂 Repository Structure

```text
NOOR-404/
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
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🧬 Architecture Support

| Architecture | Status | Typical Environment |
|:--|:--:|:--|
| **ARM64-v8a** | ✅ | Physical Android Devices |
| **x86** | ✅ | Android Emulators |
| **x86_64** | ✅ | Android Emulators |

### Library Layout

```text
ARM64/
└── libcoldstart.so

x86/
└── libcoldstart.so

x86_64/
└── libcoldstart.so
```

---

## 📱 Application Compatibility

```text
Package
com.facebook.katana

Version
555.0.0.49.59

Library
libcoldstart.so
```

The architecture of the library must match the architecture used by the target application environment.

---

## 🧪 Research Environment

A typical authorized testing environment may contain:

- Rooted Android device or emulator
- Matching Facebook APK
- Architecture-compatible native library
- HTTPS inspection proxy
- Configured test CA certificate
- ADB / Android file-management tools

Example workflow:

```text
Android Environment
        │
        ▼
Target Application
        │
        ▼
Native Library
        │
        ▼
TLS / Certificate Validation
        │
        ▼
Authorized Traffic Analysis
```

---

## ⚙️ Research Setup

### 01 — Prepare the Application

Install the compatible application version in your authorized testing environment.

Confirm:

```text
Package: com.facebook.katana
Version: 555.0.0.49.59
```

---

### 02 — Identify the Architecture

Select the library corresponding to the environment:

```text
ARM64-v8a  →  ARM64/libcoldstart.so

x86        →  x86/libcoldstart.so

x86_64     →  x86_64/libcoldstart.so
```

Using the wrong architecture can result in library-loading errors or application crashes.

---

### 03 — Preserve the Original Library

Before modifying the application, create a backup of the original native library.

Typical location:

```text
/data/data/com.facebook.katana/lib-compressed/libcoldstart.so
```

Keeping the original file makes it easier to restore the application.

---

### 04 — Configure Traffic Analysis

For an authorized security test, configure an HTTPS inspection tool such as:

```text
Reqable
Burp Suite
HTTP Canary
```

Install and configure the appropriate CA certificate according to the tool's documentation.

---

### 05 — Analyze the Test Traffic

Start the inspection environment and perform normal actions inside the authorized test account/environment.

Use the captured requests to study:

- TLS connections
- Certificate validation
- HTTP/HTTPS behavior
- Native networking components
- Application security controls

---

## 🔬 Research Areas

### Android Security

- Android application architecture
- Native `.so` libraries
- Application-private libraries
- Rooted test environments

### SSL/TLS

- Certificate validation
- Certificate pinning concepts
- Trust chains
- HTTPS interception
- TLS debugging

### Reverse Engineering

- ELF binaries
- Native code analysis
- Architecture differences
- Binary patching concepts
- Dynamic behavior analysis

---

## 🖥️ Emulator Support

The repository supports:

```text
x86
x86_64
```

For physical Android hardware:

```text
ARM64-v8a
```

Always use the native library that corresponds to the application's active ABI.

---

## 🛠️ Tools

Common tools for an authorized research environment:

| Tool | Purpose |
|:--|:--|
| **ADB** | Android debugging & file management |
| **MT Manager** | Android file inspection |
| **Reqable** | HTTPS traffic analysis |
| **Burp Suite** | Web/API security testing |
| **HTTP Canary** | Mobile traffic inspection |
| **Ghidra** | Native binary analysis |
| **IDA** | Reverse engineering |

---

## ⚠️ Compatibility Notes

### Version

Current research target:

```text
555.0.0.49.59
```

### Architecture

Supported:

```text
ARM64-v8a
x86
x86_64
```

### Important

Do not mix libraries between:

- Different application versions
- Different ABIs
- Different builds

Always verify the target version and architecture before testing.

---

## 🛡️ Responsible Use

This repository is intended for:

- Educational research
- Android security testing
- Reverse-engineering study
- Native-library analysis
- Controlled application testing
- Authorized HTTPS inspection

Only test applications, devices, accounts, and traffic for which you have permission.

Do not use this project for unauthorized interception, credential collection, session theft, account compromise, or privacy violations.

---

## 📜 Disclaimer

This project is provided for educational and authorized security-research purposes only.

The author does not encourage unauthorized modification or interception of third-party applications or user traffic.

You are responsible for complying with applicable laws, regulations, and service terms when using this repository.

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=100&section=footer&color=0:101010,50:003B2A,100:00C853" width="100%">
</p>

## 👤 NOOR-404

<div align="center">

<a href="https://github.com/NOOR-404">
<img src="https://img.shields.io/badge/GitHub-NOOR--404-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

<br><br>

**NOOR-404**

`Security Research • Reverse Engineering • Android`

<br>

<img src="https://img.shields.io/badge/ARM64-✓-00C853?style=flat-square">
<img src="https://img.shields.io/badge/x86-✓-00C853?style=flat-square">
<img src="https://img.shields.io/badge/x86__64-✓-00C853?style=flat-square">

<br><br>

**© NOOR-404**

</div>
