[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/VaFOWmpj)

# About this project
This project scrapes the roadtonationals.com website to retrieve the past 10 years of information about women's gymnastics teams, meets, gymnasts and scores and performs some analysis on the results over time.

# Team
Created by Jes Hyne (@jesatuts2)

# Replication
1. Install Python and a conda distribution (either Anaconda or Miniconda)
2. Create a new conda environment for this project and activate it

```
conda init
conda create -n gymternet -- python 3.12
conda activate gymternet 
conda install pip -y
```

3. Install the required packages

```
pip install -r ../requirements.txt
```

4. If running on VSCode, clone this repository and activate the corret environemnt every time you are running a notebook.

5. Go through each of the notebooks under the `notebooks` folder, read and then run.

## What you will find

- Scraping is time consuming and buggy. You will need to re-run the scraping methods several times to get through all the crashes.

