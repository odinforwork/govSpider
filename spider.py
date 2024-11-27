import newspaper
from newspaper import Article

def main():
    parse_source()
    
def parse_source():

    source = newspaper.build('https://fgw.beijing.gov.cn/fgwzwgk/2024zcwj/index.htm', language='zh')
    
    for category in source.category_urls():
        print('分类名称:', category)

    for article in source.articles:
        print('新闻标题:', article.title)
    
def parse_documentation(url: str):

    # 目标新闻网址
    url = 'https://fgw.beijing.gov.cn/gzdt/tztg/202411/t20241112_3939843.htm'

    # 创建Article对象
    article = Article(url, language='zh')  # language参数指定文章语言，中文为'zh'

    # 下载并解析网页
    article.download()
    article.parse()

    # 提取并打印新闻信息
    print('题目:', article.title)
    print('正文:', article.text)
    print('作者:', article.authors)
    print('关键词:', article.keywords)
    print('摘要:', article.summary)
    # 其他可提取的信息包括：配图地址（top_image）、视频地址（movies）、发布日期（publish_date）等

if __name__ == "__main__":
    main()