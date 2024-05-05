const fs = require("fs");
const cheerio = require("cheerio");

// อ่านไฟล์ HTML
const html = fs.readFileSync("./scrap/test_cut.html");

// ใช้ Cheerio เพื่อแกะสลัก DOM
const $ = cheerio.load(html);

// ตัวอย่างการค้นหาและดึงข้อมูล
const title = $("title").text(); // ดึงข้อความที่อยู่ใน tag <title>

// เก็บข้อมูลลงในไฟล์ข้อความ (.txt)
fs.writeFileSync("get_link/output.txt", `Title: ${title}\n`);

// เพิ่มข้อมูลอื่น ๆ ลงในไฟล์ (.txt)
$("a").each((index, element) => {
    const link = $(element).attr("href");
    fs.appendFileSync("get_link/output.txt", `Link ${index + 1}: ${link}\n`);
});

// ลบไฟล์ที่ไม่ใช่ .gitignore ในไดเรกทอรี scrap หลังจากใช้งานเสร็จ
const files = fs.readdirSync('scrap');
files.forEach(file => {
    if (file !== '.gitignore') {
        fs.unlinkSync(`scrap/${file}`);
    }
});

console.log("Save File ==>  get_link/output.txt Finishing!!");
