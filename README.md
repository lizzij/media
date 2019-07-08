# Media Study
Flask app for info and survey distribution.

## Documentations
### pilot
- Read [documentation](https://docs.google.com/document/d/1tng4vsgPXjuKzJaPWZg7eiDzAz9nOl0U7VqSZvYjSCk/edit?usp=sharing) here
- [Treatment](https://docs.google.com/spreadsheets/d/1rbqW0Ooj0mW6yI6AapUmkkDcs3w8OI5H3VPDT4D049o/edit?usp=sharing) T1, T2 - T2.S.M, T3 - T2.M.S, T4 - T2.M.M.N, T5 - T2.M.M.C
  - Event 6 (cohort 1: user 1-4; cohort 2: user 5)

- [Q&A Code](https://docs.google.com/spreadsheets/d/13eTESZNvaWt9HJT508376lfapPdtOMc5z4Z9fiaU_P4/edit?usp=sharing)
  - Question (from google doc), QuestionCode, Option/Subqn (from google doc), OptionCode, Relevant (note and related questions)

### xian
- [Google docs (edit mode)](https://docs.google.com/document/d/1xvPo-bulFDlbYwLeHmL--fx_NsrwSkMH_i8PZwZrUGc/edit?usp=sharing)
  - 2 days Xi'an Pilot

## Results
Paste the code into terminal, and hit Return key.
### Get allActivites.csv
Headers: user_id, day, day_complete, survey_page, day_started, curr_time
```bash
wget -qO- https://dailyeventinfo.com/allActivities | sed -e 's/<[^>]*>//g;s/^ //g;s/^[ \t]*//;s/完成情况//;/^$/d' > allActivites.csv
```

### Get allUsers.csv
Headers: user_id, day, wechat_id, cohort, treatment, user_id_hashid, day_hashid
```bash
wget -qO- https://dailyeventinfo.com/allUsers | sed -e 's/<[^>]*>//g;s/^ //g;s/^[ \t]*//;s/完成情况//;/^$/d' > allUsers.csv
```

### Get allResults.csv
Headers: user_id, day, question_id, result, created
```bash
wget -qO- https://dailyeventinfo.com/allResults | sed -e 's/<[^>]*>//g;s/^ //g;s/^[ \t]*//;s/完成情况//;/^$/d' > allResults.csv
```

### Get allEvents.csv
Paste from [here](https://dailyeventinfo.com/allEvents), or use the script below.    

Headers: event_id, title, subtitle, info_date, info_time, location, image_file, air_quality_source, air_quality_source_logo, short_description, low_temp, high_temp, suitable_for_family, suitable_for_friends, suitable_for_lover, suitable_for_baby, suitable_for_elderly, suitable_for_pet, event_details, phrase_for_week, phrase_for_day, phrase_for_header, cohort
```bash
wget -qO- https://dailyeventinfo.com/allEvents | sed -e 's/<[^>]*>//g;s/^ //g;s/^[ \t]*//;s/完成情况//;/^$/d' > allEvents.csv
```

## Cohorts
### CRUD
(Applicable to all cohorts) create, read, update and delete.  
Click [here](https://github.com/lizzij/media/blob/master/media/templates/crud/README.md) for testing links and detailed README.

### Pilot
For Shanghai cohort 1, 2 in May, June.    
Click [here](https://github.com/lizzij/media/blob/master/media/templates/pilot/README.md) for testing links and detailed README.

### Ui Test
For testing info page button and layout, Beijing in June.     
Click [here](https://github.com/lizzij/media/blob/master/media/templates/ui_test/README.md) for testing links and detailed README.

### Xi'an Trial
For Xi'an cohort 3 in July.  
Click [here](https://github.com/lizzij/media/blob/master/media/templates/xian/README.md) for testing links and detailed README.

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
**Git branches**
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

**File structure**
```bash
media
├── __init__.py
├── crud.py
├── db.py
├── pilot.py
├── schema.sql
├── static
│   ├── img
│   │   ├── ...
│   │   ├── favicon.ico
│   │   ├── favicon_package_v0.16
│   │   │   └── ...
│   ├── scripts
│   │   ├── bootstrap.js
│   │   ├── bootstrap.min.js
│   │   ├── jquery-3.3.1.slim.min.js
│   │   ├── jweixin-1.2.0.js
│   │   ├── popper.min.js
│   │   ├── survey1.js
│   │   ├── survey2.js
│   │   ├── survey3.js
│   │   ├── survey4.js
│   │   ├── survey5.js
│   │   ├── survey6.js
│   │   ├── survey7.js
│   │   ├── survey8.js
│   │   └── surveyInfo.js
│   └── styles
│       ├── bootstrap.css
│       ├── consentForm.css
│       ├── infoPage.css
│       ├── infoPageTest.css
│       └── questions.css
├── templates
│   ├── crud
│   │   ├── README.md
│   │   ├── activityList.html
│   │   ├── home.html
│   │   ├── infoList.html
│   │   ├── surveyList.html
│   │   ├── updateEvent.html
│   │   └── userList.html
│   ├── pilot
│   │   ├── README.md
│   │   ├── completionPage.html
│   │   ├── consentForm.html
│   │   ├── infoPage.html
│   │   ├── infoPageAQ.html
│   │   ├── infoPageCO.html
│   │   ├── survey1.html
│   │   ├── survey2.html
│   │   ├── survey3.html
│   │   ├── survey4.html
│   │   ├── survey5.html
│   │   ├── survey6.html
│   │   ├── survey6T3.html
│   │   ├── survey6T5.html
│   │   ├── survey7.html
│   │   ├── survey8.html
│   │   └── surveyInfo.html
│   ├── ui_test
│   │   ├── README.md
│   │   ├── infoPagea.html
│   │   ├── infoPageb.html
│   │   ├── infoPagec.html
│   │   └── infoPaged.html
│   └── xian
│       ├── README.md
│       ├── infoPagea.html
│       ├── infoPagec.html
│       ├── survey1.html
│       └── survey2.html
├── ui_test.py
├── xian.py
└── xian.pyc
```
