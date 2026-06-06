from pathlib import Path

import pytest

from toolkit.analyzer import FlutterAnalyzer


def test_happy_path(flutter_project: Path) -> None:
    analyzer = FlutterAnalyzer()

    metrics = analyzer.analyze(
        str(flutter_project)
    )

    assert metrics.dart_lines > 0
    assert metrics.widget_count == 1

    assert metrics.dependency_count == 2

    assert "provider" in metrics.dependencies
    assert "dio" in metrics.dependencies

    assert metrics.asset_count == 1
    assert metrics.asset_size_bytes > 0


def test_invalid_path() -> None:
    analyzer = FlutterAnalyzer()

    with pytest.raises(FileNotFoundError):
        analyzer.analyze(
            "this-path-does-not-exist"
        )


def test_empty_project(
    empty_project: Path,
) -> None:
    analyzer = FlutterAnalyzer()

    metrics = analyzer.analyze(
        str(empty_project)
    )

    assert metrics.dart_lines == 0
    assert metrics.widget_count == 0

    assert metrics.dependency_count == 0
    assert metrics.dependencies == []

    assert metrics.asset_count == 0
    assert metrics.asset_size_bytes == 0


def test_project_without_assets(
    no_assets_project: Path,
) -> None:
    analyzer = FlutterAnalyzer()

    metrics = analyzer.analyze(
        str(no_assets_project)
    )

    assert metrics.dart_lines > 0

    assert metrics.dependency_count == 1

    assert metrics.asset_count == 0
    assert metrics.asset_size_bytes == 0
