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
//const imageUrl = $("img").attr("src");
//fs.appendFileSync("get_link/output.txt", `Image URL: ${imageUrl}\n`);

$("a").each((index, element) => {
    const link = $(element).attr("href");
    fs.appendFileSync("get_link/output.txt", `Link ${index + 1}: ${link}\n`);
});

console.log("Save File ==>  get_link/output.txt Finishing!!");
