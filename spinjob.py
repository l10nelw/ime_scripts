# spinjob.py
# spiderjob spinner
# 2012-02-22

TEMPLATEHEAD = dict(
crawl=r'''
[{jobname}]
//Frequency={frequency}
//Section={section}
//LastChange={lastchange}
Directory=E:\Autonomy\IDOLServer\HTTPFetch\sites{fetchnum}\{jobname}
URL0={url}
''',#//Similar={similar}

rss=r'''
[{jobname}]
//FeedURL={url}
//Section={section}
//LastChange={lastchange}
Directory=E:\Autonomy\IDOLServer\HTTPFetch\sites2\{jobname}
URLFile=c:\urlfiles\{jobname}\{jobname}.txt
'''
)
TEMPLATEFACE = '''
ImportMustHaveCheck=65
ImportMustHaveCSVs=*{domain}*
FixedFieldName0=LANGUAGE
FixedFieldValue0=English
FixedFieldName1=keywords
FixedFieldValue1={keyword}
FixedFieldName2=LOCATION
FixedFieldValue2={country}
FixedFieldName3=SOURCETYPE
FixedFieldValue3=Internet News
FixedFieldName4=SOURCENAME
FixedFieldValue4={sourcename}
FixedFieldName5=Author
FixedFieldValue5=None
FixedFieldName6=SourceRank
FixedFieldValue6=1
'''

templateneck = dict(
crawl='''
MustHaveCheck=193
MustHaveCSVs=*/story/*
DateCheck=328
DateFormats="longmonth d+, yyyy, h+:nn"
AfterDate=-2
BeforeDate=7
MaxPages=6
Depth=1
HTMLImportTurnToSpaceStripTags=true
''',
rss='''
MaxPages=25
Depth=0
FollowRobotProtocol=false
'''
)
templatebody = '''
HTMLImportTurnToSpaceStartDefCSVs=<body,<footer class="news-article-footer">
HTMLImportTurnToSpaceEndDefCSVs=<!-- end of story assets carousel -->,</body>
HTMLFieldName0=Title
HTMLFieldStart0=<h1>
HTMLFieldStop0=</h1>
HTMLFieldName1=Date
HTMLFieldStart1=</h2><time datetime="
HTMLFieldStop1=">
HTMLFieldName2=Author0
HTMLFieldStart2=<cite>
HTMLFieldStop2=</cite>
ImportRemapField0=Title
ImportRemapFieldTo0=DRETITLE
ImportRemapField1=Author0
ImportRemapFieldTo1=Author
ImportFieldOp0=TopNTailWhiteSpace
ImportFieldOpApplyTo0=DRETITLE,Author
'''

FEEDSETTINGS = '<folder ID="{jobname}" NAME="{jobname}" OUTPUT="{jobname}.txt"><feed ID="{jobname}">{url}</feed></folder>\n'

