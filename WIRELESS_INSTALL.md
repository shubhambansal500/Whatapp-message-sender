# Wireless APK Installation Guide

## Method 1: Build APK and Transfer Wirelessly (Recommended)

### Step 1: Build the APK

In Android Studio:
1. **Build → Build Bundle(s) / APK(s) → Build APK(s)**
2. Wait for build to complete
3. When done, click **locate** in the notification

**OR** use Terminal:
```bash
cd /Users/shubham_bansal/Desktop/expedia/bex-userservice-internal-2/android-document-converter
./gradlew assembleDebug
```

The APK will be at:
```
app/build/outputs/apk/debug/app-debug.apk
```

### Step 2: Transfer APK to Phone Wirelessly

#### Option A: Using Google Drive / Dropbox / AirDrop
1. Upload `app-debug.apk` to:
   - **Google Drive** (if you have Gmail)
   - **Dropbox**
   - **AirDrop** (if you have a Mac and iPhone nearby)
   - **Email** it to yourself
2. Open the link/file on your phone
3. Download the APK
4. Install it (see Step 3)

#### Option B: Using ADB Wirelessly (Android 11+)
1. **Enable Wireless Debugging** on your phone:
   - Settings → Developer Options → Wireless Debugging
   - Enable it
   - Tap "Pair device with pairing code"
   - Note the IP address, port, and pairing code

2. **Connect via ADB** (Terminal on Mac):
   ```bash
   adb pair <IP_ADDRESS>:<PORT>
   # Enter the pairing code when prompted
   adb connect <IP_ADDRESS>:<PORT>
   ```

3. **Install APK wirelessly**:
   ```bash
   adb install app/build/outputs/apk/debug/app-debug.apk
   ```

#### Option C: Using a File Sharing App
1. Install a file sharing app on both devices (e.g., **Send Anywhere**, **ShareIt**)
2. Send the APK from your computer to your phone
3. Install it (see Step 3)

### Step 3: Install APK on Phone

1. **Enable "Install from Unknown Sources"**:
   - Go to **Settings → Security** (or **Apps → Special Access**)
   - Enable **"Install unknown apps"** or **"Unknown sources"**
   - Select the app you'll use to install (Chrome, Files, etc.)

2. **Open the APK file** on your phone:
   - If downloaded, tap the notification
   - Or open Files app and navigate to Downloads
   - Tap the APK file

3. **Install**:
   - Tap **Install**
   - Wait for installation
   - Tap **Open** to launch the app

## Method 2: Direct Wireless Installation via ADB

### Setup (One-time)

1. **Enable Wireless Debugging** on your phone:
   - Settings → Developer Options → Wireless Debugging
   - Enable it

2. **Pair your computer**:
   ```bash
   # Get pairing info from phone
   adb pair <IP>:<PORT>
   # Enter pairing code
   
   # Connect
   adb connect <IP>:<PORT>
   ```

3. **Verify connection**:
   ```bash
   adb devices
   # Should show your device
   ```

### Build and Install in One Command

```bash
cd /Users/shubham_bansal/Desktop/expedia/bex-userservice-internal-2/android-document-converter

# Build and install directly
./gradlew installDebug
```

This builds the APK and installs it wirelessly on your connected device!

## Method 3: Using Android Studio Wirelessly

### Setup Wireless Debugging

1. **On your phone**:
   - Settings → Developer Options → Wireless Debugging
   - Enable it
   - Note the IP address and port

2. **In Android Studio**:
   - Run → Edit Configurations
   - Or just use the Run button - it should detect wireless devices

3. **Connect**:
   - Android Studio will show your wireless device
   - Select it and run the app
   - It will build and install automatically

## Quick Reference

### Build APK Location
```
android-document-converter/app/build/outputs/apk/debug/app-debug.apk
```

### Build Commands
```bash
# Build debug APK
./gradlew assembleDebug

# Build and install wirelessly (if ADB connected)
./gradlew installDebug

# Build release APK (for Play Store)
./gradlew assembleRelease
```

### ADB Wireless Commands
```bash
# Pair device
adb pair <IP>:<PORT>

# Connect
adb connect <IP>:<PORT>

# Install APK
adb install app/build/outputs/apk/debug/app-debug.apk

# Check connected devices
adb devices
```

## Troubleshooting

### "Install blocked" on phone
- Enable "Install from Unknown Sources" in Settings
- Allow the specific app (Chrome, Files) to install apps

### ADB not found
- Make sure Android SDK platform-tools is in your PATH
- Or use full path: `~/Library/Android/sdk/platform-tools/adb`

### Wireless debugging not working
- Make sure phone and computer are on the same WiFi network
- Try disabling and re-enabling Wireless Debugging
- Restart ADB: `adb kill-server && adb start-server`

## Recommended Workflow

**For quick testing:**
1. Use **Method 2** (Wireless ADB) - fastest once set up
2. Or use **Method 3** (Android Studio wireless) - most convenient

**For sharing with others:**
1. Use **Method 1, Option A** (Google Drive/Email) - easiest to share
