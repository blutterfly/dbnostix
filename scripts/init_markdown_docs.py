"""
Purpose:
1. Use mkdocs.yml nav section to create directories and create corresponding md files
2. Add content to these files which contains Title derived from the name of the md file and brief description of the md content.
"""
import os

# Define the directory structure based on mkdocs.yml
nav_structure = {
    "dbnostix": {
        "dbnostix.md": "An overview of Dbnostix, its purpose, and key features.",
        "about.md": "Information about the Dbnostix platform, its history, and goals.",
        "contact.md": "Contact details and ways to reach out for inquiries and support.",
        "services.md": "A summary of services offered by Dbnostix."
    },
    "services": {
        "database_infrastructure.md": "Details on database infrastructure solutions and best practices.",
        "data_science.md": "An overview of data science techniques and methodologies used in Dbnostix.",
        "predictive_modeling.md": "Insights into predictive modeling and its applications.",
        "services_large_language_model.md": "An explanation of large language models and services related to them."
    },
    "python": {
        "python.md": "Introduction to Python and its applications.",
        "pandas.md": "A beginner-friendly guide to Pandas for data analysis.",
        "yfinance.md": "How to use `yfinance` to fetch and analyze stock market data.",
        "best_practice.md": "Best coding practices for Python development."
    },
    "algotrade": {
        "algotrade.md": "A deep dive into algorithmic trading concepts.",
        "extract.md": "Techniques and tools for extracting financial data.",
        "transform.md": "Transforming and cleaning financial data for analysis.",
        "load.md": "Loading financial data into storage systems for further processing."
    },
    "database": {
        "database.md": "General overview of databases and their importance.",
        "db2.md": "Introduction to IBM Db2 and its features.",
        "postgresql.md": "A guide to PostgreSQL and its use cases.",
        "duckdb.md": "Introduction to DuckDB, an in-memory analytical database."
    },
    "mkdocs": {
        "mkdocs.md": "Getting started with MkDocs for documentation.",
        "collapsible_sections.md": "How to create collapsible sections in MkDocs."
    },
    "obsidian": {
        "obsidian.md": "Overview of Obsidian as a knowledge management tool.",
        "cards.md": "Implementing card-based layouts in MkDocs."
    }
}

# Function to create directories and files
def create_mkdocs_files(base_path="."):
    for folder, files in nav_structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        
        for file, description in files.items():
            file_path = os.path.join(folder_path, file)
            title = file.replace("_", " ").replace(".md", "").title()
            content = f"# {title}\n\n{description}"
            
            if not os.path.exists(file_path):  # Avoid overwriting existing files
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Created: {file_path}")
            else:
                print(f"Skipped (already exists): {file_path}")

if __name__ == "__main__":
    create_mkdocs_files()
