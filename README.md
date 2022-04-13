# mitmproxy-hstamp

代理拦截请求并将返回值中存在时间戳的字段 X 以 yyyy-MM-dd HH:mm:ss 格式作为 X_hs 字段返回，方便测试人员抓包查看日期
https://docs.mitmproxy.org/stable/api/events.html
https://docs.mitmproxy.org/stable/api/mitmproxy/http.html#Message.set_content
