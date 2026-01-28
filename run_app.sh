#!/bin/bash

# Script to help run the Android app on a connected device

echo "Document Converter - Device Setup Helper"
echo "========================================"
echo ""

# Check if adb is available
if ! command -v adb &> /dev/null; then
    echo "❌ ADB not found in PATH"
    echo "Please add Android SDK platform-tools to your PATH"
    echo "Or use Android Studio's built-in terminal"
    exit 1
fi

# Check for connected devices
echo "Checking for connected devices..."
DEVICES=$(adb devices | grep -v "List" | grep "device$" | wc -l | tr -d ' ')

if [ "$DEVICES" -eq 0 ]; then
    echo "❌ No devices found"
    echo ""
    echo "Please:"
    echo "1. Enable USB Debugging on your device"
    echo "2. Connect your device via USB"
    echo "3. Allow USB debugging when prompted"
    echo ""
    echo "To check devices manually, run: adb devices"
    exit 1
else
    echo "✅ Found $DEVICES device(s)"
    adb devices
    echo ""
fi

echo "To run the app:"
echo "1. Open Android Studio"
echo "2. Open the project: android-document-converter"
echo "3. Click the Run button (▶️)"
echo "4. Select your device from the list"
echo ""
echo "Or use Gradle directly:"
echo "  ./gradlew installDebug"
echo ""
