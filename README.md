---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-06-07" # Date you first upload your project.
# Title of your project (we like creative title)
title: "The Effects of Word Frequency, Orthographic Neighborhood and Part of Speech in Word Processing: A MEG Study"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Ruo-Chi Yao]

# Your project GitHub repository URL
github_repo: https://github.com/Ruo-Chi/Ruo-Chi-Yao_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [meg, github, mne, python]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Word processing is influenced by different attributes of words, which can be observed vis brain imaging techniques such as MEG. Let's find evidence of the influence of word attributes by analyzing a dataset."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: ""
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Word processing is influenced by different attributes of words, which can be observed vis brain imaging techniques such as MEG. This project focuses on attributes of words, including word frequency, orthographic neighborhood, and part of speech.
- In word processing, high-frequency words are handled more easily and quickly than low-frequency words.
- An orthographic neighborhood refers to words that are similar to a target word by differing in only one letter (addition, deletion, or substitution of a single letter).
- Part of speech refers to the grammatical category or class that a word belongs to.

We have all learned and understood that various attributes of words impact word processing, whether from textbooks or lectures. However, many of us may not have had the opportunity to obtain evidence regarding this ourselves. The main question here is whether I can find evidence of the influence of word attributes by analyzing a dataset. Therefore, the primary question here is whether I can find evidence of the influence of word attributes by analyzing a dataset.

### Tools

The dataset processing by useing mne-python

### Methods

![alt text](https://github.com/Ruo-Chi/Ruo-Chi-Yao_project/blob/main/images/methods.png)

- Read & Load raw data
- Filter & Down sample
- Find event id
- Do artifact rejection & slice the data into epochs
- Working with Epoch metadata & Visualizing Evoked data


### Data

Dataset: [Auditory single word recognition in MEG – OpenNeuro](https://openneuro.org/datasets/ds004276/versions/1.0.0)
- There are files for 18 subjects, but 12 of them can be download successfully.
- 1000 trials for one subject, that is each subject listens to 1000 words.
- There are 97 extra words specifically for semantic probe tasks that involve go/no-go trials.
- Data are recorded using MEG.


### Deliverables

At the end of this project, we will have:
 - A GitHub repository.
 - A markdown document.
 - MEG data analysis with MNE-Python.

## Results

### Frequency effects

### Orthographic neighborhood

### Part of speech


## Conclusion and acknowledgement

The BHS team hope you will find this template helpful in documenting your project. Developping this template was a group effort, and benefitted from the feedback and ideas of all BHS students over the years.


## References

