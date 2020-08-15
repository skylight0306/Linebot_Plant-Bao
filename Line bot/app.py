from flask import Flask, request, abort

from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import *
import random

app = Flask(__name__)




	
# Channel Access Token
line_bot_api = LineBotApi('wU1aktJgaT6vk/1LzTInjfGzdzht4cSj214lDO+dFAimRi3Ka+a5Nn8a2d3SGWli0LIZ0r8dj2Voa9Ctyj/sZGZZ3xY+OLRNF+cNA0xiLAyfGwKkjDL9yZJpz5vnrD2rJh5+lF2IiuidAEVHh0RsXAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('4fc89cec4e120acbef76e8eb77dfb791')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
	# get X-Line-Signature header value
	signature = request.headers['X-Line-Signature']
	# get request body as text
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)
	# handle webhook body
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	reply_arr=[]

	#message = TextSendMessage(text=event.message.text)
	#line_bot_api.reply_message(event.reply_token, message)

	#message = StickerSendMessage(
	#	package_id='1',
	#	sticker_id='1'
	#)
	#line_bot_api.reply_message(event.reply_token, message)

	print(event)
	text=event.message.text
#text = "hi"
	if "嗨" in text:
		reply_arr.append( TextSendMessage(text="Hello" ))
	elif "餓" in text:
		reply_arr.append( TextSendMessage(text="種盆蘆薈來吃吧！") )
	elif "天氣" in text:
		reply_arr.append( TextSendMessage(text="我要去曬太陽！") )
	elif "笑話" in text:
		num = random.randint(1,10)
		if num == 1:
			reply_arr.append( TextSendMessage(text="桃園三結義那天，\n張飛很不滿意自己寫的字，轉頭對關羽說「我字好醜」\n於是關羽對張飛說\n「好醜你好，我字雲長」") )
		elif num == 2:
			reply_arr.append( TextSendMessage(text="我：醫生，我手術後要多久才能拉小提琴？\n醫生：一個月。\n我：謝謝你，我本來不會拉的！") )
		elif num == 3:
			reply_arr.append( TextSendMessage(text="有一天小明打電話給電話客服\n客服：很高興為您服務\n小明：你高興的太早了\n於是小明就把電話掛掉了") )
		elif num == 4:
			reply_arr.append( TextSendMessage(text="某富翁娶妻，有三個人選，富翁給了三個女孩各一千元請她們把房間裝滿。\n女孩1買了很多棉花，裝滿房間的1/2。\n女孩2買了很多氣球,裝滿房間3/4。\n女孩3買了蠟燭，讓光充滿房間。\n最終，富翁選了胸部最大的那個。") )
		elif num == 5:
			reply_arr.append( TextSendMessage(text="伊斯蘭恐怖組織ISIS以前叫什麼名稱?\n.\n.\n.\n.\nwaswas") )
		elif num == 6:
			reply_arr.append( TextSendMessage(text="有一天小明他爸很渴\n就叫小明幫他倒水\n但小明遲遲沒去倒\n小明爸就說：「你是要逼爸渴死嗎？」\n.\n.\n.\n.\n.\n.\n於是小明就開始B Box了") )
		elif num == 7:
			reply_arr.append( TextSendMessage(text="劉備字玄德\n張飛字翼德\n五佰字？？\n.\n.\n.\n.\n.\n.\n心得") )
		elif num == 8:
			reply_arr.append( TextSendMessage(text="愚公臨死前召集兒子來到床邊\n虛弱的說：「移山…移山………」\n.\n.\n.\n.\n.\n.\n.\n兒子：「亮晶晶？」\n愚公卒。\n") )
		elif num == 9:
			reply_arr.append( TextSendMessage(text="有一天 父親拿了一跟筷子給兒子要他折斷\n兒子一折就斷了\n兒子說\n「這很容易辦到。」\n接著父親拿出三隻筷子給兒子要他折斷\n兒子一折就斷了\n「這很容易辦到。」\n接著父親拿出三十隻筷子給兒子要他折斷\n兒子還是一折就斷了\n「爸，你到底要幹嘛？」\n.\n.\n.\n「沒...沒事。」") )
		elif num == 10:
			reply_arr.append( TextSendMessage(text="有一天小明跟他一個Gay朋友去吃火鍋\n小明點了海鮮鍋 Gay則是點了咖哩鍋\n以下是小明跟跟店員的對話店員：咖哩鍋喔~請問是哪位的?\n小明：咖哩給Gay\n店員：蛤?\n小明：我說咖哩給Gay\n店員️：蹦蹦蹦?") )
	elif "無聊" in text:
		reply_arr.append( TextSendMessage(text="多養一盆植物來跟我當朋友呀！或是打關鍵字-笑話-\n讓我來~讓你開心讓你有趣點~") )
	elif "你好嗎" in text:
		reply_arr.append( TextSendMessage(text="來看看我的健康檢查吧！") )
	elif "全日照" in text:
		reply_arr.append( TextSendMessage(text="每天 6-8 個小時照射陽光") )
	elif "半日照" in text:
		reply_arr.append( TextSendMessage(text="每天 3-4 個小時照射陽光") )
	elif "推薦" in text:
		reply_arr.append( TextSendMessage(text="目前網路上種植TOP10的植物：\n黃金葛\n薄荷\n仙人掌\n吊蘭\n龜背芋\n蘆薈\n常春藤\n迷迭香\n白網紋\n銅錢草") )
	elif "你好" in text:
		reply_arr.append( TextSendMessage(text="哈囉") )
	elif text == "仙人掌":
		reply_arr.append( TextSendMessage(text="仙人掌是石竹目仙人掌科的植物總稱\n別名為仙巴掌、仙人扇、霸王龍蝦樹\n為多肉植物的一類\n目前仙人掌科的植物有174屬，多於2000種物種") )
	elif text == "仙人掌1":
		reply_arr.append( TextSendMessage(text="仙人掌喜歡曬太陽\n尤其冬季更喜歡！\n必須配合良好通風環境喔~") )
		reply_arr.append( TextSendMessage(text="溫度5度以上即可安全過冬，18度以上可正常生長\n建議每隔一周或兩周在早上或傍晚澆水\n氣溫降低時，水量也要減少。") )
	elif text == "仙人掌2":
		reply_arr.append( TextSendMessage(text="駱駝會吃仙人掌，因為駱駝的嘴巴裡長滿了圓錐形的乳突，這些乳突已經部分角質化，堅韌可以保護駱駝的嘴巴在食用仙人掌時免受擦傷或刮傷。") )
	elif text == "吊蘭":
		reply_arr.append( TextSendMessage(text="吊蘭又名釣蘭、掛蘭、蘭草、折鶴蘭，歐美國家稱蜘蛛草，日本稱折鶴蘭，是相當常見的垂掛式觀葉植物，原產於南非") )
	elif text == "吊蘭1":
		reply_arr.append( TextSendMessage(text="吊蘭不耐烈日\n夏日可半日照，冬季可全日照\n避免直曬。15-25 度的環境為佳") )
		reply_arr.append( TextSendMessage(text="吊蘭喜歡水，生長期要保持淨化空氣\n土壤濕潤，可透過噴霧增加空氣濕度。避免葉片枯黃。") )
	elif text == "吊蘭2":
		reply_arr.append( TextSendMessage(text="室內吊蘭可以吸收80％的有害氣體，特別是甲醛，剛裝修的房子，很適合養1到2盆吊蘭盆栽去淨化空氣。") )
	elif text == "黃金葛":
		reply_arr.append( TextSendMessage(text="原名綠蘿，又稱黃金葛、萬年青，屬天南星科麒麟葉屬，原產於法屬玻里尼西亞的莫雷阿島，喜蔭蔽及潮濕的環境，現在在家庭中常作為觀葉植物栽培。") )
	elif text == "黃金葛1":
		reply_arr.append( TextSendMessage(text="微弱光源即可生存\n但充足的陽光可以讓黃金葛長得更好喔！") )
		reply_arr.append( TextSendMessage(text="平常一般濕度即可\n適合生長在16-27 度的環境") )
		reply_arr.append( TextSendMessage(text="建議在靠近土壤的枝幹處澆水\n若有葉片發黃，通常是過度澆水的警訊！") )
	elif text == "黃金葛2":
		reply_arr.append( TextSendMessage(text="黃金葛清除室內甲醛的效果很好。但是對貓咪來說是有毒的喔！要放在貓咪碰不到的地方唷！") )
	elif text == "薄荷":
		reply_arr.append( TextSendMessage(text="薄荷屬，爲唇形科的一屬，包含25個種，其中辣薄荷及留蘭香為最常見的品種。最早期於歐洲地中海地區及西亞一帶盛產") )
	elif text == "薄荷1":
		reply_arr.append( TextSendMessage(text="長日照植物，日照不足會產生徒長現象。") )
		reply_arr.append( TextSendMessage(text="適合生長在25-30 度為佳") )
		reply_arr.append( TextSendMessage(text="薄荷需水量大，但水分過多容易發霉\n切記不乾不澆，澆則澆透\n（植物底盤有露出些許水分）") )
	elif text == "薄荷2":
		reply_arr.append( TextSendMessage(text="薄荷含有一種叫做薄荷醇的東西。薄荷醇在常溫狀態下就可以激活我們身體感覺「涼」的神經感受器，因此吃薄荷時才會覺得涼涼的。") )
	elif text == "龜背芋":
		reply_arr.append( TextSendMessage(text="龜背芋，是天南星科龜背芋屬植物。 龜背芋適應性強，性喜溫暖，潮濕的環境，但也耐陰、耐陽及有一定的耐旱性，原產於墨西哥的熱帶雨林中") )
	elif text == "龜背芋1":
		reply_arr.append( TextSendMessage(text="適溫散射光-半日照環境皆可\n(多接受陽光生長速度快一些\n夏季有 1-2小時直射陽光即可\n冬天可全日照") )
		reply_arr.append( TextSendMessage(text="適合生長在 15 °C-30 °C環境") )
		reply_arr.append( TextSendMessage(text="以60%以上的溼度為宜\n一般居家環境約在40-60%之間\n建議可每天早上幫植物噴霧，會長得更健康哦") )
	elif text == "龜背芋2":
		reply_arr.append( TextSendMessage(text="因為葉面不規則出現的羽裂，就像起司的孔洞般，故在外國又被暱稱為\nSwiss cheese plant（瑞士起司）") )
	elif text == "蘆薈":
		reply_arr.append( TextSendMessage(text="蘆薈屬通稱蘆薈，原產於地中海、非洲，為阿福花科獨尾草亞科多年生草本、多肉植物，據考證的野生蘆薈品種300多種，主要分布於非洲等地") )
	elif text == "蘆薈1":
		reply_arr.append( TextSendMessage(text="蘆薈需要充足日照，可全日照\n但初植的蘆薈不宜曬太陽，半日照即可。") )
		reply_arr.append( TextSendMessage(text="生長最適宜的溫度為15-35 度。") )
		reply_arr.append( TextSendMessage(text="濕度在 45%-85%為宜。") )
	elif text == "蘆薈2":
		reply_arr.append( TextSendMessage(text="蘆薈表層的白粉是多肉植物的防曬乳\n可以防止植物曬傷情況發生\n蘆薈可以食用，但要記得將黏液洗乾淨，不然會苦苦的。") )
	elif text == "常春藤":
		reply_arr.append( TextSendMessage(text="常春藤，又名洋常春藤、長春藤、土鼓藤、木蔦、百角蜈蚣，是常春藤屬下的一種常綠攀援植物，在很多地區常春藤實際都屬於入侵物種。") )
	elif text == "常春藤1":
		reply_arr.append( TextSendMessage(text="長春藤適合半日照\n在強光下容易燒傷。") )
		reply_arr.append( TextSendMessage(text="生長最適宜的溫度為 15-25℃") )
		reply_arr.append( TextSendMessage(text="喜歡濕潤環境，乾澆澆透\n對空氣濕度要求較高\n每日可在盆栽周圍噴水2次") )
	elif text == "常春藤2":
		reply_arr.append( TextSendMessage(text="長春藤在希臘神話中代表酒神。有著歡樂與活力的象徵，並代表不朽與永恆的青春。") )
	elif text == "迷迭香":
		reply_arr.append( TextSendMessage(text="迷迭香是一種原產於地中海盆地，木本多年生香料植物，野生或種植於白堊土壤中。莖、葉和花都可提取芳香油") )
	elif text == "迷迭香1":
		reply_arr.append( TextSendMessage(text="需要半日照以上才會長得好\n若日光不足植株易徒長") )
		reply_arr.append( TextSendMessage(text="適應溫度範圍大\n一般在20-30℃內都能生長良好") )
		reply_arr.append( TextSendMessage(text="迷迭香較耐旱，但缺水會使花香不再\n一般以「不干不澆，澆則澆透」為原則") )
	elif text == "迷迭香2":
		reply_arr.append( TextSendMessage(text="在古代歐洲，迷迭香還被認為象徵記憶\n這個象徵可追溯到古希臘時期\n在葬禮上，悼念者們會把迷迭香樹枝丟進死者的墳墓，代表對死者的紀念") )
	elif text == "白網紋":
		reply_arr.append( TextSendMessage(text="網紋草為爵床科網紋草屬下的一個物種，又可稱白網紋草、紅網紋草，是哥倫比亞、秘魯、玻利維亞、厄瓜多和巴西北部熱帶雨林的本土植物，但不具入侵性") )
	elif text == "白網紋1":
		reply_arr.append( TextSendMessage(text="半日照即可，避免陽光直曬。") )
		reply_arr.append( TextSendMessage(text="怕冷，適合生長在溫度 20～25℃") )
		reply_arr.append( TextSendMessage(text="生長期可在葉片與盆栽周圍噴水\n澆水時避免土壤積水") )
	elif text == "白網紋2":
		reply_arr.append( TextSendMessage(text="白網紋草對乙烯極為敏感，因此不宜置於蘋果、香蕉、柿子、奇異果等易釋放乙烯之水果旁以及汽機車排氣處，以免造成枯萎現象") )
	elif text == "銅錢草":
		reply_arr.append( TextSendMessage(text="銅錢草為傘形科草本植物。多年生挺水或濕生觀賞植物。植株具有蔓生性，株高5~15cm，節上常生根。莖頂端呈褐色。葉互生，具長柄，圓盾形，直徑2~4cm，緣波狀，草綠色，葉脈15~20條放射狀") )
	elif text == "銅錢草1":
		reply_arr.append( TextSendMessage(text="以半日照或陰處為佳\n每天讓銅錢草接受 4～6 小時的散射光照或是8～10小時的人工光照\n會讓銅錢草長勢更好。") )
		reply_arr.append( TextSendMessage(text="適合在溫度10-25度環境中生長") )
		reply_arr.append( TextSendMessage(text="銅錢草喜歡濕潤，夏天要常向植株噴水。\n冬天澆水避免盆內積水。") )
	elif text == "銅錢草2":
		reply_arr.append( TextSendMessage(text="銅錢草的花會發出難聞的味道喔！而且開花後反而會讓枝葉越來越黃，越來越小。") )

	elif "狀態" in text:
		f = open('plant_inf.txt',"r")
		arr = f.readlines()
		for i in range(0,3):
			arr[i] = arr[i][0:len(arr[i])-1]
		soil = "土壤溼度的比值為 " + str(arr[0])
		moisture = "目前空氣濕度為 " + str(arr[1]) + "%RH"
		temperature = "目前溫度為 " + str(arr[2]) + "°C"
		reply_arr.append( TextSendMessage(text=soil) )
		reply_arr.append( TextSendMessage(text=moisture) )
		reply_arr.append( TextSendMessage(text=temperature) )
	elif  text == "陳昱廷醜照":
		message = ImageSendMessage(
			original_content_url='https://imagizer.imageshack.com/img923/6319/dEvpDK.jpg',
			preview_image_url='https://imagizer.imageshack.com/img923/6319/dEvpDK.jpg'
		)
		reply_arr.append( message )
		message = ImageSendMessage(
			original_content_url='https://imagizer.imageshack.com/img923/7777/o7MEEX.jpg',
			preview_image_url='https://imagizer.imageshack.com/img923/7777/o7MEEX.jpg'
		)
		reply_arr.append( message )
		message = ImageSendMessage(
			original_content_url='https://imagizer.imageshack.com/img922/8486/CV1s6P.jpg',
			preview_image_url='https://imagizer.imageshack.com/img922/8486/CV1s6P.jpg'
		)
		reply_arr.append( message )
		message = ImageSendMessage(
			original_content_url='https://imagizer.imageshack.com/img924/269/pu6LTU.jpg',
			preview_image_url='https://imagizer.imageshack.com/img924/269/pu6LTU.jpg'
		)
		reply_arr.append( message )
	elif "幹" in text:
		message = ImageSendMessage(
			original_content_url='https://i1.kknews.cc/SIG=3g4j2so/3n050002rn2515s3384o.jpg',
			preview_image_url='https://i1.kknews.cc/SIG=3g4j2so/3n050002rn2515s3384o.jpg'
		)
		reply_arr.append( message )		    
	elif "學生證" in text: 
		message = ImageSendMessage(
			original_content_url='https://imagizer.imageshack.com/img923/3792/VYkHB1.jpg',
			preview_image_url='https://imagizer.imageshack.com/img923/3792/VYkHB1.jpg'
		)
		reply_arr.append( message )		
		
	else:
		message = StickerSendMessage(package_id=11539,sticker_id=52114129)
		reply_arr.append( message )
		#reply_arr.append( TextSendMessage(text=text) )

	line_bot_api.reply_message( event.reply_token, reply_arr )
	
	
	
@app.route('/')
def index():
	return 'Hello World'

import os
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port= port )