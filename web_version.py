from flask import Flask
app=Flask(__name__)
@app.route('/')
def home(): return 'Employee Salary Management Web Running'
if __name__=='__main__': app.run()