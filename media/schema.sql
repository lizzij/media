
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS survey;
DROP TABLE IF EXISTS activity;
DROP TABLE IF EXISTS treatments;
DROP TABLE IF EXISTS infos;
DROP TABLE IF EXISTS pages;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  day INTEGER NOT NULL,
  wechat_id TEXT NOT NULL,
  treatment TEXT NOT NULL,
  user_id_hashid TEXT NOT NULL,
  day_hashid TEXT NOT NULL,
  cohort INTEGER NOT NULL
);

INSERT INTO user (user_id, day, wechat_id, treatment, user_id_hashid, day_hashid, cohort)
VALUES
  (1, 99, 'BIBOBBY18dream', 't', 'h', 'h', 1),
  (2, 99, 'Yee_970611', 't', 'h', 'h', 1),
  (3, 99, 'cherry_akashi', 't', 'h', 'h', 1),
  (4, 99, 'imwangdanqing', 't', 'h', 'h', 1),
  (5, 99, 'jiahui--1314', 't', 'h', 'h', 1),
  (6, 99, 'littlebadfox', 't', 'h', 'h', 1),
  (7, 99, 'lqy18810609835', 't', 'h', 'h', 1),
  (8, 99, 'n1015857581', 't', 'h', 'h', 1),
  (9, 99, 'scn960221', 't', 'h', 'h', 1),
  (10, 99, 'wby0209', 't', 'h', 'h', 1),
  (11, 99, 'wby0209', 't', 'h', 'h', 1),
  (12, 99, 'wxid_3y8b2ve5a8pt21', 't', 'h', 'h', 1),
  (13, 99, 'wxy19951129cjy', 't', 'h', 'h', 1),
  (14, 99, 'yznRCS', 't', 'h', 'h', 1),
  (15, 99, 'Crier-L', 't', 'h', 'h', 2),
  (16, 99, 'Ggg_000000001', 't', 'h', 'h', 2),
  (17, 99, 'LotusP731', 't', 'h', 'h', 2),
  (18, 99, 'Rocky19981203', 't', 'h', 'h', 2),
  (19, 99, 'Zziyi_1996', 't', 'h', 'h', 2),
  (20, 99, 'huangxuebinghh', 't', 'h', 'h', 2),
  (21, 99, 'jta18867921184', 't', 'h', 'h', 2),
  (22, 99, 'xujia837', 't', 'h', 'h', 2),
  (23, 99, 'Azure_Era', 't', 'h', 'h', 3),
  (24, 99, 'BillMactavish', 't', 'h', 'h', 3),
  (25, 99, 'DoubleInfinity1998', 't', 'h', 'h', 3),
  (26, 99, 'Gerrygorelxy', 't', 'h', 'h', 3),
  (27, 99, 'H1075646651', 't', 'h', 'h', 3),
  (28, 99, 'LIlu900201', 't', 'h', 'h', 3),
  (29, 99, 'LZR29866760', 't', 'h', 'h', 3),
  (30, 99, 'QJX13363915119', 't', 'h', 'h', 3),
  (31, 99, 'WHEARTS', 't', 'h', 'h', 3),
  (32, 99, 'XADoris', 't', 'h', 'h', 3),
  (33, 99, 'Xingfuma0707', 't', 'h', 'h', 3),
  (34, 99, 'angeladou1328741646', 't', 'h', 'h', 3),
  (35, 99, 'bzg956999644', 't', 'h', 'h', 3),
  (36, 99, 'dcy961201', 't', 'h', 'h', 3),
  (37, 99, 'fan414692262', 't', 'h', 'h', 3),
  (38, 99, 'jizhiruwo123456', 't', 'h', 'h', 3),
  (39, 99, 'jpf691008', 't', 'h', 'h', 3),
  (40, 99, 'maoruofan1219', 't', 'h', 'h', 3),
  (41, 99, 'qiaomu12306', 't', 'h', 'h', 3),
  (42, 99, 'qiaosan_weixin', 't', 'h', 'h', 3),
  (43, 99, 'rrrmt1', 't', 'h', 'h', 3),
  (44, 99, 'sun108861931', 't', 'h', 'h', 3),
  (45, 99, 'ttytll', 't', 'h', 'h', 3),
  (46, 99, 'weijiajie898676919', 't', 'h', 'h', 3),
  (47, 99, 'weiyutu', 't', 'h', 'h', 3),
  (48, 99, 'wh997912782', 't', 'h', 'h', 3),
  (49, 99, 'wolfieemo', 't', 'h', 'h', 3),
  (50, 99, 'wsj5523220', 't', 'h', 'h', 3),
  (51, 99, 'wx13992366388', 't', 'h', 'h', 3),
  (52, 99, 'wxid_0wpd276jr9f622', 't', 'h', 'h', 3),
  (53, 99, 'wxid_20bvofufsh6z22', 't', 'h', 'h', 3),
  (54, 99, 'wxid_7616946168811', 't', 'h', 'h', 3),
  (55, 99, 'wxid_d8x5pl6sbqta22', 't', 'h', 'h', 3),
  (56, 99, 'wxid_eby9vbrixm7i22', 't', 'h', 'h', 3),
  (57, 99, 'wxid_jhg4xpel5gri21', 't', 'h', 'h', 3),
  (58, 99, 'wxid_lbm8xlhe1mr821', 't', 'h', 'h', 3),
  (59, 99, 'wxid_wkmkdy6jxqo22', 't', 'h', 'h', 3),
  (60, 99, 'wzrzyx', 't', 'h', 'h', 3),
  (61, 99, 'xaflyfly', 't', 'h', 'h', 3),
  (62, 99, 'xiongaidashu', 't', 'h', 'h', 3),
  (63, 99, 'youge1028', 't', 'h', 'h', 3),
  (64, 99, 'z18992318877', 't', 'h', 'h', 3),
  (65, 99, 'zhang805405725', 't', 'h', 'h', 3),
  (66, 99, 'zidungxiang', 't', 'h', 'h', 3),
  (67, 99, 'zjm132325', 't', 'h', 'h', 3),
  (68, 99, 'zyh55416', 't', 'h', 'h', 3),
  (41004844, 99, '19921891007', 'T2', 'h', 'h', 4),
  (41106470, 99, 'wxid_fviwiei4j5x412', 'T3', 'h', 'h', 4),
  (41107709, 99, 'aliceluck', 'T1', 'h', 'h', 4),
  (41109482, 99, 'ElaineWinnie', 'T1', 'h', 'h', 4),
  (41111612, 99, 'mengliuxi2010', 'T3', 'h', 'h', 4),
  (41112963, 99, 'C2013072736', 'T1', 'h', 'h', 4),
  (41114824, 99, 'a39843160', 'T4', 'h', 'h', 4),
  (41118820, 99, 'lihui123____', 'T3', 'h', 'h', 4),
  (41120393, 99, 'DawnCHEN12', 'T2', 'h', 'h', 4),
  (41122511, 99, 'wxid_tsmlvx3ua4qp22', 'T2', 'h', 'h', 4),
  (41123384, 99, 'wxid_eilo515dosie21', 'T3', 'h', 'h', 4),
  (41124814, 99, 'ggmmd0', 'T4', 'h', 'h', 4),
  (41126698, 99, 'zxh-19980602', 'T1', 'h', 'h', 4),
  (41127011, 99, 'dhh11191106', 'T2', 'h', 'h', 4),
  (41128991, 99, 'hubiao950918', 'T2', 'h', 'h', 4),
  (41129485, 99, 'leguamer_tt-1', 'T1', 'h', 'h', 4),
  (41131833, 99, 'wxid_51ki7mo42vwy22', 'T1', 'h', 'h', 4),
  (41132130, 99, 'wenjingMa94', 'T3', 'h', 'h', 4),
  (41133755, 99, 'woaiwoziji_guolei', 'T3', 'h', 'h', 4),
  (41134121, 99, 'im-possible-', 'T4', 'h', 'h', 4),
  (41135682, 99, 'EmilyJovovich', 'T4', 'h', 'h', 4),
  (41136889, 99, 'Eason9382', 'T4', 'h', 'h', 4),
  (41137830, 99, 'kakalzo', 'T4', 'h', 'h', 4),
  (41140519, 99, 'lvyifanLVYIFAN', 'T4', 'h', 'h', 4),
  (41141544, 99, 'liangyue3666', 'T4', 'h', 'h', 4),
  (41142751, 99, 'wxid_yd4ek2qwm8i822', 'T2', 'h', 'h', 4),
  (41144132, 99, 'xuyue18725387695', 'T3', 'h', 'h', 4),
  (41145013, 99, 'CSM1551680495', 'T2', 'h', 'h', 4),
  (41147905, 99, 'Heroxmk', 'T4', 'h', 'h', 4),
  (41148503, 99, 'SwanLau_', 'T1', 'h', 'h', 4),
  (41149972, 99, 'zhengtao-x', 'T1', 'h', 'h', 4),
  (41150828, 99, 'YZP0202-', 'T4', 'h', 'h', 4),
  (41151836, 99, 'AnInterestingPanda', 'T2', 'h', 'h', 4),
  (41152784, 99, 'zml19660306', 'T3', 'h', 'h', 4),
  (41153337, 99, 'hare-1', 'T2', 'h', 'h', 4),
  (41154113, 99, 'LI12126972NUO', 'T3', 'h', 'h', 4),
  (41156553, 99, 't11700107', 'T4', 'h', 'h', 4),
  (41157520, 99, 'g182351520', 'T2', 'h', 'h', 4),
  (41158332, 99, 'ayuhello', 'T4', 'h', 'h', 4),
  (41160959, 99, 'zqlxialanjin0216', 'T3', 'h', 'h', 4),
  (41161391, 99, 'jz6229', 'T4', 'h', 'h', 4),
  (41162186, 99, 'iamxiaoluo', 'T1', 'h', 'h', 4),
  (41164841, 99, 'YiDanna_Zhang', 'T1', 'h', 'h', 4),
  (41165989, 99, 'Stan-Brabbit', 'T3', 'h', 'h', 4),
  (41166681, 99, 'wulacc', 'T4', 'h', 'h', 4),
  (41167049, 99, 'Zyy892898685', 'T4', 'h', 'h', 4),
  (41168365, 99, 'zhaoxia4817', 'T1', 'h', 'h', 4),
  (41170067, 99, 'wxkwxhna', 'T1', 'h', 'h', 4),
  (41171018, 99, 'dyq2104347152', 'T3', 'h', 'h', 4),
  (41182505, 99, '广东 湛江', 'T4', 'h', 'h', 4),
  (41183949, 99, 'jing_1996', 'T4', 'h', 'h', 4),
  (41184099, 99, 'refine6521', 'T3', 'h', 'h', 4),
  (41185115, 99, 'Sillyfox_1997', 'T1', 'h', 'h', 4),
  (41186381, 99, 'charlie_yu_0803', 'T2', 'h', 'h', 4),
  (41187861, 99, 'SockyChan888', 'T1', 'h', 'h', 4),
  (41188319, 99, 'shuyejuelao', 'T2', 'h', 'h', 4),
  (41197693, 99, 'wo912190723', 'T2', 'h', 'h', 4),
  (41198689, 99, 'sj714823587', 'T1', 'h', 'h', 4),
  (41199704, 99, 'SCYang-', 'T2', 'h', 'h', 4),
  (41200198, 99, 'mikeconely', 'T2', 'h', 'h', 4),
  (41201591, 99, 'YOUNG--YOUNG21', 'T4', 'h', 'h', 4),
  (41202110, 99, 'ls954606775', 'T3', 'h', 'h', 4),
  (41203344, 99, 'zhaocr2000', 'T3', 'h', 'h', 4),
  (41204336, 99, 'zyd0717', 'T1', 'h', 'h', 4),
  (41205241, 99, 'mariehmj', 'T2', 'h', 'h', 4),
  (41206028, 99, 'cyj252431395', 'T1', 'h', 'h', 4),
  (41207865, 99, 'lzyxiaojizhi', 'T2', 'h', 'h', 4),
  (41208426, 99, 's1071687079', 'T3', 'h', 'h', 4),
  (41209814, 99, 'Smile_oxx', 'T4', 'h', 'h', 4),
  (41210133, 99, 'yxl_20001031', 'T1', 'h', 'h', 4),
  (42005812, 99, 'kangld_sh', 'T4', 'h', 'h', 4),
  (42006820, 99, 'Amy_xuchengze', 'T2', 'h', 'h', 4),
  (42007038, 99, 'szxxingfugangwan', 'T1', 'h', 'h', 4),
  (42008987, 99, 'lzh18321997059', 'T2', 'h', 'h', 4),
  (42009472, 99, 'zhaoyang1999330', 'T1', 'h', 'h', 4),
  (42010959, 99, 'x96feng', 'T4', 'h', 'h', 4),
  (42011302, 99, 'my13192335963', 'T3', 'h', 'h', 4),
  (42012447, 99, 'wxid_prb73l568ld122', 'T3', 'h', 'h', 4),
  (42013283, 99, 'Akunomee', 'T2', 'h', 'h', 4),
  (42014723, 99, 'XSZX95', 'T2', 'h', 'h', 4),
  (42015207, 99, 'MRrvvw', 'T4', 'h', 'h', 4),
  (42016820, 99, 'zxd20000311', 'T4', 'h', 'h', 4),
  (42017535, 99, 'jxsue19970125', 'T3', 'h', 'h', 4),
  (42018553, 99, 'wxid_1tq4ds5v5jzd22', 'T2', 'h', 'h', 4),
  (42019796, 99, 'champagne96', 'T4', 'h', 'h', 4),
  (42020062, 99, 'shiny-3H', 'T4', 'h', 'h', 4),
  (42021240, 99, 'cvi0520', 'T4', 'h', 'h', 4),
  (42022183, 99, 'wz442641436', 'T4', 'h', 'h', 4),
  (42023104, 99, 'blackraker', 'T3', 'h', 'h', 4),
  (42024127, 99, 'wymuahhh', 'T4', 'h', 'h', 4),
  (42025633, 99, 'Selina-ZYYY', 'T3', 'h', 'h', 4),
  (42026798, 99, 'a1006854403', 'T1', 'h', 'h', 4),
  (42027285, 99, 'gwx15951657199', 'T1', 'h', 'h', 4),
  (42028270, 99, 'ycfszd1', 'T3', 'h', 'h', 4),
  (42028575, 99, 'ycfszd1', 'T3', 'h', 'h', 4),
  (42028872, 99, 'ycfszd1', 'T3', 'h', 'h', 4),
  (42029125, 99, 'yumitou1997', 'T3', 'h', 'h', 4),
  (42030230, 99, 'LuckyLZJ_0528', 'T1', 'h', 'h', 4),
  (42031316, 99, 'ss47550', 'T2', 'h', 'h', 4),
  (42032278, 99, 'Dxy1259413425', 'T1', 'h', 'h', 4),
  (42033517, 99, 'bh15293496061', 'T2', 'h', 'h', 4),
  (42035766, 99, 'wxid_r9f7vmbxc0nv22', 'T2', 'h', 'h', 4),
  (42037069, 99, 'zxcvbzxcvb987789', 'T1', 'h', 'h', 4),
  (42038049, 99, 'sher1991xyx', 'T1', 'h', 'h', 4),
  (42039688, 99, 'inovin', 'T3', 'h', 'h', 4),
  (42042439, 99, '_Fiona_Lulu', 'T1', 'h', 'h', 4),
  (42044805, 99, 'Ymmzzc_2', 'T4', 'h', 'h', 4),
  (42048854, 99, 'dkt33319990126', 'T1', 'h', 'h', 4),
  (42049043, 99, 'sound-feel-forever', 'T3', 'h', 'h', 4),
  (42051342, 99, 'goldenbold', 'T3', 'h', 'h', 4),
  (42052869, 99, 'zhuzhu985716', 'T4', 'h', 'h', 4),
  (42054225, 99, 'SERENA12-24', 'T3', 'h', 'h', 4),
  (42056294, 99, 'ShawnWang0930', 'T1', 'h', 'h', 4),
  (42057670, 99, 'L5474474', 'T3', 'h', 'h', 4),
  (42059067, 99, 'usefully', 'T4', 'h', 'h', 4),
  (42061928, 99, 'zll99927', 'T1', 'h', 'h', 4),
  (42063392, 99, 'mengmengwmj', 'T4', 'h', 'h', 4),
  (42065820, 99, 'awa89172', 'T1', 'h', 'h', 4),
  (42066138, 99, 'kerr_Greenleaf', 'T2', 'h', 'h', 4),
  (42068530, 99, 'tpy0611', 'T1', 'h', 'h', 4),
  (42070670, 99, 'ly52837', 'T4', 'h', 'h', 4),
  (42071196, 99, 'sufegaochen', 'T2', 'h', 'h', 4),
  (42073125, 99, 'ljjjj0606', 'T3', 'h', 'h', 4),
  (42075600, 99, 'winchesterjl', 'T4', 'h', 'h', 4),
  (42076790, 99, 'zqq1122334', 'T1', 'h', 'h', 4),
  (42077437, 99, 'Chris11784', 'T4', 'h', 'h', 4),
  (42078926, 99, 'He-Zihan1111', 'T1', 'h', 'h', 4),
  (42079130, 99, 'L741378264', 'T3', 'h', 'h', 4),
  (42080918, 99, 'fuer8995', 'T1', 'h', 'h', 4),
  (42082129, 99, 'wxid_p35bt2ti68ox22', 'T3', 'h', 'h', 4),
  (42083002, 99, 'WanJun25yt-L3r', 'T3', 'h', 'h', 4),
  (42085387, 99, 'Zhuyicheng_junior', 'T2', 'h', 'h', 4),
  (42086202, 99, 'Alicia1220-', 'T3', 'h', 'h', 4),
  (42087083, 99, 'jiangjun0729', 'T4', 'h', 'h', 4),
  (42088824, 99, 'zll211211zll', 'T4', 'h', 'h', 4),
  (42090341, 99, 'ww976873595', 'T4', 'h', 'h', 4),
  (42091347, 99, 'yumi_lalala', 'T4', 'h', 'h', 4),
  (42093021, 99, 'sk0012300', 'T3', 'h', 'h', 4),
  (42095656, 99, 'Originalism', 'T2', 'h', 'h', 4),
  (43034350, 99, 'yyr19990820', 'T2', 'h', 'h', 4),
  (43036952, 99, '丛沐青', 'T1', 'h', 'h', 4),
  (43040218, 99, '人来', 'T2', 'h', 'h', 4),
  (43041448, 99, 'dermund', 'T2', 'h', 'h', 4),
  (43043364, 99, 'rachel5198', 'T4', 'h', 'h', 4),
  (43045726, 99, 'lijunjie1185546870', 'T3', 'h', 'h', 4),
  (43046237, 99, 'Ywz2827911078', 'T4', 'h', 'h', 4),
  (43047978, 99, 'jhgkui', 'T1', 'h', 'h', 4),
  (43050683, 99, 'VictoriaYOUNG7', 'T1', 'h', 'h', 4),
  (43053262, 99, 'wxid_ae5jv33vwv8e22', 'T2', 'h', 'h', 4),
  (43055541, 99, 'Laiyigeng', 'T3', 'h', 'h', 4),
  (43058309, 99, 'h15124390604', 'T2', 'h', 'h', 4),
  (43060195, 99, 'haaasan687', 'T3', 'h', 'h', 4),
  (43062517, 99, 'yzsxj0913', 'T2', 'h', 'h', 4),
  (43064601, 99, 'Qhanasaki', 'T4', 'h', 'h', 4),
  (43067308, 99, 'yj13867569772', 'T2', 'h', 'h', 4),
  (43069923, 99, 'dyh15932059850', 'T2', 'h', 'h', 4),
  (43072382, 99, 'LYdia20160402', 'T3', 'h', 'h', 4),
  (43074357, 99, 'xirouloveyou', 'T3', 'h', 'h', 4),
  (43081351, 99, 'OnlyPrinceboy', 'T3', 'h', 'h', 4),
  (43084068, 99, 'wyc729553304', 'T2', 'h', 'h', 4),
  (43092020, 99, 'wulimengjun', 'T1', 'h', 'h', 4),
  (43094710, 99, 'xx03-27xx', 'T4', 'h', 'h', 4),
  (43096266, 99, 'wwj18483506823', 'T2', 'h', 'h', 4),
  (43097458, 99, 'HT_WYN', 'T1', 'h', 'h', 4),
  (43098981, 99, 'fx_991022', 'T2', 'h', 'h', 4),
  (43099807, 99, 'wxid_0q1c25bbhc6g22', 'T3', 'h', 'h', 4),
  (43100547, 99, '作用于2222266', 'T2', 'h', 'h', 4),
  (43101282, 99, 'zyy22222266', 'T2', 'h', 'h', 4),
  (43102497, 99, 'Avelve', 'T3', 'h', 'h', 4),
  (43103931, 99, 'zxy_99-05-06', 'T1', 'h', 'h', 4),
  (43104616, 99, 'oneinlove6688', 'T4', 'h', 'h', 4),
  (43105138, 99, 'wxid_qge8wx6zt0zt22', 'T4', 'h', 'h', 4),
  (43108109, 99, 'wzj-1215225', 'T3', 'h', 'h', 4),
  (43110412, 99, 'qianchaoyouyai', 'T1', 'h', 'h', 4),
  (43113645, 99, 'myp7448224476', 'T2', 'h', 'h', 4),
  (43115262, 99, 'wxid_py4olb80nb7s22', 'T3', 'h', 'h', 4),
  (43116149, 99, 'q894682441', 'T2', 'h', 'h', 4),
  (43117183, 99, 'fristljun', 'T1', 'h', 'h', 4),
  (43119950, 99, 'chiyoy_uann', 'T1', 'h', 'h', 4),
  (43121227, 99, 'ClaudioBravo1983', 'T2', 'h', 'h', 4),
  (43125617, 99, 'w1449550206', 'T1', 'h', 'h', 4),
  (43130967, 99, 'zzz32625hahaha', 'T4', 'h', 'h', 4),
  (43139981, 99, 'smx261663209', 'T3', 'h', 'h', 4),
  (43143357, 99, 'rs12345789o', 'T4', 'h', 'h', 4),
  (43146169, 99, 'Liuying6_6', 'T2', 'h', 'h', 4),
  (43155618, 99, 'Aura97', 'T4', 'h', 'h', 4),
  (43159448, 99, 'Gabriel_lib', 'T4', 'h', 'h', 4),
  (43163115, 99, 'wxid_38rh1n0m38rc22', 'T2', 'h', 'h', 4),
  (43169259, 99, 'liyubo1234567', 'T2', 'h', 'h', 4),
  (43172987, 99, 'cyy-vision1547474489', 'T4', 'h', 'h', 4),
  (43173763, 99, 'xiaoxiaoxiao3345', 'T2', 'h', 'h', 4),
  (43174014, 99, 'YYxiaaobudou', 'T3', 'h', 'h', 4),
  (43175967, 99, 'YYxiaobudou', 'T4', 'h', 'h', 4),
  (43176148, 99, 'chb992669370', 'T1', 'h', 'h', 4),
  (43177012, 99, 'C13894374945', 'T4', 'h', 'h', 4),
  (43178664, 99, 'xxrzuishuai1129', 'T1', 'h', 'h', 4),
  (43179006, 99, 'xihuanni0913_', 'T1', 'h', 'h', 4),
  (43180759, 99, 'wxid_0kjix5nqymc821', 'T3', 'h', 'h', 4),
  (43181898, 99, 'wxid_7s1a17mqh60a22', 'T3', 'h', 'h', 4),
  (43189681, 99, 'genesis_xyh', 'T2', 'h', 'h', 4),
  (43190600, 99, 'kun-ikun-zt', 'T1', 'h', 'h', 4),
  (43191982, 99, 'wxid_rd6cfkemnc4h22', 'T3', 'h', 'h', 4),
  (43192594, 99, 'M15061339321M', 'T3', 'h', 'h', 4),
  (43193312, 99, 'likexin1028', 'T3', 'h', 'h', 4),
  (43194873, 99, 'g-15008625546', 'T3', 'h', 'h', 4),
  (43195228, 99, 'xcx209717', 'T2', 'h', 'h', 4),
  (43196167, 99, 'Haaasan687', 'T2', 'h', 'h', 4);

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
  user_id INTEGER UNIQUE NOT NULL,
  day INTEGER NOT NULL,
  survey_page INTEGER,
  curr_time TIMESTAMP,
  day_complete BOOLEAN NOT NULL,
  day_started TIMESTAMP,
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
  short_description TEXT,
  low_temp INTEGER,
  high_temp INTEGER,
  suitable_for_family INTEGER,
  suitable_for_friends INTEGER,
  suitable_for_lover INTEGER,
  suitable_for_baby INTEGER,
  suitable_for_elderly INTEGER,
  suitable_for_pet INTEGER,
  event_details TEXT,
  phrase_for_week TEXT,
  phrase_for_day TEXT,
  phrase_for_header TEXT,
  cohort INTEGER NOT NULL
);

