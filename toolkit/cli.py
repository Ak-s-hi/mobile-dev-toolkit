import click

from toolkit.analyzer import FlutterAnalyzer
from toolkit.reporter import Reporter


@click.command(
    help="""
Analyze a Flutter project.

Examples:

  mobile-dev-toolkit .
  mobile-dev-toolkit ./my_flutter_app
  mobile-dev-toolkit "C:/Projects/BillingApp"
"""
)
@click.argument("project_path")
def main(project_path: str) -> None:
    try:
        analyzer = FlutterAnalyzer()

        metrics = analyzer.analyze(project_path)

        Reporter.print(metrics)

    except FileNotFoundError as error:
        click.echo(
            f"Error: {error}",
            err=True,
        )

    except NotADirectoryError as error:
        click.echo(
            f"Error: {error}",
            err=True,
        )

    except Exception as error:
        click.echo(
            f"Unexpected error: {error}",
            err=True,
        )


if __name__ == "__main__":
    main()


# click is a python library used to create command-line applications
