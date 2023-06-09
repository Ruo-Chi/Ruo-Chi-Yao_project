#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install mne')


# In[ ]:


import numpy as np
import mne
import pandas as pd


# In[ ]:


from google.colab import drive
drive.mount('/content/drive')


# In[ ]:


data_path = '/content/drive/MyDrive/Auditory_single_word_recognition_in_MEG'
sub_path = data_path + '/Sub-002'
meg_path = sub_path + '/meg'
raw_fname = meg_path + '/sub-002_task-words_meg.fif'


# In[ ]:


#Read the raw data
raw = mne.io.read_raw_fif(raw_fname)
print(raw)
#raw.plot()


# In[ ]:


raw.load_data()


# In[ ]:


raw.load_data().pick_types(meg=True, stim=True).filter(0, 100, phase= 'zero-double').resample(500)
print(raw)
raw.plot()


# In[ ]:


# event id
events = mne.find_events(raw, stim_channel="STI 014")
print(events)


# In[ ]:


# read_excel

metadata = pd.read_excel(data_path + '/Subjects_Stimuli.xlsx', 2)
metadata.head()


# In[ ]:


event_id = {'item/target': 162, 'item/post': 163, 'probe/no': 166, 'probe/yes': 167}  

tmin = -0.1         								# pre stimulis interval (in seconds) #
tmax = 0.8          								# post stimulus interval #

#min:(pre onset 0.1), max: (1 sec after onset.)
# if want to see n1, then 0.5sec is enough, but if want to see else then need longer.


#then do artifact rejection.
baseline = (None, 0)  # tmin ~ 0 , -0.1s-0s   
reject = dict(mag=5e-12)
epoch_run = mne.Epochs(raw, events, event_id, tmin, tmax,
                    baseline=baseline,
                    preload = True)

epoch_run = epoch_run['item']
epoch_run.metadata = metadata
epoch_run.drop_bad(reject=reject)
print(epoch_run)


# In[ ]:


epoch_run.save('Sub002-epo.fif')


# In[ ]:


epoch_run.average().plot()


# In[ ]:


times = np.arange(0.05, 0.45, 0.05)
evoked = epoch_run.average()
evoked.plot_topomap(times, ch_type="mag")


# In[ ]:


LF_evoked = epoch_run["FreqSUBTLEX < 63"].average()
HF_evoked = epoch_run["FreqSUBTLEX > 763"].average()
print(LF_evoked)
print(HF_evoked)
conds = ("LF", "HF")
evks = dict(zip(conds, [LF_evoked, HF_evoked]))


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(LF=0, HF=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 044",
    colors=dict(LF=0, HF=1),
    time_unit="ms",
)


# In[ ]:


nouns_evk = epoch_run['POS.str.startswith("N")'].average()
verbs_evk = epoch_run['POS.str.startswith("V")'].average()

print(nouns_evk)
print(verbs_evk)

conds = ("noun", "verb")
evks = dict(zip(conds, [nouns_evk, verbs_evk]))

mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(noun=0, verb=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 081",
    colors=dict(noun=0, verb=1),
    time_unit="ms",
)


# In[ ]:


LOrthND_evoked = epoch_run["OrthND < 1"].average()
HOrthND_evoked = epoch_run["OrthND > 15"].average()
print(LOrthND_evoked)
print(HOrthND_evoked)
conds = ("LOrthND", "HOrthND")
evks = dict(zip(conds, [LOrthND_evoked, HOrthND_evoked]))


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(LOrthND=0, HOrthND=1),
    axes="topo",
)


# In[ ]:


data_path = '/content/drive/MyDrive/Auditory_single_word_recognition_in_MEG'
sub_path = data_path + '/Sub-003'
meg_path = sub_path + '/meg'
raw_fname = meg_path + '/sub-003_task-words_meg.fif'


# In[ ]:


#Read the raw data
raw = mne.io.read_raw_fif(raw_fname)
print(raw)
#raw.plot()


# In[ ]:


raw.load_data()


# In[ ]:


raw.load_data().pick_types(meg=True, stim=True).filter(0, 100, phase= 'zero-double').resample(500)
print(raw)
raw.plot()