jobcommon = dict(
	crawl=dict( keyword='News', country='Australia', lastchange='Added', frequency='1 hour', fetchnum='0', section='Latest News'),
	rss=dict( keyword='Other', sourcename='ABC Online', domain='abc.net.au', country='Australia', lastchange='Updated', frequency='1 hour', fetchnum='2', )
)
#sourcename='ABC Online', domain='anthonyalbanese.com.au', country='Australia', lastchange='Added'
#joblistitems = ['jobname', 'url', 'keyword', 'section', 'frequency', 'musthave', 'pages', 'fetchnum']
joblistitems = dict(
	crawl=['jobname', 'url', 'sourcename', 'domain'],
	rss=['jobname', 'url', 'section']
)
joblist = dict(
# jobname	url	keyword	section	frequency	musthave	pages	fetchnum
crawl='''
FfaxReg_AraratAdvertiser	http://www.araratadvertiser.com.au/news/latest-news/	The Ararat Advertiser	araratadvertiser.com.au
FfaxReg_BoorowaNews	http://www.boorowanewsonline.com.au/news/latest-news/	Boorowa News	boorowanewsonline.com.au
FfaxReg_BraidwoodTimes	http://www.braidwoodtimes.com.au/news/latest-news/	Braidwood Times	braidwoodtimes.com.au
FfaxReg_CanowindraNews	http://www.canowindranews.com.au/news/latest-news/	Canowindra News	canowindranews.com.au
FfaxReg_CessnockAdvertiser	http://www.cessnockadvertiser.com.au/news/latest-news/	Cessnock Advertiser	cessnockadvertiser.com.au
FfaxReg_CrookwellGazette	http://www.crookwellgazette.com.au/news/latest-news/	Crookwell Gazette	crookwellgazette.com.au
FfaxReg_SouthernCross	http://www.juneesoutherncross.com.au/news/latest-news/	Southern Cross	juneesoutherncross.com.au
FfaxReg_KatherineTimes	http://www.katherinetimes.com.au/news/latest-news/	Katherine Times	katherinetimes.com.au
FfaxReg_MaitlandMercury	http://www.maitlandmercury.com.au/news/latest-news/	Maitland Mercury	maitlandmercury.com.au
FfaxReg_NorthernDailyLeader	http://www.northerndailyleader.com.au/news/latest-news/	Northern Daily Leader	northerndailyleader.com.au
FfaxReg_NamoiValleyIndependent	http://www.nvi.com.au/news/latest-news/	Namoi Valley Independent	nvi.com.au
FfaxReg_OberonReview	http://www.oberonreview.com.au/news/latest-news/	Oberon Review	oberonreview.com.au
FfaxReg_ParkesChampionPost	http://www.parkeschampionpost.com.au/news/latest-news/	Parkes Champion-Post	parkeschampionpost.com.au
FfaxReg_RiverinaLeader	http://www.riverinaleader.com.au/news/latest-news/	Riverina Leader	riverinaleader.com.au
FfaxReg_SconeAdvocate	http://www.sconeadvocate.com.au/news/latest-news/	The Scone Advocate	sconeadvocate.com.au
FfaxReg_SouthCoastRegister	http://www.southcoastregister.com.au/news/latest-news/	South Coast Register	southcoastregister.com.au
FfaxReg_SouthernHighlandNews	http://www.southernhighlandnews.com.au/news/latest-news/	Southern Highland News	southernhighlandnews.com.au
FfaxReg_TennantDistrictTimes	http://www.tennantcreektimes.com.au/news/latest-news/	Tennant & District Times	tennantcreektimes.com.au
FfaxReg_TenterfieldStar	http://www.tenterfieldstar.com.au/news/latest-news/	Tenterfield Star	tenterfieldstar.com.au
FfaxReg_TheNorthernTimes	http://www.thenortherntimes.com.au/news/latest-news/	The Northern Times	thenortherntimes.com.au
FfaxReg_TheRidgeNews	http://www.theridgenews.com.au/news/latest-news/	The Ridge News	theridgenews.com.au
FfaxReg_TheRural	http://www.therural.com.au/news/latest-news/	The Rural	therural.com.au
FfaxReg_TheWaginArgus	http://www.waginargus.com.au/news/latest-news/	The Wagin Argus	waginargus.com.au
FfaxReg_WesternAdvocate	http://www.westernadvocate.com.au/news/latest-news/	Western Advocate	westernadvocate.com.au
FfaxReg_WesternMagazine	http://www.westernmagazine.com.au/news/latest-news/	Western Magazine	westernmagazine.com.au
''',
# jobname	url	keyword	section
rss='''
ABC_ACT	http://www.abc.net.au/news/feed/48320/rss.xml	Australian Capital Territory
ABC_NSW	http://www.abc.net.au/news/feed/52498/rss.xml	New South Wales
ABC_NT	http://www.abc.net.au/news/feed/53408/rss.xml	Northern Territory
ABC_QLD	http://www.abc.net.au/news/feed/50990/rss.xml	Queensland
ABC_SA	http://www.abc.net.au/news/feed/54702/rss.xml	South Australia
ABC_TAS	http://www.abc.net.au/news/feed/50042/rss.xml	Tasmania
ABC_VIC	http://www.abc.net.au/news/feed/54242/rss.xml	Victoria
ABC_WA	http://www.abc.net.au/news/feed/52764/rss.xml	Western Australia
ABC_DRUM1	http://www.abc.net.au/news/feed/1054894/rss.xml	ABC Columnists
ABC_DRUM2	http://www.abc.net.au/news/feed/1054870/rss.xml	The Drum Opinion

'''
)

import os
from datetime import datetime

type = 0 # <------ rss 1 or crawl 0?
type = 'rss' if type else 'crawl'

outputrss = '[feedsettings]\n'
outputnum = outputjob = ''
count = 0
templatehead = TEMPLATEHEAD[type].strip() + TEMPLATEFACE + templateneck[type].strip()
jobcommon = jobcommon[type]
jobcommon['lastchange'] = ' '.join(( datetime.now().strftime('%Y-%m-%d'), os.environ['USERNAME'], jobcommon['lastchange'] ))

for job in joblist[type].strip().split('\n'):
	job = dict(zip( joblistitems[type], job.split('\t') ))
	if type=='rss': outputrss += FEEDSETTINGS.format(**job)
	outputnum += '{}={}\n'.format(count, job['jobname'])
	outputjob += templatehead.format(**dict(job, **jobcommon)) + templatebody + '\n'
	count += 1

with open('out.txt', 'w') as f:
	if type=='rss': f.write(outputrss + '\n')
	f.write('[SPIDER]\nNumber={}\n'.format(count))
	f.write(outputnum + '\n')
	f.write(outputjob)

