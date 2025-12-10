# symbols_menu.py
# A menu-driven program to display useful symbols & emojis

def show_general():
    print("\n✅ General Indicators")
    print("✔ Correct       (\\u2714)")
    print("✖ Wrong         (\\u2716)")
    print("⚠ Warning       (\\u26A0)")
    print("❌ Cross mark    (\\u274C)")
    print("✅ Check mark    (\\u2705)")
    print("ℹ Info          (\\u2139)")

def show_fun():
    print("\n🎉 Fun / Feedback")
    print("🎉 Celebration   (\\U0001F389)")
    print("👏 Clap          (\\U0001F44F)")
    print("🔥 Fire          (\\U0001F525)")
    print("⚡ Power         (\\u26A1)")
    print("🌟 Star          (\\U0001F31F)")
    print("💡 Idea          (\\U0001F4A1)")

def show_math():
    print("\n🔢 Math & Logic")
    print("π Pi            (\\u03C0)")
    print("√ Square root   (\\u221A)")
    print("∑ Summation     (\\u2211)")
    print("∞ Infinity      (\\u221E)")
    print("≠ Not equal     (\\u2260)")
    print("≤ Less equal    (\\u2264)")
    print("≥ Greater equal (\\u2265)")

def show_arrows():
    print("\n🔀 Navigation & Arrows")
    print("→ Right arrow   (\\u2192)")
    print("← Left arrow    (\\u2190)")
    print("↑ Up arrow      (\\u2191)")
    print("↓ Down arrow    (\\u2193)")
    print("↔ Left-right    (\\u2194)")
    print("⇨ Heavy right   (\\u21E8)")

def show_games():
    print("\n🎮 Games / Console")
    print("🎲 Dice         (\\U0001F3B2)")
    print("🎯 Target       (\\U0001F3AF)")
    print("🏆 Trophy       (\\U0001F3C6)")
    print("❤️ Heart        (\\u2764)")
    print("💀 Skull        (\\U0001F480)")
    print("👑 Crown        (\\U0001F451)")

def show_system():
    print("\n⚙ System / Tools")
    print("🖥 Computer     (\\U0001F5A5)")
    print("📂 Folder       (\\U0001F4C2)")
    print("📊 Chart        (\\U0001F4CA)")
    print("🔑 Key          (\\U0001F511)")
    print("🔒 Locked       (\\U0001F512)")
    print("🔓 Unlocked     (\\U0001F513)")

def show_shapes():
    print("\n🔷 Geometrical Shapes")
    print("■ Square        (\\u25A0)")
    print("□ Hollow Sq.    (\\u25A1)")
    print("▲ Triangle Up   (\\u25B2)")
    print("▼ Triangle Down (\\u25BC)")
    print("◆ Diamond       (\\u25C6)")
    print("○ Circle        (\\u25CB)")
    print("● Filled Circle (\\u25CF)")
    print("◯ Large Circle  (\\u25EF)")
    print("▭ Rectangle     (\\u25AD)")
    print("⬟ Hexagon       (\\u2B1F)")
    print("⬢ Filled Hex    (\\u2B22)")
    print("⬣ Star Shape    (\\u2B23)")

def show_all():
    show_general()
    show_fun()
    show_math()
    show_arrows()
    show_games()
    show_system()
    show_shapes()

# ---- Main Menu ----
while True:
    print("\n====== SYMBOLS & EMOJIS MENU ======")
    print("1. General Indicators")
    print("2. Fun / Feedback")
    print("3. Math & Logic")
    print("4. Navigation & Arrows")
    print("5. Games / Console")
    print("6. System / Tools")
    print("7. Geometrical Shapes")
    print("8. Exit")
    print("9. Show ALL Categories")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        show_general()
    elif choice == "2":
        show_fun()
    elif choice == "3":
        show_math()
    elif choice == "4":
        show_arrows()
    elif choice == "5":
        show_games()
    elif choice == "6":
        show_system()
    elif choice == "7":
        show_shapes()
    elif choice == "8":
        print("👋 Exiting... Have fun with symbols & emojis!")
        break
    elif choice == "9":
        show_all()
    else:
        print("⚠ Invalid choice! Try again.")
