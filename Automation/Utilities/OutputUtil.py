from datetime import datetime
from Config import config
import os

class OutputUtil:
    f = None
    open_date = None
    close_date = None
    step_no = 0

    @staticmethod
    def DeleteFileContent():
        OutputUtil.f = open(config.OUTPUT_FILE, "w").close()

    @staticmethod
    def OpenFileInWriteMode():
        global open_date
        # print("Open output file")
        OutputUtil.step_no = 0
        OutputUtil.open_date = datetime.now()
        OutputUtil.f = open(config.OUTPUT_FILE, "w")
        start_date = OutputUtil.open_date.strftime("%d-%m-%Y")
        start_time = OutputUtil.open_date.strftime("%H:%M:%S")
        config.TEST_START_DATE_TIME = start_date+"_"+start_time
        # config.TEST_START_TIME = start_time
        OutputUtil.f.write("Execution Details * \n")
        OutputUtil.f.write("\n")
        OutputUtil.f.write("Start Date * " + start_date + " \n")
        OutputUtil.f.write("Start Time * " + start_time + " \n")
        OutputUtil.f.write("\n")
        OutputUtil.f.write("Steps Executed * \n")

    @staticmethod
    def OpenFileInReadMode():
        OutputUtil.f = open(config.OUTPUT_FILE, "r")

    @staticmethod
    def WriteFile(message):
        OutputUtil.step_no = OutputUtil.step_no + 1
        final_prefix = "Step "+str(OutputUtil.step_no)+" * "
        final_message = final_prefix + message
        OutputUtil.f.write(final_message)

    @staticmethod
    def CloseFile():
        OutputUtil.close_date = datetime.now()
        end_time = OutputUtil.close_date.strftime("%H:%M:%S")
        time_delta = (OutputUtil.close_date - OutputUtil.open_date)
        duration = str(time_delta).split(".")[0]
        OutputUtil.f.write("\n")
        OutputUtil.f.write("Duration * " + duration + " \n")
        OutputUtil.f.write("\n")
        OutputUtil.f.close()

    @staticmethod
    def ReadFile():
        return OutputUtil.f.read()

    @staticmethod
    def ReadFileLineByLine():
        return OutputUtil.f.readlines()

    @staticmethod
    def ClearFile():
        return OutputUtil.f.truncate(0)

