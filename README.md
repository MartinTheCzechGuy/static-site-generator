![App Architecture](architecture.png)

The flow of data through the full system is:
- Markdown files are in the /content directory. A template.html file is in the root of the project.
- The static site generator (the Python code in src/) reads the Markdown files and the template file.
- The generator converts the Markdown files to a final HTML file for each page and writes them to the /public directory.