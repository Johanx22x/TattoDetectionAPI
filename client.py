import requests

def detect_objects(image_path, api_url):
    # Open the image file
    with open(image_path, 'rb') as file:
        # Send a POST request to the API endpoint
        response = requests.post(api_url + '/detect', files={'image': file})
        
        # Check if the request was successful
        if response.status_code == 200:
            # Print the detected objects
            print(response.json())
        else:
            print('Error:', response.text)

if __name__ == '__main__':
    # Set the path to the image file
    image_path = './tattoo2.jpg'
    
    # Set the URL of your API
    api_url = 'http://localhost:5000'  # Change this to your API URL
    
    # Call the detect_objects function
    detect_objects(image_path, api_url)
