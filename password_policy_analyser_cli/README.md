# Password Policy Analyser (CLI)


Audits organisational password policies.

## Features
- Benchmarked against NIST SP 800-63B guidelines
- Identifies weak or outdated requirements
- Provides remediation recommendations

## Usage
```bash
sudo python3 password_analyser.py

```
## Example Output

```text
=== Password Policy Analyzer ===

=== Policy Analysis (NIST SP 800-63B) ===

✔ Length (12): Meets NIST minimum
✔ Complexity: Strong (all character types)
✔ Expiration: Meets NIST guidance

Overall Score: 3/3

=== NIST SP 800-63B Recommendations ===
- Use passphrases (12+ characters preferred)
- Allow all printable ASCII characters
- Avoid forced complexity rules
- Avoid periodic password resets
- Screen against breached password lists
- Use MFA where possible

Press Enter to return to portfolio...

