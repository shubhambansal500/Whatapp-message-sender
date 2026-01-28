# Quick Start Guide

## 🚀 Get Running in 5 Minutes

### 1. Open in Android Studio
```
File > Open > Select "android-document-converter" folder
```

### 2. Wait for Gradle Sync
- First time: 5-10 minutes (downloading dependencies)
- Subsequent: 1-2 minutes

### 3. Connect Your Phone
- Enable Developer Options (tap Build Number 7 times)
- Enable USB Debugging
- Connect via USB
- Allow USB debugging when prompted

### 4. Run the App
- Click the green ▶️ Run button
- Select your device
- App installs and launches automatically!

## 📱 Testing

1. **PDF → Word:**
   - Tap "Select File" → Choose PDF → Tap "Convert"
   - Find output in: Downloads/DocumentConverter/

2. **Word → PDF:**
   - Tap "Select File" → Choose Word file → Tap "Convert"
   - Find output in: Downloads/DocumentConverter/

## ⚠️ Troubleshooting

**No device found?**
```bash
adb devices
# If empty, check USB debugging is enabled
```

**Build fails?**
- File > Invalidate Caches / Restart
- Check internet connection (needed for first build)

**App crashes?**
- Check Logcat in Android Studio
- Grant storage permissions when prompted

## 📦 For Play Store

See `README.md` for complete publishing guide.

Key steps:
1. Generate signing keystore
2. Update version in `app/build.gradle.kts`
3. Build release: `./gradlew bundleRelease`
4. Upload to Google Play Console
