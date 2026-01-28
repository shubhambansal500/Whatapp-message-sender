# Fixing Proxy Authentication Issue

## The Problem

Android Studio is asking for proxy authentication for `127.0.0.1` (localhost). This happens when:
- A proxy server is configured in your system/Android Studio
- Gradle is trying to download dependencies through the proxy
- The proxy requires authentication

## Solutions

### Option 1: Disable Proxy in Android Studio (Recommended if you don't need it)

1. Open **Android Studio**
2. Go to **Preferences** (Mac) or **Settings** (Windows/Linux)
3. Navigate to **Appearance & Behavior** → **System Settings** → **HTTP Proxy**
4. Select **No proxy**
5. Click **Apply** and **OK**
6. **Invalidate Caches / Restart**: File → Invalidate Caches → Invalidate and Restart

### Option 2: Configure Proxy Properly

If you actually need a proxy:

1. In Android Studio: **Preferences** → **System Settings** → **HTTP Proxy**
2. Select **Manual proxy configuration**
3. Enter your proxy details:
   - **Host name**: Your proxy server
   - **Port number**: Proxy port (usually 8080 or 3128)
   - **Username** and **Password**: Your proxy credentials
4. Check **Remember** to save credentials
5. Click **Apply** and **OK**

### Option 3: Bypass Proxy for Localhost

I've already added this to `gradle.properties`:
```properties
systemProp.http.nonProxyHosts=localhost|127.0.0.1|*.local
systemProp.https.nonProxyHosts=localhost|127.0.0.1|*.local
```

This tells Gradle to bypass the proxy for localhost connections.

### Option 4: Enter Credentials in the Dialog

If you know your proxy credentials:
1. Enter your **Login** (username)
2. Enter your **Password**
3. Check **Remember** to save them
4. Click **OK**

## After Fixing

1. **Sync Gradle**: Click "Sync Now" or File → Sync Project with Gradle Files
2. If issues persist, try:
   ```bash
   ./gradlew clean
   ./gradlew --refresh-dependencies
   ```

## Still Having Issues?

If the problem persists:
1. Check if you have a VPN or network tool running that might be intercepting traffic
2. Check your system proxy settings (System Preferences → Network → Advanced → Proxies on Mac)
3. Try building from command line to see if it's an Android Studio-specific issue
