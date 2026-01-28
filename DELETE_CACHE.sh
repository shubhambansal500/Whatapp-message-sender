#!/bin/bash

echo "=========================================="
echo "Deleting Gradle Cache to Fix JDK/jlink Error"
echo "=========================================="
echo ""

# Close Android Studio first
echo "⚠️  Make sure Android Studio is CLOSED before running this script!"
echo ""
read -p "Press Enter to continue or Ctrl+C to cancel..."

# Delete all transforms cache
echo "Deleting transforms cache..."
rm -rf ~/.gradle/caches/transforms-3/

# Delete all Gradle cache (more thorough)
echo "Deleting all Gradle cache..."
rm -rf ~/.gradle/caches/

# Clean project
echo "Cleaning project..."
cd "$(dirname "$0")"
./gradlew clean 2>/dev/null || echo "Gradle clean skipped (may fail if cache is corrupted)"
rm -rf .gradle
rm -rf app/build
rm -rf build

echo ""
echo "✅ Cache deletion complete!"
echo ""
echo "Next steps:"
echo "1. Open Android Studio"
echo "2. File → Invalidate Caches / Restart"
echo "3. Select 'Invalidate and Restart'"
echo "4. Wait for restart"
echo "5. File → Sync Project with Gradle Files"
echo "6. Build → Rebuild Project"
echo ""
