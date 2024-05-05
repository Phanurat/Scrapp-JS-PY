const puppeteer = require('puppeteer');
const { minify } = require('html-minifier');
const fs = require('fs');

// ฟังก์ชันสำหรับบันทึกเนื้อหา HTML จาก URL ลงในไฟล์
async function saveHTMLFromLink(linkURL, outputFilePath) {
    try {
        const browser = await puppeteer.launch({ headless: false });
        const page = await browser.newPage();

        await page.goto(linkURL, { waitUntil: 'networkidle2' });
        await page.click('[aria-label="Close"]');
        await page.waitForSelector('body');

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

// ฟังก์ชันสำหรับการประมวลผลลิงก์ในโฟลเดอร์ link_post
async function processLinks() {
    // วนลูปไฟล์ในโฟลเดอร์ link_post
    const linkDirectory = 'link_post';
    const contentDirectory = 'html_post';
    const linkFiles = fs.readdirSync(linkDirectory);
    
    // ตรวจสอบว่ามีไฟล์ใน link_post หรือไม่
    if (linkFiles.length === 0) {
        console.log('ไม่มีไฟล์ในโฟลเดอร์ link_post');
        return;
    }

    // วนลูปเพื่อประมวลผลลิงก์
    for (const linkFile of linkFiles) {
        const linkFilePath = `${linkDirectory}/${linkFile}`;
        const linkURL = fs.readFileSync(linkFilePath, 'utf8').trim();

        // สร้างชื่อไฟล์ HTML ตามลำดับของไฟล์ link
        const index = linkFile.split('.')[0].replace('link', '');
        const outputFilePath = `${contentDirectory}/content${index}_post.html`;

        // เรียกใช้งานฟังก์ชัน saveHTMLFromLink เพื่อบันทึกเนื้อหา HTML
        await saveHTMLFromLink(linkURL, outputFilePath);
    }
}

// เรียกใช้งานฟังก์ชัน processLinks เพื่อเริ่มการประมวลผลลิงก์
processLinks();
