```markdown
# Dynamic Dockerized LaTeX Resume Builder

A lightweight, fully isolated tool to generate professional, ATS-friendly LaTeX resumes from dynamic JSON data. 

This setup allows you to maintain multiple variations of your resume (e.g., different roles or industries) entirely in JSON. A Python script translates the data into LaTeX snippets, which are then compiled into a polished PDF—all inside a Docker container. **No local LaTeX or Python installation is required.**

## 🌟 Features
* **100% Data-Driven:** Header, Experience, Education, and Skills are all generated from JSON. 
* **Zero Local Dependencies:** Uses Docker and Docker Compose to handle the entire build process.
* **Multi-Profile Support:** Maintain different JSON folders for different job applications and switch between them seamlessly.
* **Auto-Cleanup:** Automatically deletes messy `.aux`, `.log`, and temporary `.tex` files after a successful build.
* **Version Control Ready:** Pre-configured `.gitignore` prevents accidentally committing personal PDFs or build artifacts.

## 📂 Project Structure

```text
/workspace
├── script/
│   └── build.py              # Python script to parse JSON to .tex
├── template/
│   └── resume.tex            # The master LaTeX layout file
├── data/
│   ├── main/                 # Your default resume profile
│   │   ├── header.json
│   │   ├── experience.json
│   │   ├── education.json
│   │   └── skills.json
│   └── frontend_role/        # Example of an alternative profile
│       ├── header.json
│       ├── experience.json
│       ├── education.json
│       └── skills.json
├── docker-compose.yml        # Compose configuration
├── Dockerfile                # Container instructions
└── .gitignore                # Git ignore rules
```

## 🚀 Getting Started

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running.

### Standard Build (Default Profile)
To generate your resume using the data inside the `data/main/` folder, simply open your terminal in the root directory and run:

```bash
docker compose up
```
If successful, a fresh `resume.pdf` will instantly appear in your root folder!

### Building Custom Profiles
To build a resume using a different data folder (e.g., `data/frontend_role/`), you can pass the folder name via the `PROFILE` environment variable.

**Option 1: Using a `.env` file (Recommended for Windows)**
1. Create a file named `.env` in the root directory.
2. Add the following line: `PROFILE=frontend_role`
3. Run `docker compose up`

**Option 2: Inline Terminal Commands**
* **Mac/Linux:** `PROFILE=frontend_role docker compose up`
* **Windows (PowerShell):** `$env:PROFILE="frontend_role"; docker compose up`
* **Windows (CMD):** `set PROFILE=frontend_role&& docker compose up`

## 🛠️ Configuration & Customization

### The Double Backslash Rule
Because standard LaTeX uses special characters (like `\`, `%`, and `&`), you must escape them inside your JSON files using a **double backslash** to prevent crashes.

* **Bold Text:** `"reducing load times by \\textbf{40\\%}"`
* **Hyperlinks:** `"\\href{https://github.com/username}{GitHub}"`
* **Ampersands:** `"Research \\& Development"`
* **Tildes (Approximate):** `"$\\sim$20\\%"`

### Adding New Sections
To add a new section (like "Projects" or "Certifications"):
1. Create a new `projects.json` file inside your profile folders.
2. Update `script/build.py` with a `build_projects(data_dir)` function to read the JSON and output `projects.tex`.
3. Add `\input{projects.tex}` into your `template/resume.tex` layout where you want it to appear.

## 🧹 Clean Up
The `Dockerfile` is configured to automatically remove auxiliary files after compilation. If you ever need to manually force a rebuild of the Docker image (for example, if you add a new LaTeX font package to the Dockerfile), run:

```bash
docker compose up --build
```