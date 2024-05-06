const puppeteer = require('puppeteer');
const { minify } = require('html-minifier');
const fs = require('fs');

async function saveHTMLFromLink(linkURL, outputFilePath) {
    try {
        const browser = await puppeteer.launch({ headless: true });
        const page = await browser.newPage();

        console.log('Processing Working!!! ....');

        await page.goto(linkURL, { waitUntil: 'networkidle2' });
        await page.click('[aria-label="Close"]');
        await page.waitForNavigation(); // Wait for navigation after clicking close button

        const htmlContent = await page.content();
        const minifiedHTML = minify(htmlContent, {
            collapseWhitespace: true,
            conservativeCollapse: true,
            minifyCSS: true,
            minifyJS: true
        });

        fs.writeFileSync(outputFilePath, minifiedHTML);
        await browser.close();

        console.log(`บันทึก HTML POST ไปยัง ${outputFilePath} เรียบร้อยแล้ว`);
    } catch (error) {
        console.error('เกิดข้อผิดพลาด:', error);
    }
}

async function processLinks() {
    const linkDirectory = 'link_post';
    const contentDirectory = 'html_post';

    if (!fs.existsSync(contentDirectory)) {
        fs.mkdirSync(contentDirectory);
    }

    const linkFiles = fs.readdirSync(linkDirectory);

    if (linkFiles.length === 0) {
        console.log('ไม่มีไฟล์ในโฟลเดอร์ link_post');
        return;
    }

    for (const linkFile of linkFiles) {
        const linkFilePath = `${linkDirectory}/${linkFile}`;
        const linkURL = fs.readFileSync(linkFilePath, 'utf8').trim();

        const index = linkFile.split('.')[0].replace('link', '');
        const outputFilePath = `${contentDirectory}/content${index}_post.html`;

        await saveHTMLFromLink(linkURL, outputFilePath);
    }
}

processLinks();
