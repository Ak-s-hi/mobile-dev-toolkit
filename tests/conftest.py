from pathlib import Path

import pytest


@pytest.fixture
def flutter_project(tmp_path: Path) -> Path:
    # Dart file
    (tmp_path / "main.dart").write_text(
        """
class HomePage extends StatelessWidget {
}
""",
        encoding="utf-8",
    )

    # Assets
    assets = tmp_path / "assets"
    assets.mkdir()

    (assets / "logo.png").write_bytes(
        b"fake-image-data"
    )

    # pubspec
    (tmp_path / "pubspec.yaml").write_text(
        """
dependencies:
  provider: ^6.1.2
  dio: ^5.0.0

flutter:
  assets:
    - assets/
""",
        encoding="utf-8",
    )

    return tmp_path


@pytest.fixture
def empty_project(tmp_path: Path) -> Path:
    return tmp_path


@pytest.fixture
def no_assets_project(tmp_path: Path) -> Path:
    (tmp_path / "main.dart").write_text(
        """
class HomePage extends StatelessWidget {
}
""",
        encoding="utf-8",
    )

    (tmp_path / "pubspec.yaml").write_text(
        """
dependencies:
  provider: ^6.1.2
""",
        encoding="utf-8",
    )

    return tmp_path
