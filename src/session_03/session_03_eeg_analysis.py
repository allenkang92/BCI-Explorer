import mne
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def load_eeg_data(subject):
    data_path = Path(__file__).parents[2] / 'data' / 'Auditory-visual Shift Study'
    file_name = f'{subject}/eeg/{subject}_task-AuditoryVisualShift_run-01_eeg.set'
    return mne.io.read_raw_eeglab(data_path / file_name, preload=True)

def preprocess_eeg(raw):
    raw.drop_channels(['EOG1', 'EOG2']) # 실제 채널 이름에 따라 조정해야 함.
    raw.filter(l_freq=1, h_freq=40)
    raw.set_eeg_reference('average', projection=True)
    return raw

def visualize_eeg(raw):
    raw.plot(duration=10, n_channels=20)
    raw.plot_sensors(show_names=True)
    raw.plot_psd(fmax=50)
    freqs = np.logspace(*np.log10([1, 50]), num=50)
    raw.plot_psd_topo(tmin=0, tmax=60, fmin=1, fmax=50, proj=True)

def analyze_erp(raw):
    events, event_id = mne.events_from_annotations(raw)
    tmin, tmax = -0.2, 0.5
    epochs = mne.Epochs(raw, events, event_id, tmin, tmax, proj=True, baseline=(None, 0), preload=True)
    evoked_dict = {condition: epochs[condition].average() for condition in epochs.event_id}
    mne.viz.plot_compare_evokeds(evoked_dict, picks='eeg')
    for condition, evoked in evoked_dict.items():
        evoked.plot_topomap(times=[0, 0.1, 0.2, 0.3, 0.4], average=0.05)

def main():
    subject = 'sub-001'
    raw = load_eeg_data(subject)
    raw = preprocess_eeg(raw)
    visualize_eeg(raw)
    analyze_erp(raw)

if __name__ == '__main__':
    main()