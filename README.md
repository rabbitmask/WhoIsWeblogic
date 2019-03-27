	软件作者：Tide_RabbitMask
    免责声明：Pia!(ｏ ‵-′)ノ”(ノ﹏<。)
    本工具仅用于安全测试，请勿用于非法使用，要乖哦~
        
    WhoIsWeblogic  V1.0简介：
	提供weblogic批量模糊识别检测。
	weblogicdomain.py针对域名，weblogicip.py针对IP。
	
	
	WhoIsWeblogic  V1.0开发背景：
	最近拿到了一个小任务，需要从百万级的域名/IP中进行weblogic 漏洞分析。
	鉴于时间比较紧张，我只能尽可能模糊的进行url的存活检测、weblogic服务器识别，
	然后对再筛选后的结果进行weblogic poc批量检测，此工具正是为了筛选工作准备的。

	
	WhoIsWeblogic  V1.0特色：
		1.完善的超时处理机制
		2.多进程任务高效并发
		3.简洁直观的监控界面
		4.健全的日志记录功能
		5.健全的异常处理机制
		
	WhoIsWeblogic  V1.0文件说明：
		domain.txt:域名待读取
		domainalive.txt:记录存活域名
		domainlog.txt:记录扫描日志
		domainresult.txt:记录疑似weblogic域名
	
		ip.txt:IP待读取
		iplog.txt:记录扫描日志
		ipresult.txt:记录疑似weblogic IP
	
	【软件使用Demo】
	【此处只提供了本机单机扫描demo，多线程实战场面太过血腥，请在家长陪同下自行体验】
	
	#weblogicip控制台：
	=========================================================================
	当前站点：http://127.0.0.1:7001/console/login/LoginForm.jsp     状态码：200
	当前站点：http://127.0.0.1:7001/wls-wsat/CoordinatorPortType    状态码：200
	>>>>>任务结束
	=========================================================================
	
		
	#iplog.txt：
	=========================================================================
	当前站点：http://127.0.0.1:7001/console/login/LoginForm.jsp     状态码：200
	当前站点：http://127.0.0.1:7001/wls-wsat/CoordinatorPortType    状态码：200
	=========================================================================
	
	
	#ipresult.txt:【Tips:ipresult.txt文件可直接用于Weblogic++ V1.1调用。】
	=========================================================================
	127.0.0.1
	=========================================================================
	
	weblogicdomain Demo 同理weblogicip，在此不做演示。