# In[ ]:


# event id
events = mne.find_events(raw, stim_channel="STI 014")
print(events)


# In[ ]:


# read_excel

metadata = pd.read_excel(data_path + '/Subjects_Stimuli.xlsx', 3)
metadata.head()


# In[ ]:


event_id = {'item/target': 162, 'item/post': 163, 'probe/no': 166, 'probe/yes': 167}  

tmin = -0.1         								# pre stimulis interval (in seconds) #
tmax = 0.8          								# post stimulus interval #

#min:(pre onset 0.1), max: (1 sec after onset.)
# if want to see n1, then 0.5sec is enough, but if want to see else then need longer.


#then do artifact rejection.
baseline = (None, 0)  # tmin ~ 0 , -0.1s-0s   
reject = dict(mag=5e-12)
epoch_run = mne.Epochs(raw, events, event_id, tmin, tmax,
                    baseline=baseline,
                    preload = True)

epoch_run = epoch_run['item']
epoch_run.metadata = metadata
epoch_run.drop_bad(reject=reject)
print(epoch_run)


# In[ ]:


epoch_run.save('Sub003-epo.fif')


# In[ ]:


epoch_run.average().plot()


# In[ ]:


times = np.arange(0.05, 0.45, 0.05)
evoked = epoch_run.average()
evoked.plot_topomap(times, ch_type="mag")


# In[ ]:


LF_evoked = epoch_run["FreqSUBTLEX < 63"].average()
HF_evoked = epoch_run["FreqSUBTLEX > 763"].average()
print(LF_evoked)
print(HF_evoked)
conds = ("LF", "HF")
evks = dict(zip(conds, [LF_evoked, HF_evoked]))


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(LF=0, HF=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 044",
    colors=dict(LF=0, HF=1),
    time_unit="ms",
)


# In[ ]:


nouns_evk = epoch_run['POS.str.startswith("N")'].average()
verbs_evk = epoch_run['POS.str.startswith("V")'].average()

print(nouns_evk)
print(verbs_evk)

conds = ("noun", "verb")
evks = dict(zip(conds, [nouns_evk, verbs_evk]))

mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(noun=0, verb=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 081",
    colors=dict(noun=0, verb=1),
    time_unit="ms",
)


# In[ ]:


LOrthND_evoked = epoch_run["OrthND < 1"].average()
HOrthND_evoked = epoch_run["OrthND > 40"].average()
print(LOrthND_evoked)
print(HOrthND_evoked)
conds = ("LOrthND", "HOrthND")
evks = dict(zip(conds, [LOrthND_evoked, HOrthND_evoked]))


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(LOrthND=0, HOrthND=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 043",
    colors=dict(LOrthND=0, HOrthND=1),
    time_unit="ms",
)


# In[ ]:


data_path = '/content/drive/MyDrive/Auditory_single_word_recognition_in_MEG'
sub_path = data_path + '/Sub-004'
meg_path = sub_path + '/meg'
raw_fname = meg_path + '/sub-004_task-words_meg.fif'


# In[ ]:


#Read the raw data
raw = mne.io.read_raw_fif(raw_fname)
print(raw)
#raw.plot()


# In[ ]:


raw.load_data()


# In[ ]:


raw.load_data().pick_types(meg=True, stim=True).filter(0, 100, phase= 'zero-double').resample(500)
print(raw)
raw.plot()


# In[ ]:


# event id
events = mne.find_events(raw, stim_channel="STI 014")
print(events)


# In[ ]:


# read_excel

metadata = pd.read_excel(data_path + '/Subjects_Stimuli.xlsx', 4)
metadata.head()


# In[ ]:


event_id = {'item/target': 162, 'item/post': 163, 'probe/no': 166, 'probe/yes': 167}  

tmin = -0.1         								# pre stimulis interval (in seconds) #
tmax = 0.8          								# post stimulus interval #

#min:(pre onset 0.1), max: (1 sec after onset.)
# if want to see n1, then 0.5sec is enough, but if want to see else then need longer.


