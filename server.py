from http.server import HTTPServer, BaseHTTPRequestHandler 
content="""

<html>
<head>
<title> My Web Server</title>
</head>

<body>
<center><h1>List of Protocols in TCP/IP</h1/center>
<center><h2>Protocol Suite</h2></center><br>
<table border="1"  align="center" cellpadings="20" bgcolor="yellow">
            <thead>
                <tr>
                  <th>S.no</th>
                  <th>Name of the layer</th>
                  <th>Name of the protocol</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                  <td>1</td>
                  <td>Application Layer</td>
                  <td>HTTP,FTP,DNS,Telnut</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Transport Layer</td>
                  <td>TCP & UDP</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Network Layer</td>
                  <td>IPV4,IPV6</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>Link Layer</td>
                  <td>MAC,Ethernet</td>
                </tr>
            </tbody>
        </table>
</body>
</html>
"""
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver")
server_address =('',5000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()