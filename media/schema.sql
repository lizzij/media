DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS survey;
DROP TABLE IF EXISTS activity;
DROP TABLE IF EXISTS treatments;
DROP TABLE IF EXISTS infos;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  day INTEGER NOT NULL,
  wechat_id TEXT NOT NULL,
  treatment TEXT NOT NULL,
  user_id_hashid TEXT NOT NULL,
  day_hashid TEXT NOT NULL
);

CREATE TABLE survey (
  survey_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  day INTEGER,
  result TEXT NOT NULL,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  question_id TEXT,
  FOREIGN KEY (user_id) REFERENCES user (user_id)
);

CREATE TABLE activity (
  activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  day INTEGER NOT NULL,
  curr_time TIMESTAMP,
  status TEXT NOT NULL,
  current_url TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (user_id)
);

CREATE TABLE treatments (
  treatment_id INTEGER PRIMARY KEY AUTOINCREMENT,
  treatment TEXT NOT NULL,
  day INTEGER NOT NULL,
  event_id INTEGER NOT NULL,
  FOREIGN KEY (treatment) REFERENCES user (treatment)
);

CREATE TABLE infos (
  info_id INTEGER PRIMARY KEY AUTOINCREMENT,
  event_id INTEGER NOT NULL,
  title TEXT,
  subtitle TEXT,
  info_date TEXT,
  info_time TEXT,
  location TEXT,
  image_file TEXT,
  air_quality_source TEXT,
  air_quality_source_logo TEXT,
  headword TEXT,
  short_description TEXT,
  low_temp INTEGER,
  high_temp INTEGER,
  suitable_for_family INTEGER,
  suitable_for_friends INTEGER,
  suitable_for_lover INTEGER,
  suitable_for_baby INTEGER,
  suitable_for_elderly INTEGER,
  suitable_for_pet INTEGER,
  event_details TEXT
);

INSERT INTO user (user_id, day, wechat_id, treatment, user_id_hashid, day_hashid)
VALUES
  (1, 0, 'b83120371', 'T1', 'nBEXdMJkv56ymRZx', 'vQp4l04x0q'),
  (1, 1, 'b83120371', 'T1', 'lq13ZopK7pbrkJ7X', 'BKzwNEGg9y'),
  (1, 2, 'b83120371', 'T1', 'j9Z4Jbol5rwABVxl', 'd7kZonDXxO'),
  (1, 3, 'b83120371', 'T1', 'zdRBqlnO1Mgk7vA5', '0M4kEvea92'),
  (1, 4, 'b83120371', 'T1', 'kaBxo92L02dbXL4K', 'B2J6joM8xb'),
  (1, 5, 'b83120371', 'T1', 'WgkBxb2bv219qRDJ', 'rxn69e6N38'),
  (1, 6, 'b83120371', 'T1', '5gKLM4A7vwr3aBlm', 'K0zAVkYV8W'),
  (1, 7, 'b83120371', 'T1', 'ZdwQaPxbdk8Lne3B', '83AwJbw2RV'),
  (1, 8, 'b83120371', 'T1', 'wMWaznOryK6prqe2', 'Ey3l4RPxZV'),
  (2, 1, 'wzx0501153533', 'T1', 'a3k47g0J60EmWOjD', 'QGngX7ZREN'),
  (3, 1, 'citizen0411', 'T1', 'klzKE7O7vabVm81B', '1ENB753m7V');

INSERT INTO infos (event_id, title, subtitle,
  info_date, info_time, location,
  image_file, air_quality_source, air_quality_source_logo,
  headword, short_description,
  low_temp, high_temp,
  suitable_for_family, suitable_for_friends, suitable_for_lover, suitable_for_baby, suitable_for_elderly, suitable_for_pet,
  event_details)
