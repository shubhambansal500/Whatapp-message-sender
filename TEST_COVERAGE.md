# Test Coverage Guide

## Running Tests

### Unit Tests
```bash
./gradlew testDebugUnitTest
```

### Instrumented Tests (requires device/emulator)
```bash
./gradlew connectedAndroidTest
```

### All Tests
```bash
./gradlew test
```

## Generating Coverage Report

### Generate Coverage Report
```bash
./gradlew jacocoTestReport
```

### View Coverage Report
After running the coverage report, open:
```
app/build/reports/jacoco/jacocoTestReport/html/index.html
```

## Coverage Target

The project aims for **90%+ code coverage** across:
- ✅ Data Models (100%)
- ✅ Repositories (90%+)
- ✅ Use Cases (100%)
- ✅ Services (90%+)
- ✅ ViewModels (90%+)
- ✅ Activities (80%+)

## Test Structure

### Unit Tests (`app/src/test/`)
- `data/model/` - Model tests
- `data/repository/` - Repository tests
- `domain/usecase/` - Use case tests
- `domain/service/` - Service tests
- `ui/viewmodel/` - ViewModel tests

### Instrumented Tests (`app/src/androidTest/`)
- `ui/` - Activity UI tests

## Running Coverage in Android Studio

1. Right-click on `app/src/test` folder
2. Select "Run 'Tests in 'test'' with Coverage"
3. View coverage in the Coverage tool window

## Continuous Integration

For CI/CD pipelines, add:
```yaml
- name: Run tests with coverage
  run: ./gradlew testDebugUnitTest jacocoTestReport
```