#then do artifact rejection.
baseline = (None, 0)  # tmin ~ 0 , -0.1s-0s   
reject = dict(mag=5e-12)
epoch_run = mne.Epochs(raw, events, event_id, tmin, tmax,
                    baseline=baseline,
                    preload = True)

epoch_run = epoch_run['item']
epoch_run.metadata = metadata
epoch_run.drop_bad(reject=reject)
print(epoch_run)


# In[ ]:


epoch_run.save('Sub004-epo.fif')


# In[ ]:


epoch_run.average().plot()


# In[ ]:


times = np.arange(0.05, 0.45, 0.05)
evoked = epoch_run.average()
evoked.plot_topomap(times, ch_type="mag")


# In[ ]:


LF_evoked = epoch_run["FreqSUBTLEX < 63"].average()
HF_evoked = epoch_run["FreqSUBTLEX > 763"].average()
print(LF_evoked)
print(HF_evoked)
conds = ("LF", "HF")
evks = dict(zip(conds, [LF_evoked, HF_evoked]))


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(LF=0, HF=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 048",
    colors=dict(LF=0, HF=1),
    time_unit="ms",
)


# In[ ]:


nouns_evk = epoch_run['POS.str.startswith("N")'].average()
verbs_evk = epoch_run['POS.str.startswith("V")'].average()

print(nouns_evk)
print(verbs_evk)

conds = ("noun", "verb")
evks = dict(zip(conds, [nouns_evk, verbs_evk]))

mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(noun=0, verb=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 044",
    colors=dict(noun=0, verb=1),
    time_unit="ms",
)


# In[ ]:


LOrthND_evoked = epoch_run["OrthND < 1"].average()
HOrthND_evoked = epoch_run["OrthND > 15"].average()
print(LOrthND_evoked)
print(HOrthND_evoked)
conds = ("LOrthND", "HOrthND")
evks = dict(zip(conds, [LOrthND_evoked, HOrthND_evoked]))


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(LOrthND=0, HOrthND=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 077",
    colors=dict(LOrthND=0, HOrthND=1),
    time_unit="ms",
)


# In[ ]:


data_path = '/content/drive/MyDrive/Auditory_single_word_recognition_in_MEG'
sub_path = data_path + '/Sub-005'
meg_path = sub_path + '/meg'
raw_fname = meg_path + '/sub-005_task-words_meg.fif'


# In[ ]:


#Read the raw data
raw = mne.io.read_raw_fif(raw_fname)
print(raw)
#raw.plot()


# In[ ]:


raw.load_data()


# In[ ]:


raw.load_data().pick_types(meg=True, stim=True).filter(0, 100, phase= 'zero-double').resample(500)
print(raw)
raw.plot()


# In[ ]:


# event id
events = mne.find_events(raw, stim_channel="STI 014")
print(events)


# In[ ]:


# read_excel

metadata = pd.read_excel(data_path + '/Subjects_Stimuli.xlsx', 5)
metadata.head()


# In[ ]:


event_id = {'item/target': 162, 'item/post': 163, 'probe/no': 166, 'probe/yes': 167}  

tmin = -0.1         								# pre stimulis interval (in seconds) #
tmax = 0.8          								# post stimulus interval #

#min:(pre onset 0.1), max: (1 sec after onset.)
# if want to see n1, then 0.5sec is enough, but if want to see else then need longer.


#then do artifact rejection.
baseline = (None, 0)  # tmin ~ 0 , -0.1s-0s   
reject = dict(mag=5e-12)
epoch_run = mne.Epochs(raw, events, event_id, tmin, tmax,
                    baseline=baseline,
                    preload = True)

epoch_run = epoch_run['item']
epoch_run.metadata = metadata
epoch_run.drop_bad(reject=reject)
print(epoch_run)


# In[ ]:


epoch_run.save('Sub005-epo.fif')


# In[ ]:


epoch_run.average().plot()


# In[ ]:


times = np.arange(0.05, 0.45, 0.05)
evoked = epoch_run.average()
evoked.plot_topomap(times, ch_type="mag")


# In[ ]:


