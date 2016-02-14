import pandas

columns = [line.strip() for line in open("data/columns.txt").readlines()]
dataFile = "data/echocardiogram_data.txt"


# Function which loads ECG data useful for regression with survivial duration
# as target
# Data cleaning motivation described in initial_exploration notebook
def loadData():
  ecg = pandas.read_csv(dataFile, na_values=["?"],
                        error_bad_lines=False,
                        names=columns)

  # Remove subjects missing essential data and those still alive
  ecg = ecg[ecg.survival.notnull()]
  ecg = ecg[ecg.still_alive.notnull()]
  ecg = ecg[ecg.still_alive == 0]
  # Drop columns which won't provide information
  del ecg['name']
  del ecg['group']
  del ecg['mult']
  del ecg['still_alive']
  del ecg['alive_at_1']

  return ecg

