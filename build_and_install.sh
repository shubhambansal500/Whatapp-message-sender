#!/bin/bash

# Script to build APK and optionally install wirelessly

echo "=========================================="
echo "Document Converter - Build & Install"
echo "=========================================="
echo ""

cd "$(dirname "$0")"

# Check if ADB is available
if command -v adb &> /dev/null; then
    echo "ADB found. Checking for connected devices..."
    DEVICES=$(adb devices | grep -v "List" | grep "device$" | wc -l | tr -d ' ')
    
    if [ "$DEVICES" -gt 0 ]; then
        echo "✅ Found $DEVICES device(s) connected"
        adb devices
        echo ""
        read -p "Do you want to build and install directly? (y/n): " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo "Building and installing..."
            ./gradlew installDebug
            echo ""
            echo "✅ App installed! Check your device."
            exit 0
        fi
    else
        echo "⚠️  No devices found via ADB"
        echo "   To connect wirelessly:"
        echo "   1. Enable Wireless Debugging on your phone"
        echo "   2. Run: adb pair <IP>:<PORT>"
        echo "   3. Run: adb connect <IP>:<PORT>"
        echo ""
    fi
else
    echo "⚠️  ADB not found in PATH"
    echo "   Install Android SDK platform-tools or use Android Studio"
    echo ""
fi

# Build APK
echo "Building APK..."
./gradlew assembleDebug

if [ $? -eq 0 ]; then
    APK_PATH="app/build/outputs/apk/debug/app-debug.apk"
    echo ""
    echo "✅ APK built successfully!"
    echo ""
    echo "APK location:"
    echo "  $APK_PATH"
    echo ""
    echo "To install on your phone:"
    echo "  1. Transfer APK to your phone (Google Drive, Email, AirDrop, etc.)"
    echo "  2. Enable 'Install from Unknown Sources' in phone settings"
    echo "  3. Open the APK file on your phone and install"
    echo ""
    echo "Or use ADB to install:"
    echo "  adb install $APK_PATH"
    echo ""
    
    # Try to open the folder (Mac)
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open "$(dirname "$APK_PATH")"
    fi
else
    echo ""
    echo "❌ Build failed. Check the errors above."
    exit 1
fi