INSERT INTO infos (event_id, title, subtitle,
  info_date, info_time, location,
  image_file, air_quality_source, air_quality_source_logo,
  short_description,
  low_temp, high_temp,
  suitable_for_family, suitable_for_friends, suitable_for_lover, suitable_for_baby, suitable_for_elderly, suitable_for_pet,
  event_details,
  phrase_for_week, phrase_for_day, phrase_for_header,
  cohort)
VALUES
  (1, '相约网红自行车公园', '骑行最美茶海小径',
'2019.05.13 - 05.18', '每天 07:30 am - 19:30 pm', '地点 长宁区 虹桥路地铁站',
'img/event 1.jpg', '', 'img/transparent.png',
'乘坐巴士，到距离上海不远的小城宜兴, 深藏着一个自行车主题公园。 这里是江苏第一个自行车主题公园。', 23, 31,
0,1,1,0,0,0,
'行程安排：
7:40 开始在指定地点签到集合，自由交流。（记得调好闹钟，不要迟到哦，迟到将错过车和活动）
7:50 准时出发，领队在车上介绍行程，并组织大家自我介绍相互认识，一路欢歌笑语奔赴小城宜兴。
11:20 抵达自行车公园。先取车，然后一起骑行。
12:30 适时午餐，午餐请自带干粮。
16:00 回到指定地点集合，准备返程。
19:30 我们的大巴回到上海市区。大家依依惜别，下次再聚。',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
1),

  (2, '漫步上海周边的最美樱花小镇', '探索江南水乡枫泾古镇',
'2019.05.13 - 2019.05.18', '每天 08:30 am - 17:00 pm', '地点 长宁区 虹桥路地铁站',
'img/event 2.jpg', '', 'img/transparent.png',
'漫步平湖樱花小镇，探索江南水乡枫泾古镇（1天活动）。 藏着一个花团锦簇的浪漫樱花小镇。', 23, 31,
1,1,1,0,1,1,
'行程安排：
8:50 开始在指定地点签到集合，自由交流。（记得调好闹钟，不要迟到哦，迟到将错过车和活动）
9:00 准时出发，领队在车上介绍行程，并组织大家自我介绍相互认识，一路欢歌笑语奔赴平湖。
10:30 抵达樱花小镇。
12:45 逛差不多了吧？在指定地点集合啦，上车去枫泾古镇。
13:20 到达枫泾古镇景区停车场。
“枫泾寻画”是沪上新八景之一。古镇河渠纵横，清冽的河水好像一幅画布，
白墙黑瓦、廊桥街树、楼台亭阁在画布上一一呈现。
15:40 回到景区停车场集合，适时上车返程。
17:00 我们的大巴回到上海市区。大家依依惜别，下次再聚。',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
1),

