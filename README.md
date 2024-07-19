# ai_calendar
Receive description in natural language or a photo and turn it into calendar data.   
This is a project of Rong Chang Cup by Jiao Tong University.   

# Deployment
*First Step*   
```
conda create --name ai_calendar --file requirements.txt
```
*Second Step*   
Obtain your API Key and Secret Key at ai.baidu.com.    
Obtain your Access Token at aistudio.baidu.com.     
```
export API_KEY=your_api_key
export SECRET_KEY=your_secret_key
export ACCESS_TOKEN=your_access_token
```  
   
# Run
```
conda activate ai_calendar
python main.py
```