# DSP 439: Exam 4

This project provides tools for exploring genome sequences, specifically through the detection and evaluation of k-mers. It includes features to determine the minimal k value at which every k-mer within a group of sequences uniquely prescribes its following k-mer.

# Overview
The project includes a Python script that:
- Identifies all k-mers in a given sequence and maps each k-mer to its possible subsequent k-mers
- Processes multiple sequences to collect this mapping across all given sequences
- Finds the smallest k such that each k-mer uniquely identifies its following k-mer across all provided sequences

# Installation
Clone this repository to your local terminal using the following command:
```bash
git clone https://https://github.com/carlycarroll25/DSP-439-Exam-4.git
