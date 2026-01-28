# App Icon Setup

## Current Status

The app currently uses a simple XML drawable as a placeholder icon. For Play Store publishing, you should replace this with proper launcher icons.

## Creating App Icons

### Option 1: Use Android Studio's Image Asset Studio (Recommended)

1. In Android Studio, right-click on `app/src/main/res`
2. Select **New > Image Asset**
3. Choose **Launcher Icons (Adaptive and Legacy)**
4. Configure your icon:
   - **Foreground Layer**: Upload your icon image (1024x1024px recommended)
   - **Background Layer**: Choose a color or image
   - **Legacy Icon**: Will be auto-generated
5. Click **Next** and **Finish**

This will automatically create icons in all required sizes:
- `mipmap-mdpi/ic_launcher.png` (48x48)
- `mipmap-hdpi/ic_launcher.png` (72x72)
- `mipmap-xhdpi/ic_launcher.png` (96x96)
- `mipmap-xxhdpi/ic_launcher.png` (144x144)
- `mipmap-xxxhdpi/ic_launcher.png` (192x192)
- And round versions for each

### Option 2: Use Online Icon Generator

1. Visit: https://icon.kitchen/ or https://www.appicon.co/
2. Upload your 1024x1024px icon image
3. Download the generated Android icon set
4. Extract and copy to `app/src/main/res/`

### Option 3: Manual Creation

Create icons in these sizes:
- **mdpi**: 48x48px
- **hdpi**: 72x72px
- **xhdpi**: 96x96px
- **xxhdpi**: 144x144px
- **xxxhdpi**: 192x192px

Place them in:
- `app/src/main/res/mipmap-mdpi/ic_launcher.png`
- `app/src/main/res/mipmap-hdpi/ic_launcher.png`
- `app/src/main/res/mipmap-xhdpi/ic_launcher.png`
- `app/src/main/res/mipmap-xxhdpi/ic_launcher.png`
- `app/src/main/res/mipmap-xxxhdpi/ic_launcher.png`

And round versions:
- `app/src/main/res/mipmap-mdpi/ic_launcher_round.png`
- (same for other densities)

## After Creating Icons

Update `AndroidManifest.xml` to use the mipmap icons:

```xml
<application
    android:icon="@mipmap/ic_launcher"
    android:roundIcon="@mipmap/ic_launcher_round"
    ...>
```

## Icon Design Tips

- Use simple, recognizable designs
- Ensure icons are readable at small sizes
- Follow Material Design guidelines
- Use appropriate colors for your brand
- Test on different backgrounds

## For Play Store

Play Store requires:
- **High-res icon**: 512x512px (PNG, 32-bit)
- **Feature graphic**: 1024x500px (optional but recommended)

These are separate from the app launcher icons.
