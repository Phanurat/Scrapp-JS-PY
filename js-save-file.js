const puppeteer = require('puppeteer');
const { minify } = require('html-minifier');
const fs = require('fs');

(async () => {
    try {
        const browser = await puppeteer.launch({ headless: false }); 
        const page = await browser.newPage();

        await page.goto('https://www.facebook.com/aseanfootball', { waitUntil: 'networkidle2' });
        await page.click('[aria-label="Close"]');
        
        await page.waitForSelector('body');

        // เริ่มการเลื่อนลงทุก 1000 มิลลิวินาที (1 วินาที)
        const scrollInterval = setInterval(async () => {
            await page.evaluate(() => {
                window.scrollBy(0, window.innerHeight); // เลื่อนลง
            });
        }, 1000);

        // รอเวลา 60 วินาที (1 นาที)
        await new Promise(resolve => setTimeout(resolve, 60000));

        // หยุดการเลื่อนหน้าเว็บหลังจากเวลาที่กำหนด (1 นาที)
        clearInterval(scrollInterval);

        const htmlContent = await page.content();
        const minifiedHTML = minify(htmlContent, {
            collapseWhitespace: true,
            conservativeCollapse: true,
            minifyCSS: true,
            minifyJS: true
        });

        fs.writeFileSync('scrap/test_cut.html', minifiedHTML);
        await browser.close();

        console.log('Facebook page after login saved as facebook_after_login.html');
    } catch (error) {
        console.error('Error:', error);
    }
})();