#!/bin/bash

# Quick fix script for JDK/jlink error
# Run this script to clean caches and rebuild

echo "Cleaning project..."
cd "$(dirname "$0")"
./gradlew clean
rm -rf .gradle
rm -rf app/build
rm -rf build

echo ""
echo "Cleaning Gradle cache (requires manual confirmation)..."
echo "Please run this command manually:"
echo "rm -rf ~/.gradle/caches/transforms-3/"
echo ""
echo "Or in Android Studio:"
echo "1. File → Invalidate Caches / Restart"
echo "2. Select 'Invalidate and Restart'"
echo ""
echo "After cleaning, try building again in Android Studio."
