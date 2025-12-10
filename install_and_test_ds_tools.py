import subprocess
import importlib

# List of libraries to install and test
packages = [
    "numpy", "pandas", "matplotlib", "seaborn",
    "scikit-learn", "plotly", "statsmodels",
    "xgboost", "lightgbm"
]

print("🔧 Installing packages...\n")

# Step 1: Install all packages using pip
subprocess.call(["pip", "install", *packages])

print("\n✅ Installation complete.\n")
print("🔍 Now testing imports:\n")

# Step 2: Test importing each package
for pkg in packages:
    try:
        importlib.import_module(pkg)
        print(f"✅ {pkg} imported successfully.")
    except ImportError:
        print(f"❌ Failed to import {pkg}. Please check installation.")

print("\n🎉 Done!")
