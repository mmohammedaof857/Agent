import re
import urllib.parse
import urllib.request


def grt_vid(query):

  try:
    encoded = urllib.parse.quote(query)

  url = (
      "https://www.youtube.com/results"
      "?search_query=" + encoded
  )

  request = urlib.request.Request(
    url,
      headers=(
        "user-Agent": "mozilla/5.0"
        }
      }

  data = urllib.request.urlopen(
    request,
    timeout=5
  ).read()_.decode("utf-8",errors="ignore")

ids = re.findall(
  r'"videoId':"([^'']+)"',
  data
)
  return ids[0] if ids else None

except Exception:
  return None

def create_youtube_url(command):

  text = command.lower().strip()

  paterns = [
    r"play\s+song\s(.+)",
    r"play\s+music\s+(.+)",
    r"play\s+(.+)
    r"youtube\s+(.+)"
  ]

query = c0mmand

for pattern in patterns:

    math = re.search(
      pattern,
      text
    )
  


  
