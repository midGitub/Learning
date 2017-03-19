"come config for my spider,like:url,agent or pattern"

url="http://www.qiushibaike.com/8hr/page/"
url_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
pattern=(
            r'div.*?author.*?img.*?<a.*?<h2>(.*?)</h2'
            r'.*?<div.*?content.*?span>+(.*?)</span'
            r'.*?<span.*?stats-vote.*?number.*?>(.*?)</i>'
        )