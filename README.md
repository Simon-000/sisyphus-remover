TODO: test the instructions in README works as expected.
TODO: replace AWS specific references in README with local setup and OpenAPI.

# Purpose

Prototype a new feature of the RepairSense called SisyphusRemover that: 
1. Identifies jobs which are reoccurring issues.
2. Highlight properties which have the most repeat issues to find the root cause.



# Software Prerequisites

 a. [pipenv](https://pipenv.pypa.io/en/latest/installation/)

 b. [Git](https://git-scm.com/downloads)




# First Time Setup


1. Install software from above section.

2. Open terminal.

3. Navigate to folder where you want to clone your repository into:

 a. `cd "path"`

4. Set your Git credentials:

 a. `git config --global user.name "John Doe"`

 b. `git config --global user.email johndoe@example.com`

5. Clone Git repository:

 a. `git clone <repos-cloning-key>`

6. Navigate inside the repository:

 a. `cd path/to/repository`

7. In the root of your repository create hidden “.aws” folder:

 a. `mkdir .aws`

8. In ".aws" folder create file called "credentials" and add AWS secrets (access key ID and secret access key as a minimum; note below only creates "default" credentials but you can add multiple versions for different environments):

 a. `cd .aws`

 b. `nano credentials`

 c. Above opens text editor in your terminal so define any secrets (!!!DO NOT SHARE THIS WITH ANYONE OR EXPOSE IT!!) you will require. It should look something like this:

[default]
aws_access_key_id=my_access_key_id
aws_secret_access_key=my_secret_access_key

 c. Once you finished editing save and exit the editor (CTRL+O, Enter, CTRL+X).

9. Repeat step 8 but call newly created file "config".

10. Create your pipenv environment:

 a. `pipenv install --ignore-pipfile`





# Data Privacy, Security and Best Practice

1. Do NOT download any data on your local machine without explicit permission of the Project Owner. Use appropriate database connectors or work within secure AWS environment.

2. Do NOT version control any secretes i.e. passwords, IP addresses, SSH keys etc. Use AWS Secrets Manager for those.

3. Do NOT version control knitted Jupyter/RMarkdown notebooks or large outputs e.g. html plots. Instead please publish final version of your analytical notebook knitted as HTML in the S3 bucket.

4. Please follow "Quality Expectations" section for each analytical piece of work. By the time you finish the notebook should fulfil acceptance criteria, include interactive tests, code comments and narrative including executive summary written in a way that anyone can easily comprehend.

5. If your analysis includes any other outputs please upload them to the relevant S3 sub-bucket.

6. When working locally try to use VPN for added security (please note free VPNs tend to be spywares under the hood so either use company's VPN or your own private one).


# Quality Expectations

## Analytical/Data Science Work

The process is based on golden data science triangle, that through combining 3 key tools (analytical notebooks, version control and dependency/environment control) into unified process achieves maximum efficiency. This is because instead of treating each element of the data analysis (coding, annotation of results, testing, documentation, quality assurance and dissemination of results) as a separate entity, we deliver them all together. Furthermore this ensures every piece of analysis is perfectly reproducible, easily troubleshooted and over time creates many benefits through interoperability (this part is dependent on wider data infrastructure and processes surrounding it).

| Tool | Expectation |
| --- | --- |
| Analytical notebooks (e.g. Jupyter) | Notebook is easily traced to its originating ticket. |
|  | It contains “Executive Summary” section at the top that provides high level summary of key findings written in plain English/accessible to ALL stakeholders.|
|  | Is split in smaller sections easily navigated through interactive table of contents. |
|  | Markdown/text chunks are used to provide “the what, why and how” of the analysis including description of outputs and any potential caveats. |
|  | Code chunks are annotated through code comments explaining its purpose (not code itself, that’s what documentation pages are for). |
|  | All data operations are tested through interactive (i.e. requiring human judgment) tests. |
|  | All visualisations are created according to best practice meaning that anyone who looks at them should be able to easily understand information contained in the plot i.e. formatting makes it easy to absorb the information, axes are described including units, title provided and any other legend is included. |
|  | Technical language and techniques are welcome, except for “Executive Summary” section, but should be used as needed (do not over-engineer, simpler is always better) but they need to be explained to the level where average user (i.e. your team and stakeholders) can easily understand it. |
|  | Once the work is finished, including peer review, you should knit it and publish it where all stakeholders can easily access it. |
|  | Code for repetitive tasks is transformed as a documented function/method, published and disseminated for future use. |
|  | The notebook itself is version controlled whilst it’s rendered/knitted version plus any other outputs are stored in pre-agreed location. |
|  | As long as the task is achieved in a timely manner it does not matter how is it coded. Having said that data libraries, e.g. pandas, tend to be far more efficient. |
|  | Ideally if your audience requires specific output format you can knit your notebook as appropriate, possibly requiring additional formatting (e.g. for slides you need to specify the breaks). Copy/pasting is a waste of time so it always should be challenged. |
| Version control (e.g. Git) | Each task/ticket corresponds to a branch.| 
| | At minimum, Pull Requests require a single peer review. This should be scaled as appropriate depending on complexity and risks involved in particular project. |
| | Git strategy is defined, agreed and followed. Ideally this should be enforced through automated rules. |
| | You commit often and provide meaningful commit messages. |
| | DO NOT version control any secrets (passwords, API keys etc.), data or heavy outputs. |
| | DO NOT operate on main branch directly or merge anything without the peer review. |
| Dependency/environment control (e.g. Anaconda) | Add libraries/packages as you see fit and ensure every change is reflected in version control. |



# Git Strategy

TODO: write-up Git strategy for the repo - this should be discussed & agreed within the team.


## Analytical Feature Process

1. Grab analytical ticket from the current sprint and assign it to yourself.

2. Open terminal and navigate to the root of your repository:

 a. `cd path/to/repository`

3. Activate your pipenv environment (note environment is attached to location i.e. repository):

 a. `pipenv shell`

4. Make sure you are on “main” branch and update it:

 a. `git checkout main`

 b. `git pull`

5. Create feature branch forked from main that uses ticket name and switch to it (branch name is an example):

 a. `git checkout -b feature/ticket-number-raw-data-characterisation`

6. Copy appropriate template from “templates” into “notebooks” (below is an example for Jupyter template) and rename it :

 a. `cp templates/jupyter_template.ipynb notebooks/ticket-number-raw-data-characterisation.ipynb`
 
 b. If you have multiple files then create a folder starting from ticket name e.g. “ticket-number-raw-data-characterisation”, and move all your files there.

7. Keep existing terminal window open to interact with Git/pipenv and open new terminal.

8. Navigate to the root of your repository using your new terminal:

 a. `cd path/to/repository`

9. Activate your pipenv environment:

 a. `pipenv shell`

10. Launch Jupyter (or IDE of your choosing/open IDE and select environment from `path/to/repository`):

 a. `jupyter notebook`

11. Above opens Jupyter in the root of your repository so navigate to your notebook and open it.

12. Fill the template as instructed - template describes minimal set of information required so those need to be provided but beyond that feel free to extend it as you see fit.

13. Commit often and use meaningful commit messages e.g.

 a. `git add notebooks/ticket-number-raw-data-characterisation.ipynb`

 b. `git commit -m "Added subsection 4.4 Histograms"`

14. Once you finish your analysis open Pull Request between your branch and “main” branch, find data colleague from the team to review it and assign it to them. Please note that each Pull Request requires at least single review.

15. Complete the Pull Request as per reviewers feedback.

16. Once reviewer approves the Pull Request, they need to merge it and delete the feature branch.


## Infrastructure Feature Process

TODO: write-up infrastructure feature process.


## Hot-fix (a.k.a. bug fix ticket) Process

TODO: write-up hot-fix process.



## Adding New Libraries/Packages

### Development Environment

1. Activate your pipenv environment:

 a. Open terminal and navigate to the root of your repository:

  i. `cd path/to/repository`

 b. Activate the environment:

  i. `pipenv shell`

2. Switch to relevant feature branch:

 a. `git checkout feature/<your-branch-name>`

3. Make sure you have latest version of the branch:

 a. `git pull`

4. Freeze the current working environment, commit and push it:

 a. `pipenv lock`

 b. `git add .`

 c. `git commit -m "Added latest working version of the pipenv environment"`

 d. `git push`

5. Install libraries/packages you want (you can use pip instead of pipenv in this setup):

 a. `pipenv install <package-name>`

6. Restart Jupyter kernel, add the new module and load your modules to use new library.

7. If you get dependency errors with the new environment then you need to roll it back to last committed working version from step 4:

  a. `git reset --hard`

  b. `pipenv install --ignore-pipfile`

8. If everything went well and new environment is working then we need to add new libraries to environment definition i.e. “Pipfile.lock” file:

 a. `pipenv lock`

 b. `git add .`

 c. `git commit -m "Adding <library-name> library"`

 d. `git push`


### Infrastructure Environments

TODO: write-up process for updating respective infrastructure environments.
