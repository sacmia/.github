# Create a Sacmia Flutter repository

Follow the [common repository guide](../NEW_REPOSITORY_GUIDE.md), using
[`sacmia/template-flutter`](https://github.com/sacmia/template-flutter).

## Setup

Install the Flutter stable SDK and confirm the required platform toolchains:

```bash
flutter doctor
gh repo clone sacmia/REPOSITORY_NAME
cd REPOSITORY_NAME
git switch development
git pull origin development
git switch -c docs/project-setup
```

Replace project placeholders in `README.md`, `CLAUDE.md`,
`docs/PROJECT_DECISIONS.md`, `pubspec.yaml`, and platform identifiers before publishing
to an app store.

Run the official Flutter checks:

```bash
flutter pub get
dart format --output=none --set-exit-if-changed .
flutter analyze
flutter test
```

## Connect to a local API

Keep API base URLs in environment/build configuration; do not hardcode them in widgets
or commit secrets with them.

- Flutter web and iOS Simulator normally reach an API on the same computer through
  `http://localhost:PORT`.
- Android Emulator uses `http://10.0.2.2:PORT` to reach the host computer.
- A physical device uses the development computer's LAN IP, such as
  `http://192.168.1.20:PORT`. The API must listen on `0.0.0.0`, and both devices must
  be on the same trusted network.

Never expose a local development API directly to the public internet. Document the
project's actual ports and environment selection in its own Flutter developer guide.

```bash
git add .
git commit -m "Configure project documentation and Claude instructions"
git push -u origin docs/project-setup
gh pr create --base development
```

## Flutter verification

- [ ] Flutter stable SDK is used and `flutter doctor` has no relevant errors
- [ ] Application ID / bundle ID is unique and approved before release
- [ ] Formatting, analysis, unit tests, and widget tests pass
- [ ] CI uses the shared Sacmia Flutter workflow
- [ ] API URLs and signing credentials are environment-specific and not hardcoded
- [ ] Android/iOS signing material is stored outside Git
- [ ] Store builds and deployment workflows are added only when release accounts exist
