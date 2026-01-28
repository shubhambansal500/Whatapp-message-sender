# Quick Setup Guide for Running on Your Device

## Step 1: Install Android Studio

1. Download Android Studio from: https://developer.android.com/studio
2. Install it following the installation wizard
3. Open Android Studio and let it complete the initial setup

## Step 2: Open the Project

1. Open Android Studio
2. Click "Open" (or File > Open)
3. Navigate to: `/Users/shubham_bansal/Desktop/expedia/bex-userservice-internal-2/android-document-converter`
4. Click "OK"
5. Wait for Gradle to sync (this may take a few minutes on first run)

## Step 3: Enable Developer Options on Your Android Device

1. On your Android phone, go to **Settings**
2. Scroll down to **About Phone** (or **About Device**)
3. Find **Build Number** and tap it **7 times**
4. You'll see a message saying "You are now a developer!"
5. Go back to Settings and you'll see **Developer Options**

## Step 4: Enable USB Debugging

1. Open **Developer Options** in Settings
2. Enable **USB Debugging**
3. Connect your phone to your computer via USB cable
4. On your phone, you may see a prompt asking to "Allow USB debugging" - tap **Allow**

## Step 5: Verify Device Connection

1. Open Terminal (on Mac) or Command Prompt (on Windows)
2. Navigate to the Android SDK platform-tools directory (usually in Android Studio's installation)
   - Or use: `adb` if it's in your PATH
3. Run: `adb devices`
4. You should see your device listed (e.g., "ABC123XYZ    device")

If you don't see your device:
- Make sure USB debugging is enabled
- Try a different USB cable
- Try a different USB port
- On your phone, check if there's a notification about USB connection - select "File Transfer" or "MTP" mode

## Step 6: Run the App

1. In Android Studio, click the green **Run** button (▶️) at the top
2. Or go to **Run > Run 'app'**
3. Select your device from the list
4. Click **OK**
5. Android Studio will build the app and install it on your device
6. The app will automatically launch on your device!

## Troubleshooting

### "No devices found"
- Make sure USB debugging is enabled
- Try: `adb kill-server` then `adb start-server`
- Unplug and replug your USB cable
- Restart Android Studio

### "Gradle sync failed"
- Check your internet connection (Gradle needs to download dependencies)
- In Android Studio: File > Invalidate Caches / Restart
- Try: `./gradlew clean` in Terminal

### "Build failed"
- Make sure you have JDK 17 installed
- In Android Studio: File > Project Structure > SDK Location
- Check that Android SDK is properly configured

### App crashes on device
- Check Logcat in Android Studio for error messages
- Make sure your device is running Android 8.0 (API 26) or higher
- Grant storage permissions when prompted

## Testing the App

Once the app is running:

1. **Test PDF to Word:**
   - Tap "Select File" under "PDF to Word"
   - Choose a PDF file
   - Tap "Convert"
   - Check Downloads/DocumentConverter folder for the converted file

2. **Test Word to PDF:**
   - Tap "Select File" under "Word to PDF"
   - Choose a Word file (.docx or .doc)
   - Tap "Convert"
   - Check Downloads/DocumentConverter folder for the converted file

## Next Steps for Play Store

When you're ready to publish:

1. **Create a release keystore** (for signing the app)
2. **Update version numbers** in `app/build.gradle.kts`
3. **Build a release APK or AAB**
4. **Create a Google Play Console account** ($25 one-time fee)
5. **Upload your app** to Play Console

See the main README.md for detailed Play Store publishing instructions.
