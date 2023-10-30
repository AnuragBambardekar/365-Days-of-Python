# PyArmor

```cmd
pip install pyarmor
```

PyArmor is a tool designed to protect Python scripts and applications by obfuscating and encrypting the code, making it more challenging for others to reverse-engineer or tamper with your Python software. 

**It's not difficult to reverse this. Don't think that if we publish this, people are not going to be able to reverse this and understand it.**

## PyArmor Features:

Code Obfuscation: PyArmor renames variables, functions, and classes within your Python code, making it harder for someone to understand the code by reading it.

Code Encryption: Sensitive parts of your Python code can be encrypted to protect against unauthorized access and tampering.

License Management: PyArmor provides tools for managing licenses, controlling how your software is distributed, and ensuring that only authorized users can run your application.

Platform Compatibility: PyArmor is compatible with various Python versions and can be used on different operating systems, making it versatile for protecting your Python projects.

Integration: It can be integrated into your build process or deployment pipeline to automatically protect your Python code before distribution.

## Use Cases for PyArmor:

Commercial Software: If you're developing commercial software in Python, PyArmor can help protect your intellectual property by making it more difficult for others to reverse-engineer and pirate your software.

Confidential Information: If your Python code contains sensitive information, such as proprietary algorithms or confidential data, PyArmor can be used to encrypt and obfuscate this information to prevent unauthorized access.

Licensing and Distribution Control: PyArmor enables you to control the distribution of your software through licensing, ensuring that only authorized users can execute your application.

## Options to protect script

Using --enable-jit tells Pyarmor processes some sensitive data by c function generated in runtime.

Using --mix-str 1 could mix the string constant (length > 8) in the scripts.

Using --assert-call makes sure function is obfuscated, to prevent called function from being replaced by special ways

Using --private makes the script could not be imported by plain scripts

## What's the most security pyarmor could do?

The following options could improve security

--enable-rft almost doesn’t impact performance

--enable-bcc may be a little faster than a plain script, but it consumes more memory to load binary code

--enable-jit prevents static decompilation

--enable-themida prevents most of debuggers, only available in Windows, and reduces performance remarkably

--mix-str protects string constants in the script

pyarmor cfg mix_argnames=1 may broken annotations

--obf-code 2 could make it more difficult to reverse byte code


## For Django application or serving web request

If RFT mode is safe enough, you can check the transformed scripts to make a decision, using these options

--enable-rft

--obf-code 0

--obf-module 0

--mix-str with filter

If RFT mode is not safe enough, using these options

--enable-rft

--no-wrap

--mix-str with filter