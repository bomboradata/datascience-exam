<div class="clearfix" style="padding: 10px; padding-left: 0px">

<p>
<a href="http://bombora.com"><img src="https://app.box.com/shared/static/e0j9v1xjmubit0inthhgv3llwnoansjp.png" width="150px" class="pull-right" style="display: inline-block; margin: 5px; vertical-align: middle;"></a>
<h1> Bombora Data Science: Interview Exam </h1>
</div>
<img width="200px" src=https://app.box.com/shared/static/15slg1mvjd1zldbg3xkj9picjkmhzpa5.png >

---


# Welcome!

From all of us at Bombora Data Science, we're excited to get to know you! To do so, we'd like to begin by engaging in a few exercises exploring concepts we're interested in (and hope you are as well). 

**NOTE**: We'll be leveraging open tools and public repositories. Ethics and professional aspirations should drive you to work creatively, enthusiastically, and *independently*. Clearly, you should leverage all resources you can, but please, *do not* share this exam or your solutions with any other entity, man or machine. :)

Thank you so much! Now, get comfortable and let's go!

# Instructions

## Overview
We're going to leverage typical analysis and development workflows used by our team to conduct an interview exam. In short, you'll:

- fork this repository and setup a working directory on your machine
- open the exam Jupyter notebook in an [POSIX environment](https://en.wikipedia.org/wiki/POSIX) of your choice (web or local), using a language (kernel) of your choice (you can choose between Scala, R, Haskell, Ruby, Python 2/3, Julia, Octave or even Bash)
- answer three questions of your choice, one from each section
- add, commit, and push your solution + resume (and other docs, if you wish) to your remote repo
- send us completed exam submittal via a [pull request PR](https://help.github.com/articles/about-pull-requests/)

## Details

### 0. Configure exam params:
Define a few parameters used throughout the exam:
- `your-gh-username`: your [GitHub username](https://help.github.com/articles/remembering-your-github-username-or-email/).
- `ds-position`: the title of the position you're applying to, specified in the email you recieved (e.g., `data-engineer-2019-q2`, `data-scientist-intern-2019-spring`)
- `mylastname-myfirstname`: your name, backwards of course!

If you're a POSIX shell user (e.g., linux or osx), you can set these params via environment variables so future commands won't have to be manually modified!
 
```bash
export GH_USERNAME='carlsagan'
export DS_POSITION='data-science-director'
export DS_EXAM_NAME='sagan-carl'
```

### 1. Make your own copy of repo

#### Fork repo to your GitHub account

It's the button above that looks like the one below (you can click either):

<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/bomboradata/datascience-exam/fork" data-style="mega" aria-label="Fork bomboradata/datascience-exam on GitHub">Fork</a>

#### Local Clone

On your local machine, with `git` installed:
```bash
git clone git@github.com:$GH_USERNAME/datascience-exam.git
cd datascience-exam
```

#### Checkout `$DS_POSITION` branch

Develop against a branch titled for the position you're applying to:

```bash
git checkout $DS_POSITION
```
	

### 2. Setup your exam working directory

1. Create your *exam directory*:

    ```bash
    mkdir ./submittals/$DS_POSITION/$DS_EXAM_NAME
    ```

2. Copy exam notebook (`ds-interview-exam.ipynb`) to your *exam directory*:
    
    ```bash
    cp ds-interview-exam.ipynb ./submittals/$DS_POSITION/$DS_EXAM_NAME/
    ```

### 3. Setup Jupyter Notebook Environment

#### 3.1 Launch Jupyter
You have two options:

1. **Upload the included `ds-interview-exam` notebook to [try.jupyter.org](https://try.jupyter.org/)** (easy and recommended):
	- open [try.jupyter.org](https://try.jupyter.org/),
	- Upload this notebook to Jupyter session
		- click `upload` in upper right corner
   		- select the local notebook file (e.g., your copy of `data-science-exam.ipynb`)
    - click on notebook to open.

2. or, **create a local conda env**, if you prefer (much) more control of packages, (difficult):
    - [install conda / miniconda](http://conda.pydata.org/).
    - create `bombora-datascience-exam` conda environment, via (from repo root): 
        `conda env create -f bombora-datascience-exam.yml`
    - activate conda environment, via: 
        `source activate bombora-datascience-exam`
    - launch Jupyter, via: 
        `jupyter notebook`
    - open your copy of `ds-interview-exam.ipynb` notebook 

#### 3.2 Setup Jupyter

**Note**: for those not familiar with Jupyter notebook, please view the *Welcome to ...* intro notebooks included in file listing. Also, you can review the [Notebook Basics tutorial](http://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb).

After opening your notebook, you'll need to select a language kernel of your choice, (you can choose between Scala, R, Haskell, Python 2 or 3, Julia or even Bash).

- from menubar of the opened notebook, select * Kernel > Change Kernel > <your language>*
 

### 4. Solve *THREE* problems, one from each section.

1. Take note that there are **three** sections, they are:
	- *1. Algo + Data Structures*
	- *2. Prob + Stats*
    - *3. Conceptual ML*

2. Take 15 minutes to review questions across each section.

3. Select and answer **ONE** question from **EACH** section, or to be totally explicit:
	- select and answer a question from section 1 (e.g., either Q1.1 or Q1.2).
	- select and answer a question from section 2 (e.g., either Q2.1, Q2.2, Q2.3, Q2.4, Q2.5 or Q 2.6).
    - select and answer a question from section 3 (e.g Q3.1, Q3.2)

This is you, _shining_ :sparkles:. Think, Hack, Solve, Repeat. Do enjoy this part. :smile:


### 5. Commit results and push to your remote repo.
 
- copy your resume (and additional docs) to your exam directory:
    ```bash
    cp path/to/my-resume.pdf ./submittals/$DS_POSITION/$DS_EXAM_NAME/
    # (optional)
    cp path/to/my-other-docs.pdf  ./submittals/$DS_POSITION/$DS_EXAM_NAME/
    ```
- add your *exam directory* and commit
    ```bash
    git add ./submittals/$DS_POSITION/$DS_EXAM_NAME
    git commit -m "Exam submittal for $DS_POSITION"
    ```
- push to remote repo
    ```bash
    git push origin $DS_POSITION
    ```

### 6. Open Pull Request to submit exam

To submit, [please open a PR](https://help.github.com/articles/creating-a-pull-request/) to the `$DS_POSITION-submittals` branch (*note*: this is a different branch name) of the repo.


## Questions?

Open an issue in the GH repo, we provide a button right here, for your convenience. 

<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/bomboradata/datascience-exam/issues" data-icon="octicon-issue-opened" data-style="mega" data-count-api="/repos/bomboradata/datascience-exam#open_issues_count" data-count-aria-label="# issues on GitHub" aria-label="Issue bomboradata/datascience-exam on GitHub">Issue</a>


## Finished, what's next? 

Go enjoy your day—you deserve it!


<!-- Place this tag in your head or just before your close body tag. -->
<script async defer src="https://buttons.github.io/buttons.js"></script>