(3, '公益之家', '资助项目',
'2019.05.18 周六', '10:00 am - 20:00 pm', '地点 徐汇区 上海体育场',
'img/event 3.png', '', 'img/transparent.png',
'参加公益之家成员大会,一起集思广益如何主动去救助更多的有需要的人群。', 23, 31,
0,1,1,0,1,0,
'如果你有固定的精力来参与公益之家的事务,
例如: 每周参加一次成员大会;
一起集思广益如何主动去救助更多的有需要的人群;
无论贫富，如果你愿意将自己收入的一部分，
献出来帮助那些存在生存困难的人们，
请加入我们。',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
1),

  (4, '漫步上海老街', '边走边聊',
'2019.05.18 周六', '14:00 pm - 17:00 pm', '地点 徐汇区 地铁到门店',
'img/event 4.jpg', '', 'img/transparent.png',
'漫步上海老街, 走过那些老建筑, 仿佛置身于那时那景那人。', 23, 31,
0,1,1,0,1,1,
'活动形式：
1、14点集合，轮流自我介绍。14：30分准时出发，
迟到的同学，自己骑车追上。或者直接到下一个休息点。
2、出发后，每3，4人，分一组，分享与交流。
3、中间设置几个休息点，有社交小游戏。
4、活动设置两个领队，一前一后，防止走散。',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
1),

  (5, '夜徒法租界', '梧桐树下聊天交友散步',
'2019.05.15 周三', '19:30 pm - 20:30 pm', '地点 徐汇区 徐家汇',
'img/event 5.jpg', '（来自：新闻广播FM93.4）', 'img/SourceNewsRadioLogo.jpg',
'徒步路线：徐家汇——衡山路——淮海路 。扩大自己的视野，认识一些有趣的人。', 23, 31,
0,1,1,0,0,0,
'行程安排：
19:30地铁徐家汇站14号口集合，
大概半个小时左右开始今晚的徒步：衡山路-淮海路，
大家可以边走边聊，看见有趣的小店可以随便看一下，
到达陕西南路站大家依依惜别。',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
1),

  (6, '游走魔都', '',
'2019.05.19 周日', '14:00 pm - 16:30 pm', '地点 徐汇区 武康大楼',
'img/event 6.jpg', '', 'img/transparent.png',
'请放慢自己的脚步，跟随自己的心，用眼睛去重新发现这个有很多故事的上海。', 23, 31,
0,1,1,0,1,0,
'喜欢漫步找寻曾经的华美
喜欢细细品味当下的静谧
一边游走
一边记录
碰到喜欢的小店就走进去点一杯咖啡
庸懒的享受一整个下午的时光
如果你也喜欢
一起结伴同行吧? ',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
1),

  (7, '世纪公园踏春', '做游戏-K歌',
'2019.05.18 周六', '12:00 pm - 19:00 pm', '地点 浦东新区 上海世纪公园',
'img/event 7.jpg', '', 'img/transparent.png',
'世纪公园里已经色彩缤纷，到处散发着安静祥和的气息。', 23, 31,
0,0,1,0,0,0,
'行程计划：
11:50 世纪公园门口集合
12:00-12:30 自我介绍
12:30-13:30 做游戏
13:30-15:30 公园散步聊天
15:30-19:00附近KTV欢唱
活动结束后想用餐的附近AA,不想用餐的各回各家，下次再见！',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
1),

