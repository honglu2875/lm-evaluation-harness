import matplotlib.pyplot as plt

results = {
    0: {
        "arc_challenge": {
            "acc": 0.2030716723549488,
            "acc_stderr": 0.011755899303705582,
            "acc_norm": 0.2431740614334471,
            "acc_norm_stderr": 0.01253655414458709
        },
        "arc_easy": {
            "acc": 0.30134680134680136,
            "acc_stderr": 0.009415259879351615,
            "acc_norm": 0.30008417508417506,
            "acc_norm_stderr": 0.009404000558513367
        },
        "boolq": {
            "acc": 0.3782874617737003,
            "acc_stderr": 0.008482001133931005
        },
        "hellaswag": {
            "acc": 0.27285401314479185,
            "acc_stderr": 0.004445160997618378,
            "acc_norm": 0.28121888070105555,
            "acc_norm_stderr": 0.00448675220043036
        },
        "lambada_openai": {
            "ppl": 130683.86749488341,
            "ppl_stderr": 6130.3893242234035,
            "acc": 0.0,
            "acc_stderr": 0.0
        },
        "piqa": {
            "acc": 0.5914036996735582,
            "acc_stderr": 0.011469240387245137,
            "acc_norm": 0.5952121871599565,
            "acc_norm_stderr": 0.011452361375057025
        },
        "sciq": {
            "acc": 0.242,
            "acc_stderr": 0.01355063170555596,
            "acc_norm": 0.298,
            "acc_norm_stderr": 0.014470846741134705
        },
        "triviaqa": {
            "acc": 0.0,
            "acc_stderr": 0.0
        },
        "winogrande": {
            "acc": 0.5043409629044988,
            "acc_stderr": 0.0140519560640769
        }
    },
    1: {
        "arc_challenge": {
            "acc": 0.19027303754266212,
            "acc_stderr": 0.0114704241792257,
            "acc_norm": 0.22696245733788395,
            "acc_norm_stderr": 0.01224049153613287
        },
        "arc_easy": {
            "acc": 0.43813131313131315,
            "acc_stderr": 0.010180937100600062,
            "acc_norm": 0.3947811447811448,
            "acc_norm_stderr": 0.010030038935883556
        },
        "boolq": {
            "acc": 0.4871559633027523,
            "acc_stderr": 0.008742169169427055
        },
        "hellaswag": {
            "acc": 0.2891854212308305,
            "acc_stderr": 0.00452457589295296,
            "acc_norm": 0.31139215295757816,
            "acc_norm_stderr": 0.004621163476949214
        },
        "lambada_openai": {
            "ppl": 40.05485179107735,
            "ppl_stderr": 1.48804659673212,
            "acc": 0.32563555210556955,
            "acc_stderr": 0.00652867895783546
        },
        "piqa": {
            "acc": 0.6289445048966268,
            "acc_stderr": 0.011271222398600523,
            "acc_norm": 0.6251360174102285,
            "acc_norm_stderr": 0.011294565805619014
        },
        "sciq": {
            "acc": 0.75,
            "acc_stderr": 0.013699915608779773,
            "acc_norm": 0.644,
            "acc_norm_stderr": 0.015149042659306625
        },
        "triviaqa": {
            "acc": 0.015115354017501989,
            "acc_stderr": 0.0011471815321400067
        },
        "winogrande": {
            "acc": 0.516179952644041,
            "acc_stderr": 0.014045126130978604
        }
    },
    1.25: {
        "arc_challenge": {
            "acc": 0.19368600682593856,
            "acc_stderr": 0.01154842540997854,
            "acc_norm": 0.22098976109215018,
            "acc_norm_stderr": 0.012124929206818258
        },
        "arc_easy": {
            "acc": 0.45075757575757575,
            "acc_stderr": 0.010209906101011117,
            "acc_norm": 0.414983164983165,
            "acc_norm_stderr": 0.010110383151961114
        },
        "boolq": {
            "acc": 0.5409785932721712,
            "acc_stderr": 0.008715635308774412
        },
        "hellaswag": {
            "acc": 0.29665405297749453,
            "acc_stderr": 0.004558491550673689,
            "acc_norm": 0.3158733320055766,
            "acc_norm_stderr": 0.004639126951051424
        },
        "lambada_openai": {
            "ppl": 5.299848050912554,
            "ppl_stderr": 0.24609331152718822,
            "acc": 0.41121676693188436,
            "acc_stderr": 0.0068552799833578966
        },
        "piqa": {
            "acc": 0.6327529923830251,
            "acc_stderr": 0.011247128539690563,
            "acc_norm": 0.6273122959738846,
            "acc_norm_stderr": 0.01128131833289775
        },
        "sciq": {
            "acc": 0.779,
            "acc_stderr": 0.013127502859696251,
            "acc_norm": 0.682,
            "acc_norm_stderr": 0.014734079309311901
        },
        "triviaqa": {
            "acc": 0.02360116679925749,
            "acc_stderr": 0.001427284878928031
        },
        "winogrande": {
            "acc": 0.505130228887135,
            "acc_stderr": 0.01405174596179051
        }
    },
    1.5: {
        "arc_challenge": {
            "acc": 0.19880546075085323,
            "acc_stderr": 0.01166285019817553,
            "acc_norm": 0.23037542662116042,
            "acc_norm_stderr": 0.01230492841874761
        },
        "arc_easy": {
            "acc": 0.4595959595959596,
            "acc_stderr": 0.010226230740889025,
            "acc_norm": 0.4212962962962963,
            "acc_norm_stderr": 0.01013188249819314
        },
        "boolq": {
            "acc": 0.5700305810397553,
            "acc_stderr": 0.00865885369072926
        },
        "hellaswag": {
            "acc": 0.3004381597291376,
            "acc_stderr": 0.004575116093931892,
            "acc_norm": 0.31915952997410874,
            "acc_norm_stderr": 0.004651982864043493
        },
        "lambada_openai": {
            "ppl": 0.7012481167551132,
            "ppl_stderr": 0.04045141281948315,
            "acc": 0.44556568988938483,
            "acc_stderr": 0.006924572910496155
        },
        "piqa": {
            "acc": 0.6332970620239391,
            "acc_stderr": 0.011243625019038257,
            "acc_norm": 0.6376496191512514,
            "acc_norm_stderr": 0.011215040215104576
        },
        "sciq": {
            "acc": 0.782,
            "acc_stderr": 0.0130631790405953,
            "acc_norm": 0.708,
            "acc_norm_stderr": 0.01438551156347735
        },
        "triviaqa": {
            "acc": 0.02784407319013524,
            "acc_stderr": 0.0015469085832672488
        },
        "winogrande": {
            "acc": 0.505130228887135,
            "acc_stderr": 0.014051745961790513
        }
    },
    1.75: {
        "arc_challenge": {
            "acc": 0.20392491467576793,
            "acc_stderr": 0.011774262478702247,
            "acc_norm": 0.23293515358361774,
            "acc_norm_stderr": 0.012352507042617407
        },
        "arc_easy": {
            "acc": 0.4659090909090909,
            "acc_stderr": 0.010235908103438695,
            "acc_norm": 0.43308080808080807,
            "acc_norm_stderr": 0.010167478013701796
        },
        "boolq": {
            "acc": 0.5856269113149847,
            "acc_stderr": 0.00861586377642113
        },
        "hellaswag": {
            "acc": 0.3018323043218482,
            "acc_stderr": 0.004581147247963198,
            "acc_norm": 0.32204740091615214,
            "acc_norm_stderr": 0.004663060828376788
        },
        "lambada_openai": {
            "ppl": 0.0927854764508389,
            "ppl_stderr": 0.006493872451365119,
            "acc": 0.46167281195420146,
            "acc_stderr": 0.0069454818340364795
        },
        "piqa": {
            "acc": 0.6365614798694232,
            "acc_stderr": 0.01122227939530451,
            "acc_norm": 0.6354733405875952,
            "acc_norm_stderr": 0.011229456510295962
        },
        "sciq": {
            "acc": 0.785,
            "acc_stderr": 0.012997843819031815,
            "acc_norm": 0.731,
            "acc_norm_stderr": 0.014029819522568198
        },
        "triviaqa": {
            "acc": 0.02890479978785468,
            "acc_stderr": 0.0015752380305831106
        },
        "winogrande": {
            "acc": 0.5059194948697711,
            "acc_stderr": 0.014051500838485807
        }
    },
    2: {
        "arc_challenge": {
            "acc": 0.20648464163822525,
            "acc_stderr": 0.011828865619002316,
            "acc_norm": 0.22440273037542663,
            "acc_norm_stderr": 0.012191404938603838
        },
        "arc_easy": {
            "acc": 0.46885521885521886,
            "acc_stderr": 0.010239860250021755,
            "acc_norm": 0.4335016835016835,
            "acc_norm_stderr": 0.010168640625454115
        },
        "boolq": {
            "acc": 0.5975535168195719,
            "acc_stderr": 0.008576992126012484
        },
        "hellaswag": {
            "acc": 0.3062139016132245,
            "acc_stderr": 0.004599776866717473,
            "acc_norm": 0.3234415455088628,
            "acc_norm_stderr": 0.004668335725410296
        },
        "lambada_openai": {
            "ppl": 0.012276887671923368,
            "ppl_stderr": 0.0010178536476367311,
            "acc": 0.47059965068891907,
            "acc_stderr": 0.006953924718792958
        },
        "piqa": {
            "acc": 0.6338411316648531,
            "acc_stderr": 0.011240106070308462,
            "acc_norm": 0.6436343852013058,
            "acc_norm_stderr": 0.011174109865864732
        },
        "sciq": {
            "acc": 0.786,
            "acc_stderr": 0.012975838021968769,
            "acc_norm": 0.741,
            "acc_norm_stderr": 0.01386041525752791
        },
        "triviaqa": {
            "acc": 0.029346769203571113,
            "acc_stderr": 0.0015868742109548702
        },
        "winogrande": {
            "acc": 0.505130228887135,
            "acc_stderr": 0.014051745961790513
        }
    },
    3: {
        "arc_challenge": {
            "acc": 0.22184300341296928,
            "acc_stderr": 0.012141659068147882,
            "acc_norm": 0.2235494880546075,
            "acc_norm_stderr": 0.012174896631202605
        },
        "arc_easy": {
            "acc": 0.4537037037037037,
            "acc_stderr": 0.010215708295494126,
            "acc_norm": 0.4364478114478115,
            "acc_norm_stderr": 0.010176569980111043
        },
        "boolq": {
            "acc": 0.6140672782874618,
            "acc_stderr": 0.008514444495863343
        },
        "hellaswag": {
            "acc": 0.31009759012148974,
            "acc_stderr": 0.004615880352799743,
            "acc_norm": 0.32304321848237405,
            "acc_norm_stderr": 0.004666833452796192
        },
        "lambada_openai": {
            "ppl": 3.762889211457798e-06,
            "ppl_stderr": 5.183817025307134e-07,
            "acc": 0.47331651465165925,
            "acc_stderr": 0.006956050915151105
        },
        "piqa": {
            "acc": 0.6262241566920566,
            "acc_stderr": 0.011287972563201017,
            "acc_norm": 0.6349292709466812,
            "acc_norm_stderr": 0.011233021830554833
        },
        "sciq": {
            "acc": 0.785,
            "acc_stderr": 0.012997843819031811,
            "acc_norm": 0.752,
            "acc_norm_stderr": 0.013663187134877658
        },
        "triviaqa": {
            "acc": 0.027313709891275524,
            "acc_stderr": 0.001532523155683461
        },
        "winogrande": {
            "acc": 0.5074980268350434,
            "acc_stderr": 0.014050905521228573
        }
    },
    4: {
        "arc_challenge": {
            "acc": 0.22781569965870307,
            "acc_stderr": 0.012256708602326916,
            "acc_norm": 0.2226962457337884,
            "acc_norm_stderr": 0.012158314774829936
        },
        "arc_easy": {
            "acc": 0.44612794612794615,
            "acc_stderr": 0.010200057828765008,
            "acc_norm": 0.4356060606060606,
            "acc_norm_stderr": 0.010174341733665222
        },
        "boolq": {
            "acc": 0.6162079510703364,
            "acc_stderr": 0.00850558472910497
        },
        "hellaswag": {
            "acc": 0.31228838876717785,
            "acc_stderr": 0.004624796348128792,
            "acc_norm": 0.3218482374029078,
            "acc_norm_stderr": 0.004662303395239619
        },
        "lambada_openai": {
            "ppl": 1.1533326921851272e-09,
            "ppl_stderr": 2.2590256233570883e-10,
            "acc": 0.46594216960993595,
            "acc_stderr": 0.00694979869493088
        },
        "piqa": {
            "acc": 0.6251360174102285,
            "acc_stderr": 0.011294565805619015,
            "acc_norm": 0.6322089227421109,
            "acc_norm_stderr": 0.011250616646678787
        },
        "sciq": {
            "acc": 0.777,
            "acc_stderr": 0.01316983084342568,
            "acc_norm": 0.751,
            "acc_norm_stderr": 0.013681600278702313
        },
        "triviaqa": {
            "acc": 0.026252983293556086,
            "acc_stderr": 0.0015032897729967127
        },
        "winogrande": {
            "acc": 0.5098658247829518,
            "acc_stderr": 0.014049749833367596
        }
    },
    5: {
        "arc_challenge": {
            "acc": 0.23208191126279865,
            "acc_stderr": 0.012336718284948853,
            "acc_norm": 0.21928327645051193,
            "acc_norm_stderr": 0.01209124578761573
        },
        "arc_easy": {
            "acc": 0.44065656565656564,
            "acc_stderr": 0.010187264635711986,
            "acc_norm": 0.42424242424242425,
            "acc_norm_stderr": 0.010141333654958569
        },
        "boolq": {
            "acc": 0.617125382262997,
            "acc_stderr": 0.008501734385335953
        },
        "hellaswag": {
            "acc": 0.3148775144393547,
            "acc_stderr": 0.004635178371110037,
            "acc_norm": 0.3218482374029078,
            "acc_norm_stderr": 0.004662303395239619
        },
        "lambada_openai": {
            "ppl": 3.5349864492905835e-13,
            "ppl_stderr": 9.090264719586164e-14,
            "acc": 0.4575975160100912,
            "acc_stderr": 0.006940883209964994
        },
        "piqa": {
            "acc": 0.6256800870511425,
            "acc_stderr": 0.01129127680119499,
            "acc_norm": 0.6305767138193689,
            "acc_norm_stderr": 0.011260988628572324
        },
        "sciq": {
            "acc": 0.769,
            "acc_stderr": 0.013334797216936433,
            "acc_norm": 0.75,
            "acc_norm_stderr": 0.013699915608779773
        },
        "triviaqa": {
            "acc": 0.024308317864403784,
            "acc_stderr": 0.0014479849783186442
        },
        "winogrande": {
            "acc": 0.5082872928176796,
            "acc_stderr": 0.014050555322824189
        }
    },
    6: {
        "arc_challenge": {
            "acc": 0.2354948805460751,
            "acc_stderr": 0.012399451855004743,
            "acc_norm": 0.22525597269624573,
            "acc_norm_stderr": 0.012207839995407305
        },
        "arc_easy": {
            "acc": 0.4364478114478115,
            "acc_stderr": 0.010176569980111043,
            "acc_norm": 0.42213804713804715,
            "acc_norm_stderr": 0.010134620524592271
        },
        "boolq": {
            "acc": 0.6192660550458715,
            "acc_stderr": 0.008492625561656215
        },
        "hellaswag": {
            "acc": 0.31826329416450905,
            "acc_stderr": 0.004648503177353936,
            "acc_norm": 0.32065325632344155,
            "acc_norm_stderr": 0.00465773839890092
        },
        "lambada_openai": {
            "ppl": 1.0834799425360282e-16,
            "ppl_stderr": 3.491759526794049e-17,
            "acc": 0.4533281583543567,
            "acc_stderr": 0.00693556383084106
        },
        "piqa": {
            "acc": 0.6229597388465724,
            "acc_stderr": 0.011307569752543897,
            "acc_norm": 0.6229597388465724,
            "acc_norm_stderr": 0.011307569752543899
        },
        "sciq": {
            "acc": 0.769,
            "acc_stderr": 0.013334797216936433,
            "acc_norm": 0.751,
            "acc_norm_stderr": 0.013681600278702312
        },
        "triviaqa": {
            "acc": 0.02342437903297092,
            "acc_stderr": 0.0014220579166004726
        },
        "winogrande": {
            "acc": 0.505130228887135,
            "acc_stderr": 0.014051745961790513
        }
    },
    7: {
        "arc_challenge": {
            "acc": 0.24573378839590443,
            "acc_stderr": 0.012581033453730107,
            "acc_norm": 0.22781569965870307,
            "acc_norm_stderr": 0.01225670860232691
        },
        "arc_easy": {
            "acc": 0.4356060606060606,
            "acc_stderr": 0.010174341733665222,
            "acc_norm": 0.42003367003367004,
            "acc_norm_stderr": 0.010127718838529398
        },
        "boolq": {
            "acc": 0.6192660550458715,
            "acc_stderr": 0.008492625561656215
        },
        "hellaswag": {
            "acc": 0.3196574387572197,
            "acc_stderr": 0.0046539074717856285,
            "acc_norm": 0.31935869348735313,
            "acc_norm_stderr": 0.004652753439460147
        },
        "lambada_openai": {
            "ppl": 3.3208869766955366e-20,
            "ppl_stderr": 1.3022785651764598e-20,
            "acc": 0.45002910925674366,
            "acc_stderr": 0.006931101003281439
        },
        "piqa": {
            "acc": 0.6196953210010882,
            "acc_stderr": 0.01132662089257031,
            "acc_norm": 0.6202393906420022,
            "acc_norm_stderr": 0.011323483504715843
        },
        "sciq": {
            "acc": 0.764,
            "acc_stderr": 0.013434451402438699,
            "acc_norm": 0.748,
            "acc_norm_stderr": 0.013736254390651148
        },
        "triviaqa": {
            "acc": 0.022805621850967912,
            "acc_stderr": 0.0014035947693080114
        },
        "winogrande": {
            "acc": 0.5059194948697711,
            "acc_stderr": 0.014051500838485807
        }
    },
    8: {
        "arc_challenge": {
            "acc": 0.24488054607508533,
            "acc_stderr": 0.012566273985131354,
            "acc_norm": 0.2295221843003413,
            "acc_norm_stderr": 0.012288926760890797
        },
        "arc_easy": {
            "acc": 0.43097643097643096,
            "acc_stderr": 0.01016155286349375,
            "acc_norm": 0.41835016835016836,
            "acc_norm_stderr": 0.010122061470742861
        },
        "boolq": {
            "acc": 0.6186544342507645,
            "acc_stderr": 0.008495245917063549
        },
        "hellaswag": {
            "acc": 0.32194781915952997,
            "acc_stderr": 0.0046626822330937704,
            "acc_norm": 0.31756622186815375,
            "acc_norm_stderr": 0.0046457830480045505
        },
        "lambada_openai": {
            "ppl": 1.017858069809116e-23,
            "ppl_stderr": 4.762172104089814e-24,
            "acc": 0.4477003687172521,
            "acc_stderr": 0.006927765449003233
        },
        "piqa": {
            "acc": 0.6164309031556039,
            "acc_stderr": 0.011345128734116281,
            "acc_norm": 0.6147986942328618,
            "acc_norm_stderr": 0.011354179751257075
        },
        "sciq": {
            "acc": 0.763,
            "acc_stderr": 0.013454070462577964,
            "acc_norm": 0.748,
            "acc_norm_stderr": 0.013736254390651148
        },
        "triviaqa": {
            "acc": 0.02209847078582162,
            "acc_stderr": 0.0013821620843703553
        },
        "winogrande": {
            "acc": 0.5074980268350434,
            "acc_stderr": 0.014050905521228573
        }
    },
    9: {
        "arc_challenge": {
            "acc": 0.24914675767918087,
            "acc_stderr": 0.012639407111926433,
            "acc_norm": 0.22696245733788395,
            "acc_norm_stderr": 0.012240491536132865
        },
        "arc_easy": {
            "acc": 0.4276094276094276,
            "acc_stderr": 0.010151683397430677,
            "acc_norm": 0.4166666666666667,
            "acc_norm_stderr": 0.010116282977781249
        },
        "boolq": {
            "acc": 0.6186544342507645,
            "acc_stderr": 0.008495245917063549
        },
        "hellaswag": {
            "acc": 0.3205536745668194,
            "acc_stderr": 0.004657356402226426,
            "acc_norm": 0.3156741684923322,
            "acc_norm_stderr": 0.004638339207348916
        },
        "lambada_openai": {
            "ppl": 3.1197540576178944e-27,
            "ppl_stderr": 1.7179623134386346e-27,
            "acc": 0.44537162817776055,
            "acc_stderr": 0.006924276272696474
        },
        "piqa": {
            "acc": 0.6131664853101197,
            "acc_stderr": 0.011363095931902855,
            "acc_norm": 0.6099020674646355,
            "acc_norm_stderr": 0.011380525046581562
        },
        "sciq": {
            "acc": 0.762,
            "acc_stderr": 0.013473586661967225,
            "acc_norm": 0.749,
            "acc_norm_stderr": 0.013718133516888926
        },
        "triviaqa": {
            "acc": 0.021479713603818614,
            "acc_stderr": 0.001363105474104001
        },
        "winogrande": {
            "acc": 0.5074980268350434,
            "acc_stderr": 0.014050905521228573
        }
    },
    10: {
        "arc_challenge": {
            "acc": 0.24658703071672355,
            "acc_stderr": 0.012595726268790132,
            "acc_norm": 0.22696245733788395,
            "acc_norm_stderr": 0.012240491536132865
        },
        "arc_easy": {
            "acc": 0.4225589225589226,
            "acc_stderr": 0.010135978222981077,
            "acc_norm": 0.41792929292929293,
            "acc_norm_stderr": 0.010120628211017887
        },
        "boolq": {
            "acc": 0.6186544342507645,
            "acc_stderr": 0.008495245917063547
        },
        "hellaswag": {
            "acc": 0.32135032861979684,
            "acc_stderr": 0.00466040556533875,
            "acc_norm": 0.31358295160326627,
            "acc_norm_stderr": 0.0046300082939256275
        },
        "lambada_openai": {
            "ppl": 9.562105306242716e-31,
            "ppl_stderr": 6.139188298099282e-31,
            "acc": 0.44420725790801474,
            "acc_stderr": 0.006922474004090816
        },
        "piqa": {
            "acc": 0.6169749727965179,
            "acc_stderr": 0.011342081709082845,
            "acc_norm": 0.6077257889009793,
            "acc_norm_stderr": 0.01139184674407223
        },
        "sciq": {
            "acc": 0.761,
            "acc_stderr": 0.013493000446937591,
            "acc_norm": 0.746,
            "acc_norm_stderr": 0.01377220656516854
        },
        "triviaqa": {
            "acc": 0.021214531954388757,
            "acc_stderr": 0.0013548486579008626
        },
        "winogrande": {
            "acc": 0.5059194948697711,
            "acc_stderr": 0.014051500838485807
        }
    },
}

# plot accuracies for increasing values of cfg
plt.figure(figsize=(10, 5))
longest_test = max([len(t) for t in results[0].keys()])


def pad(s):
    return s + " " * (longest_test - len(s))


tests = list(results[0].keys())
#tests = [t for t in tests if "ppl" in results[0][t]]
cfgs = list(results.keys())[1:]
cfgs.sort()
print(pad('CFG'), '\t'.join(str(c) for c in cfgs))
for test in tests:
    key = 'acc_norm' if 'acc_norm' in results[0][test] else 'acc'
    print(
        pad(test),
        '\t'.join([f'{100 * results[cfg][test][key]:>5.2f}' for cfg in cfgs]))
    #print( pad('  std'), '\t'.join([ f'{100 * results[cfg][test]["acc_stderr"]:>5.2f}' for cfg in cfgs ]))
    plt.plot(cfgs, [results[cfg][test][key] for cfg in cfgs], 'o-')
plt.legend(tests)
plt.xlabel("guidance strength")
plt.ylabel("Accuracy")
plt.title("Results for GPT2-small")
plt.savefig("cfg_results.png")
