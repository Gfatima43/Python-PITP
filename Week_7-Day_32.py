# Start Flask
# Install Flask in cmd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Web Development with Flask!"

if __name__ == "__main__":
    app.run(debug=True)

#%%
# chatgpt code
from flask import Flask, request
import csv
import os

app = Flask(__name__)

# Path to the CSV file where data will be stored
CSV_FILE = 'form_data.csv'

# Function to write data to CSV
def save_to_csv(name, email, message):
    # Check if the CSV file already exists. If not, create it and add headers.
    file_exists = os.path.isfile(CSV_FILE)
    
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # If the file doesn't exist, write the header (column names)
        if not file_exists:
            writer.writerow(['Name', 'Email', 'Message'])
        
        # Write the form data as a new row
        writer.writerow([name, email, message])

# Route for displaying the form and handling POST request
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':  # When the form is submitted
        # Get data from the form
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Save the data to the CSV file
        save_to_csv(name, email, message)
        
        # Provide feedback to the user
        return f'''
        <h2>Form Submitted Successfully!</h2>
        <p><b>Name:</b> {name}</p>
        <p><b>Email:</b> {email}</p>
        <p><b>Message:</b> {message}</p>
        '''
    
    # If the request method is GET, return the form page
    return '''
    <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                }
                .form-container {
                    width: 300px;
                    margin: 0 auto;
                    padding: 20px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                input, textarea {
                    width: 100%;
                    padding: 10px;
                    margin: 5px 0;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                button {
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    cursor: pointer;
                    border-radius: 5px;
                }
            </style>
        </head>
        <body>
            <div class="form-container">
                <h2>Contact Us</h2>
                <form method="POST">
                    <label for="name">Name:</label><br>
                    <input type="text" id="name" name="name" required><br><br>
                    
                    <label for="email">Email:</label><br>
                    <input type="email" id="email" name="email" required><br><br>
                    
                    <label for="message">Message:</label><br>
                    <textarea id="message" name="message" rows="4" required></textarea><br><br>
                    
                    <button type="submit">Submit</button>
                </form>
            </div>
        </body>
    </html>
    '''

if __name__ == "__main__":

    app.run(debug=True)