# URGENT: Fix JDK/jlink Error

## The Problem

The `jlink` tool is failing when Gradle tries to create a JDK image. This is a known issue with Android Gradle Plugin 8.x and certain JDK versions.

## IMMEDIATE FIX (Do This Now)

### Step 1: Close Android Studio
**Completely quit Android Studio** (not just close the window).

### Step 2: Delete ALL Gradle Cache

Open **Terminal** and run:

```bash
# Delete ALL Gradle cache (this will force a fresh download)
rm -rf ~/.gradle/caches/
```

**OR** run the provided script:
```bash
cd /Users/shubham_bansal/Desktop/expedia/bex-userservice-internal-2/android-document-converter
./DELETE_CACHE.sh
```

### Step 3: Clean Project

```bash
cd /Users/shubham_bansal/Desktop/expedia/bex-userservice-internal-2/android-document-converter
rm -rf .gradle app/build build
```

### Step 4: Reopen Android Studio

1. Open Android Studio
2. **File → Invalidate Caches / Restart**
3. Select **"Invalidate and Restart"**
4. Wait for complete restart

### Step 5: Sync and Build

1. **File → Sync Project with Gradle Files**
2. Wait for sync (may take 5-10 minutes first time)
3. **Build → Rebuild Project**

## If Still Failing: Use System JDK

If the error persists, use a system JDK instead of Android Studio's bundled JDK:

### Download JDK 11:
1. Go to: https://adoptium.net/temurin/releases/?version=11
2. Download **macOS x64** JDK 11
3. Install it (it will be in `/Library/Java/JavaVirtualMachines/`)

### Configure Android Studio:
1. **File → Project Structure → SDK Location**
2. Under **JDK location**, click the folder icon
3. Navigate to: `/Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home`
4. Click **OK** and **Apply**
5. Sync project again

## Alternative: Reinstall Android SDK Platform

1. **Tools → SDK Manager**
2. **SDK Platforms** tab
3. Uncheck **Android 14.0 (API 34)** → **Apply**
4. Wait for uninstallation
5. Check **Android 14.0 (API 34)** again → **Apply**
6. Wait for reinstallation

## What I Changed

- Downgraded Android Gradle Plugin to 8.0.2 (more stable)
- Java version set to 11 (better compatibility)

## Why This Happens

The Android Gradle Plugin 8.x uses `jlink` to create custom JDK images. Sometimes the bundled JDK in Android Studio has issues with this process, especially on macOS. Using a system JDK usually resolves it.

## Still Not Working?

If none of the above works:
1. Update Android Studio to the latest version
2. Try using Android Gradle Plugin 7.4.2 (older but more stable)
3. Check Android Studio logs: **Help → Show Log in Finder**
