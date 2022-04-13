"""
代理拦截请求并将返回值中存在时间戳的字段 X 以 yyyy-MM-dd HH:mm:ss 格式作为 X_hs 字段返回，方便测试人员抓包查看日期
https://docs.mitmproxy.org/stable/api/events.html
https://docs.mitmproxy.org/stable/api/mitmproxy/http.html#Message.set_content
"""

from mitmproxy import ctx
import json
import hstamp

class HumanTimeStamp:
    # def request(self, flow):
    #     ctx.log(f"request url: {flow.request.url=}")

    def response(self, flow):
        resp = flow.response
        if(resp is None):
            return
        headers = {} if resp.headers is None  else  resp.headers
        mime = headers.get('Content-Type', '')
        bytes = resp.content if('application/json' in mime) else None
        try:
            content = json.loads(bytes)
            modify = hstamp.humanstamp(content, None)
            resp.set_text(json.dumps(modify))
        except BaseException as exp:
            ctx.log(f"response:{exp=}")

addons =  [
    HumanTimeStamp()
]