(8, '儿童慈善徒步运动', '',
'2019.05.18 周六', '12:00 pm - 19:00 pm', '任何户外地点',
'img/walkathon.png', '（来自：上海市环境监测中心）', 'img/SourceSHEnvironmentLogo.jpg',
'步行4000-7000步。 我们将代表您向上海联合基金会捐款！独自行走或与您的朋友和家人一起散步，并使用微信步数记录您步数！', 23, 31,
1,1,1,0,0,1,
'我们将捐钱给上海联劝公益基金会，它的使命是：授权捐助者支持中国的基层非政府组织目前，大多数基层非政府组织缺乏有效的专业筹款方法，大多数中国官方基金会提供的补助机会非常有限。 由此产生的资金缺口迫使他们将不成比例的时间集中在维持其组织的运作上。 因此，他们通常既没有精力也没有资金进行大规模筹款活动，或者专注于改善其计划的影响。 上海联劝公益基金会（SUF）专注于为基层非政府组织筹集资金，以减轻限制有前途组织增长和影响的大部分财政负担。',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
1),

(1, 'cohort2', '骑行最美茶海小径',
'2019.05.13 - 05.18', '每天 07:30 am - 19:30 pm', '地点 长宁区 虹桥路地铁站',
'img/event 1.jpg', '', 'img/transparent.png',
'乘坐巴士，到距离上海不远的小城宜兴, 深藏着一个自行车主题公园。 这里是江苏第一个自行车主题公园。', 23, 31,
0,1,1,0,0,0,
'行程安排：
7:40 开始在指定地点签到集合，自由交流。（记得调好闹钟，不要迟到哦，迟到将错过车和活动）
7:50 准时出发，领队在车上介绍行程，并组织大家自我介绍相互认识，一路欢歌笑语奔赴小城宜兴。
11:20 抵达自行车公园。先取车，然后一起骑行。
12:30 适时午餐，午餐请自带干粮。
16:00 回到指定地点集合，准备返程。
19:30 我们的大巴回到上海市区。大家依依惜别，下次再聚。',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
2),

