# security_report_generator.py
import os
from datetime import datetime

def generate_report(scan_results, output_file="security_report.html"):
    report_content = f"""
    <html>
    <head>
        <title>Security Scan Report - {datetime.now().strftime('%Y-%m-%d')}</title>
    </head>
    <body>
        <h1>Security Scan Report</h1>
        <p>Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <h2>Scan Results:</h2>
        <pre>
    """
    for result in scan_results:
        report_content += result + "\n"
    report_content += """
        </pre>
    </body>
    </html>
    """
    with open(output_file, 'w') as f:
        f.write(report_content)
    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    scan_results = []
    results_dir = "scan_results"
    if os.path.exists(results_dir):
        for file in os.listdir(results_dir):
            with open(os.path.join(results_dir, file), 'r') as f:
                scan_results.append(f"--- {file} ---\n" + f.read())
    generate_report(scan_results)
