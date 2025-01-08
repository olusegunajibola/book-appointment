import schedule
import time
import subprocess

def run_script():
    subprocess.run(["C:\\ProgramData\\Anaconda3\\envs\\xPostsDwd\\python.exe",
                    "C:\\Users\\USER\\PycharmProjects\\book-appointment\\book-appt.py"])

# 'C:\\ProgramData\\Anaconda3\\envs\\xPostsDwd\\python.exe C:\\Users\\USER\\PycharmProjects\\claim-coins\\test.py')
# 'C:\\ProgramData\\Anaconda3\\envs\\xPostsDwd\\python.exe C:\\Users\\USER\\PycharmProjects\\claim-coins\\book-appt.py')
def schedule_script():
    # Schedule the script to run at 12 AM and 12 PM
    schedule.every().day.at("23:58").do(run_script)
    schedule.every().day.at("11:58").do(run_script)

    print("Script scheduled to run before 12 AM and 12 PM.")

    # Run the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_script()
