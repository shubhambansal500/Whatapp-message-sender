# Production Release Checklist

## Pre-Release

### Code Quality
- [x] All test cases written and passing
- [x] Code reviewed and commented
- [x] No debug code in release builds
- [x] ProGuard rules configured
- [x] Error handling implemented
- [x] Logging configured (debug only)

### Build Configuration
- [x] Version code and name set correctly
- [x] Signing configuration ready
- [x] Minify and shrink resources enabled for release
- [x] Build variants configured (debug/release)

### Play Store Compliance
- [x] Privacy Policy created
- [x] No unnecessary permissions
- [x] Content rating: Everyone
- [x] App description and screenshots ready
- [x] Feature graphic created
- [x] Data safety section completed

### Testing
- [x] Unit tests passing
- [x] UI tests passing
- [x] Manual testing on multiple devices
- [x] Tested on different Android versions (5.0+)
- [x] Tested with WhatsApp installed
- [x] Tested with WhatsApp Business installed
- [x] Tested without WhatsApp installed (error handling)

### Security
- [x] No hardcoded secrets
- [x] ProGuard enabled
- [x] No debug logging in release
- [x] Secure data handling (none in this app)

### Performance
- [x] App size optimized
- [x] No memory leaks
- [x] Fast startup time
- [x] Smooth UI interactions

## Release Steps

1. **Build Release APK/AAB**
   ```bash
   ./gradlew assembleRelease
   # or
   ./gradlew bundleRelease
   ```

2. **Test Release Build**
   - Install release APK on test device
   - Verify all features work
   - Check ProGuard didn't break anything

3. **Create Keystore** (if not exists)
   ```bash
   keytool -genkey -v -keystore whatsapp-sender-release.jks \
     -keyalg RSA -keysize 2048 -validity 10000 \
     -alias whatsapp-sender
   ```

4. **Configure Signing**
   - Add keystore to `app/` directory
   - Configure in `build.gradle.kts` or `local.properties`
   - **NEVER commit keystore to git**

5. **Upload to Play Store**
   - Create app listing
   - Upload AAB file
   - Add screenshots
   - Add feature graphic
   - Complete store listing
   - Complete content rating
   - Complete data safety section
   - Submit for review

## Post-Release

- [ ] Monitor crash reports
- [ ] Monitor user reviews
- [ ] Monitor analytics (if added)
- [ ] Plan updates based on feedback

## Version Management

- Increment `versionCode` for each release
- Update `versionName` following semantic versioning (MAJOR.MINOR.PATCH)
- Update "What's New" section in Play Store

## Signing Configuration

Add to `local.properties` (DO NOT COMMIT):
```properties
RELEASE_STORE_FILE=whatsapp-sender-release.jks
RELEASE_STORE_PASSWORD=your_store_password
RELEASE_KEY_ALIAS=whatsapp-sender
RELEASE_KEY_PASSWORD=your_key_password
```

Then in `build.gradle.kts`:
```kotlin
signingConfigs {
    create("release") {
        val keystorePropertiesFile = rootProject.file("local.properties")
        if (keystorePropertiesFile.exists()) {
            val keystoreProperties = java.util.Properties()
            keystoreProperties.load(java.io.FileInputStream(keystorePropertiesFile))
            
            storeFile = file(keystoreProperties["RELEASE_STORE_FILE"] as String)
            storePassword = keystoreProperties["RELEASE_STORE_PASSWORD"] as String
            keyAlias = keystoreProperties["RELEASE_KEY_ALIAS"] as String
            keyPassword = keystoreProperties["RELEASE_KEY_PASSWORD"] as String
        }
    }
}

buildTypes {
    release {
        signingConfig = signingConfigs.getByName("release")
        // ... other config
    }
}
```
