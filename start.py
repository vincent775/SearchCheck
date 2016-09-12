# coding: UTF-8
from conneMssql import MsSqlIN
from connMysql import MySqlIN

IP22 = '* '
IP26 = '*'
adict = {}
adict ={'ask':'bbs.dbo.ViewSphinxSearchAsk',
        'bbs':'bbs.dbo.ViewSphinxSearchbbsTopic',
        'yuanchuang':'ViewSphinxSearchYuanChuang',
        'bbsimg':'ViewSphinxSearchBBSImg',
        'ssboard':'ViewSphinxSearchSsBoard',
        'news':'ViewSphinxSearchNews',
        'subjectnews':'ViewSphinxSearchSubjectNews',
        'wapsolution':'ViewSphinxSearchWapSolution',
        'searchsubject':'ViewSphinxSearchSubject',
        'bid':'ViewSphinxSearchBid',
        'hainfo':'ViewSphinxSearchHaInfo',
        'conf':'ViewSphinxSearchConf',
        'expo':'ViewSphinxSearchExpo',
        'ilogarticle':'ViewSphinxSearchIlogArticle',
        'shownews':'ViewSphinxSearchShowNews',
        'othersearch':'ViewSphinxSearchOtherSearch',
        'paper':'ViewSphinxSearchPaper',
        'repaper':'ViewSphinxSearchRepaper',
        'reportitem':'ViewSphinxSearchReportItem',
        'result':'ViewSphinxSearchResult',
        'ilogconf':'ViewSphinxSearchILogConfig',
        'app':'ViewSphinxSearchApp',
        'company':'ViewSphinxSearchCompany',
        'imshowtype':'ViewSphinxSearchImshowType',
        'job':'ViewSphinxSearchJob',
        'lexicon':'ViewSphinxSearchlexicon',
        'service':'ViewSphinxSearchService',
        'serviceindex':'ViewSphinxSearchServiceIndex',
        'testinfo':'ViewSphinxSearchTestInfo',
        'testitem':'ViewSphinxSearchTestitem',
        'showb':'ViewSphinxSearchShowb',
        'solutionpaper':'ViewSphinxSearchSolutionPaper',
        'solutionshowb':'ViewSphinxSearchSolutionShowb',
        'solution':'ViewSphinxSearchSolution',
        'standardmain':'ViewSphinxSearchStandardMain',
        'subjectapp':'ViewSphinxSearchSubjectApp',
        'training':'ViewSphinxSearchTraining',
        'vip':'ViewSphinxSearchVip',
        'webinar':'ViewSphinxSearchWebinar',
        'webinarmeeting':'ViewSphinxSearchWebinarMeeting',
        'quotation':'ViewSphinxSearchQuotation'
        }
Port={}
Port = {'ask':23022,
        'bbs':23022,
        'yuanchuang':23022,
        'bbsimg':23022,
        'ssboard':23022,
        'news':23004,
        'subjectnews':23004,
        'wapsolution':23004,
        'searchsubject':23004,
        'bid':23004,
        'hainfo':23004,
        'conf':23004,
        'expo':23004,
        'ilogarticle':23004,
        'shownews':23004,
        'othersearch':23038,
        'paper':23038,
        'repaper':23038,
        'reportitem':23038,
        'result':23038,
        'ilogconf':23038,
        'app':23038,
        'company':23038,
        'imshowtype':23038,
        'job':23038,
        'lexicon':23038,
        'service':23025,
        'serviceindex':23025,
        'testinfo':23025,
        'testitem':23025,
        'showb':23001,
        'solutionpaper':23044,
        'solutionshowb':23044,
        'solution':23044,
        'standardmain':23044,
        'subjectapp':23044,
        'training':23029,
        'vip':23029,
        'webinar':23029,
        'webinarmeeting':23029,
        'quotation':23008
        }
def min():
    print 'start'
    print 'dbsource || mssql || 22server || 26server'
    for item,value in adict.items():
        print '%s || %s || %s || %s' %(item,  MsSqlIN(value),MySqlIN(item,IP22,Port[item]),MySqlIN(item,IP26,Port[item]))
    print 'end'


if __name__=="__main__":
    min()
