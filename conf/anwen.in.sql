/*
Navicat MySQL Data Transfer

Source Server         : libo
Source Server Version : 50160
Source Host           : 113.11.199.77:3306
Source Database       : anwen.in

Target Server Type    : MYSQL
Target Server Version : 50160
File Encoding         : 65001

Date: 2012-09-18 20:29:08
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `comments`
-- ----------------------------
DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author_id` int(11) NOT NULL,
  `share_id` int(11) NOT NULL DEFAULT '0',
  `commentbody` mediumtext NOT NULL,
  `commenttime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `published` (`commenttime`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comments
-- ----------------------------
INSERT INTO `comments` VALUES ('1', '2', '5', '<p>tt</p>', '2012-08-28 11:32:04');

-- ----------------------------
-- Table structure for `likes`
-- ----------------------------
DROP TABLE IF EXISTS `likes`;
CREATE TABLE `likes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `share_id` int(11) NOT NULL DEFAULT '0',
  `liketime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `published` (`liketime`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of likes
-- ----------------------------
INSERT INTO `likes` VALUES ('28', '2', '6', '2012-08-19 13:10:15');
INSERT INTO `likes` VALUES ('29', '2', '6', '2012-08-19 13:10:21');
INSERT INTO `likes` VALUES ('30', '2', '6', '2012-08-19 13:10:26');
INSERT INTO `likes` VALUES ('31', '2', '5', '2012-08-19 14:31:49');
INSERT INTO `likes` VALUES ('32', '2', '5', '2012-08-19 14:31:53');
INSERT INTO `likes` VALUES ('33', '2', '6', '2012-08-19 14:57:16');
INSERT INTO `likes` VALUES ('34', '2', '6', '2012-08-19 14:57:18');
INSERT INTO `likes` VALUES ('35', '2', '6', '2012-08-19 14:57:36');
INSERT INTO `likes` VALUES ('36', '2', '5', '2012-08-19 14:58:36');
INSERT INTO `likes` VALUES ('37', '2', '5', '2012-08-19 14:58:40');
INSERT INTO `likes` VALUES ('38', '2', '4', '2012-08-19 14:59:59');

-- ----------------------------
-- Table structure for `shares`
-- ----------------------------
DROP TABLE IF EXISTS `shares`;
CREATE TABLE `shares` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author_id` int(11) NOT NULL,
  `title` varchar(512) NOT NULL,
  `sharetype` varchar(20) NOT NULL DEFAULT 'pencil',
  `markdown` mediumtext NOT NULL,
  `html` mediumtext NOT NULL,
  `published` datetime NOT NULL,
  `commentnum` int(11) NOT NULL DEFAULT '0',
  `updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `likes` int(11) NOT NULL DEFAULT '0',
  `hits` int(11) NOT NULL DEFAULT '0',
  `slug` varchar(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`,`likes`),
  KEY `published` (`published`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shares
-- ----------------------------
INSERT INTO `shares` VALUES ('1', '2', '史蒂夫 乔布斯Steve.Jobs在2005年对斯坦福大学Stanford毕业生的演讲(中英字幕)', 'film', '.....................................................................................................\r\n<embed src=\"http://player.youku.com/player.php/sid/XMjQ4MzkwMjIw/v.swf\" allowFullScreen=\"true\" quality=\"high\" width=\"480\" height=\"400\" align=\"middle\" allowScriptAccess=\"always\" type=\"application/x-shockwave-flash\"></embed>', '<p>.....................................................................................................\n<embed src=\"http://player.youku.com/player.php/sid/XMjQ4MzkwMjIw/v.swf\" allowFullScreen=\"true\" quality=\"high\" width=\"480\" height=\"400\" align=\"middle\" allowScriptAccess=\"always\" type=\"application/x-shockwave-flash\"></embed></p>', '2012-08-14 11:37:07', '0', '2012-08-18 22:36:07', '0', '0', '0');
INSERT INTO `shares` VALUES ('2', '2', '吉米·威尔士关于维基百科诞生的演讲', 'pencil', 'TED演讲集.2005.07.吉米·威尔士关于维基百科诞生的演讲.中英字幕\r\nJimmy.Wales.on.the.birth.of.Wikipedia.Chi_Eng.640X480-YYeTs人人影视制作.rmvb\r\n<embed src=\"http://player.youku.com/player.php/sid/XMjE4NjIzMzM2/v.swf\" quality=\"high\" width=\"480\" height=\"400\" align=\"middle\" allowScriptAccess=\"sameDomain\" allowFullscreen=\"true\" type=\"application/x-shockwave-flash\"></embed>', '<p>TED演讲集.2005.07.吉米·威尔士关于维基百科诞生的演讲.中英字幕\nJimmy.Wales.on.the.birth.of.Wikipedia.Chi_Eng.640X480-YYeTs人人影视制作.rmvb\n<embed src=\"http://player.youku.com/player.php/sid/XMjE4NjIzMzM2/v.swf\" quality=\"high\" width=\"480\" height=\"400\" align=\"middle\" allowScriptAccess=\"sameDomain\" allowFullscreen=\"true\" type=\"application/x-shockwave-flash\"></embed></p>', '2012-08-16 14:27:43', '0', '2012-08-18 22:36:13', '0', '0', '0');
INSERT INTO `shares` VALUES ('3', '2', '关于安问', 'fire', '###安问致力于创造和分享有趣有价值东西\r\n\r\n* 我们专注于为大家提供有意思的互联网，文学，影音，生活等方面的资讯、文字，并期待以此引发大家的思考，给大家带来快乐。\r\n* 人生要有趣~我们将用这个平台，记录平凡但坚定的智慧和创举，分享敢于行动勇于付出的精神和理想。\r\n* 我们相信真诚的创造与分享可以让世界更漂亮。\r\n\r\n安问工作室是一个致力于在大众文化层面传播美好的东西的非营利机构，成立于2011年3月4日。团队汇聚了一批愿意创造和分享的年轻人，旨在“用创造和分享的力量将世界变得更漂亮”。欢迎认同我们理念的人加入~\r\n\r\n* 我们会为那些真诚的贡献者实现更多的价值\r\n* 投给安问的优秀稿件都会有稿费以及更多回报\r\n* 原创文章每篇1~10元起，被阅读更多收获也更多\r\n* 推荐文章和给我们的好的建议，即使来稿未选中也有稿费\r\n* 稿酬会不断增多\r\n\r\n###为什么要建立安问？\r\n\r\n* 面对信息爆炸，安问将致力于提供最精简最有价值的资讯，在快节奏的生活中为大家带来一方安静的网络空间和交流平台\r\n* 读更多的好书，看更多的美景，认识更多志同道合的朋友。和更多的人分享有价值有趣的东西。相互交流，分享发现\r\n\r\n###安问名字的来源：\r\n\r\n>豺狼当道，安问狐狸——《后汉书·张纲传》\r\n\r\n* 话说东汉末年，外戚诸梁姻族满朝，大将军梁冀专权。朝廷派遣张纲等八人分道巡按各州郡，纠察收审贪官污吏。张纲衔命出洛阳，叹道：“豺狼当道，安问狐狸？”遂将车轮埋于都亭，起草弹劾梁冀的奏章。用豺狼比喻祸国殃民的人，用狐狸比喻小偷等小坏蛋，就是说国家祸国殃民的人还没除净，（却派我）去查那些小贪小污的小官。\r\n* Origin: askender.com is a website all about creating and sharing nice things. We provide valuable messages and passages for everyone,money for every creator and sharer. We believe everyone’s creativity and spirit of sharing have the power of promoting a better world.\r\nIf there are real evils,why should we kill ants?\r\n* 当然安问的名字也来源于屈原的《天问》以及奥森·斯科特·卡德（Orson Scott Card）的《安德的游戏》\r\n\r\n\r\n###加入安问\r\n\r\n* 安问的每个开发管理者和写作者也都是安问每日的用户，分享着自己心爱的发现，也从大家的创造和分享中受益。\r\n* 邮箱：askender43@gmail.com\r\n* 安问工作室用户群：127343260\r\n* 安问工作室核心群：148673816\r\n\r\n###安问团队介绍：\r\n\r\n* 柏舟(askender)，物理学转互联网，热爱科幻，阅读，围棋...大学刚毕业，理想没死，希望靠自己的力量改变一些什么\r\n* 刘超（kelvin），主修通信，喜欢折腾与被折腾，热爱互联网，爱好巨多，这里写不下\r\n* sailor\r\n* 郭伟楠，荆州，专业地球化学，不成形geek一枚，未修成正果松鼠一只，爱好不计其数，以科幻，米奇，古典文化最甚，琴棋书画皆略懂，鬼点子多，可家养，可外放\r\n* 都磊(石头儿)，湖北襄樊，专科毕业，计算机专业，之后参加了北大青鸟2年的培训，热爱互联网，10年4月来到上海，参加工作。目前在一家私营企业做高级软件工程师，主要是用.Net开发一些管理系统\r\n* anti,魏景亮,周潇粤,Yungstedt,盲眼A,青青子矜\r\n* ireading,A-cat,盲眼A,林子,H1K9\r\n* 月  从前的巴菲就是愤青，将不能创作的理由推给“经费、人力、胶卷和市场”。现在的巴菲只是个单纯的说书人，一支笔、一张纸、几句话，简简单单，不为其它  “我”的总合借由潜意识转化为梦境，巴菲印刻就是将梦境造出的出版社。\r\n\r\n###联系我们\r\n* 邮箱：askender43@gmail.com\r\n* 微博：http://weibo.com/askender\r\n* github: https://github.com/askender\r\n\r\n###安问策划\r\n* 成为优质内容发布、阅读与分享的一个独特和独立平台，作者收入更多，读者阅读体验更好，交流互动更有意思。我们会与资源版权方深度合作，让正版资源能够以方便、低价，互动性更强的方式呈现于读者面前。\r\n* 创建一个氛围独特的优质互动社区，使网站内容的质量保持在高水平。\r\n* 研发智能推荐算法，提供更好的用户体验和用户价值实现。\r\n\r\n###安问分支\r\n* 全新 安问 anwen.in\r\n* 多人独立博客平台：[安问网](http://askender.com/)、[安问科幻网](http://anwensf.com/),其中安问科幻网吸引高校众多科幻社团参与，立志打造有趣的科幻网站。\r\n* 人工智能Ender\r\n\r\n~期待有新的成员加入~@@\r\n\r\n* 一个开源的分享最打动大家东西的微型社区项目\r\n* [anwen.in@github](https://github.com/askender/anwen.in)正在不断开发中，欢迎大家fork\r\n* 构建于tornado，欢迎大家批评指正，askender43@gmail.com', '<h3>安问致力于创造和分享有趣有价值东西</h3>\n<ul>\n<li>我们专注于为大家提供有意思的互联网，文学，影音，生活等方面的资讯、文字，并期待以此引发大家的思考，给大家带来快乐。</li>\n<li>人生要有趣~我们将用这个平台，记录平凡但坚定的智慧和创举，分享敢于行动勇于付出的精神和理想。</li>\n<li>我们相信真诚的创造与分享可以让世界更漂亮。</li>\n</ul>\n<p>安问工作室是一个致力于在大众文化层面传播美好的东西的非营利机构，成立于2011年3月4日。团队汇聚了一批愿意创造和分享的年轻人，旨在“用创造和分享的力量将世界变得更漂亮”。欢迎认同我们理念的人加入~</p>\n<ul>\n<li>我们会为那些真诚的贡献者实现更多的价值</li>\n<li>投给安问的优秀稿件都会有稿费以及更多回报</li>\n<li>原创文章每篇1~10元起，被阅读更多收获也更多</li>\n<li>推荐文章和给我们的好的建议，即使来稿未选中也有稿费</li>\n<li>稿酬会不断增多</li>\n</ul>\n<h3>为什么要建立安问？</h3>\n<ul>\n<li>面对信息爆炸，安问将致力于提供最精简最有价值的资讯，在快节奏的生活中为大家带来一方安静的网络空间和交流平台</li>\n<li>读更多的好书，看更多的美景，认识更多志同道合的朋友。和更多的人分享有价值有趣的东西。相互交流，分享发现</li>\n</ul>\n<h3>安问名字的来源：</h3>\n<blockquote>\n<p>豺狼当道，安问狐狸——《后汉书·张纲传》</p>\n</blockquote>\n<ul>\n<li>话说东汉末年，外戚诸梁姻族满朝，大将军梁冀专权。朝廷派遣张纲等八人分道巡按各州郡，纠察收审贪官污吏。张纲衔命出洛阳，叹道：“豺狼当道，安问狐狸？”遂将车轮埋于都亭，起草弹劾梁冀的奏章。用豺狼比喻祸国殃民的人，用狐狸比喻小偷等小坏蛋，就是说国家祸国殃民的人还没除净，（却派我）去查那些小贪小污的小官。</li>\n<li>Origin: askender.com is a website all about creating and sharing nice things. We provide valuable messages and passages for everyone,money for every creator and sharer. We believe everyone’s creativity and spirit of sharing have the power of promoting a better world.\nIf there are real evils,why should we kill ants?</li>\n<li>当然安问的名字也来源于屈原的《天问》以及奥森·斯科特·卡德（Orson Scott Card）的《安德的游戏》</li>\n</ul>\n<h3>加入安问</h3>\n<ul>\n<li>安问的每个开发管理者和写作者也都是安问每日的用户，分享着自己心爱的发现，也从大家的创造和分享中受益。</li>\n<li>邮箱：askender43@gmail.com</li>\n<li>安问工作室用户群：127343260</li>\n<li>安问工作室核心群：148673816</li>\n</ul>\n<h3>安问团队介绍：</h3>\n<ul>\n<li>柏舟(askender)，物理学转互联网，热爱科幻，阅读，围棋...大学刚毕业，理想没死，希望靠自己的力量改变一些什么</li>\n<li>刘超（kelvin），主修通信，喜欢折腾与被折腾，热爱互联网，爱好巨多，这里写不下</li>\n<li>sailor</li>\n<li>郭伟楠，荆州，专业地球化学，不成形geek一枚，未修成正果松鼠一只，爱好不计其数，以科幻，米奇，古典文化最甚，琴棋书画皆略懂，鬼点子多，可家养，可外放</li>\n<li>都磊(石头儿)，湖北襄樊，专科毕业，计算机专业，之后参加了北大青鸟2年的培训，热爱互联网，10年4月来到上海，参加工作。目前在一家私营企业做高级软件工程师，主要是用.Net开发一些管理系统</li>\n<li>anti,魏景亮,周潇粤,Yungstedt,盲眼A,青青子矜</li>\n<li>ireading,A-cat,盲眼A,林子,H1K9</li>\n<li>月  从前的巴菲就是愤青，将不能创作的理由推给“经费、人力、胶卷和市场”。现在的巴菲只是个单纯的说书人，一支笔、一张纸、几句话，简简单单，不为其它  “我”的总合借由潜意识转化为梦境，巴菲印刻就是将梦境造出的出版社。</li>\n</ul>\n<h3>联系我们</h3>\n<ul>\n<li>邮箱：askender43@gmail.com</li>\n<li>微博：http://weibo.com/askender</li>\n<li>github: https://github.com/askender</li>\n</ul>\n<h3>安问策划</h3>\n<ul>\n<li>成为优质内容发布、阅读与分享的一个独特和独立平台，作者收入更多，读者阅读体验更好，交流互动更有意思。我们会与资源版权方深度合作，让正版资源能够以方便、低价，互动性更强的方式呈现于读者面前。</li>\n<li>创建一个氛围独特的优质互动社区，使网站内容的质量保持在高水平。</li>\n<li>研发智能推荐算法，提供更好的用户体验和用户价值实现。</li>\n</ul>\n<h3>安问分支</h3>\n<ul>\n<li>全新 安问 anwen.in</li>\n<li>多人独立博客平台：<a href=\"http://askender.com/\">安问网</a>、<a href=\"http://anwensf.com/\">安问科幻网</a>,其中安问科幻网吸引高校众多科幻社团参与，立志打造有趣的科幻网站。</li>\n<li>人工智能Ender</li>\n</ul>\n<p>~期待有新的成员加入~@@</p>\n<ul>\n<li>一个开源的分享最打动大家东西的微型社区项目</li>\n<li><a href=\"https://github.com/askender/anwen.in\">anwen.in@github</a>正在不断开发中，欢迎大家fork</li>\n<li>构建于tornado，欢迎大家批评指正，askender43@gmail.com</li>\n</ul>', '2012-08-18 16:51:57', '0', '2012-08-29 21:45:14', '4', '0', 'about');
INSERT INTO `shares` VALUES ('4', '2', '升级日志', 'fire', '###120730\r\n\r\n* 全新安问使用tornado重新构建\r\n* 重写新的关于页面\r\n* 模板构建\r\n* chatroom\r\n\r\n###120818\r\n\r\n* 架构改进\r\n* 添加文章和评论功能\r\n\r\n###120819\r\n* 桉叶、喜欢功能\r\n\r\n###120828\r\n* 分页\r\n\r\n###120903\r\n* 征求建议\r\n* 版面设计(todo)\r\n* 正文页的智能推荐(todo)\r\n* 与安德AI的整合(todo)\r\n* 更多成员加入(todo)\r\n* 推荐排序(todo)\r\n* 充实基础内容(todo)\r\n* 密码找回(todo)\r\n* 消息系统(todo)\r\n* 文章高级markdown编辑器(todo)\r\n* 图片上传(todo)\r\n* 全新安德(anwen.in/ande)(todo)\r\n* SQLAlchemy整合(todo)\r\n* oauth登录(todo)', '<h3>120730</h3>\n<ul>\n<li>全新安问使用tornado重新构建</li>\n<li>重写新的关于页面</li>\n<li>模板构建</li>\n<li>chatroom</li>\n</ul>\n<h3>120818</h3>\n<ul>\n<li>架构改进</li>\n<li>添加文章和评论功能</li>\n</ul>\n<h3>120819</h3>\n<ul>\n<li>桉叶、喜欢功能</li>\n</ul>\n<h3>120828</h3>\n<ul>\n<li>分页</li>\n</ul>\n<h3>120903</h3>\n<ul>\n<li>征求建议</li>\n<li>版面设计(todo)</li>\n<li>正文页的智能推荐(todo)</li>\n<li>与安德AI的整合(todo)</li>\n<li>更多成员加入(todo)</li>\n<li>推荐排序(todo)</li>\n<li>充实基础内容(todo)</li>\n<li>密码找回(todo)</li>\n<li>消息系统(todo)</li>\n<li>文章高级markdown编辑器(todo)</li>\n<li>图片上传(todo)</li>\n<li>全新安德(anwen.in/ande)(todo)</li>\n<li>SQLAlchemy整合(todo)</li>\n<li>oauth登录(todo)</li>\n</ul>', '2012-08-18 17:13:10', '0', '2012-09-04 07:13:29', '5', '0', 'changelog');
INSERT INTO `shares` VALUES ('5', '2', '提建议或咨询--欢迎联系我们', 'fire', '虚心接受大家的批评指教，只为创造我们心中最棒的理想主义网站\r\n\r\n我们的宗旨始终是：创造和分享美好\r\n\r\n邮箱：askender43@gmail.com\r\n\r\nQQ：527639661  QQ群：127343260\r\n\r\n[邮件列表][1]：需修改hosts或越过长城，若不能访问可在群里问\r\n\r\n[github](https://github.com/askender/anwen.in)\r\n\r\n[微博][2]\r\n\r\n[google plus][3]：需修改hosts或越过长城\r\n\r\nYY频道ID：19043661（几乎没怎么使用）\r\n\r\n\r\n[1]: https://groups.google.com/d/forum/our-anwen        \"安问邮件列表\"\r\n[2]: http://weibo.com/askender\r\n[3]: https://plus.google.com/110129569739358072859', '<p>虚心接受大家的批评指教，只为创造我们心中最棒的理想主义网站</p>\n<p>我们的宗旨始终是：创造和分享美好</p>\n<p>邮箱：askender43@gmail.com</p>\n<p>QQ：527639661  QQ群：127343260</p>\n<p><a href=\"https://groups.google.com/d/forum/our-anwen\" title=\"安问邮件列表\">邮件列表</a>：需修改hosts或越过长城，若不能访问可在群里问</p>\n<p><a href=\"https://github.com/askender/anwen.in\">github</a></p>\n<p><a href=\"http://weibo.com/askender\">微博</a></p>\n<p><a href=\"https://plus.google.com/110129569739358072859\">google plus</a>：需修改hosts或越过长城</p>\n<p>YY频道ID：19043661（几乎没怎么使用）</p>', '2012-08-18 17:45:46', '0', '2012-08-28 16:45:44', '4', '0', 'help');
INSERT INTO `shares` VALUES ('6', '2', 'Markdown漫游指南', 'ask', 'Markdown 的目标是实现「易读易写」，成为一种适用于网络的书写语言。\r\n\r\n* Markdown 的语法全由一些精挑细选的符号所组成，其作用一目了然。\r\n* 它实际上是个非常简单、非常容易学习的语法。这个语法简单到每个人都可以在5分钟以内学会。应该是为数不多，你真的可以彻底学会的语言。\r\n* 更重要的是，Markdown语法所有要素，是与写作的习惯一脉相承的，套用句俗语：仅为写作而生。[1][1]\r\n\r\n\r\n比如：\r\n\r\n在文字两旁加上星号，看起来就像*强调*；两个星号，**粗体**。\r\n\r\n<pre>*强调*  **粗体**</pre>\r\n\r\n要写引用网址了，就是这么写[]再加个()，如：[豆瓣](http://www.douban.com)\r\n\r\n<pre>[豆瓣](http://www.douban.com)</pre>\r\n\r\n要引用大段文字，就是直接 >后面写引用\r\n>习惯是人生最大的指导。\r\n\r\n<pre>>习惯是人生最大的指导。</pre>\r\n\r\n标题：在行首插入 1 到 6 个 # ，对应到标题 1 到 6 阶\r\n# 标题 1\r\n## 标题 2\r\n### 标题 3\r\n\r\n<pre>\r\n# 标题 1\r\n## 标题 2\r\n### 标题 3\r\n</pre>\r\n\r\n无序列表：在使用星号、加号或者减号来做为列表的项目标记(星号后要加空格)\r\n\r\n* 安问\r\n* 柏舟\r\n* 成长\r\n\r\n<pre>\r\n* 安问\r\n* 柏舟\r\n* 成长\r\n</pre>\r\n\r\n有序列表则是使用一般的数字接着一个英文句点作为项目标记：\r\n\r\n1. Red\r\n2. Green\r\n3. Blue\r\n\r\n<pre>\r\n1. Red\r\n2. Green\r\n3. Blue\r\n</pre>\r\n\r\n图片\r\n\r\n图片的语法和链接很像。（title 是选择性的）：\r\n\r\n![豆瓣](http://img1.douban.com/pics/nav/lg_main_a10.png \"豆瓣logo\")\r\n\r\n<pre>\r\n![豆瓣](http://img1.douban.com/pics/nav/lg_main_a10.png \"豆瓣logo\")\r\n</pre>\r\n\r\n####进阶\r\n\r\n参考形式的链接让你可以为链接定一个名称，之后你可以在文件的其他地方定义该链接的内容：\r\n\r\n<pre>\r\nI get 10 times more traffic from [Google][1] than from\r\n[Yahoo][2] or [MSN][3].\r\n\r\n[1]: http://google.com/ \"Google\"\r\n[2]: http://search.yahoo.com/ \"Yahoo Search\"\r\n[3]: http://search.msn.com/ \"MSN Search\"\r\n</pre>\r\n\r\n代码块\r\n\r\n<pre>\r\n```python\r\ndef hello():\r\n    return True\r\n```\r\n</pre>\r\n\r\n一切就这么简单。Markdown之所以越来越流行,是因为它足够简单。\r\n\r\n参考文献：\r\n\r\n1. [为什么Markdown+R有较大概率成为科技写作主流？][1]\r\n\r\n2. [Markdown 语法说明(简体中文版)][2]\r\n\r\n3. [Markdown Syntax Documentation][3]\r\n\r\n[1]:http://www.yangzhiping.com/tech/r-markdown-knitr.html\r\n[2]:http://wowubuntu.com/markdown/basic.html\r\n[3]:http://daringfireball.net/projects/markdown/syntax', '<p>Markdown 的目标是实现「易读易写」，成为一种适用于网络的书写语言。</p>\n<ul>\n<li>Markdown 的语法全由一些精挑细选的符号所组成，其作用一目了然。</li>\n<li>它实际上是个非常简单、非常容易学习的语法。这个语法简单到每个人都可以在5分钟以内学会。应该是为数不多，你真的可以彻底学会的语言。</li>\n<li>更重要的是，Markdown语法所有要素，是与写作的习惯一脉相承的，套用句俗语：仅为写作而生。<a href=\"http://www.yangzhiping.com/tech/r-markdown-knitr.html\">1</a></li>\n</ul>\n<p>比如：</p>\n<p>在文字两旁加上星号，看起来就像<em>强调</em>；两个星号，<strong>粗体</strong>。</p>\n<pre>*强调*  **粗体**</pre>\n\n<p>要写引用网址了，就是这么写[]再加个()，如：<a href=\"http://www.douban.com\">豆瓣</a></p>\n<pre>[豆瓣](http://www.douban.com)</pre>\n\n<p>要引用大段文字，就是直接 &gt;后面写引用</p>\n<blockquote>\n<p>习惯是人生最大的指导。</p>\n</blockquote>\n<pre>>习惯是人生最大的指导。</pre>\n\n<p>标题：在行首插入 1 到 6 个 # ，对应到标题 1 到 6 阶</p>\n<h1>标题 1</h1>\n<h2>标题 2</h2>\n<h3>标题 3</h3>\n<pre>\n# 标题 1\n## 标题 2\n### 标题 3\n</pre>\n\n<p>无序列表：在使用星号、加号或者减号来做为列表的项目标记(星号后要加空格)</p>\n<ul>\n<li>安问</li>\n<li>柏舟</li>\n<li>成长</li>\n</ul>\n<pre>\n* 安问\n* 柏舟\n* 成长\n</pre>\n\n<p>有序列表则是使用一般的数字接着一个英文句点作为项目标记：</p>\n<ol>\n<li>Red</li>\n<li>Green</li>\n<li>Blue</li>\n</ol>\n<pre>\n1. Red\n2. Green\n3. Blue\n</pre>\n\n<p>图片</p>\n<p>图片的语法和链接很像。（title 是选择性的）：</p>\n<p><img alt=\"豆瓣\" src=\"http://img1.douban.com/pics/nav/lg_main_a10.png\" title=\"豆瓣logo\" /></p>\n<pre>\n![豆瓣](http://img1.douban.com/pics/nav/lg_main_a10.png \"豆瓣logo\")\n</pre>\n\n<h4>进阶</h4>\n<p>参考形式的链接让你可以为链接定一个名称，之后你可以在文件的其他地方定义该链接的内容：</p>\n<pre>\nI get 10 times more traffic from [Google][1] than from\n[Yahoo][2] or [MSN][3].\n\n[1]: http://google.com/ \"Google\"\n[2]: http://search.yahoo.com/ \"Yahoo Search\"\n[3]: http://search.msn.com/ \"MSN Search\"\n</pre>\n\n<p>代码块</p>\n<pre>\n```python\ndef hello():\n    return True\n```\n</pre>\n\n<p>一切就这么简单。Markdown之所以越来越流行,是因为它足够简单。</p>\n<p>参考文献：</p>\n<ol>\n<li>\n<p><a href=\"http://www.yangzhiping.com/tech/r-markdown-knitr.html\">为什么Markdown+R有较大概率成为科技写作主流？</a></p>\n</li>\n<li>\n<p><a href=\"http://wowubuntu.com/markdown/basic.html\">Markdown 语法说明(简体中文版)</a></p>\n</li>\n<li>\n<p><a href=\"http://daringfireball.net/projects/markdown/syntax\">Markdown Syntax Documentation</a></p>\n</li>\n</ol>', '2012-08-19 06:41:59', '0', '2012-08-28 16:45:57', '8', '0', 'markdown');
INSERT INTO `shares` VALUES ('7', '2', '桉叶说明', 'ask', '桉叶是用户在安问价值的回馈之一\r\n\r\n分享：10叶\r\n\r\n喜欢：1叶 作者2叶\r\n\r\n评论：1叶（todo）', '<p>桉叶是用户在安问价值的回馈之一</p>\n<p>分享：10叶</p>\n<p>喜欢：1叶 作者2叶</p>\n<p>评论：1叶（todo）</p>', '2012-08-22 13:12:56', '0', '2012-08-28 16:46:09', '0', '0', '0');
INSERT INTO `shares` VALUES ('8', '2', '站点分享', 'fire', '###社区\r\n[豆瓣](http://www.douban.com/)\r\n[V2EX](http://www.v2ex.com/ \"创意工作者们的社区\")\r\n[](http://codinn.com/ \"联结开发者\")\r\n\r\n###工具\r\n[Google 阅读器](https://www.google.com/reader/ )', '<h3>社区</h3>\n<p><a href=\"http://www.douban.com/\">豆瓣</a>\n<a href=\"http://www.v2ex.com/\" title=\"创意工作者们的社区\">V2EX</a>\n<a href=\"http://codinn.com/\" title=\"联结开发者\"></a></p>\n<h3>工具</h3>\n<p><a href=\"https://www.google.com/reader/\">Google 阅读器</a></p>', '2012-08-22 13:19:40', '0', '2012-08-28 16:47:29', '0', '0', '0');
INSERT INTO `shares` VALUES ('9', '2', '学习实验', 'pencil', '###一些自己的和别人的demo，仅供学习使用\r\n\r\n[chats](/chats) WebSocket\r\n\r\n[chat](/chat) Ajax Long-Polling', '<h3>一些自己的和别人的demo，仅供学习使用</h3>\n<p><a href=\"/chats\">chats</a> WebSocket</p>\n<p><a href=\"/chat\">chat</a> Ajax Long-Polling</p>', '2012-08-22 13:23:56', '0', '2012-08-28 16:47:23', '0', '0', '0');
INSERT INTO `shares` VALUES ('10', '2', '链接收集', 'fire', '###技术\r\n\r\n[程序员技术练级攻略](http://coolshell.cn/articles/4990.html)\r\n\r\n[程序员能力矩阵 Programmer Competency Matrix](http://static.icybear.net/%5BCN%5DProgrammer%20competency%20matrix.htm)', '<h3>技术</h3>\n<p><a href=\"http://coolshell.cn/articles/4990.html\">程序员技术练级攻略</a></p>\n<p><a href=\"http://static.icybear.net/%5BCN%5DProgrammer%20competency%20matrix.htm\">程序员能力矩阵 Programmer Competency Matrix</a></p>', '2012-08-27 15:39:58', '0', '2012-08-28 16:47:09', '0', '0', '0');
INSERT INTO `shares` VALUES ('11', '2', '节点', 'pencil', '[创造](/node/pencil \"\")  \r\n\r\n[音乐](/node/music \"\")\r\n\r\n[视频](/node/film \"\")\r\n\r\n[读书](/node/book \"\")\r\n\r\n[新闻](/node/news \"\")\r\n\r\n[疑问](/node/ask \"\")\r\n\r\n[科幻](/node/sf \"\")\r\n\r\n[行动](/node/fire \"\")', '<p><a href=\"/node/pencil\">创造</a><br />\n</p>\n<p><a href=\"/node/music\">音乐</a></p>\n<p><a href=\"/node/film\">视频</a></p>\n<p><a href=\"/node/book\">读书</a></p>\n<p><a href=\"/node/news\">新闻</a></p>\n<p><a href=\"/node/ask\">疑问</a></p>\n<p><a href=\"/node/sf\">科幻</a></p>\n<p><a href=\"/node/fire\">行动</a></p>', '2012-08-28 05:45:03', '0', '2012-08-28 20:25:35', '0', '0', 'nodes');
INSERT INTO `shares` VALUES ('12', '2', '一些书', 'book', '《黑客与画家》\r\n\r\n《失控：机器、社会与经济的新生物学》\r\n\r\n欢迎推荐好书', '<p>《黑客与画家》</p>\n<p>《失控：机器、社会与经济的新生物学》</p>\n<p>欢迎推荐好书</p>', '2012-09-05 19:11:46', '0', '2012-09-06 05:37:38', '0', '0', '0');

-- ----------------------------
-- Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `user_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_name` varchar(60) NOT NULL DEFAULT '',
  `user_pass` varchar(64) NOT NULL DEFAULT '',
  `user_email` varchar(100) NOT NULL DEFAULT '',
  `user_say` mediumtext,
  `user_leaf` int(11) NOT NULL DEFAULT '0',
  `user_domain` varchar(20) NOT NULL,
  `user_url` varchar(100) NOT NULL DEFAULT '',
  `user_registered` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_activation_key` varchar(60) NOT NULL DEFAULT '',
  `user_status` int(11) NOT NULL DEFAULT '0',
  `user_city` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `user_name` (`user_name`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('2', '柏舟', 'c4ca4238a0b923820dcc509a6f75849b', 'askender43@gmail.com', 'sfsdfsdfs\r\n\r\ncreate', '40', 'askender', '', '2012-09-06 03:11:46', '', '0', '武汉');
INSERT INTO `users` VALUES ('12', '527639661', '96e79218965eb72c92a549dd5a330112', '527639661@qq.com', null, '0', '527639661', '', '2012-09-06 23:42:45', '', '0', null);