(2, 'cohort2', '探索江南水乡枫泾古镇',
'2019.05.13 - 2019.05.18', '每天 08:30 am - 17:00 pm', '地点 长宁区 虹桥路地铁站',
'img/event 2.jpg', '', 'img/transparent.png',
'漫步平湖樱花小镇，探索江南水乡枫泾古镇（1天活动）。 藏着一个花团锦簇的浪漫樱花小镇。', 23, 31,
1,1,1,0,1,1,
'行程安排：
8:50 开始在指定地点签到集合，自由交流。（记得调好闹钟，不要迟到哦，迟到将错过车和活动）
9:00 准时出发，领队在车上介绍行程，并组织大家自我介绍相互认识，一路欢歌笑语奔赴平湖。
10:30 抵达樱花小镇。
12:45 逛差不多了吧？在指定地点集合啦，上车去枫泾古镇。
13:20 到达枫泾古镇景区停车场。
“枫泾寻画”是沪上新八景之一。古镇河渠纵横，清冽的河水好像一幅画布，
白墙黑瓦、廊桥街树、楼台亭阁在画布上一一呈现。
15:40 回到景区停车场集合，适时上车返程。
17:00 我们的大巴回到上海市区。大家依依惜别，下次再聚。',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
2),

(3, 'cohort2', '资助项目',
'2019.05.18 周六', '10:00 am - 20:00 pm', '地点 徐汇区 上海体育场',
'img/event 3.png', '', 'img/transparent.png',
'参加公益之家成员大会,一起集思广益如何主动去救助更多的有需要的人群。', 23, 31,
0,1,1,0,1,0,
'如果你有固定的精力来参与公益之家的事务,
例如: 每周参加一次成员大会;
一起集思广益如何主动去救助更多的有需要的人群;
无论贫富，如果你愿意将自己收入的一部分，
献出来帮助那些存在生存困难的人们，
请加入我们。',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
2),

(4, 'cohort2', '边走边聊',
'2019.05.18 周六', '14:00 pm - 17:00 pm', '地点 徐汇区 地铁到门店',
'img/event 4.jpg', '', 'img/transparent.png',
'漫步上海老街, 走过那些老建筑, 仿佛置身于那时那景那人。', 23, 31,
0,1,1,0,1,1,
'活动形式：
1、14点集合，轮流自我介绍。14：30分准时出发，
迟到的同学，自己骑车追上。或者直接到下一个休息点。
2、出发后，每3，4人，分一组，分享与交流。
3、中间设置几个休息点，有社交小游戏。
4、活动设置两个领队，一前一后，防止走散。',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
2),

(5, 'cohort2', '梧桐树下聊天交友散步',
'2019.05.15 周三', '19:30 pm - 20:30 pm', '地点 徐汇区 徐家汇',
'img/event 5.jpg', '（来自：新闻广播FM93.4）', 'img/SourceNewsRadioLogo.jpg',
'徒步路线：徐家汇——衡山路——淮海路 。扩大自己的视野，认识一些有趣的人。', 23, 31,
0,1,1,0,0,0,
'行程安排：
19:30地铁徐家汇站14号口集合，
大概半个小时左右开始今晚的徒步：衡山路-淮海路，
大家可以边走边聊，看见有趣的小店可以随便看一下，
到达陕西南路站大家依依惜别。',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
2),

