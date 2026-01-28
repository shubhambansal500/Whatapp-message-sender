# WhatsApp Message Sender

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-green.svg)](LICENSE)

A simple, **completely open source** Android app that allows users to open a WhatsApp chat with a phone number without saving the contact.

**100% Free and Open Source** - No proprietary code, no hidden dependencies, fully transparent.

## Features

- **No Contact Saving Required**: Open WhatsApp chats directly using phone numbers
- **Country Code Support**: Default country code (+91) with customizable input
- **Optional Message**: Pre-fill message text (user must still manually send)
- **Clean Material Design UI**: Modern, minimal interface
- **Offline App**: No backend, no login, fully offline
- **Play Store Compliant**: Uses official WhatsApp deep links only

## How It Works

The app uses WhatsApp's official deep link format:
```
https://wa.me/{country_code}{phone_number}?text={encoded_message}
```

### Example:
- Country Code: `+91`
- Phone Number: `9876543210`
- Message: `Hello!`

Result URL: `https://wa.me/919876543210?text=Hello%21`

When the user clicks "Send Message", the app:
1. Validates the phone number (non-empty, numeric, minimum 7 digits)
2. Builds the WhatsApp deep link URL
3. Opens WhatsApp using an Intent
4. If WhatsApp is not installed, shows a Toast message

**Note**: The app does NOT auto-send messages. Users must manually tap the send button inside WhatsApp.

## Technical Details

### Requirements
- **Min SDK**: 21 (Android 5.0 Lollipop)
- **Target SDK**: 34
- **Language**: Kotlin
- **Architecture**: Single Activity

### Dependencies
- Material Design Components
- AndroidX Core KTX
- AndroidX AppCompat
- ConstraintLayout

### Permissions
**No permissions required!** The app only uses Intent to open WhatsApp, which doesn't require any special permissions.

### Code Structure

```
app/src/main/
├── java/com/whatsappmessagesender/app/ui/
│   └── MainActivity.kt          # Main activity with all logic
├── res/
│   ├── layout/
│   │   └── activity_main.xml    # UI layout
│   └── values/
│       └── strings.xml          # String resources
└── AndroidManifest.xml          # App configuration
```

## Building the App

1. Open the project in Android Studio
2. Sync Gradle files
3. Build and run on device or emulator

## Testing

1. Install the app on your device
2. Make sure WhatsApp is installed
3. Enter a phone number (e.g., `9876543210`)
4. Optionally enter a message
5. Click "Send Message"
6. WhatsApp should open with the chat ready

## AdMob Integration (Optional)

To add AdMob banner ads:

1. Uncomment the AdMob dependency in `build.gradle.kts`:
   ```kotlin
   implementation("com.google.android.gms:play-services-ads:22.6.0")
   ```

2. Add your AdMob App ID to `AndroidManifest.xml`:
   ```xml
   <meta-data
       android:name="com.google.android.gms.ads.APPLICATION_ID"
       android:value="ca-app-pub-XXXXXXXXXXXXXXXX~XXXXXXXXXX"/>
   ```

3. Uncomment the AdView in `activity_main.xml`

4. Initialize AdMob in `MainActivity.kt`:
   ```kotlin
   MobileAds.initialize(this) {}
   ```

## Play Store Compliance

✅ Uses official WhatsApp deep links only  
✅ No unofficial APIs  
✅ No unnecessary permissions  
✅ No data collection  
✅ Fully offline app  

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### Open Source Commitment

This app is **100% open source**:
- ✅ All source code is freely available
- ✅ No proprietary dependencies
- ✅ No hidden code or obfuscation
- ✅ Free to use, modify, and distribute
- ✅ Community contributions welcome

### Dependencies

All dependencies used in this project are open source:
- **AndroidX Libraries** - Apache 2.0 License
- **Material Design Components** - Apache 2.0 License
- **Kotlin** - Apache 2.0 License

### Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## Acknowledgments

- Built with open source tools and libraries
- Uses official WhatsApp deep link API
- Material Design by Google
