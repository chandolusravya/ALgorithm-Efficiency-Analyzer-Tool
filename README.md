# ALgorithm-Efficiency-Analyzer-Tool

This tool analyzes and visualizes the efficiencies of different sorting algorithms.

# Instructions to run the Application ( MacOS )
Clone the repository using this URL
---
git clone https://github.com/chandolusravya/ALgorithm-Efficiency-Analyzer-Tool.git
---
cd AlgoAnalyzerTool
chmod +x setup app # This will give execute permission to setup and app files
./setup # This create a virtual environment and install all the dependencies
./app # This will run the application
Rules
All changes must be made using a Pull Request (PR), Follow instructions below to do one
Steps to create a PR and merge your changes
Clone the repository using this URL
git clone https://github.com/keshavlingala/AlgoAnalyzerTool
Make a branch/s for your changes, use the below command to create a branch
git checkout -b <your-name>
Example

git checkout -b keshav
Make your changes...
Add your changes using the below command
git add filename.py
Commit Your Changes
git commit -m "description of changes"
Push your changes
git push origin <branch-name>
Example

git push origin keshav
This will create a branch in the github.com (remote)

Now go to this URL https://github.com/keshavlingala/AlgoAnalyzerTool/branches here, you can see your branch , on your branch name, click New pull request button

Add title and description(optional) for the PR and click Create pull request

And then copy the URL and paste in our group chat to request for code review.

After at least 1 approval, you can merge your branch using the Merge Pull Request in the same PR link.

Important

When your changes are merged and you are going to make new changes YOU MUST FOLLOW BELOW STEPS

Rebase your branch to main branch before making new changes

git pull origin master
git rebase master
