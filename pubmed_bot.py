import requests
import datetime

# 填入你剛才複製的 Webhook URL
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1475097421879972055/rk1xvdkZ4UKY3IP4zfrovondTImwBpTL890v74Myt9BXpS6XcSY0z1LtLlMFVHTOTNlw"

def fetch_pubmed():
    # 搜尋關鍵字：運動醫學、復健、最新文章
    query = "Sports Medicine[Title/Abstract] AND Rehabilitation[Title/Abstract]"
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query}&retmode=json&reldate=1"
    
    response = requests.get(url).json()
    id_list = response.get('esearchresult', {}).get('idlist', [])
    
    if not id_list:
        return "今天沒有新的相關文獻。"

    content = "📚 **今日運動醫學文獻推薦**\n\n"
    for pmid in id_list[:3]: # 每次推播前 3 篇避免洗板
        content += f"🔗 https://pubmed.ncbi.nlm.nih.gov/{pmid}/\n"
    
    return content

def send_to_discord(text):
    data = {"content": text}
    requests.post(WEBHOOK_URL, json=data)

if __name__ == "__main__":
    news = fetch_pubmed()
    send_to_discord(news)
