# Python 2.7 simple web server that serves a directory that contains a built Vue.js app
# Run this script from the command line with:


from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import time
import subprocess

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('src/index.html', 'r') as f:
                self.wfile.write(f.read())
            return
        # Host the /media/p4/Presets/setlists directory
        elif self.path == '/media/p4/Presets/setlists':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('/media/p4/Presets/setlists', 'r') as f:
                self.wfile.write(f.read())
            return

        else:
            path = "." + self.path
            # Serve the file requested
            # Check if the file exists
            if os.path.isfile(path):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                with open(path, 'r') as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('404: File not found')

            return
    
    def do_POST(self):
        if self.path.split('?')[0] == '/zen':
            args = self.path.split('?')[1].split('&')
            #print(self.headers)
            print("Command: " + str(args[0].split('=')[1]) + " Package: " + str(args[1].split('=')[1]))
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(time.asctime())
            return


if __name__ == '__main__':
    try:
        server = HTTPServer(('0.0.0.0', 5555), MyHandler)
        print('Started httpserver on port ' , 5555)

        server.serve_forever()

    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        server.socket.close()
        