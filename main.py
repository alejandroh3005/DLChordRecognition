import re
import os
import pandas as pd
from hpcp_generator import hpcp

def wav_to_csv():
    # Set directories to access wav files
    abs_directory = r'C:\Users\alega\PycharmProjects\hpcp'
    wav_directory = abs_directory + r'\piano_triads'
    n_bins = 120
    dataset = pd.DataFrame()
    labels = []
    for file_name in os.listdir(wav_directory):
        if file_name.endswith('4_0.wav') or file_name.endswith('4_1.wav'):  # This will be changed to '.wav'
            # len(output) = n_time_steps, len(output[0]) = n_bins
            output = hpcp(fr'{wav_directory}\{file_name}', bins_per_octave=n_bins)  # from 1307 timesteps, 120 bins
            hpcp_df = pd.DataFrame(output)
            hpcp_means = hpcp_df.mean(axis=0)
            dataset = dataset.append(hpcp_means, ignore_index=True)
            exp = '[A-Za-z]*_[A-Za-z]*[A-Za-z]'
            label = re.search(exp, file_name)
            labels.append(label.group(0))
            # if len(dataset) >= 30:  # This is just an early exit bc I don't have many files rn
            #    break
        else:
            continue
    dataset.columns = [f'Bin {i}' for i in range(1, n_bins + 1)]
    dataset['Labels'] = labels
    dataset.to_csv("test.csv", index=False)
    print(dataset)


if __name__ == '__main__':
    wav_to_csv()