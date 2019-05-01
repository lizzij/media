# Flask

## Local  
0. http://127.0.0.1:5000/nBEXdMJkv56ymRZx/vQp4l04x0q/info
1. http://127.0.0.1:5000/lq13ZopK7pbrkJ7X/BKzwNEGg9y/info  
2. http://127.0.0.1:5000/j9Z4Jbol5rwABVxl/d7kZonDXxO/info  
3. http://127.0.0.1:5000/zdRBqlnO1Mgk7vA5/0M4kEvea92/info  
4. http://127.0.0.1:5000/kaBxo92L02dbXL4K/B2J6joM8xb/info  
5. http://127.0.0.1:5000/WgkBxb2bv219qRDJ/rxn69e6N38/info  
6. http://127.0.0.1:5000/5gKLM4A7vwr3aBlm/K0zAVkYV8W/info  
7. http://127.0.0.1:5000/ZdwQaPxbdk8Lne3B/83AwJbw2RV/survey  
8. http://127.0.0.1:5000/wMWaznOryK6prqe2/Ey3l4RPxZV/survey  

http://127.0.0.1:5000/completion/detail
http://127.0.0.1:5000/activity
http://127.0.0.1:5000/allActivities
http://127.0.0.1:5000/allUsers

## HTTPS  
0. https://dailyeventinfo.com/nBEXdMJkv56ymRZx/vQp4l04x0q/info
1. https://dailyeventinfo.com/lq13ZopK7pbrkJ7X/BKzwNEGg9y/info
2. https://dailyeventinfo.com/j9Z4Jbol5rwABVxl/d7kZonDXxO/info
3. https://dailyeventinfo.com/zdRBqlnO1Mgk7vA5/0M4kEvea92/info
4. https://dailyeventinfo.com/kaBxo92L02dbXL4K/B2J6joM8xb/info
5. https://dailyeventinfo.com/WgkBxb2bv219qRDJ/rxn69e6N38/info
6. https://dailyeventinfo.com/5gKLM4A7vwr3aBlm/K0zAVkYV8W/info
7. https://dailyeventinfo.com/ZdwQaPxbdk8Lne3B/83AwJbw2RV/survey
8. https://dailyeventinfo.com/wMWaznOryK6prqe2/Ey3l4RPxZV/survey

https://dailyeventinfo.com/completion/detail
https://dailyeventinfo.com/activity
https://dailyeventinfo.com/allActivities
https://dailyeventinfo.com/allUsers

## How to run locally:
- Clone repo locally
```
git clone https://github.com/lizzij/media.git
cd media
```

- Navigate to root dir
```
source venv/bin/activate
export FLASK_APP=media
export FLASK_ENV=development
flask run
```

- Initialize database
```
flask init-db
```

## How to run remotely:
- Login (with password)
```
ssh donghee@202.182.126.239
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
