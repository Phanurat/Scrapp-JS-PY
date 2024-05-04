@echo off

REM Install Python packages
pip install bs4
pip install requests
pip install selenium
pip install pyppeteer
pip install pythainlp

REM Install Node.js packages
npm install puppeteer
npm install @hapi/hapi
npm install minify-html
npm install axios
npm install html-minifier

echo Installation completed.
pause
