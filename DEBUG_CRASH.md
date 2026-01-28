# Debugging App Crash During PDF Conversion

## What I Fixed

1. **Added comprehensive error handling** with try-catch blocks
2. **Added logging** throughout the conversion process
3. **Ensured conversion runs on IO dispatcher** (background thread)
4. **Added file validation** before processing
5. **Improved resource cleanup** in finally blocks

## How to Debug the Crash

### Step 1: Check Logcat

In Android Studio:
1. Open **Logcat** (bottom panel)
2. Filter by: `PdfToWordConverter` or `MainViewModel`
3. Look for error messages (red) when the crash happens
4. Copy the full stack trace

### Step 2: Common Issues and Fixes

#### Issue 1: "FileNotFoundException" or "Permission Denied"
**Fix**: The app might not have storage permissions
- Go to device Settings → Apps → Document Converter → Permissions
- Grant Storage permission
- Or grant permission when prompted in the app

#### Issue 2: "OutOfMemoryError"
**Fix**: PDF file is too large
- Try with a smaller PDF file first
- The app will handle this gracefully now with error messages

#### Issue 3: "PDFBox initialization error"
**Fix**: PDFBox Android might need initialization
- Check Logcat for specific error
- May need to add initialization code

#### Issue 4: "ClassNotFoundException" for PDFBox
**Fix**: Library not properly included
- Clean and rebuild: **Build → Clean Project**, then **Build → Rebuild Project**
- Check if `com.tom-roush:pdfbox-android:2.0.27.0` is in dependencies

### Step 3: Test with Simple PDF

1. Create a simple PDF with just text (no images, no complex formatting)
2. Try converting that first
3. If it works, the issue might be with complex PDFs

### Step 4: Check File Access

The app now logs:
- When file is being saved
- File size after saving
- When conversion starts
- Any errors during conversion

Check Logcat for these messages to see where it's failing.

## What to Share for Further Help

If the crash persists, share:
1. **Full Logcat output** (filter by your app package: `com.whatsappmessagesender.app`)
2. **The PDF file** you're trying to convert (if possible)
3. **Android version** of the emulator/device
4. **Error message** from the crash dialog

## Quick Test

Try this in Logcat to see what's happening:
```bash
adb logcat | grep -E "(PdfToWordConverter|MainViewModel|AndroidRuntime)"
```

This will show all relevant logs and the crash stack trace.
