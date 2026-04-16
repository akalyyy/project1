from datetime import datetime

def summary(config, processed_files, quarantined_files, processed_count, quarantined_count):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d__%H-%M-%S")
    filename = f"{config['reports_folder']}/summary_report_{timestamp}.txt"

    with open (filename, "w") as report:
        report.write("FileFlow Summary:\n\n")
        report.write(f"main.py execution time and date: {now}\n\n")

        report.write("PROCESSED FILES:\n")
        for file in processed_files:
            report.write(file + "\n")
        report.write(f"\nTotal processed files: {processed_count}\n\n")
        
        report.write("QUARANTINED FILES:\n")
        for file in quarantined_files:
            report.write(file + "\n")
        report.write(f"\nTotal quarantined files: {quarantined_count}\n")