LF_evoked = epoch_run["FreqSUBTLEX < 63"].average()
HF_evoked = epoch_run["FreqSUBTLEX > 763"].average()
print(LF_evoked)
print(HF_evoked)
conds = ("LF", "HF")
evks = dict(zip(conds, [LF_evoked, HF_evoked]))


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(LF=0, HF=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 037",
    colors=dict(LF=0, HF=1),
    time_unit="ms",
)


# In[ ]:


nouns_evk = epoch_run['POS.str.startswith("N")'].average()
verbs_evk = epoch_run['POS.str.startswith("V")'].average()

print(nouns_evk)
print(verbs_evk)

conds = ("noun", "verb")
evks = dict(zip(conds, [nouns_evk, verbs_evk]))

mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(noun=0, verb=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 049",
    colors=dict(noun=0, verb=1),
    time_unit="ms",
)


# In[ ]:


LOrthND_evoked = epoch_run["OrthND < 1"].average()
HOrthND_evoked = epoch_run["OrthND > 15"].average()
print(LOrthND_evoked)
print(HOrthND_evoked)
conds = ("LOrthND", "HOrthND")
evks = dict(zip(conds, [LOrthND_evoked, HOrthND_evoked]))


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(LOrthND=0, HOrthND=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 128",
    colors=dict(LOrthND=0, HOrthND=1),
    time_unit="ms",
)


# In[ ]:





# In[ ]:


data_path = '/content/drive/MyDrive/Auditory_single_word_recognition_in_MEG'
sub_path = data_path + '/Sub-007'
meg_path = sub_path + '/meg'
raw_fname = meg_path + '/sub-007_task-words_meg.fif'


# In[ ]:


#Read the raw data
raw = mne.io.read_raw_fif(raw_fname)
print(raw)
#raw.plot()


# In[ ]:


raw.load_data()


# In[ ]:


raw.load_data().pick_types(meg=True, stim=True).filter(0, 100, phase= 'zero-double').resample(500)
print(raw)
raw.plot()


# In[ ]:


# event id
events = mne.find_events(raw, stim_channel="STI 014")
print(events)


# In[ ]:


# read_excel

metadata = pd.read_excel(data_path + '/Subjects_Stimuli.xlsx', 7)
metadata.head()


# In[ ]:


event_id = {'item/target': 162, 'item/post': 163, 'probe/no': 166, 'probe/yes': 167}  

tmin = -0.1         								# pre stimulis interval (in seconds) #
tmax = 0.8          								# post stimulus interval #

#min:(pre onset 0.1), max: (1 sec after onset.)
# if want to see n1, then 0.5sec is enough, but if want to see else then need longer.


#then do artifact rejection.
baseline = (None, 0)  # tmin ~ 0 , -0.1s-0s   
reject = dict(mag=5e-12)
epoch_run = mne.Epochs(raw, events, event_id, tmin, tmax,
                    baseline=baseline,
                    preload = True)

epoch_run = epoch_run['item']
epoch_run.metadata = metadata
epoch_run.drop_bad(reject=reject)
print(epoch_run)


# In[ ]:


epoch_run.save('Sub007-epo.fif')


# In[ ]:


epoch_run.average().plot()


# In[ ]:


times = np.arange(0.05, 0.45, 0.05)
evoked = epoch_run.average()
evoked.plot_topomap(times, ch_type="mag")


# In[ ]:


LF_evoked = epoch_run["FreqSUBTLEX < 63"].average()
HF_evoked = epoch_run["FreqSUBTLEX > 763"].average()
print(LF_evoked)
print(HF_evoked)
conds = ("LF", "HF")
evks = dict(zip(conds, [LF_evoked, HF_evoked]))


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(LF=0, HF=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 049",
    colors=dict(LF=0, HF=1),
    time_unit="ms",
)


# In[ ]:


nouns_evk = epoch_run['POS.str.startswith("N")'].average()
verbs_evk = epoch_run['POS.str.startswith("V")'].average()

print(nouns_evk)
print(verbs_evk)

conds = ("noun", "verb")
evks = dict(zip(conds, [nouns_evk, verbs_evk]))

mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(noun=0, verb=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 040",
    colors=dict(noun=0, verb=1),
    time_unit="ms",
)


