const http = require("http");
const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  res.writeHead(200, {"Content-Type":"text/html"});
  res.end(`
    <h1>Implementing DevOps Solutions</h1>
    <p>Name: <b>Jason Mihari</b> | Student ID: <b>100959264</b></p>
    <p>Path: ${req.url}</p>
  `);
});

server.listen(PORT, () => console.log(`Server on :${PORT}`));
