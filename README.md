# Flask

## Results
### Get allActivites.csv
eaders: user_id, day, day_complete, survey_page, day_started, curr_time
```bash
wget -qO- https://dailyeventinfo.com/allActivities | sed -e 's/<[^>]*>//g;s/^ //g;s/^[ \t]*//;s/完成情况//;/^$/d' > allActivites.csv
```

### Get allUsers.csv
eaders: user_id, day, wechat_id, treatment, user_id_hashid, day_hashid
```bash
wget -qO- https://dailyeventinfo.com/allUsers | sed -e 's/<[^>]*>//g;s/^ //g;s/^[ \t]*//;s/完成情况//;/^$/d' > allUsers.csv
```

### Get allResults.csv
headers: user_id, day, question_id, result, created
```bash
wget -qO- https://dailyeventinfo.com/allResults | sed -e 's/<[^>]*>//g;s/^ //g;s/^[ \t]*//;s/完成情况//;/^$/d' > allResults.csv
```

## Local  
 [Treatment](https://docs.google.com/spreadsheets/d/1rbqW0Ooj0mW6yI6AapUmkkDcs3w8OI5H3VPDT4D049o/edit?usp=sharing)
 - Event 6 (cohort 1: user 1-4; cohort 3: user 5)

**user_id: 1 (T1)**  

0. http://127.0.0.1:5000/nBEXdMJkv56ymRZx/vQp4l04x0q/info
1. http://127.0.0.1:5000/lq13ZopK7pbrkJ7X/BKzwNEGg9y/info  
2. http://127.0.0.1:5000/j9Z4Jbol5rwABVxl/d7kZonDXxO/info  
3. http://127.0.0.1:5000/zdRBqlnO1Mgk7vA5/0M4kEvea92/info  
4. http://127.0.0.1:5000/kaBxo92L02dbXL4K/B2J6joM8xb/info  
5. http://127.0.0.1:5000/WgkBxb2bv219qRDJ/rxn69e6N38/info  
6. http://127.0.0.1:5000/5gKLM4A7vwr3aBlm/K0zAVkYV8W/info  
7. http://127.0.0.1:5000/ZdwQaPxbdk8Lne3B/83AwJbw2RV/survey  
8. http://127.0.0.1:5000/wMWaznOryK6prqe2/Ey3l4RPxZV/survey  

**user_id: 2 (T2 - T2.S.M)**  

0. http://127.0.0.1:5000/Pd1aWzXvArJqBAkv/RlgLN2LVAy/info
1. http://127.0.0.1:5000/a3k47g0J60EmWOjD/QGngX7ZREN/info
2. http://127.0.0.1:5000/KLjpVX7zr7gy80wv/waA5xNgGBo/info
3. http://127.0.0.1:5000/eNgrz2DvZDjWoGYk/1N3EQRmKkB/info
4. http://127.0.0.1:5000/3xJwy7M9Oeogn6aj/o2jMjq6VJy/info
5. http://127.0.0.1:5000/rY9PkmGVZGAQel7d/1k0JN9bwEA/info
6. http://127.0.0.1:5000/WgbVQrxQjq7KZB0N/2xynrXRY6p/info
7. http://127.0.0.1:5000/D0npXYO6vOq1a9Qj/eAoO5AOV5J/survey
8. http://127.0.0.1:5000/qQ3rMl6O07OgbXDa/pqNAOm9MEz/survey

**user_id: 3 (T3 - T2.M.S)**  

0. http://127.0.0.1:5000/NWLgZQrw3rPXRjd3/ay3KxzDe2A/info
1. http://127.0.0.1:5000/klzKE7O7vabVm81B/1ENB753m7V/info
2. http://127.0.0.1:5000/n5aWdxrKLjYLZGEM/2DeEQvl48G/info
3. http://127.0.0.1:5000/1ElkqYNKePeXR2Dd/7oG0Nybg4e/info
4. http://127.0.0.1:5000/gj1q87Aa1AOm3p2N/eyx3Wjwljb/info
5. http://127.0.0.1:5000/YWdv0POjwgkyXbm9/DpvE6pwj6N/info
6. http://127.0.0.1:5000/q0xB9akeykzLVrDN/0opwpMANLj/info
7. http://127.0.0.1:5000/o8KA7kDnx9MRV0La/YQwRkwRV26/survey
8. http://127.0.0.1:5000/5K4OgV8pd8bWo6nM/DOW7EvRxb6/survey

**user_id: 4 (T4 - T2.M.M.N)**  

0. http://127.0.0.1:5000/XVvqpgPkEOdbW8jY/A1080l8kYl/info
1. http://127.0.0.1:5000/K7JpVY69VlQEAM8b/RA0EvZEYaZ/info
2. http://127.0.0.1:5000/OKe24R078PAwzkEX/DnPq7bxv78/info
3. http://127.0.0.1:5000/eqzrYQ65xGPXgpKa/VyW8wK8xg4/info
4. http://127.0.0.1:5000/a1NGEq8dL8O30dvR/enGXVpZplv/info
5. http://127.0.0.1:5000/32r8pAgOAN4Qlved/YBVw1LMd8y/info
6. http://127.0.0.1:5000/PW5ebVJOeDR4lwLM/XMvKkdPJ7q/info
7. http://127.0.0.1:5000/qQ9nL6R5QRB75AX1/Ee8rRgbLA5/survey
8. http://127.0.0.1:5000/ve5oEQLZa8j63K49/kmjgdnrvD8/survey

**user_id: 5 (T5 - T2.M.M.C)**   

0. http://127.0.0.1:5000/yR1b89ly6jQ4e5kM/Ge94yz6xPz/info
1. http://127.0.0.1:5000/4w08DXWoV2aNb6Oo/4apzLw9drO/info
2. http://127.0.0.1:5000/VQ6Lj5W5DBZDP2mr/zB5nNYlZW7/info
3. http://127.0.0.1:5000/badqeQgMegOGWRM7/PGQowAk8xV/info
4. http://127.0.0.1:5000/vbwP4Z1AQ1a2qApK/ZnMwr8eDd9/info
5. http://127.0.0.1:5000/Y2BLrMobroyQpGz5/R5PrzLJBEO/info
6. http://127.0.0.1:5000/NadJDQzk4Rj0rq6k/NWnzyLb6Lm/info
7. http://127.0.0.1:5000/vB6yXbw2vw1oEZep/51OArlkDlY/survey
8. http://127.0.0.1:5000/6XmQ08RlOMkjg2zn/NGm9R0ebZM/survey

**check**
- http://127.0.0.1:5000/allResults
- http://127.0.0.1:5000/activity
- http://127.0.0.1:5000/allActivities
- http://127.0.0.1:5000/allUsers

## HTTPS  
**user_id: 1 (T1)**  

0. https://dailyeventinfo.com/nBEXdMJkv56ymRZx/vQp4l04x0q/info
1. https://dailyeventinfo.com/lq13ZopK7pbrkJ7X/BKzwNEGg9y/info
2. https://dailyeventinfo.com/j9Z4Jbol5rwABVxl/d7kZonDXxO/info
3. https://dailyeventinfo.com/zdRBqlnO1Mgk7vA5/0M4kEvea92/info
4. https://dailyeventinfo.com/kaBxo92L02dbXL4K/B2J6joM8xb/info
5. https://dailyeventinfo.com/WgkBxb2bv219qRDJ/rxn69e6N38/info
6. https://dailyeventinfo.com/5gKLM4A7vwr3aBlm/K0zAVkYV8W/info
7. https://dailyeventinfo.com/ZdwQaPxbdk8Lne3B/83AwJbw2RV/survey
8. https://dailyeventinfo.com/wMWaznOryK6prqe2/Ey3l4RPxZV/survey

**check**
- https://dailyeventinfo.com/allResults
- https://dailyeventinfo.com/activity
- https://dailyeventinfo.com/allActivities
- https://dailyeventinfo.com/allUsers

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
