# Fixing JDK/jlink Error

## The Problem

Gradle is failing when trying to use `jlink` to create a JDK image. This is usually caused by:
- Corrupted Gradle cache
- Issues with Android Studio's bundled JDK
- Missing Android SDK components

## Solutions (Try in Order)

### Solution 1: Clean Gradle Cache (Most Common Fix)

1. **Close Android Studio**

2. **Delete Gradle cache:**
   ```bash
   rm -rf ~/.gradle/caches/
   ```

3. **Delete project build folders:**
   ```bash
   cd android-document-converter
   ./gradlew clean
   rm -rf .gradle
   rm -rf app/build
   ```

4. **Reopen Android Studio and sync**

### Solution 2: Invalidate Caches in Android Studio

1. In Android Studio: **File → Invalidate Caches / Restart**
2. Select **Invalidate and Restart**
3. Wait for Android Studio to restart and reindex

### Solution 3: Check Android SDK Installation

1. In Android Studio: **Tools → SDK Manager**
2. Go to **SDK Platforms** tab
3. Make sure **Android 14.0 (API 34)** is installed
4. Go to **SDK Tools** tab
5. Make sure **Android SDK Build-Tools** is installed
6. Click **Apply** to install any missing components

### Solution 4: Update Gradle Wrapper

The project might need a newer Gradle version. Check `gradle/wrapper/gradle-wrapper.properties` and ensure it's using a recent version.

### Solution 5: Use System JDK Instead of Bundled JDK

1. In Android Studio: **File → Project Structure → SDK Location**
2. Under **JDK location**, try selecting a system JDK instead of the bundled one
3. Or download JDK 17 from: https://adoptium.net/

### Solution 6: Reinstall Android SDK Platform

1. In Android Studio: **Tools → SDK Manager**
2. Uncheck **Android 14.0 (API 34)**
3. Click **Apply** to uninstall
4. Check it again and click **Apply** to reinstall

## Quick Command Line Fix

Run these commands in terminal:

```bash
cd /Users/shubham_bansal/Desktop/expedia/bex-userservice-internal-2/android-document-converter

# Clean everything
./gradlew clean
rm -rf .gradle
rm -rf app/build
rm -rf build

# Clear Gradle cache
rm -rf ~/.gradle/caches/transforms-3/

# Rebuild
./gradlew build --refresh-dependencies
```

## If Nothing Works

1. **Update Android Studio** to the latest version
2. **Update Android Gradle Plugin** in `build.gradle.kts`
3. **Check Android Studio logs**: Help → Show Log in Finder
