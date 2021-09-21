from django.shortcuts import render
import pyrebase

# Create your views here.
config={
    "apiKey": "AIzaSyAxOhg2XQiRpktrfDpPGWoqjgQD7alSmq0",
    "authDomain": "fireapp-c3e36.firebaseapp.com",
    "databaseURL": "https://fireapp-c3e36-default-rtdb.firebaseio.com",
    "projectId": "fireapp-c3e36",
    "storageBucket": "fireapp-c3e36.appspot.com",
    "messagingSenderId": "564960363824",
    "appId": "1:564960363824:web:ff9ee05d0330b7f75734f5",
    "measurementId": "G-NBBM679DH2"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


def index(request):
        name = database.child('Data').child('Name').get().val()
        stack = database.child('Data').child('Stack').get().val()
        framework = database.child('Data').child('Framework').get().val()
        # return render(request, 'index.html', {
        #     "name":name,
        #     "stack":stack,
        #     "framework":framework 
        # })

        context = {
            'name':name,
            'stack':stack,
            'framework':framework
        }
        return render(request, 'index.html', context)