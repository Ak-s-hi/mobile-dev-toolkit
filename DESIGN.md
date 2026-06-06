# Mobile Dev Toolkit

Analyze Flutter projects from the command line.



Mobile-dev-toolkit 
CLI commands supports 
Mobile-dev-toolkit analyse <project_path>
Options : --json and �verbose
Also separate commands for lines, widgets, assets and deps.

Expected output: 

Project: billing_app
Dart Files : 120
Dart Lines : 15400
Widgets : 420
Asset size : 52 MB
Dependencies : 18
(Need to design the user experience too )

Data structures needed ? 

@dataclass
Class ProjectMetrics:
   Project_name: str
   Dart_lines: int
   Widget_count: int
   Asset_size_bytes: int
   Dependency_count: int

( what informed must be stored and what information is calculated )

How will the project be organized ?

Mobile_dev_toolkit/
 ->  cli.py
 -> analyzers/
 -> models/
 -> services/
 -> tests/

How will each metric be calculated?
(writing algorithm in plain English)
COUNT DART LINES :
1. Traverse project folders
2. Find all .dart files
3. Read each file
4. Count lines
5. Sum total

COUNT DEPENDENCIES :
1. Open pubspec.yaml
2. Read dependencies section
3. Count entries

ASSET SIZE :
1. Navigate to assets folders
2. Read and count how assets are there 
3. Calculate size of each assets and sum them 


