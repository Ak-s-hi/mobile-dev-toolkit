from toolkit.analyzer import ProjectMetrics
import json


class Reporter:
    @staticmethod
    def print(metrics: ProjectMetrics) -> None:

        report = {
            "lines": metrics.dart_lines,
            "widgets": metrics.widget_count,
            "assets": {
                "count": metrics.asset_count,
                "totalSizeMB": round(
                    metrics.asset_size_bytes / (1024 * 1024),
                    2,
                ),
            },
            "dependencies": {
                "count": metrics.dependency_count,
                "list": metrics.dependencies,
            },
        }

        print(
            json.dumps(
                report,
                indent=2,
            )
        )