(6, 'cohort2', '',
'2019.05.19 周日', '14:00 pm - 16:30 pm', '地点 徐汇区 武康大楼',
'img/event 6.jpg', '', 'img/transparent.png',
'请放慢自己的脚步，跟随自己的心，用眼睛去重新发现这个有很多故事的上海。', 23, 31,
0,1,1,0,1,0,
'喜欢漫步找寻曾经的华美
喜欢细细品味当下的静谧
一边游走
一边记录
碰到喜欢的小店就走进去点一杯咖啡
庸懒的享受一整个下午的时光
如果你也喜欢
一起结伴同行吧? ',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
2),

(7, 'cohort2', '做游戏-K歌',
'2019.05.18 周六', '12:00 pm - 19:00 pm', '地点 浦东新区 上海世纪公园',
'img/event 7.jpg', '', 'img/transparent.png',
'世纪公园里已经色彩缤纷，到处散发着安静祥和的气息。', 23, 31,
0,0,1,0,0,0,
'行程计划：
11:50 世纪公园门口集合
12:00-12:30 自我介绍
12:30-13:30 做游戏
13:30-15:30 公园散步聊天
15:30-19:00附近KTV欢唱
活动结束后想用餐的附近AA,不想用餐的各回各家，下次再见！',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
2),

(8, 'cohort2', '',
'2019.05.18 周六', '12:00 pm - 19:00 pm', '任何户外地点',
'img/walkathon.png', '（来自：上海市环境监测中心）', 'img/SourceSHEnvironmentLogo.jpg',
'如果您步行5000步，我们将以您的名义向上海联合基金会捐赠10元人民币。在此基础上每多走1000步，捐赠数额将增加10元，上限为30元。', 23, 31,
1,1,1,0,0,1,
'我们将捐钱给上海联劝公益基金会，它的使命是：授权捐助者支持中国的基层非政府组织目前，大多数基层非政府组织缺乏有效的专业筹款方法，大多数中国官方基金会提供的补助机会非常有限。 由此产生的资金缺口迫使他们将不成比例的时间集中在维持其组织的运作上。 因此，他们通常既没有精力也没有资金进行大规模筹款活动，或者专注于改善其计划的影响。 上海联劝公益基金会（SUF）专注于为基层非政府组织筹集资金，以减轻限制有前途组织增长和影响的大部分财政负担。',
'2019年5月13-19日', '2019年5月18日', '五月13至19日',
2),

(10, '儿童慈善徒步运动', '',
'2019.08.24 周六', '00:00 am - 11:59 pm', '任何户外地点',
'img/walkathon.png', '', 'img/transparent.png',
'如果您步行1000步，我们将以您的名义向中国儿童少年基金会捐赠2元人民币。在此基础上每多走1000步，捐赠数额将增加2元，上限为30元。', 22, 32,
1,1,1,0,0,1,
'中国儿童少年基金会，成立于1981年7月28日，是新中国成立后的第一家国家级公募基金会，隶属于全国妇联，在中国基金会序列中，被民政部评定为最高等级——5A级。',
'2019年8月19-25日', '2019年8月24日', '八月19至25日',
3),

(11, '凤县', '秦蜀咽喉 汉北锁钥',
'2019.08.24 周六', '10:00 am - 18:00 pm', '地点 宝鸡市凤县',
'img/xian1.jpg', '', 'img/transparent.png',
'县古称“凤州，是宝鸡的著名旅游圣地。无论你是向往人文还是自然，这里都能满足你！', 22, 32,
1,1,1,0,0,1,
'long description',
'2019年8月19-25日', '2019年8月24日', '八月19至25日',
3),

(12, '乾坤湾', '爱情岛',
'2019.08.24 周六', '10:00 am - 18:00 pm', '地点 大荔县乾坤湾',
'img/xian2.jpg', '', 'img/transparent.png',
'坤湾依托黄河支流，形成了自然又神秘的河道图案，与其同样拥有神秘色彩的爱情岛与乾坤湾隔湖相望。', 22, 32,
1,1,1,0,0,1,
'long description',
'2019年8月19-25日', '2019年8月24日', '八月19至25日',
3),

(13, '儿童慈善徒步运动', '',
'2019.10.12 周六', '00:00 am - 11:59 pm', '任何户外地点',
'img/walkathon.png', '', 'img/transparent.png',
'如果您步行1000步，我们将以您的名义向上海联合基金会捐赠2元人民币。在此基础上每多走1000步，捐赠数额将增加2元，上限为30元。', 17, 23,
1,1,1,0,0,1,
'中国儿童少年基金会，成立于1981年7月28日，是新中国成立后的第一家国家级公募基金会，隶属于全国妇联，在中国基金会序列中，被民政部评定为最高等级——5A级。',
'2019年10月07-13日', '2019年10月12日', '十月07至13日',
4),

(14, 'City Walk', '逛吃上海最浪漫的文艺道路',
'2019.10.12 周六 - 2019.10.13 周日', '14:00 pm - 18:00 pm', '地点 虹口区 海伦路地铁口',
'img/shanghai2.jpg', '', 'img/transparent.png',
'既有鲁迅公园、1933、多伦路文化名人街的文化底蕴，又有甜爱路、网红餐厅、山阴路的浪漫风情。报名公众号：A伙伴', 17, 23,
1,1,1,0,0,1,
'long description',
'2019年10月07-13日', '2019年10月12日', '十月07至13日',
4),

(15, '滨江', '骑行',
'2019.10.13 周日', '18:30 pm - 21:00 pm', '地点 黄浦区中山东一路',
'img/shanghai5.jpg', '', 'img/transparent.png',
'一辆单车，一个背包即可出行，简单又环保;和谁一起骑行也很重要， 我们是一群爱生活的小伙伴,也欢迎你加入。参加活动：联系人xiao xiao，微信luoleilai2。', 17, 23,
1,1,1,0,0,1,
'long description',
'2019年10月07-13日', '2019年10月12日', '十月07至13日',
4),

(16, '边走边聊认识新朋友', '之黄浦滨江线8公里',
'2019.10.12 周六 - 2019.10.13 周日', '18:30 pm - 21:30 pm', '地点 黄浦区 耀华路地铁站',
'img/shanghai3.jpg', '', 'img/transparent.png',
'这是一条很长的滨江线，可以吹着江风，看着夜上海的灯火辉煌，一边和不同行业的小伙伴边走边聊。参加活动：18:30耀华路地铁站集合。', 17, 23,
1,1,1,0,0,1,
'long description',
'2019年10月07-13日', '2019年10月12日', '十月07至13日',
4),

(17, '夜徒法租界', '梧桐树下聊天交友散步',
'2019.10.09 周三', '19:30 pm - 21:00 pm', '地点 徐汇区 徐家汇',
'img/shanghai4.jpg', '', 'img/transparent.png',
'白天忙着上班，晚上如果有空就出来走走吧，同时一起聊聊天，扩大自己的视野，认识一些有趣的人。徒步路线：徐家汇——衡山路——淮海路。参加活动：19:30地铁徐家汇站14号口集合。', 17, 23,
1,1,1,0,0,1,
'long description',
'2019年10月07-13日', '2019年10月12日', '十月07至13日',
4),

