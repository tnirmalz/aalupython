# motivation from: https://blog.usejournal.com/how-recon-helped-samsung-protect-their-production-repositories-of-samsungtv-ecommerce-estores-4c51d6ec4fdd
# Usage: python3 lazydork.py <target.com>

import time
import webbrowser
import sys

target = sys.argv[1]
osint_sites = [
    "stackoverflow.com",
    "codepad.co",
    "scribd.com",
    "npmjs.com",
    "npm.runkit.com",
    "libraries.io",
    "ycombinator.com",
    "coggle.it",
    "papaly.com",
    "google.com",
    "trello.com",
    "prezi.com",
    "jsdelivr.net",
    "codepen.io",
    "codeshare.io",
    "sharecode.io",
    "pastebin.com",
    "gist.github.com",
    "repl.it",
    "productforums.google.com",
    "gitter.im",
    "bitbucket.org",
    "*.atlassian.net",
    "gitlab.com",
    "speakerdeck.com",
    "slideshare.net",
    "linkedin.com",
    "hub.docker.com",
    "dotnetfiddle.net",
    "jsfiddle.net",
    "asciinema.org",
    "developpez.net",
    "slides.com",
    "ideone.com",
    "codebeautify.org",
    "justpaste.it"
    ]

for x in osint_sites:
    webbrowser.open('https://www.google.com.np/search?q=site:{}%20%22{}%22'.format(x, target))
    time.sleep(6)  # avoid captcha