# In[ ]:


LOrthND_evoked = epoch_run["OrthND < 1"].average()
HOrthND_evoked = epoch_run["OrthND > 15"].average()
print(LOrthND_evoked)
print(HOrthND_evoked)
conds = ("LOrthND", "HOrthND")
evks = dict(zip(conds, [LOrthND_evoked, HOrthND_evoked]))


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(LOrthND=0, HOrthND=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 044",
    colors=dict(LOrthND=0, HOrthND=1),
    time_unit="ms",
)


# In[ ]:





# In[ ]:


data_path = '/content/drive/MyDrive/Auditory_single_word_recognition_in_MEG'
sub_path = data_path + '/Sub-008'
meg_path = sub_path + '/meg'
raw_fname = meg_path + '/sub-008_task-words_meg.fif'


# In[ ]:


#Read the raw data
raw = mne.io.read_raw_fif(raw_fname)
print(raw)
#raw.plot()


# In[ ]:


raw.load_data()


# In[ ]:


raw.load_data().pick_types(meg=True, stim=True).filter(0, 100, phase= 'zero-double').resample(500)
print(raw)
raw.plot()


# In[ ]:


# event id
events = mne.find_events(raw, stim_channel="STI 014")
print(events)


# In[ ]:


# read_excel

metadata = pd.read_excel(data_path + '/Subjects_Stimuli.xlsx', 8)
metadata.head()


# In[ ]:


event_id = {'item/target': 162, 'item/post': 163, 'probe/no': 166, 'probe/yes': 167}  

tmin = -0.1         								# pre stimulis interval (in seconds) #
tmax = 0.8          								# post stimulus interval #

#min:(pre onset 0.1), max: (1 sec after onset.)
# if want to see n1, then 0.5sec is enough, but if want to see else then need longer.


#then do artifact rejection.
baseline = (None, 0)  # tmin ~ 0 , -0.1s-0s   
reject = dict(mag=5e-12)
epoch_run = mne.Epochs(raw, events, event_id, tmin, tmax,
                    baseline=baseline,
                    preload = True)

epoch_run = epoch_run['item']
epoch_run.metadata = metadata
epoch_run.drop_bad(reject=reject)
print(epoch_run)


# In[ ]:


epoch_run.save('Sub008-epo.fif')


# In[ ]:


epoch_run.average().plot()


# In[ ]:


times = np.arange(0.05, 0.45, 0.05)
evoked = epoch_run.average()
evoked.plot_topomap(times, ch_type="mag")


# In[ ]:


LF_evoked = epoch_run["FreqSUBTLEX < 63"].average()
HF_evoked = epoch_run["FreqSUBTLEX > 763"].average()
print(LF_evoked)
print(HF_evoked)
conds = ("LF", "HF")
evks = dict(zip(conds, [LF_evoked, HF_evoked]))


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(LF=0, HF=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 048",
    colors=dict(LF=0, HF=1),
    time_unit="ms",
)


# In[ ]:


nouns_evk = epoch_run['POS.str.startswith("N")'].average()
verbs_evk = epoch_run['POS.str.startswith("V")'].average()

print(nouns_evk)
print(verbs_evk)

conds = ("noun", "verb")
evks = dict(zip(conds, [nouns_evk, verbs_evk]))

mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(noun=0, verb=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 081",
    colors=dict(noun=0, verb=1),
    time_unit="ms",
)


# In[ ]:


LOrthND_evoked = epoch_run["OrthND < 1"].average()
HOrthND_evoked = epoch_run["OrthND > 15"].average()
print(LOrthND_evoked)
print(HOrthND_evoked)
conds = ("LOrthND", "HOrthND")
evks = dict(zip(conds, [LOrthND_evoked, HOrthND_evoked]))


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="mag",
    colors=dict(LOrthND=0, HOrthND=1),
    axes="topo",
)


# In[ ]:


mne.viz.plot_compare_evokeds(
    evks,
    picks="MEG 049",
    colors=dict(LOrthND=0, HOrthND=1),
    time_unit="ms",
)


# In[ ]:





# In[ ]:




