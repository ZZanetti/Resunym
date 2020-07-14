# Resunym
Job hunting utility built with Python.

## What is Resunym?

Resunym is a Python Application that is intended for job hunters who want to gain an edge on their competition by increasing the amount of keywords shared between the users resume or cover letter and the job posting. 

## What <em>Should</em> Resunym Do?
Resunym shoud:
1. Take two sets of input:
   - Set 1 - one or more documents (your resume and/or cover letter) that you would like to improve, the targets.
   - Set 2 - one or more documents (a job posting or similar) that you would like to use as a key.
2. Parse the documents and produce an initial score from 1 to 100 based on word overlap.
3. Try to improve the score by trying to find and replace words in the following ways:
      - Synonym approach - use wordnet python interface to query for synonyms of words within the targets and keys, using synonym overlap to make replacements. 
      - Recognize "node" vs "node.js" issue - if the job posting wants "node" experience, and your resume says node.js, can you guarantee the HR software will count your experience? It is better not to leave it to chance and replace your use of node.js with node for this particular application. 
      - Prompt further action approach - should ask the user questions like "Do you know Python? The job posting mentions it 4 times, mentions it after the keystone word qualifications, but your target docs do not have the word. If you know it... add it!" 

## Why Build Resunym?

I am building Resunym because finding a job is often a difficult task. If I could do something quick and easy with my resume or cover letter before sending it to make myself feel more confident, why not do it? 

One can Google "matching words in job posting" and see that services already exist for this type of purpose, however, my application will be different. No email sign up, no login, no cookies, and no $89.95 for three months. This app will be free for anyone to use, however many times they want. All the source code will be public on Github. Help is welcome! 

## How Does It Work? 

Python CLI, WordNet
