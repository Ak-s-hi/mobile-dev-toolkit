from dataclasses import dataclass
from pathlib import Path
import yaml


@dataclass
class ProjectMetrics:
    dart_lines: int
    widget_count: int
    asset_count: int
    asset_size_bytes: int
    dependency_count: int
    dependencies: list[str]


class FlutterAnalyzer:

    def calculate_asset_size(
            self,
            project_root: Path,
            asset_paths: list[str], ) -> tuple[int, int]:

        total_size = 0
        asset_count = 0

        for asset_path in asset_paths:
            full_path = project_root / asset_path

            if not full_path.exists():
                continue

            if full_path.is_file():
                asset_count += 1
                total_size += full_path.stat().st_size

            elif full_path.is_dir():
                for file in full_path.rglob("*"):
                    if file.is_file():
                        asset_count += 1
                        total_size += file.stat().st_size

        return asset_count, total_size

    def analyze(self, project_path: str) -> ProjectMetrics:
        root = Path(project_path)
        dependency_count = 0
        dependencies = []
        asset_count = 0
        asset_size_bytes = 0
        dart_lines = 0
        widget_count = 0
        dart_files_found = 0
        if not root.exists():
            raise FileNotFoundError(
                f"Project path does not exist: {project_path}"
            )

        if not root.is_dir():
            raise NotADirectoryError(
                f"Expected a directory, got: {project_path}"
            )
        for dart_file in root.rglob("*.dart"):
            dart_files_found += 1
            try:
                content = dart_file.read_text(encoding="utf-8")

                # Count lines
                dart_lines += len(content.splitlines())

                # Count widget classes
                widget_count += content.count("extends StatelessWidget")
                widget_count += content.count("extends StatefulWidget")
                widget_count += content.count("extends Widget")

            except Exception as e:
                print(f"Error reading {dart_file}: {e}")
        if dart_files_found == 0:
            print(
                "Warning: No Dart files found in the project."
            )

        pubspec = {}
        pubspec_path = root / "pubspec.yaml"

        if pubspec_path.exists():
            with open(pubspec_path, "r", encoding="utf-8") as file:
                loaded = yaml.safe_load(file)
                if isinstance(loaded, dict):
                    pubspec = loaded

        else:
            print(
                "Warning: pubspec.yaml not found. "
                "Skipping dependency and asset analysis."
            )

        dependencies_dict = pubspec.get("dependencies", {})
        dependency_count = len(dependencies_dict)
        dependencies = list(dependencies_dict.keys())
        dependency_count = len(
            pubspec.get("dependencies", {})
        )

        asset_paths = (
            pubspec.get("flutter", {})
            .get("assets", [])
        )

        asset_count, asset_size_bytes = self. calculate_asset_size(
            root,
            asset_paths,
        )
        return ProjectMetrics(
            dart_lines=dart_lines,
            widget_count=widget_count,
            asset_count=asset_count,
            asset_size_bytes=asset_size_bytes,
            dependency_count=dependency_count,
            dependencies=dependencies,
        )
