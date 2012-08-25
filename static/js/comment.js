function getCookie(name) {
	var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
	return r ? r[1] : undefined;
}
preAllow = true; //定义一个变量，主要是为了防止恶刷，也是为了防止重复提交，在返回结果之前是不能点击的
$(function() {
	$("#addCommentForm").submit(function(e) //使用jquery封装js
	{
		e.preventDefault();
		if (preAllow) {
			preAllow = false;
			//alert("here");
			var flag = 1; //定义一个变量，当下面的一些检查发现问题会置0，这样就不会发送post请求了
			// 	var htmlElement = encodeURI(encodeURI($("#myhtml").val()));  //使用jquery获取DOM 
			// 	if (/(\w+)\.html/.exec(htmlElement) == null||htmlElement=="")  //使用js的正则匹配判断格式不符合  或者  为空  都会alert
			// 	{
			// 		alert("请输入正确的html文件");
			// 		flag=0;
			// }
			//var commentbody = encodeURI(encodeURI($("#commentbody").val()));
			var commentbody = $("#commentbody").val();
			var share_id = encodeURI(encodeURI($("#share_id").val()));
			if (commentbody == "") {
				$("textarea[name=commentbody]").select();
				flag = 0;
			}
			var argsxsrf = getCookie("_xsrf");
			if (flag) {
				$('#submit').val('感谢您的评论，努力提交中..');
				$.ajax({ //使用了jquery的ajax，因为我需要回调没有使用$.get
					type: "POST",
					//调用类型
					url: "/sharecomment",
					//调用的url地址
					//data: {"html":htmlElement,"table":tableElement,"sender":senderElement,"head":headElement,"senderid":senderidElement},  //传送的dict数据
					data: {
						"share_id": share_id,
						"commentbody": commentbody,
						"_xsrf": argsxsrf
					},
					//传送的dict数据
					success: function(data) { //回调函数，alert返回结果
						//alert(decodeURI(data));
						//data = decodeURI(decodeURI(data));
						$(data).hide().insertBefore('#addCommentContainer').slideDown();
						$('#commentbody').val('');
						preAllow = true;
						$('#submit').val('提交');
					}
				});
			}
		}
	});


	$("#likeit").submit(function(e) //使用jquery封装js
	{

		e.preventDefault();
		if (preAllow) {
			preAllow = false;
			var flag = 1; //定义一个变量，当下面的一些检查发现问题会置0，这样就不会发送post请求了
			var share_id = encodeURI(encodeURI($("#share_id").val()));
			var share_likes = encodeURI(encodeURI($("#share_likes").val()));
			var argsxsrf = getCookie("_xsrf");
			if (flag) {
				$('#like').val('感谢您的喜欢，努力提交中..');
				$.ajax({ //使用了jquery的ajax，因为我需要回调没有使用$.get
					type: "POST",
					//调用类型
					url: "/sharelike",
					//调用的url地址
					//data: {"html":htmlElement,"table":tableElement,"sender":senderElement,"head":headElement,"senderid":senderidElement},  //传送的dict数据
					data: {
						"share_id": share_id,
						"share_likes": share_likes,
						"_xsrf": argsxsrf
					},
					//传送的dict数据
					success: function(data) { //回调函数，alert返回结果
						//alert(decodeURI(data));
						preAllow = true;
						$('#like').val(data);
						$('#like').attr("disabled", "disabled"); 
					}
				});
			}
		}
	});



})