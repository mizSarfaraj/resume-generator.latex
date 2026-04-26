import json
import sys
import os

def build_experience(data_dir):
    with open(os.path.join(data_dir, 'experience.json'), 'r') as f:
        jobs = json.load(f)

    latex_output = ""
    for job in jobs:
        latex_output += f"\\noindent\\textbf{{{job['title']}}} \\hfill {job['startDate']} - {job['endDate']} \\\\\n"
        latex_output += f"\\noindent\\textbf{{{job['companyName']}}} \\hfill {job['location']}\n"
        latex_output += "\\begin{itemize}[leftmargin=0.5cm, topsep=0pt, itemsep=0pt, parsep=0pt]\n"
        for bullet in job['bullets']:
            latex_output += f"  \\item {bullet}\n"
        latex_output += "\\end{itemize}\n\\vspace{0.2cm}\n\n"

    with open('experience.tex', 'w') as f:
        f.write(latex_output)

def build_skills(data_dir):
    with open(os.path.join(data_dir, 'skills.json'), 'r') as f:
        skills = json.load(f)

    latex_output = "\\begin{itemize}[leftmargin=0.5cm, itemsep=0pt, parsep=0pt, topsep=0pt]\n"
    for skill in skills:
        latex_output += f"  \\item \\textbf{{{skill['category']}:}} {skill['items']}\n"
    latex_output += "\\end{itemize}\n\\vspace{0.4cm}\n"

    with open('skills.tex', 'w') as f:
        f.write(latex_output)

def build_education(data_dir):
    with open(os.path.join(data_dir, 'education.json'), 'r') as f:
        schools = json.load(f)

    latex_output = ""
    for school in schools:
        latex_output += f"\\noindent\\textbf{{{school['instituteName']}}} \\hfill {school['location']} \\\\\n"
        latex_output += f"\\noindent {school['Degree']} \\hfill {school['startYear']} - {school['endYear']} \\\\\n"
        latex_output += "\\vspace{0.2cm}\n\n"

    with open('education.tex', 'w') as f:
        f.write(latex_output)

def build_header(data_dir):
    with open(os.path.join(data_dir, 'header.json'), 'r') as f:
        header = json.load(f)

    # Build the center-aligned header
    latex_output = "\\begin{center}\n"
    latex_output += f"    {{\\huge \\textbf{{{header['name']}}}}}\\\\[0.2cm]\n"
    
    # Automatically join all items in the details array with a separator
    contact_line = " \\textbar{} ".join(header['details'])
    latex_output += f"    {contact_line}\n"
    
    latex_output += "\\end{center}\n"
    
    # Add the separator line and spacing underneath
    latex_output += "\\vspace{0.1cm}\n\\hrule\n\\vspace{0.3cm}\n"

    with open('header.tex', 'w') as f:
        f.write(latex_output)

if __name__ == "__main__":
    # Get the folder name from the command line, default to 'main' if none provided
    profile = sys.argv[1] if len(sys.argv) > 1 else 'main'
    data_dir = os.path.join('data', profile)
    
    # Safety check to ensure the folder actually exists
    if not os.path.exists(data_dir):
        print(f"Error: The directory '{data_dir}' does not exist.")
        sys.exit(1)
        
    print(f"Building resume using data from: {data_dir}")
    build_experience(data_dir)
    build_skills(data_dir)
    build_education(data_dir)
    build_header(data_dir)
    print("Resume built successfully!")