VALUES
  (1, '相约网红自行车公园', '骑行最美茶海小径',
'2019.05.06 - 2019.05.12', '每天 07:30 am - 19:30 pm', '地点 长宁区 虹桥路地铁站',
'img/event 1.jpg', '', 'img/transparent.png',
'在', '距离上海不远的小城宜兴,
深藏着一个自行车主题公园。
因为一望无际的茶海风光而迅速走红。
这里是江苏第一个自行车主题公园,
大片大片的绿色荡漾在斜坡上,
周末用一整天的时光，
和互助网一起去这里吧。', 18, 25,
1,1,1,0,0,0,
'行程安排：
7:40 开始在指定地点签到集合，自由交流。（记得调好闹钟，不要迟到哦，迟到将错过车和活动）
7:50 准时出发，领队在车上介绍行程，并组织大家自我介绍相互认识，一路欢歌笑语奔赴小城宜兴。
11:20 抵达自行车公园。先取车，然后一起骑行。
12:30 适时午餐，午餐请自带干粮。
16:00 回到指定地点集合，准备返程。
19:30 我们的大巴回到上海市区。大家依依惜别，下次再聚。'),

(2, '漫步上海周边的最美樱花小镇', '探索江南水乡枫泾古镇',
'2019.05.06 - 2019.05.12', '每天 08:30 am - 17:00 pm', '地点 长宁区 虹桥路地铁站',
'img/event 2.jpg', '', 'img/transparent.png',
'为', '什么和互助网一起去旅行？
自助游太操心？做攻略太麻烦？毫无方向感？一个人出行太孤单？
不想参加传统旅行社的跟团？不想去人挤人的大众景点？
还在为周末去哪儿而烦恼？来，和互助网一起出游吧！', 18, 25,
1,1,1,0,0,0,
'行程安排：
8:50 开始在指定地点签到集合，自由交流。（记得调好闹钟，不要迟到哦，迟到将错过车和活动）
9:00 准时出发，领队在车上介绍行程，并组织大家自我介绍相互认识，一路欢歌笑语奔赴平湖。
10:30 抵达樱花小镇。
12:45 逛差不多了吧？在指定地点集合啦，上车去枫泾古镇。
13:20 到达枫泾古镇景区停车场。
“枫泾寻画”是沪上新八景之一。古镇河渠纵横，清冽的河水好像一幅画布，
白墙黑瓦、廊桥街树、楼台亭阁在画布上一一呈现。
15:40 回到景区停车场集合，适时上车返程。
17:00 我们的大巴回到上海市区。大家依依惜别，下次再聚。'),

(3, '公益之家', '资助项目',
'2019.05.11', '每周六 10:00 am - 20:00 pm', '地点 徐汇区 上海体育场',
'img/event 3.png', '', 'img/transparent.png',
'每', '周六参加公益之家成员大会, 一起集思广益如何主动去救助更多的有需要的人群。', 18, 25,
1,1,1,1,1,1,
'如果你有固定的精力来参与公益之家的事务,
例如: 每周参加一次成员大会;
一起集思广益如何主动去救助更多的有需要的人群;
无论贫富，
如果你愿意将自己收入的一部分，
献出来帮助那些存在生存困难的人们，
请加入我们。'),

  (4, '漫步上海老街', '边走边聊',
'2019.05.11', '每周六 14:00 pm - 17:00 pm', '地点 徐汇区 地铁到门店',
'img/event 4.jpg', '（来自：新闻晨报）', 'img/SourceMorningPostLogo.jpg',
'漫', '步上海老街,
走过那些老建筑, 仿佛置身于那时那景那人，
在这个快节奏的生活状态下,
无疑不是一种放松心情，放慢生活的方式。
使自己高速运转的大脑在这一时刻真正轻松下来,
感受着历史的痕迹。', 18, 25,
0,1,1,0,1,0,
'活动形式：
1、14点集合，轮流自我介绍。14：30分准时出发，
迟到的同学，自己骑车追上。或者直接到下一个休息点。
2、出发后，每3，4人，分一组，分享与交流。
3、中间设置几个休息点，有社交小游戏。
4、活动设置两个领队，一前一后，防止走散。'),

  (5, '夜徒法租界', '梧桐树下聊天交友散步',
'2019.05.08', '每周三 19:30 pm - 20:30 pm', '地点 徐汇区 徐家汇',
'img/event 5.jpg', '（来自：新闻广播FM93.4）', 'img/SourceNewsRadioLogo.jpg',
'衡', '山路 走过才知道，
白天的衡山路和晚上判若两人。
不宽的马路，干净的街道，两边风格迥异的建筑，
一切都在日光下简单直接，和酒吧暧昧无关。', 18, 25,
0,1,1,0,0,0,
'行程安排：
19：30地铁徐家汇站14号口集合，
大概半个小时左右开始今晚的徒步：衡山路-淮海路，
大家可以边走边聊，看见有趣的小店可以随便看一下，
到达陕西南路站大家依依惜别。'),

  (6, '游走魔都', '',
'2019.05.12', '每周日 14:00 pm - 16:30 pm', '地点 徐汇区 武康大楼',
'img/event 6.jpg', '', 'img/transparent.png',
'这', '里，是小说刻划的段落；
这里，是电影移过的场景；
这里，有岁月留下的痕迹。
请放慢自己的脚步，跟随自己的心，
用眼睛去重新发现这个有很多故事的上海。', 18, 25,
0,1,1,0,0,0,
'喜欢漫步找寻曾经的华美
喜欢细细品味当下的静谧
一边游走
一边记录
碰到喜欢的小店就走进去点一杯咖啡
庸懒的享受一整个下午的时光
如果你也喜欢
一起结伴同行吧? '),

  (7, '世纪公园踏春', '做游戏-K歌',
'2019.05.11', '每周六 12:00 pm - 19:00 pm', '地点 浦东新区 上海世纪公园',
'img/event 7.jpg', '（来自：上海市环境监测中心）', 'img/SourceSHEnvironmentLogo.jpg',
'平', '时忙着上班，
周末如果有空就出来过一天有趣的生活，
春暖花开，世纪公园里已经色彩缤纷，
让紧张工作一周的烦恼和压力都飞到九霄云外吧！', 18, 25,
0,0,1,0,0,0,
'行程计划：
11:50 世纪公园门口集合
12:00-12：30 自我介绍
12：30-13:30 做游戏
13:30-15:30 公园散步聊天
15：30-19:00附近KTV欢唱
活动结束后想用餐的附近AA,不想用餐的各回各家，下次再见！');
