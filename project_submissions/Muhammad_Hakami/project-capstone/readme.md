# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Part 1: Pitch + Problem Statement

## Overview

In the field of data science, good projects are **practical**. Your capstone project should be manageable and affect a real world audience. This might be a domain you are familiar with, a particular interest you have, something that affects a community you are involved in, or an area that relates to a field you wish to work in.

One of the best ways to test ideas quickly is to share them with others. A good data scientist has to be comfortable discussing ideas and presenting to audiences. That's why for Part 1 of your Capstone project, you'll be proposing some potential interest areas and datasets.

This deliverable will provide you with guidance to help you select an awesome topic and begin to build a polished Capstone project. 

**Goal**: Edit README by describing *at least two* project proposals, including associated data, goals, audiences, and metrics.

Here are some ideas: 
https://docs.google.com/document/d/1m7JotdnRb2LfXCUl_NhshrrhAwV29XXjSa90aHc7fF8/edit?usp=sharing

---

## Requirements
1. Edit the README of your capstone project with **at least two** potential topics for your DSI capstone project. For each topic, define **all** required areas:

2. Topic 1
   - Problem Statement
   - Potential Audience 
   - Goals
   - Success Metrics
   - Data Source(s)
   
3. Topic 2
   - Problem Statement
   - Potential Audience 
   - Goals
   - Success Metrics
   - Data Source(s)

#### BONUS
4. Beyond the two required topics, what other potential topics might you explore? (e.g. 3 or more)
5. For all datasets, identify their source, format, and necessary action items to obtain or access them.
6. Create a blog post of at least 500 words (and 1-2 graphics!) that describes your project idea, data, and audience. Link to it in your presentation appendix.
 
 ***Remember, if you can't find data to support your topic, then you can't move forward.***

---

## Deliverable Format & Submission

- Edit README and open pull request for capstone part-1. 

---

## Suggested Ways to Get Started

**Begin by Asking:**
- What is the scope of the need or problem I wish to investigate?
- Who is this for? Who is impacted or affected by this data? Who would benefit from this model?
- What are my goals for this investigation?
- What does success look like? How will I know if my model performs well?
- Where will I find data for this project? Is the data available?

**For the Bonus, Ask:**
- What format is the data in? What specific steps do I need to take to access it?
- How will I explain this project to outside audiences?

**Other Tips:**
- For your 1st potential topic, start with an idea, then look for potential data that could be used to support that idea.
- For your 2nd potential topic, reverse the process; look for interesting data and then extrapolate problems it could solve and audiences it could impact.
- Choose a topic that you have interest in as you will be working on this a lot, or choose a topic with data from the industry you wish to be hired into.

---

## Useful Resources

- [How to find the data you need.](http://flowingdata.com/2009/10/01/30-resources-to-find-the-data-you-need/)
- [How to give a good lightning talk.](https://www.semrush.com/blog/16-ways-to-prepare-for-a-lightning-talk/)

---

## Project Feedback + Evaluation

[Attached here is a complete rubric for this project.](./capstone-part-01-rubric.md)

Your instructors will score each of your technical requirements using the scale below:

Score  | Expectations
--- | ---
**0** | _Incomplete._
**1** | _Does not meet expectations._
**2** | _Meets expectations, good job!_

---

## 1- The hunt for exoplanets.
   - Problem Statement.
Exoplanets(planets not orbiting our sun) are really hard to spot using telescope due to the light of each star, but scientist can detect it by looking at the decrease in flux(light intensity) due to a planet blocking part of the flux to our point of view, so to gather data NASA launched kepler a space telescope back in 2009. 
The mission was a success and it brought back 14 billion data points with some being noisy unrealistic for a human to go through, so thats where Machine Learning can help, taking part of the data i want to use ML to find the point where a scientist can then confirm it, i will try other filtering method to handle the noise like ICA and cluster the data to find the stars with highest number of exoplanets.
If i manage to finish all that and found time, then i will proceed to see if i can classify planets as habitable or not with other features.
   - Potential Audience 
Astronomers looking for faster way to parse through data to find exoplanets.
   - Goals
Classify if star has planet or not, then cluster to find the highest number of planets in a star.
   - Success Metrics
Accuracy, Recall and f1 score.
   - Data Source(s)
NASA open data's database.

--

## 2- Search for dark matter hints at CERN experiment.
   - Problem Statement
Dark matter is considered to be one of most puzzling phenomena about space, weather it exist or not and if it does exists, is it the reason for the universe's expansion?, while these questions are interesting im clustering to search for a specific pattern not trying to answer the privous questions.
   - Potential Audience 
physicist, Astronomers and ML enthusiasts.
   - Goals
To find a spicific pattern in a 3D plot using clustering methods.
   - Success Metrics
The Silhouette Coefficient.
   - Data Source(s)
CERN's kaggle competition.