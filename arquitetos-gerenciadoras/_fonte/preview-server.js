const http=require("http"),fs=require("fs"),path=require("path");
const ROOT="/Users/mac/Desktop/buildv/oneoffice/oneoffice-obras-corporativas";
const PORT=process.env.PORT||6421;
const T={".html":"text/html",".css":"text/css",".js":"application/javascript",".svg":"image/svg+xml",".png":"image/png",".jpg":"image/jpeg",".jpeg":"image/jpeg",".webp":"image/webp",".ttf":"font/ttf",".woff2":"font/woff2",".ico":"image/x-icon",".mp4":"video/mp4",".otf":"font/otf",".json":"application/json"};
http.createServer((req,res)=>{
  let p=decodeURIComponent(req.url.split("?")[0]);
  if(p==="/")p="/arquitetos-gerenciadoras/index.html";
  let fp=path.join(ROOT,p);
  if(fs.existsSync(fp)&&fs.statSync(fp).isDirectory())fp=path.join(fp,"index.html");
  fs.readFile(fp,(e,d)=>{
    if(e){res.writeHead(404);res.end("404 "+p);return;}
    res.writeHead(200,{"Content-Type":T[path.extname(fp).toLowerCase()]||"application/octet-stream","Cache-Control":"no-cache"});
    res.end(d);
  });
}).listen(PORT,()=>console.log("preview on http://localhost:"+PORT));
