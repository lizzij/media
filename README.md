# Media Study
Flask app for info and survey distribution.   
To read more about the research project and the development process, please head to the *[Power of Repetition repo](https://github.com/lizzij/powerofrepetition)*.

## Documentations
### pilot
- Read documentation here: [Google docs (read only mode)](https://docs.google.com/document/d/1tng4vsgPXjuKzJaPWZg7eiDzAz9nOl0U7VqSZvYjSCk/edit?usp=sharing) here
- [Treatment](https://docs.google.com/spreadsheets/d/1rbqW0Ooj0mW6yI6AapUmkkDcs3w8OI5H3VPDT4D049o/edit?usp=sharing) T1, T2 - T2.S.M, T3 - T2.M.S, T4 - T2.M.M.N, T5 - T2.M.M.C
  - Event 6 (cohort 1: user 1-4; cohort 2: user 5)

- [Q&A Code](https://docs.google.com/spreadsheets/d/13eTESZNvaWt9HJT508376lfapPdtOMc5z4Z9fiaU_P4/edit?usp=sharing)
  - Question (from google doc), QuestionCode, Option/Subqn (from google doc), OptionCode, Relevant (note and related questions)

### xian
- Read documentation here: [Google docs (edit mode)](https://docs.google.com/document/d/1xvPo-bulFDlbYwLeHmL--fx_NsrwSkMH_i8PZwZrUGc/edit?usp=sharing)
  - 2 days Xi'an Pilot

### shanghai
- Read documentation here: [Google docs (edit mode)](https://docs.google.com/document/d/1AGfqTfGdcXFwWeM3YDiKz9QFVAWLMIoK75PEA8e1hwI/edit?usp=sharing)
  - 8 days Shanghai Pilot

### shanghai v2
- Read documentation here: [Google docs (edit mode)](https://docs.google.com/document/d/1AGfqTfGdcXFwWeM3YDiKz9QFVAWLMIoK75PEA8e1hwI/edit?usp=sharing)
  - 8 days Shanghai Pilot

## Results
Paste the code into terminal, and hit Return key.
### Get allActivites.csv
Headers: user_id, day, day_complete, survey_page, day_started, curr_time
```bash
wget -qO- https://dailyeventinfo.com/allActivities | sed -e 's/<[^>]*>//g;s/^ //g;s/^[ \t]*//;s/All Activities//;/^$/d' > allActivites.csv
```

### Get allUsers.csv
Headers: user_id, day, wechat_id, cohort, treatment, user_id_hashid, day_hashid
```bash
wget -qO- https://dailyeventinfo.com/allUsers | sed -e 's/<[^>]*>//g;s/^ //g;s/^[ \t]*//;s/All Users//;/^$/d' > allUsers.csv
```

### Get allResults.csv
Headers: user_id, day, question_id, result, created
```bash
wget -qO- https://dailyeventinfo.com/allResults | sed -e 's/<[^>]*>//g;s/^ //g;s/^[ \t]*//;s/All Results//;/^$/d' > allResults.csv
```

### Get allEvents.csv
Paste from [here](https://dailyeventinfo.com/allEvents), or use the script below.    

Headers: event_id, title, subtitle, info_date, info_time, location, image_file, air_quality_source, air_quality_source_logo, short_description, low_temp, high_temp, suitable_for_family, suitable_for_friends, suitable_for_lover, suitable_for_baby, suitable_for_elderly, suitable_for_pet, event_details, phrase_for_week, phrase_for_day, phrase_for_header, cohort
```bash
wget -qO- https://dailyeventinfo.com/allEvents | sed -e 's/<[^>]*>//g;s/^ //g;s/^[ \t]*//;s/All Event Info//;/^$/d' > allEvents.csv
```

## Cohorts
### CRUD
(Applicable to all cohorts) create, read, update and delete

| local                               | https                                    |
|-------------------------------------|------------------------------------------|
| http://localhost:5000/allResults    | https://dailyeventinfo.com/allResults    |
| http://localhost:5000/allActivities | https://dailyeventinfo.com/allActivities |
| http://localhost:5000/allUsers      | https://dailyeventinfo.com/allUsers      |
| http://localhost:5000/allEvents     | https://dailyeventinfo.com/allEvents     |
| http://localhost:5000/allPages      | https://dailyeventinfo.com/allPagse      |
| http://localhost:5000/eventUpdate   | https://dailyeventinfo.com/eventUpdate   |

### Pilot
For Shanghai cohort 1, 2 in May, June.    
Click [here](https://github.com/lizzij/media/blob/master/media/templates/pilot/README.md) for testing links and detailed README.

### Ui Test
For testing info page button and layout, Beijing in June.     
Click [here](https://github.com/lizzij/media/blob/master/media/templates/ui_test/README.md) for testing links and detailed README.

### Xi'an Trial
For Xi'an cohort 3 in July.  
Click [here](https://github.com/lizzij/media/blob/master/media/templates/xian/README.md) for testing links and detailed README.

### Shanghai Trial
For Shanghai cohort 4 in Sept/Oct.  
Click [here](https://github.com/lizzij/media/blob/master/media/templates/shanghai/README.md) for testing links and detailed README.

### Shanghai Trial V2
For Shanghai cohort 5 in Oct.  
Click [here](https://github.com/lizzij/media/blob/master/media/templates/shanghai/README.md) for testing links and detailed README.  
Distribution protocol [here](https://docs.google.com/document/d/1X7trhFmjKuQd4UWLsr00Zr5oqtovVxmtUySEcGZhhbQ/edit).

## How to run locally:
- Clone repo locally
```
git clone https://github.com/lizzij/media.git
cd media
```

- Navigate to root dir
```
source venv/bin/activate
flask run
```

- Initialize database
```
flask init-db
```

## How to run remotely:
- Login (with password)
```
ssh username@202.182.126.239
```
- Navigate to folder
```
cd ~/media
```

- Make changes
```
git pull
sudo systemctl restart media
```

## Developing...
####


#### Module management
- Installing packages using pip and virtual environments `pip install <module>` then `python -m flask run`
- [packaging guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- update `requirement.txt` with `pip freeze > requirements.txt` then
  - run `pip install -r requirements.txt` locally
  - or in server run `pip3 install --user -r requirements.txt`


#### Git branches
- `master` = deployed
  - merge `dev` to `master`

  ```
  (on dev)$ git merge master
  (resolve any merge conflicts if there are any)
  git checkout master
  git merge dev (there won't be any conflicts now)
  ```

- `dev` = latest working demo, merge into master regularly for deployment
  - push `dev` branch work to `dev`: `git push -u origin dev`
- `<feature-branch>` = developing, merge into dev branch regularly
  - start a new feature: `git checkout -b <feature-branch> dev`
  - commit, test and push `git push --set-upstream origin <feature-branch>`
  - merge to `dev`

  ```
  git commit -am "Your message"
  git checkout dev
  git merge --no-ff <feature-branch>
  git push origin dev
  git push origin <feature-branch>
  ```

- get changes from master to branches
  - `git checkout <branch>` get to the branch
  - `git rebase master` (discard history) or `git merge origin/master`

#### File structure
- use `tree` in `./media` dir to get the file tree
```bash
media
├── __init__.py
├── crud.py
├── db.py
├── info.py
├── pilot.py
├── schema.sql
├── shanghai.py
├── static
│   ├── img
│   │   ├── favicon.ico
│   │   ├── favicon_package_v0.16
│   │   │   └── …
│   │   └── …
│   ├── scripts
│   │   ├── bootstrap.min.js
│   │   ├── jquery-3.3.1.slim.min.js
│   │   ├── jweixin-1.2.0.js
│   │   ├── popper.min.js
│   │   └── …
│   └── styles
│       ├── bootstrap.css
│       └── …
├── templates
│   ├── crud
│   │   ├── README.md
│   │   ├── activityList.html
│   │   ├── getLink.html
│   │   ├── home.html
│   │   ├── infoList.html
│   │   ├── surveyList.html
│   │   ├── surveyorNumber.html
│   │   ├── updateEvent.html
│   │   ├── updateWechatID.html
│   │   └── userList.html
│   ├── pilot
│   │   ├── README.md
│   │   ├── completionPage.html
│   │   ├── consentForm.html
│   │   ├── infoPage.html
│   │   ├── infoPageAQ.html
│   │   ├── infoPageCO.html
│   │   ├── surveyInfo.html
│   │   └── …
│   ├── shanghai
│   │   ├── README.md
│   │   ├── consentForm.html
│   │   ├── infoPage.html
│   │   ├── infoPageAQ.html
│   │   ├── …
│   ├── ui_test
│   │   ├── README.md
│   │   ├── infoPagea.html
│   │   └── …
│   └── xian
│       ├── README.md
│       ├── infoPage.html
│       ├── …
│       ├── survey1.html
│       └── …
├── ui_test.py
└── xian.py

12 directories, 166 files
```
