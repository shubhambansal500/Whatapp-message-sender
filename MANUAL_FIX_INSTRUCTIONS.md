# Manual Fix Instructions for JDK/jlink Error

The error persists because the Gradle cache needs to be manually cleared. Follow these steps:

## Step 1: Close Android Studio Completely

Make sure Android Studio is fully closed (not just minimized).

## Step 2: Delete Gradle Cache (Terminal)

Open Terminal and run:

```bash
# Delete the specific corrupted cache
rm -rf ~/.gradle/caches/transforms-3/a5c68e4f09964abcf4e266a99ad7bfe4

# Or delete all transforms cache (more thorough)
rm -rf ~/.gradle/caches/transforms-3/

# Delete all Gradle cache (nuclear option if above doesn't work)
rm -rf ~/.gradle/caches/
```

If you get "Operation not permitted" errors, you may need to:
1. Use `sudo` (not recommended unless necessary)
2. Or manually delete through Finder:
   - Press `Cmd+Shift+G` in Finder
   - Go to: `~/.gradle/caches/transforms-3/`
   - Delete the folder `a5c68e4f09964abcf4e266a99ad7bfe4`

## Step 3: Clean Project

In Terminal, navigate to the project and clean:

```bash
cd /Users/shubham_bansal/Desktop/expedia/bex-userservice-internal-2/android-document-converter
./gradlew clean
rm -rf .gradle
rm -rf app/build
rm -rf build
```

## Step 4: Reinstall Android SDK Platform (If Still Failing)

1. Open Android Studio
2. Go to **Tools → SDK Manager**
3. In **SDK Platforms** tab:
   - Uncheck **Android 14.0 (API 34)**
   - Click **Apply** to uninstall
   - Wait for uninstallation
   - Check **Android 14.0 (API 34)** again
   - Click **Apply** to reinstall
4. Wait for installation to complete

## Step 5: Invalidate Caches in Android Studio

1. In Android Studio: **File → Invalidate Caches / Restart**
2. Select **Invalidate and Restart**
3. Wait for restart

## Step 6: Sync and Build

1. **File → Sync Project with Gradle Files**
2. Wait for sync to complete
3. **Build → Rebuild Project**

## Alternative: Use System JDK

If the above doesn't work, try using a system JDK instead of Android Studio's bundled JDK:

1. Download JDK 11 or 17 from: https://adoptium.net/
2. Install it
3. In Android Studio: **File → Project Structure → SDK Location**
4. Under **JDK location**, browse to your installed JDK (e.g., `/Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home`)
5. Click **Apply** and **OK**
6. Sync project again

## What I Changed

I've also:
- Downgraded Android Gradle Plugin from 8.2.0 to 8.1.4 (more stable)
- Changed Java version from 17 to 11 (better compatibility)

Try the manual cache deletion first (Step 2), as that's the most likely fix.
