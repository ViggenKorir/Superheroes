from app import create_app

app = create_app() 

if __name__ == '__main__':
    # Run the application in debug mode on localhost
    app.run(debug=True, host='127.0.0.1', port=5555)
