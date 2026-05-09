import os
import PyPDF2
import glob

pdf_dir = r"c:\Users\hvhar\OneDrive\Desktop\codeing\InterviewPlan-2\JavaIntervewMetrial"
output_dir = r"c:\Users\hvhar\OneDrive\Desktop\codeing\TCS_Preparation_plan"

plan = {
    "Day01": {
        "title": "Core Java Basics",
        "files": ["Step-1-Core-Java-Level-I-1.pdf", "Step-2-Core-Java-Level-II-1.pdf"]
    },
    "Day02": {
        "title": "Core Java Advanced & Coding",
        "files": ["Step-3-Core-Java-Level-III.pdf", "Common-Step-Java-Coding.pdf"]
    },
    "Day03": {
        "title": "Stream API",
        "files": ["Common-Step-Stream-API-Coding-Level-I.pdf", "Common-Step-Stream-API-Coding-Level-II.pdf"]
    },
    "Day04": {
        "title": "Spring Framework & MVC",
        "files": ["Step-4-Spring-Framework-Level-I.pdf", "Step-5-Spring-framework-Level-II.pdf", "Step-10-Spring-MVC-Level-I-Optional.pdf"]
    },
    "Day05": {
        "title": "Spring Boot Basics",
        "files": ["Step-6-Spring-Boot-Level-I.pdf", "Step-7-Spring-Boot-Level-II.pdf"]
    },
    "Day06": {
        "title": "Spring Boot Advanced & Security",
        "files": ["Step-8-Spring-Boot-Level-III-Scenario-Based.pdf", "Step-9-Spring-Security-Level-I.pdf"]
    },
    "Day07": {
        "title": "Databases & Spring Data JPA",
        "files": ["Step-11-SQL.pdf", "Step-12-Spring-Data-JPA-and-Other-DB-Level-I.pdf"]
    },
    "Day08": {
        "title": "Microservices",
        "files": ["Step-14-Microservices-Level-I.pdf"]
    },
    "Day09": {
        "title": "DevOps, Maven & Git",
        "files": ["Step-15-Maven-and-Git-Level-I.pdf", "Step-16-Maven-and-Git-Gradle-and-Deployments-Level-II.pdf"]
    },
    "Day10": {
        "title": "Testing & Kafka",
        "files": ["Step-17-Junit-and-Mockito.pdf", "Step-13-Kafka-Optional.pdf"]
    }
}

def extract_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""

# Format raw text to markdown-ish
def format_to_md(title, text):
    lines = text.split('\n')
    md_lines = [f"# {title}\n"]
    
    in_code_block = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Simple heuristic: if line starts with 'Q' and a number like 'Q1.' or 'Q20.'
        if line.startswith('Q') and '.' in line[:5]:
            md_lines.append(f"\n- [ ] **{line}**\n")
        elif "{" in line or "}" in line or line.startswith('public class') or line.startswith('public static'):
            if not in_code_block:
                md_lines.append("\n```java")
                in_code_block = True
            md_lines.append(line)
        else:
            if in_code_block and not (line.startswith('//') or line.endswith(';') or "{" in line or "}" in line):
                # Probably out of code block
                md_lines.append("```\n")
                in_code_block = False
            
            md_lines.append(line)
            
    if in_code_block:
        md_lines.append("```\n")
        
    return "\n".join(md_lines)

for day, info in plan.items():
    day_dir = os.path.join(output_dir, day)
    os.makedirs(day_dir, exist_ok=True)
    
    full_text = ""
    for file_name in info["files"]:
        pdf_path = os.path.join(pdf_dir, file_name)
        if os.path.exists(pdf_path):
            full_text += f"\n## {file_name.replace('.pdf', '')}\n"
            full_text += extract_text(pdf_path)
        else:
            print(f"Warning: {file_name} not found.")
            
    md_content = format_to_md(info["title"], full_text)
    
    with open(os.path.join(day_dir, "notes.md"), 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"Generated {day}/notes.md")

print("Done generating markdown files.")
