import re

COMMON_TYPOS = (
    (r'^https://(.*?.youtube.com)/', r'http://los.fcing.email/user22334455/https/\1/'),
    # (r'^https://', r'httpss://'),
)
url = "https://www.youtube.com/watch?v=rTSI-pUWgF0";
for mistake, fixup in COMMON_TYPOS:
    if re.match(mistake, url):
        print(re.sub(mistake, fixup, url))
print(url)
