import os

def clear():
    os.system("clear")

def banner():
    print("=== Password Policy Analyzer ===\n")

def yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "n"):
            return ans == "y"

def audit(policy):
    results = []
    score = 0

    # Length check (NIST)
    if policy["length"] >= 8:
        results.append(("✔", f"Length ({policy['length']}): Meets NIST minimum"))
        score += 1
    else:
        results.append(("✖", f"Length ({policy['length']}): Below NIST minimum (8)"))

    # Complexity
    if policy["upper"] and policy["lower"] and policy["number"] and policy["special"]:
        results.append(("✔", "Complexity: Strong (all character types)"))
        score += 1
    else:
        results.append(("✖", "Complexity: Missing character types"))

    # Expiration
    if policy["expiry"] == 0 or policy["expiry"] >= 365:
        results.append(("✔", "Expiration: Meets NIST guidance"))
        score += 1
    else:
        results.append(("!", "Expiration: NIST discourages frequent rotation"))

    return results, score

def recommendations():
    print("\n=== NIST SP 800-63B Recommendations ===")
    print("- Use passphrases (12+ characters preferred)")
    print("- Allow all printable ASCII characters")
    print("- Avoid forced complexity rules")
    print("- Avoid periodic password resets")
    print("- Screen against breached password lists")
    print("- Use MFA where possible")

def main():
    clear()
    banner()

    print("Enter organisation password policy:\n")

    policy = {
        "length": int(input("Minimum length: ")),
        "upper": yes_no("Require uppercase? (y/n): "),
        "lower": yes_no("Require lowercase? (y/n): "),
        "number": yes_no("Require numbers? (y/n): "),
        "special": yes_no("Require special characters? (y/n): "),
        "expiry": int(input("Password expiry (days, 0 = never): "))
    }

    clear()
    banner()
    print("=== Policy Analysis (NIST SP 800-63B) ===\n")

    results, score = audit(policy)

    for symbol, message in results:
        print(f"{symbol} {message}")

    print(f"\nOverall Score: {score}/3")

    recommendations()

    input("\nPress Enter to return to portfolio...")

if __name__ == "__main__":
    main()