(18, '古镇探索 ', '探秘上海千年古镇--朱家角',
'2019.10.12 周六', '14:00 pm - 17:00 pm', '地点 青浦区 朱家角古镇',
'img/shanghai1.jpg', '', 'img/transparent.png',
'朱家角，坐落在上海青浦区境内。宋元时期形成集镇，名朱家村，明朝称为珠里、珠溪，清称为珠蔚，民国时米市最为鼎盛。参加活动：加主办方微信daoxiang866，进群了解更多活动信息。', 17, 23,
1,1,1,0,0,1,
'long description',
'2019年10月07-13日', '2019年10月12日', '十月07至13日',
4),

(19, '夜徒外滩', '黄埔江畔聊天交友散步',
'2019.10.12 周六', '19:00 pm - 21:00 pm', '地点 虹口区 天潼路地铁站',
'img/shanghai6.jpg', '', 'img/transparent.png',
'徒步路线：天潼路站- 河南北路-北 苏州路-乍浦路桥-南苏州路- 中山东一路- 中山东二路-中山南路。路程大约2-3小时，建议穿舒适运动鞋或平底鞋。参加活动：报名添加微信quranclub，并注明“外滩”。每周六19:00天潼路地铁站集合。', 17, 23,
1,1,1,0,0,1,
'long description',
'2019年10月07-13日', '2019年10月12日', '十月07至13日',
4),

(20, '儿童慈善徒步运动', '',
'2019.11.16 周六', '00:00 am - 11:59 pm', '任何户外地点',
'img/walkathon.png', '', 'img/transparent.png',
'如果您步行1000步，我们将以您的名义向上海联合基金会捐赠2元人民币。在此基础上每多走1000步，捐赠数额将增加2元，上限为30元。', 17, 23,
1,1,1,0,0,1,
'中国儿童少年基金会，成立于1981年7月28日，是新中国成立后的第一家国家级公募基金会，隶属于全国妇联，在中国基金会序列中，被民政部评定为最高等级——5A级。',
'2019年11月11-17日', '2019年11月16日', '十一月11至17日',
5),

(21, '遇见浪漫旋转木马，', '感受黄浦江的风',
'2019.11.16 周六', '19:00 pm - 21:00 pm', '地点 龙华中路地铁站6号口',
'img/shv2_event1.jpg', '', 'img/transparent.png',
'徒步路线长约4公里，耗时大约2个小时。添加微信号：redhot121 备注：豆瓣夜徒', 17, 23,
1,1,1,0,0,1,
'long description',
'2019年11月11-17日', '2019年11月16日', '十一月11至17日',
5),

(22, '每周日陆家嘴江边', '一起来锻炼',
'2019.11.17 周日', '08:00 am - 22:30 pm', '地点 浦东新区 杨家渡渡口',
'img/shv2_event2.jpg', '', 'img/transparent.png',
'我们会带上专业的健身教练为大家提供健身指导，免费带大家锻炼。添加微信号：chenxiao_6598  备注: 豆瓣 江边锻炼 ', 17, 23,
1,1,1,0,0,1,
'long description',
'2019年11月11-17日', '2019年11月16日', '十一月11至17日',
5),

(23, '夜跑', '',
'2019.11.11 周三 - 2019.11.17 周日', '07:30 am - 21:00 pm', '地点 闵行区 上海康城',
'img/shv2_event3.jpg', '', 'img/transparent.png',
'让我们一起夜跑进入百公里、千公里俱乐部吧！添加微信号：pei1711944147 备注：夜跑', 17, 23,
1,1,1,0,0,1,
'long description',
'2019年11月11-17日', '2019年11月16日', '十一月11至17日',
5),

(24, '看看别人的世界之边走边聊：', '滨江线行走八公里',
'2019.11.17 周日', '06:30 pm - 21:30 pm', '地点 浦东新区 中华艺术宫-4口',
'img/shv2_event4.jpg', '', 'img/transparent.png',
'这是一条很长的滨江线，可以吹着江风，看着夜上海的灯火辉煌。添加微信号：pei1711944147 备注：夜跑', 17, 23,
1,1,1,0,0,1,
'long description',
'2019年11月11-17日', '2019年11月16日', '十一月11至17日',
5),

(25, '边走边聊：', '中秋赏江月，八公里滨江线',
'2019.11.16 周六', '06:30 pm - 21:00 pm', '地点 浦东新区 中华艺术宫-4口',
'img/shv2_event5.jpg', '', 'img/transparent.png',
'一起来走一下8公里滨江线，和小伙伴们一起边走边聊赏江月。添加微信号:sanrihua_nick 备注: A伙伴', 17, 23,
1,1,1,0,0,1,
'long description',
'2019年11月11-17日', '2019年11月16日', '十一月11至17日',
5),


(26, '游走魔都 ', '',
'2019.11.17 周日', '13:30 pm - 16:30 pm', '地点 徐汇区 武康大楼',
'img/shv2_event6.jpg', '', 'img/transparent.png',
'请放慢自己的脚步，跟随自己的心，用眼睛去重新发现这个有很多故事的上海。添加微信号:iami-keats  备注: 游走活动', 17, 23,
1,1,1,0,0,1,
'long description',
'2019年11月11-17日', '2019年11月16日', '十一月11至17日',
5);

CREATE TABLE pages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  day INTEGER NOT NULL,
  page INTEGER NOT NULL,
  question_name TEXT NOT NULL,
  cohort INTEGER NOT NULL
);

