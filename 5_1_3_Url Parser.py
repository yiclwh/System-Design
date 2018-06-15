"""
Parse a html page, extract the Urls in it.

Hint: use regex to parse html.

Given the following html page:

<html>
  <body>
    <div>
      <a href="http://www.google.com" class="text-lg">Google</a>
      <a href="http://www.facebook.com" style="display:none">Facebook</a>
    </div>
    <div>
      <a href="https://www.linkedin.com">Linkedin</a>
      <a href = "http://github.io">LintCode</a>
    </div>
  </body>
</html>
You should return the Urls in it:

[
  "http://www.google.com",
  "http://www.facebook.com",
  "https://www.linkedin.com",
  "http://github.io"
]

"""

class HtmlParser:
    """
    @param: content: content source code
    @return: a list of links
    """
    def parseUrls(self, content):
        # write your code here
        import re
        links = re.findall(r'\s*(?i)href\s*=\s*("|\')+([^"\'>\s]*)', content, re.I)
        links = [link[1] for link in links if len(link[1]) and not link[1].startswith('#')]
        return list(links)