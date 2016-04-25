import math, cgi, cgitb
cgitb.enable()

print("Content-type: text/html")
print("")

print("<link rel='stylesheet' type='text/css' href='../style.css'>")
print("<h1>CGI Square Root Calculator</h1>")
print("<h2><i>Powered by Python</i></h2>")
print("Hello, world!<br>")
form = cgi.FieldStorage()
if form:
    print("Your number is {0}.<br>".format(int(form['num'].value)))
    print("Your number's square root is {0}.".format(round(math.sqrt(int(form['num'].value)),3)))