INSERT INTO pages (day, page, question_name, cohort)
VALUES
  (1, 1, 'walkathonInterest', 5),
  (1, 1, 'walkathonSteps', 5),
  (1, 2, 'weatherStarCountGroup1Input', 5),
  (1, 2, 'weatherStarCountGroup2Input', 5),
  (1, 2, 'weatherStarCountGroup3Input', 5),
  (1, 2, 'weatherStarCountGroup4Input', 5),
  (1, 3, 'blueGraySky', 5),
  (1, 4, 'starCountGroup1Input', 5),
  (1, 4, 'starCountGroup2Input', 5),
  (1, 4, 'starCountGroup3Input', 5),
  (1, 4, 'starCountGroup4Input', 5),
  (1, 4, 'starCountGroup5Input', 5),
  (1, 4, 'starCountGroup6Input', 5),
  (1, 5, 'trustOptionsOrder', 5),
  (1, 5, 'dontKnowFamilyFriends', 5),
  (1, 5, 'trust1', 5),
  (1, 5, 'dontKnowStrangers', 5),
  (1, 5, 'trust2', 5),
  (1, 5, 'dontKnowForeigners', 5),
  (1, 5, 'trust3', 5),
  (1, 5, 'dontKnowMedia', 5),
  (1, 5, 'trust4', 5),
  (1, 5, 'dontKnowGovernment', 5),
  (1, 5, 'trust5', 5),
  (1, 5, 'dontKnowHS', 5),
  (1, 5, 'trust6', 5),
  (1, 5, 'dontKnowNGO', 5),
  (1, 5, 'trust7', 5),
  (1, 5, 'dontKnowCorporation', 5),
  (1, 5, 'trust8', 5),
  (1, 6, 'willingnessAmount', 5),
  (1, 6, 'donationWillingness', 5),

  (2, 1, 'eventNameOrder', 5),
  (2, 1, 'eventName', 5),
  (2, 1, 'signUpFeeAmount', 5),
  (2, 2, 'outingLocation', 5),
  (2, 2, 'outingTransportation', 5),
  (2, 2, 'outingTemperature', 5),
  (2, 2, 'outingAirQuality', 5),
  (2, 2, 'outingFriends', 5),
  (2, 3, 'newsSourceDomesticWebsite', 5),
  (2, 3, 'newsSourceForeignWebsite', 5),
  (2, 3, 'newsSourceDomesticMedia', 5),
  (2, 3, 'newsSourceForeignMedia', 5),
  (2, 3, 'newsSourceChatWithFriends', 5),
  (2, 4, 'trustOptionsOrder', 5),
  (2, 4, 'dontKnowPeoplesDaily', 5),
  (2, 4, 'trustPeoplesDaily', 5),
  (2, 4, 'dontKnowMorningPost', 5),
  (2, 4, 'trustMorningPost', 5),
  (2, 4, 'dontKnowFM', 5),
  (2, 4, 'trustFM', 5),
  (2, 4, 'dontKnowSEMC', 5),
  (2, 4, 'trustSEMC', 5),
  (2, 4, 'dontKnowCNTA', 5),
  (2, 4, 'trustCNTA', 5),
  (2, 4, 'dontKnowNYT', 5),
  (2, 4, 'trustNYT', 5),
  (2, 5, 'gender', 5),
  (2, 5, 'birthYear', 5),
  (2, 5, 'province', 5),
  (2, 5, 'city', 5),
  (2, 5, 'university', 5),
  (2, 5, 'otherUniAnswer', 5),
  (2, 5, 'liveOnCampus', 5),
  (2, 5, 'address', 5),
  (2, 5, 'dormName', 5),
  (2, 5, 'otherMailInfo', 5),
  (2, 5, 'major', 5),
  (2, 5, 'grade', 5),

  (3, 1, 'donationWilling', 5),
  (3, 2, 'activity1', 5),
  (3, 2, 'activity2', 5),
  (3, 2, 'activity3', 5),
  (3, 2, 'outdoorTime', 5),
  (3, 2, 'exerciseTime', 5),
  (3, 2, 'beenToCountries', 5),
  (3, 3, 'newsQuestionsOrder', 5),
  (3, 3, 'event1HasHappened', 5),
  (3, 3, 'event2HasHappened', 5),
  (3, 3, 'event3HasHappened', 5),
  (3, 3, 'event4HasHappened', 5),
  (3, 3, 'event5HasHappened', 5),

  (4, 1, 'signUpFee', 5),

  (5, 1, 'signUpFee', 5),

  (6, 1, 'signUpFeeEvent1', 5),
  (6, 2, 'secondEventNextButton', 5),
  (6, 3, 'signUpFeeEvent2', 5),
  (6, 4, 'walkathonNextButton', 5),
  (6, 5, 'blueGraySky', 5),
  (6, 6, 'starCountGroup1Input', 5),
  (6, 6, 'starCountGroup2Input', 5),
  (6, 6, 'starCountGroup3Input', 5),
  (6, 6, 'starCountGroup4Input', 5),
  (6, 6, 'starCountGroup5Input', 5),
  (6, 6, 'starCountGroup6Input', 5),
  (6, 7, 'walkathonInterest', 5),
  (6, 8, 'outingLocation', 5),
  (6, 8, 'outingTransportation', 5),
  (6, 8, 'outingTemperature', 5),
  (6, 8, 'outingAirQuality', 5),
  (6, 8, 'outingFriends', 5),
  (6, 9, 'otherSource', 5),
  (6, 9, 'otherSourceNumberOfTimes', 5),
  (6, 9, 'weatherNumberOfTimes', 5),
  (6, 10, 'recallAirQuality', 5),
  (6, 10, 'recallAirQualitySource', 5),
  (6, 11, 'recallNumberOfAirQualitySource', 5),
  (6, 11, 'recallWhichAirQualitySource', 5),
  (6, 11, 'weatherInfoFrom', 5),
  (6, 12, 'notReportingProbability', 5),
  (6, 13, 'trustOptionsOrder', 5),
  (6, 13, 'dontKnowPeoplesDaily', 5),
  (6, 13, 'trustPeoplesDaily', 5),
  (6, 13, 'dontKnowMorningPost', 5),
  (6, 13, 'trustMorningPost', 5),
  (6, 13, 'dontKnowFM', 5),
  (6, 13, 'trustFM', 5),
  (6, 13, 'dontKnowSEMC', 5),
  (6, 13, 'trustSEMC', 5),
  (6, 13, 'dontKnowCNTA', 5),
  (6, 13, 'trustCNTA', 5),
  (6, 13, 'dontKnowNYT', 5),
  (6, 13, 'trustNYT', 5),

  (7, 1, 'blueGraySky', 5),
  (7, 2, 'starCountGroup1Input', 5),
  (7, 2, 'starCountGroup2Input', 5),
  (7, 2, 'starCountGroup3Input', 5),
  (7, 2, 'starCountGroup4Input', 5),
  (7, 2, 'starCountGroup5Input', 5),
  (7, 2, 'starCountGroup6Input', 5),
  (7, 3, 'walkathonInterest', 5),
  (7, 3, 'walkathonSteps', 5),
  (7, 4, 'whoToldMeWrongAnswers', 5),
  (7, 4, 'whoToldMe', 5),
  (7, 4, 'checkBeanNumberSourceButton', 5),
  (7, 4, 'guessedBeanNumber', 5),
  (7, 5, 'math1Answer', 5),
  (7, 5, 'math1timeover', 5),
  (7, 5, 'math2Answer', 5),
  (7, 5, 'math2timeover', 5),
  (7, 5, 'math3Answer', 5),
  (7, 5, 'math3timeover', 5),
  (7, 5, 'math4Answer', 5),
  (7, 5, 'math4timeover', 5),
  (7, 5, 'math5Answer', 5),
  (7, 5, 'math5timeover', 5),

  (8, 1, 'blueGraySky', 5),
  (8, 2, 'questionOrder', 5),
  (8, 2, 'starCountGroup1Input', 5),
  (8, 2, 'starCountGroup2Input', 5),
  (8, 2, 'starCountGroup3Input', 5),
  (8, 2, 'starCountGroup4Input', 5),
  (8, 2, 'starCountGroup5Input', 5),
  (8, 2, 'starCountGroup6Input', 5),
  (8, 3, 'trustOptionsOrder', 5),
  (8, 3, 'dontKnowPeoplesDaily', 5),
  (8, 3, 'trustPeoplesDaily', 5),
  (8, 3, 'dontKnowMorningPost', 5),
  (8, 3, 'trustMorningPost', 5),
  (8, 3, 'dontKnowFM', 5),
  (8, 3, 'trustFM', 5),
  (8, 3, 'dontKnowSEMC', 5),
  (8, 3, 'trustSEMC', 5),
  (8, 3, 'dontKnowCNTA', 5),
  (8, 3, 'trustCNTA', 5),
  (8, 3, 'dontKnowNYT', 5),
  (8, 3, 'trustNYT', 5);

























--------
