import os

def clear():
    os.system("clear")

def show_banner(title):
    clear()
    print("=" * 40)
    print(f"  {title}")
    print("=" * 40)
    print()
